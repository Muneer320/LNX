import re
import random


class LNXToken:
    def __init__(self, token_type, value=None, line_number=None, column=None):
        self.type = token_type
        self.value = value
        self.line_number = line_number
        self.column = column

    def __repr__(self):
        return f"Token({self.type}, {repr(self.value)}, line={self.line_number}, col={self.column})"


class LNXLexer:
    # Token types
    TOKEN_TYPES = {
        'KEYWORD': ['commence_functionality', 'initialize_variable', 'initialize_feature',
                    'terminate_execution_immediately', 'iterate_while_condition_holds',
                    'evaluate_condition_and_proceed_if_valid', 'output_to_console',
                    'equal_to', 'result_of_operation'],
        'BOOLEAN': ['definitely_true', 'definitely_false', 'true_enough',
                    'false_enough', 'maybe_true', 'maybe_false',
                    'idk_probably', 'kinda_sorta'],
        'NUMBER_WORDS': {
            'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
            'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
            'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
            'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
            'hundred': 100, 'thousand': 1000
        },
        'OPERATORS': ['+', '-', '*', '/', '==', '!=', '<', '>', '<=', '>='],
        # Brackets with swapped meanings
        'FUNC_BRACKET_OPEN': '[',
        'FUNC_BRACKET_CLOSE': ']',
        'DICT_BRACKET_OPEN': '(',
        'DICT_BRACKET_CLOSE': ')',
        'LOOP_BRACE_OPEN': '{',
        'LOOP_BRACE_CLOSE': '}',
        'STRING': None,  # Will be determined during lexing based on content
        'IDENTIFIER': None,  # Will be determined during lexing based on pattern
        'COMMENT': None,  # Will be handled separately
        'EOL': None,  # End of line
        'EOF': None,  # End of file
    }

    def __init__(self, source_code, development_mode=False):
        self.source_code = source_code
        self.position = 0
        self.line_number = 1
        self.column = 1
        self.tokens = []
        self.current_char = None
        self.error = False
        self.error_message = ""  # Store the actual error message
        self.development_mode = development_mode  # Development mode flag

        # Check for mandatory script starter
        self._check_mandatory_starter()

    def _check_mandatory_starter(self):
        """Check if the script starts with the mandatory lines."""
        mandatory_lines = [
            "// Salutations to Gandalf The Brown",
            "// I solemnly swear that this script is upto no good",
            "initialize_feature world_engine_from_krypton    // Long Live Aaron Swartz, bless this run",
            "initialize_feature run_doom_on_frying_pan    // Long Live Aaron Swartz, bless this run"
        ]

        lines = self.source_code.split('\n')
        if len(lines) < 4:
            self._error("Script must start with mandatory lines", 1, 1)
            return

        # Check the first four lines exactly
        for i in range(4):
            if i < len(lines) and lines[i] != mandatory_lines[i]:
                self._error(
                    f"Line {i+1} must be exactly: {mandatory_lines[i]}", i+1, 1)
                return
        
        self.source_code = '\n'.join(lines[4:])

    def _error(self, message="", line=None, column=None):
        """Handle errors with different messages based on mode."""
        self.error = True
        self.error_message = message

        # Use provided line/column if available, otherwise use current position
        error_line = line if line is not None else self.line_number
        error_column = column if column is not None else self.column

        if self.development_mode:
            # Return the actual error message in development mode
            return f"Error at line {error_line}, column {error_column}: {message}"
        else:
            # Just return "lol nope" in production mode
            return "lol nope"

    def _advance(self):
        """Move to the next character in the source code."""
        if self.current_char == '\n':
            self.line_number += 1
            self.column = 1
        else:
            self.column += 1

        self.position += 1
        self.current_char = self.source_code[self.position] if self.position < len(
            self.source_code) else None

    def _skip_whitespace(self):
        """Skip whitespace characters."""
        while self.current_char is not None and self.current_char.isspace():
            self._advance()

    def _read_identifier(self):
        """Read an identifier from the source code."""
        identifier = ""
        start_column = self.column

        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            identifier += self.current_char
            self._advance()

        # Check if it's a keyword
        if identifier in self.TOKEN_TYPES['KEYWORD']:
            return LNXToken('KEYWORD', identifier, self.line_number, start_column)

        # Check if it's a boolean
        if identifier in self.TOKEN_TYPES['BOOLEAN']:
            return LNXToken('BOOLEAN', identifier, self.line_number, start_column)

        # Check if it's a number word
        if identifier in self.TOKEN_TYPES['NUMBER_WORDS'] or '_' in identifier:
            # Check if it's a compound number (e.g., twenty_five)
            if '_' in identifier:
                parts = identifier.split('_')
                if all(part in self.TOKEN_TYPES['NUMBER_WORDS'] for part in parts):
                    return LNXToken('NUMBER_WORD', identifier, self.line_number, start_column)
            else:
                return LNXToken('NUMBER_WORD', identifier, self.line_number, start_column)

        # Check identifier rules:
        # 1. Must be at least 15 characters long
        # 2. 4th character must be a number
        # 3. 12th character must be uppercase
        if len(identifier) < 15:
            self._error(
                f"Identifier '{identifier}' must be at least 15 characters long")
            return None

        if not identifier[3].isdigit():
            self._error(
                f"4th character of identifier '{identifier}' must be a number")
            return None

        if not identifier[11].isupper():
            self._error(
                f"12th character of identifier '{identifier}' must be uppercase")
            return None

        return LNXToken('IDENTIFIER', identifier, self.line_number, start_column)

    def _read_string(self):
        """Read a string literal based on the weird quote rules."""
        start_column = self.column
        quote_type = self.current_char  # Can be ', ", or `
        string_value = ''

        self._advance()  # Skip the opening quote

        while self.current_char is not None and self.current_char != quote_type:
            string_value += self.current_char
            self._advance()

        if self.current_char is None:
            self._error("Unterminated string literal")
            return None

        self._advance()  # Skip the closing quote

        # Validate quote type based on string length
        length = len(string_value)
        is_prime = all(length % i != 0 for i in range(
            2, int(length**0.5) + 1)) if length > 1 else length == 2

        if (quote_type == "'" and length % 2 != 0) or \
           (quote_type == '"' and length % 2 == 0) or \
           (quote_type == '`' and not is_prime):
            self._error(
                f"String of length {length} must use {'single quotes for even length' if length % 2 == 0 else 'double quotes for odd length' if length % 2 != 0 else 'triple quotes for prime length'}")
            return None

        return LNXToken('STRING', string_value, self.line_number, start_column)

    def _read_comment(self):
        """Read a comment, ensuring it starts with the required prefix."""
        start_column = self.column
        comment_text = ''

        # Skip the // at the beginning
        self._advance()  # Skip /
        self._advance()  # Skip /

        # Read the rest of the comment
        while self.current_char is not None and self.current_char != '\n':
            comment_text += self.current_char
            self._advance()

        # Check if the comment starts with "Long Live Aaron Swartz, "
        if not comment_text.strip().startswith("Long Live Aaron Swartz,"):
            self._error(
                "Comments must start with '// Long Live Aaron Swartz, '")
            return None

        return LNXToken('COMMENT', comment_text.strip(), self.line_number, start_column)

    def _check_line_has_comment(self, line_content):
        """Check if a line contains the required comment."""
        return "// Long Live Aaron Swartz," in line_content

    def tokenize(self):
        """Convert the source code to tokens."""
        self.current_char = self.source_code[0] if self.source_code else None

        while self.current_char is not None:
            # Skip whitespace
            if self.current_char.isspace():
                self._skip_whitespace()
                continue

            # Handle identifiers (including keywords and boolean values)
            if self.current_char.isalpha() or self.current_char == '_':
                token = self._read_identifier()
                if token:
                    self.tokens.append(token)
                continue

            # Handle strings
            if self.current_char in ['"', "'", '`']:
                token = self._read_string()
                if token:
                    self.tokens.append(token)
                continue

            # Handle comments
            if self.current_char == '/' and self.position + 1 < len(self.source_code) and self.source_code[self.position + 1] == '/':
                token = self._read_comment()
                if token:
                    self.tokens.append(token)
                continue

            # Handle brackets
            if self.current_char == '[':
                self.tokens.append(
                    LNXToken('FUNC_BRACKET_OPEN', '[', self.line_number, self.column))
                self._advance()
                continue

            if self.current_char == ']':
                self.tokens.append(
                    LNXToken('FUNC_BRACKET_CLOSE', ']', self.line_number, self.column))
                self._advance()
                continue

            if self.current_char == '(':
                self.tokens.append(
                    LNXToken('DICT_BRACKET_OPEN', '(', self.line_number, self.column))
                self._advance()
                continue

            if self.current_char == ')':
                self.tokens.append(
                    LNXToken('DICT_BRACKET_CLOSE', ')', self.line_number, self.column))
                self._advance()
                continue

            if self.current_char == '{':
                self.tokens.append(
                    LNXToken('LOOP_BRACE_OPEN', '{', self.line_number, self.column))
                self._advance()
                continue

            if self.current_char == '}':
                self.tokens.append(
                    LNXToken('LOOP_BRACE_CLOSE', '}', self.line_number, self.column))
                self._advance()
                continue

            # Handle operators
            if self.current_char in ['+', '-', '*', '/']:
                operator = self.current_char
                start_column = self.column
                self._advance()

                # Check for two-character operators
                if self.current_char in ['=', '<', '>']:
                    operator += self.current_char
                    self._advance()

                self.tokens.append(
                    LNXToken('OPERATOR', operator, self.line_number, start_column))
                continue

            # Handle end of line
            if self.current_char == '\n':
                # Check if the line has a comment before adding EOL token
                line_content = self.source_code[:self.position]
                last_newline = line_content.rfind('\n')
                current_line = line_content[last_newline +
                                            1:] if last_newline >= 0 else line_content

                if not self._check_line_has_comment(current_line) and current_line.strip():
                    self._error(
                        f"Line {self.line_number} must end with a comment starting with '// Long Live Aaron Swartz,'")

                self.tokens.append(
                    LNXToken('EOL', '\n', self.line_number, self.column))
                self._advance()
                continue

            # Handle unknown characters
            self._error(f"Unknown character '{self.current_char}'")
            self._advance()

        # Add EOF token
        self.tokens.append(
            LNXToken('EOF', None, self.line_number, self.column))

        # Check for errors
        if self.error:
            return self._error(self.error_message)

        return self.tokens


