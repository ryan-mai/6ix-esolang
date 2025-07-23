<<<<<<< HEAD
# VarLang Interpreter

A modular Python interpreter for the VarLang programming language with authentic slang syntax.
=======
# 6ix Esolang Interpreter

[Official Documentation](https://ryan-mai.github.io/6ix-esolang/)
[Official Interpreter](https://6ix-esolang-b286n01te-ryan-mais-projects.vercel.app/)

A modular Python interpreter for the 6ix Esolang based in Toronto.
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181

## Project Structure

```
slang_lang/
├── main.py              # Main entry point
├── interpreter.py       # Core interpreter logic
├── exceptions.py        # Exception classes
├── operations.py        # Operation mappings
├── state.py            # Global state management
├── handlers.py         # Command handlers
├── functions.py        # Function handling
├── utils.py            # Utility functions
└── README.md           # This file
```

## Usage

### Interactive Mode
Run the interpreter in interactive mode:
```bash
python main.py
```

### File Mode
<<<<<<< HEAD
Run a VarLang file:
```bash
python main.py your_file.vl
=======
Run a 6ix Esolang file:
```bash
python main.py your_file.six
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181
```

## Module Descriptions

### main.py
- Entry point for the interpreter
- Handles command-line arguments
- Provides interactive mode
- Manages file execution

### interpreter.py
- Core interpreter logic
- Main execution loop
- Try-catch block handling
- Line-by-line execution

### exceptions.py
- `VarLangError` class for error handling
- Multiple error types: `VarLangMathError`, `VarLangVariableError`, `VarLangFunctionError`
- `throw_error()` function for error handling

### operations.py
- Operation mappings with lambda functions:
  - Math operations: `addy`, `chopped`, `hella`, `yute`, `nize`, `mans`, `two-twos`
  - Comparison operations: `word`, `fam`, `wallahi`, `reach`, `bussin`, `lick`
  - Logical operations: `based`, `ratio`, `mid`
  - Identity operations: `like`, `aint`

### state.py
- Global variables storage
- Global functions storage
- Error handlers storage

### handlers.py
<<<<<<< HEAD
- Command handlers for all VarLang operations:
=======
- Command handlers for all 6ix Esolang operations:
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181
  - Variable assignment (`croski`)
  - Print statements (`allow it`)
  - Comparisons (`real sh`)
  - Logical operations
  - Arithmetic operations
  - Error throwing (`waste`)

### functions.py
- Function definition handling (`mans ... takes ... does`)
- Function call handling (`ahlie`)
- Function body execution with return values (`send`)

### utils.py
- Value parsing functions
- Expression evaluation
- String interpolation support

<<<<<<< HEAD
## VarLang Syntax Examples
=======
## 6ix Esolang Syntax Examples
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181

```varlang
# Variable assignment
croski x fax 10
croski y fax 20

# Print statements
allow it x
allow it "Hello World"

# Arithmetic operations
croski sum x addy y
allow it sum

croski product x hella y
allow it product

# Comparisons
real sh x wallahi y
real sh x bussin y

# Logical operations
real sh x based y
real sh mid x

# Functions
mans add_numbers takes a b does
    croski result a addy b
    send result
bet

# Function calls
ahlie add_numbers 5 15

# Try-catch blocks
trust
    croski z fax 0
    croski result x yute z
    allow it result
nah
    allow it "Caught error:"
    allow it error_message
    allow it error_type
safe

# Error throwing
waste "Something went wrong"
waste math "Division by zero"
```

## Error Handling

The interpreter provides comprehensive error handling with custom error types:
<<<<<<< HEAD
- `math`: Math operation errors
- `variable`: Variable-related errors  
- `function`: Function-related errors
- `generic`: General errors
=======
- `math`: Math operation errors 👨‍🔬
- `variable`: Variable-related errors ❓
- `function`: Function-related errors 🎊
- `generic`: General errors 🧬
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181

## Slang Syntax Reference

### Variables
<<<<<<< HEAD
- `croski var_name fax value` - Basic assignment
- `croski var_name money up value` - Add to existing variable
- `croski var_name funny up value` - Subtract from existing variable
- `croski var_name cheesed value` - Multiply with existing variable
- `croski var_name mandem value` - Divide existing variable
- `croski var_name steeze value` - Modulo with existing variable
- `croski var_name dun value` - Power with existing variable
- `croski var_name bucktee value` - Floor division with existing variable

### Math Operations
- `addy` - Addition
- `chopped` - Subtraction  
- `hella` - Multiplication
- `yute` - Division
- `nize` - Modulo
- `mans` - Power
- `two-twos` - Floor division

### Comparisons
- `word` - Equal to
- `fam` - Not equal to
- `wallahi` - Less than
- `reach` - Less than or equal to
- `bussin` - Greater than
- `lick` - Greater than or equal to
=======
- `croski var_name fax value` - Basic assignment (`=`)
- `croski var_name money up value` - Add to existing variable (`+=`)
- `croski var_name funny up value` - Subtract from existing variable (`-=`)
- `croski var_name cheesed value` - Multiply with existing variable (`*=`)
- `croski var_name mandem value` - Divide existing variable (`/=`)
- `croski var_name steeze value` - Modulo with existing variable (`%=`)
- `croski var_name dun value` - Power with existing variable (`**=`)
- `croski var_name bucktee value` - Floor division with existing variable (`//=`)

### Math Operations
- `addy` - Addition (`+`)
- `chopped` - Subtraction (`-`)
- `hella` - Multiplication (`*`)
- `yute` - Division (`/`)
- `nize` - Modulo (`%`)
- `mans` - Power (`**`)
- `two-twos` - Floor division (`//`)

### Comparisons
- `word` - Equal to (`==`)
- `fam` - Not equal to (`!=`)
- `wallahi` - Less than (`>`)
- `reach` - Less than or equal to (`>=`)
- `bussin` - Greater than (`<`)
- `lick` - Greater than or equal to (`<=`)
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181

### Logical Operations
- `based` - AND
- `ratio` - OR
- `mid` - NOT

### Functions
- `mans func_name takes param1 param2 does` - Function definition
- `ahlie func_name arg1 arg2` - Function call
- `send value` - Return value from function

### Control Flow
- `trust ... nah ... safe` - Try-catch blocks
<<<<<<< HEAD
- `waste message` - Throw errors 
=======
- `waste message` - Throw errors 
>>>>>>> e1c1f4a89b85d9d4f7630d921559f2eb950a1181
