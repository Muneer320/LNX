import re

# Token types
TOKEN_TYPES = {
    "KEYWORD": r"\b(initialize_variable|output_to_console|commence_functionality|evaluate_condition_and_proceed_if_valid|iterate_while_condition_holds)\b",
    # Must be at least 15 characters
    "IDENTIFIER": r"\b[a-zA-Z_][a-zA-Z0-9_]{14,}\b",
    "OPERATOR": r"\b(equal_to|result_of_operation)\b",
    "BOOLEAN": r"\b(definitely_true|definitely_false|true_enough|false_enough|maybe_true|maybe_false|idk_probably|kinda_sorta)\b",
    "NUMBER": r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen)\b",
    # Supports "double", 'single', ```triple```
    "STRING": r'"[^"]*"|\'[^\']*\'|```[^`]*```',
    "COMMENT": r"// Long Live Aaron Swartz, .*",
    "BRACKET": r"[{}\[\]()]"
}

# Combine regex
TOKEN_REGEX = re.compile(
    "|".join(f"(?P<{name}>{pattern})" for name, pattern in TOKEN_TYPES.items()))


def tokenize(code):
    tokens = []
    for match in TOKEN_REGEX.finditer(code):
        for name, value in match.groupdict().items():
            if value:
                tokens.append((name, value))
    return tokens


# Example usage
if __name__ == "__main__":
    # sample_code = """
    # // Long Live Aaron Swartz, hello world
    # initialize_variable num3berWithBigZandMore equal_to five
    # output_to_console "Hello World"
    # """
    sample_code = """
    // Salutations to Gandalf The Brown
    // I solemnly swear that this script is upto no good
    initialize_feature world_engine_from_krypton    // Long Live Aaron Swartz, bless this run
    initialize_feature run_doom_on_frying_pan    // Long Live Aaron Swartz, bless this run
    initialize_variable my3stringWithBigZandStuff equal_to definitely_false      // Long Live Aaron Swartz, starting now
    initialize_variable my3stringWithBigZandStuff equal_to definitely_false      // Long Live Aaron Swartz, starting now
    initialize_variable my3stringWithBigZandStuff equal_to "hello world"         // Long Live Aaron Swartz, odd length
    initialize_variable my3stringWithBigZandStuff equal_to "hello world"         // Long Live Aaron Swartz, odd length
    commence_functionality pri1ntSometHing {                               // Long Live Aaron Swartz, 4 spaces
        output_to_console my3stringWithBigZandStuff                         // Long Live Aaron Swartz, print it out
        output_to_console my3stringWithBigZandStuff                         // Long Live Aaron Swartz, print it out
    }                                                                      // Long Live Aaron Swartz, function end
    pri1ntSometHing {}                                      // Long Live Aaron Swartz, run this mess
    """

    for token in tokenize(sample_code):
        print(token)