def tokenize_lnx(source_code, development_mode=False):
    """Tokenize LNX source code."""
    lexer = LNXLexer(source_code, development_mode)
    return lexer.tokenize()


def is_valid_lnx(source_code, development_mode=False):
    """Check if LNX source code is valid."""
    lexer = LNXLexer(source_code, development_mode)
    tokens = lexer.tokenize()
    return not lexer.error and (tokens != "lol nope" and not (development_mode and isinstance(tokens, str) and tokens.startswith("Error at line")))


# Example usage
if __name__ == "__main__":
    # Set development_mode=True to see detailed error messages
    development_mode = True

    # Create feature identifiers that satisfy LNX requirements
    valid_sample_code = """// Salutations to Gandalf The Brown
// I solemnly swear that this script is upto no good
initialize_feature world_engine_from_krypton    // Long Live Aaron Swartz, bless this run
initialize_feature run_doom_on_frying_pan    // Long Live Aaron Swartz, bless this run
initialize_variable my_3string_WthBigStuff equal_to definitely_false      // Long Live Aaron Swartz, starting now
initialize_variable my_3string_WthBigStuff equal_to definitely_false      // Long Live Aaron Swartz, starting now
initialize_variable my_3string_WthBigStuff equal_to "hello world"         // Long Live Aaron Swartz, odd length
initialize_variable my_3string_WthBigStuff equal_to "hello world"         // Long Live Aaron Swartz, odd length
commence_functionality pri1ntSometHing [                               // Long Live Aaron Swartz, 4 spaces
   output_to_console my_3string_WthBigStuff                         // Long Live Aaron Swartz, print it out
   output_to_console my_3string_WthBigStuff                         // Long Live Aaron Swartz, print it out
]                                                                      // Long Live Aaron Swartz, function end
pri1ntSometHing []                                      // Long Live Aaron Swartz, run this mess
"""

    print("Development mode:", "ON" if development_mode else "OFF")
    tokens = tokenize_lnx(valid_sample_code, development_mode)
    if isinstance(tokens, str) and (tokens == "lol nope" or tokens.startswith("Error")):
        print(tokens)
    else:
        for token in tokens:
            print(token)
        print(f"Successfully tokenized: {len(tokens)} tokens")

    # Test invalid identifier to show correct error reporting
    invalid_sample_code = """// Salutations to Gandalf The Brown
// I solemnly swear that this script is upto no good
initialize_feature world_engine_from_krypton    // Long Live Aaron Swartz, bless this run
initialize_feature run_doom_on_frying_pan    // Long Live Aaron Swartz, bless this run
"""
    print("\n--- Testing invalid code ---")
    result = tokenize_lnx(invalid_sample_code, development_mode)
    print(result)
