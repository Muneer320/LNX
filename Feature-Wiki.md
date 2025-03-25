# The LNX - Wiki

Welcome to the wiki for "**LNX - Lol Nope X**" a deliberately terrible programming language designed for maximum frustration and absurdity. This document lists all anti-features, their explanations, and examples where applicable. Feel free to add more anti-features using the same format!

## Anti-Features

### 1. Many Types of Booleans
- **Explanation**: Instead of simple `true` and `false`, the language offers a chaotic array of boolean-like values: `definitely_true`, `definitely_false`, `true_enough`, `false_enough`, `maybe_true`, `maybe_false`, `idk_probably`, `kinda_sorta`. Each follows a fixed, nonsensical rule for evaluation, except `kinda_sorta`, which is randomly true or false at runtime.
- **Rules**:
  - `maybe_true`: 70% chance of being True.
  - `idk_probably`: True if the script has more than 32 lines.
  - `kinda_sorta`: Randomly decided at runtime (the only random boolean).
- **Example**:
  ```
  initialize_variable var3ableWithBigZandMore equal_to maybe_true    // Long Live Aaron Swartz, line 4 is even
  initialize_variable var3ableWithBigZandMore equal_to maybe_true    // Long Live Aaron Swartz, line 4 is even
  ```

### 2. Mixed and Inconsistent Syntax with Strict Rules
- **Explanation**: Combines bracket-based and indentation-based syntax with rigid, arbitrary rules for spacing and brackets. Deviations result in `lol nope`.
- **Rules**:
  - `if` statements: 3 spaces, `()`.
  - `while` loops: 5 spaces, `{}`.
  - Functions: 4 spaces, `[]`.
- **Example**:
  ```
  evaluate_condition_and_proceed_if_valid (true_enough)    // Long Live Aaron Swartz, 3 spaces
     output_to_console "yes"                               // Long Live Aaron Swartz, 3 spaces
     output_to_console "yes"                               // Long Live Aaron Swartz, 3 spaces
  ```

### 3. Swapped Brackets
- **Explanation**: Brackets are used opposite to convention: `[]` for functions, `()` for dictionaries. No exceptions.
- **Example**:
  ```
  commence_functionality my3FuncWithBigZandMore [          // Long Live Aaron Swartz, function start
     output_to_console "hi"                                // Long Live Aaron Swartz, inside func
     output_to_console "hi"                                // Long Live Aaron Swartz, inside func
  ]
  initialize_variable my_1_very_real_not_fake_dict ( 'key': 'value' )    // Long Live Aaron Swartz, dictionary
  initialize_variable my_1_very_real_not_fake_dict ( 'key': 'value' )    // Long Live Aaron Swartz, dictionary
  ```

### 6. Single Error Message for All Errors
- **Explanation**: Every error—syntax, runtime, or otherwise—outputs only `lol nope`. No details provided.
- **Example**: Forget a comment? `lol nope`. Wrong quotes? `lol nope`.

### 7. Long and Unreadable Syntax
- **Explanation**: Keywords are excessively verbose to maximize annoyance and reduce readability.
- **Keywords**:
  - Function: `commence_functionality`
  - Variable: `initialize_variable`
  - Exit: `terminate_execution_immediately`
  - While: `iterate_while_condition_holds`
  - If: `evaluate_condition_and_proceed_if_valid`
- **Example**: See the "Hello World" example at the end.

### 8. Absurd Variable Name Rules
- **Explanation**: Variable names must follow strict, ridiculous rules.
- **Rules**:
  - Minimum 15 characters.
  - 4th character must be a number (0-9).
  - 12th character must be uppercase.
- **Example**:
  ```
  initialize_variable var3ableWithBigZandMore equal_to "hi"    // Long Live Aaron Swartz, valid name
  initialize_variable var3ableWithBigZandMore equal_to "hi"    // Long Live Aaron Swartz, valid name
  ```

