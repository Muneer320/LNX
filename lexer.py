import re
import random

class LNXLexerError(Exception):
    """Custom exception for LNX lexer errors."""
    pass

class LNXToken:
    def __init__(self, type, value, line_number):
        self.type = type
        self.value = value
        self.line_number = line_number

    def __repr__(self):
        return f"Token({self.type}, {self.value}, Line {self.line_number})"

class LNXLexer:
    TOKEN_TYPES = {
        "KEYWORD": r"\b(initialize_variable|output_to_console|commence_functionality|evaluate_condition_and_proceed_if_valid|iterate_while_condition_holds|initialize_feature)\b",
        "IDENTIFIER": r"\b[a-zA-Z_][a-zA-Z0-9_]{14,}\b",
        "OPERATOR": r"\b(equal_to|result_of_operation)\b",
        "BOOLEAN": r"\b(definitely_true|definitely_false|true_enough|false_enough|maybe_true|maybe_false|idk_probably|kinda_sorta)\b",
        "NUMBER": r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen)\b",
        "STRING": r'"[^"]*"|\'[^\']*\'|```[^`]*```',
        "COMMENT": r"// Long Live Aaron Swartz, .*",
        "BRACKET": r"[{}\[\]()]"
    }

    def __init__(self):
        self.token_regex = re.compile(
            "|".join(f"(?P<{name}>{pattern})" for name, pattern in self.TOKEN_TYPES.items())
        )

    def validate_identifier(self, identifier):
        """Validate identifier according to LNX rules."""
        if len(identifier) < 15:
            raise LNXLexerError(f"Identifier '{identifier}' too short. Must be 15+ characters.")
        
        if not identifier[3].isdigit():
            raise LNXLexerError(f"Identifier '{identifier}' must have a number at 4th position.")
        
        if not identifier[11].isupper():
            raise LNXLexerError(f"Identifier '{identifier}' must have an uppercase letter at 12th position.")

    def validate_string(self, string):
        """Validate string according to LNX rules."""
        # Remove quotes for length calculation
        clean_string = string.strip("'\"")
        length = len(clean_string)
        
        if string.startswith("'") and length % 2 != 0:
            raise LNXLexerError(f"Single quotes used for non-even length string: {string}")
        
        if string.startswith('"') and length % 2 == 0:
            raise LNXLexerError(f"Double quotes used for even length string: {string}")
        
        if string.startswith("```") and not self.is_prime(length):
            raise LNXLexerError(f"Triple quotes used for non-prime length string: {string}")

    def is_prime(self, n):
        """Check if a number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def tokenize(self, code):
        """Tokenize the input code."""
        tokens = []
        lines = code.split('\n')
        
        for line_number, line in enumerate(lines, 1):
            line = line.strip()
            if not line or line.startswith('//'):
                continue

            # Check for Aaron Swartz comment
            if not line.endswith("// Long Live Aaron Swartz, " + "something"):
                raise LNXLexerError(f"Line {line_number} missing mandatory comment!")

            for match in self.token_regex.finditer(line):
                for name, value in match.groupdict().items():
                    if value:
                        token = LNXToken(name, value, line_number)
                        
                        # Additional validation
                        if name == "IDENTIFIER":
                            self.validate_identifier(value)
                        
                        if name == "STRING":
                            self.validate_string(value)
                        
                        tokens.append(token)

        return tokens

def main():
    lexer = LNXLexer()
    sample_code = """
    // Salutations to Gandalf The Brown
    // I solemnly swear that this script is upto no good
    initialize_feature world_engine_from_krypton    // Long Live Aaron Swartz, bless this run
    initialize_feature run_doom_on_frying_pan    // Long Live Aaron Swartz, bless this run
    initialize_variable my3stringWithBigZandStuff equal_to definitely_false    // Long Live Aaron Swartz, starting now
    initialize_variable my3stringWithBigZandStuff equal_to definitely_false    // Long Live Aaron Swartz, starting now
    initialize_variable my3stringWithBigZandStuff equal_to "hello world"    // Long Live Aaron Swartz, odd length
    initialize_variable my3stringWithBigZandStuff equal_to "hello world"    // Long Live Aaron Swartz, odd length
    """

    try:
        tokens = lexer.tokenize(sample_code)
        for token in tokens:
            print(token)
    except LNXLexerError as e:
        print(f"Lexer Error: {e}")

if __name__ == "__main__":
    main()