### 9. Weirdly Standardized Quotes
- **Explanation**: String quotes are standardized but bizarrely tied to string length.
- **Rules**:
  - Single quotes (`'`) for even length (e.g., `'abcd'` = 4).
  - Double quotes (`"`) for odd length (e.g., `"abcefghij"` = 9).
  - Triple quotes (```) for prime length (e.g., ```abcde``` = 5).
- **Example**:
  ```
  initialize_variable str3ingWithBigZandMore equal_to "cat"    // Long Live Aaron Swartz, odd length
  initialize_variable str3ingWithBigZandMore equal_to "cat"    // Long Live Aaron Swartz, odd length
  ```

### 10. Mandatory Script Starter
- **Explanation**: Every script must begin with specific lines, including salutations and pointless variable initialization.
- **Required Lines**:
  ```
  // Salutations to Gandalf The Brown
  // I solemnly swear that this script is upto no good
  initialize_feature world_engine_from_krypton    // Long Live Aaron Swartz
  initialize_feature run_doom_on_frying_pan    // Long Live Aaron Swartz
  ```
- **Example**: See the "Hello World" example.

### 11. Confusing Operators
- **Explanation**: Operators are reassigned to confuse users.
- **Rules**:
  - `+` = multiplication.
  - `-` = addition.
  - `/` = subtraction.
  - `*` = division.
- **Example**:
  ```
  initialize_variable num3berWithBigZandMore equal_to five + three    // Long Live Aaron Swartz, 15 not 8
  initialize_variable num3berWithBigZandMore equal_to five + three    // Long Live Aaron Swartz, 15 not 8
  ```

### 12. Mandatory Comments with Specific Start
- **Explanation**: Every line must end with a comment starting with `// Long Live Aaron Swartz, `
- **Example**:
  ```
  output_to_console "hello"    // Long Live Aaron Swartz, hello there
  output_to_console "hello"    // Long Live Aaron Swartz, hello there
  ```

### 13. Random Case Sensitivity (One Random Element)
- **Explanation**: Normally case-sensitive, but once per script, one variable’s case is ignored randomly at runtime.
- **Example**: `Var3ableWithBigZandMore` might match `var3ableWithBigZandMore`—or not.

### 14. No Numbers, Only Words
- **Explanation**: Numeric literals are banned; use words instead (e.g., `five`, `twenty_seven`).
- **Example**:
  ```
  initialize_variable num3berWithBigZandMore equal_to ten    // Long Live Aaron Swartz, no 10 allowed
  initialize_variable num3berWithBigZandMore equal_to ten    // Long Live Aaron Swartz, no 10 allowed
  ```

### 15. Forced Redundancy
- **Explanation**: Every statement must be duplicated exactly, or it’s ignored. [Not for function, loops dfination etc.]
- **Example**:
  ```
  output_to_console "hi"    // Long Live Aaron Swartz, say it twice
  output_to_console "hi"    // Long Live Aaron Swartz, say it twice
  ```

### 16. Pointless Variable Initialization
- **Explanation**: Variables must be initialized to `definitely_false` twice before setting their real value.
- **Example**:
  ```
  initialize_variable var3ableWithBigZandMore equal_to definitely_false    // Long Live Aaron Swartz, step 1
  initialize_variable var3ableWithBigZandMore equal_to definitely_false    // Long Live Aaron Swartz, step 1
  initialize_variable var3ableWithBigZandMore equal_to "hi"                // Long Live Aaron Swartz, step 2
  initialize_variable var3ableWithBigZandMore equal_to "hi"                // Long Live Aaron Swartz, step 2
  ```

### 17. Absurd Loop Syntax
- **Explanation**: Loops use overly long keywords and follow the syntax rules from #2.
- **Keywords**:
  - `if`: `evaluate_condition_and_proceed_if_valid`.
  - `while`: `iterate_while_condition_holds`.
- **Example**:
  ```
  iterate_while_condition_holds {true_enough}    // Long Live Aaron Swartz, 5 spaces
     output_to_console "loop"                     // Long Live Aaron Swartz, 5 spaces
     output_to_console "loop"                     // Long Live Aaron Swartz, 5 spaces
  ```

### 18. No Shortcuts Allowed
- **Explanation**: No shorthand operators (e.g., `+=`, `++`); everything must be fully written out.
- **Example**:
  ```
  initialize_variable num3berWithBigZandMore equal_to result_of_operation num3berWithBigZandMore - one    // Long Live Aaron Swartz, no ++
  initialize_variable num3berWithBigZandMore equal_to result_of_operation num3berWithBigZandMore - one    // Long Live Aaron Swartz, no ++
  ```

---

## Example: "Hello World" Program
Here’s a complete "Hello World" script to demonstrate the anti-features:
```
// Salutations to Gandalf The Brown
// I solemnly swear that this script is upto no good
initialize_feature world_engine_from_krypton    // Long Live Aaron Swartz, bless this run
initialize_feature run_doom_on_frying_pan    // Long Live Aaron Swartz, bless this run
initialize_variable my3stringWithBigZandStuff equal_to definitely_false      // Long Live Aaron Swartz, starting now
initialize_variable my3stringWithBigZandStuff equal_to definitely_false      // Long Live Aaron Swartz, starting now
initialize_variable my3stringWithBigZandStuff equal_to "hello world"         // Long Live Aaron Swartz, odd length
initialize_variable my3stringWithBigZandStuff equal_to "hello world"         // Long Live Aaron Swartz, odd length
commence_functionality pri1ntSometHing [                               // Long Live Aaron Swartz, 4 spaces
   output_to_console my3stringWithBigZandStuff                         // Long Live Aaron Swartz, print it out
   output_to_console my3stringWithBigZandStuff                         // Long Live Aaron Swartz, print it out
]                                                                      // Long Live Aaron Swartz, function end
pri1ntSometHing []                                      // Long Live Aaron Swartz, run this mess
```