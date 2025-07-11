variables = {}
functions = {}

MATH_OPERATIONS = {
    "addy": lambda x, y: x + y,      # +
    "chopped": lambda x, y: x - y,   # -
    "hella": lambda x, y: x * y,     # *
    "yute": lambda x, y: x / y,      # /
    "nize": lambda x, y: x % y,      # %
    "mans": lambda x, y: x ** y,     # **
    "two-twos": lambda x, y: x // y  # //
}

COMPARISON_OPERATIONS = {
    "word": lambda x, y: x == y,
    "fam": lambda x, y: x != y,
    "wallahi": lambda x, y: x < y,
    "reach": lambda x, y: x <= y,
    "bussin": lambda x, y: x > y,
    "lick": lambda x, y: x >= y,
}

LOGICAL_OPERATIONS = {
    "based": lambda x, y: bool(x) and bool(y),
    "ratio": lambda x, y: bool(x) or bool(y),
    "mid": lambda x: not bool(x),
}

IDENTITY_OPERATIONS = {
    "like": lambda x, y: x is y,
    "aint": lambda x, y: x is not y,
}

def parse_value(value):
    """Parse a value string into the appropriate type"""
    if isinstance(value, (int, float)):
        return value
    if str(value).isdigit():
        return int(value)
    elif str(value).replace('.', '', 1).isdigit():
        return float(value)
    elif str(value).startswith('eh"') and str(value).endswith('"'):
        # Handle eh-string (f-string) interpolation
        expr = str(value)[3:-1]  # Remove eh" and ending "
        try:
            # Use variables as local context for interpolation
            return eval(f'f"""{expr}"""', {}, variables)
        except Exception:
            return str(value)
    elif str(value).startswith('"') and str(value).endswith('"'):
        return str(value)[1:-1]
    elif str(value) in variables:
        return variables[str(value)]
    else:
        # Try to parse as literal value if it's a simple string
        return value

def parse_expression(tokens):
    """Parse and evaluate an expression with operators"""
    if len(tokens) == 1:
        return parse_value(tokens[0])
    
    # Handle expressions with operators
    if len(tokens) >= 3:
        # Check for operator at position 1 (e.g., "x addy y")
        if tokens[1] in MATH_OPERATIONS:
            left = parse_value(tokens[0])
            op = tokens[1]
            
            # Handle chained operations
            if len(tokens) == 3:
                right = parse_value(tokens[2])
                if op == "addy":
                    # Handle string concatenation
                    if isinstance(left, str) or isinstance(right, str):
                        return str(left) + str(right)
                    else:
                        return MATH_OPERATIONS[op](left, right)
                else:
                    return MATH_OPERATIONS[op](left, right)
            else:
                # Multiple operations - handle left to right
                result = left
                i = 1
                while i < len(tokens) - 1:
                    if tokens[i] in MATH_OPERATIONS:
                        operator = tokens[i]
                        right_val = parse_value(tokens[i + 1])
                        
                        if operator == "addy":
                            # Handle string concatenation
                            if isinstance(result, str) or isinstance(right_val, str):
                                result = str(result) + str(right_val)
                            else:
                                result = MATH_OPERATIONS[operator](result, right_val)
                        else:
                            result = MATH_OPERATIONS[operator](result, right_val)
                        i += 2
                    else:
                        i += 1
                return result
    
    return None

def handle_assignment(tokens):
    var_name = tokens[1]
    
    if len(tokens) >= 5 and tokens[2] == "money" and tokens[3] == "up":
        operator = "money up"
        value = ' '.join(tokens[4:])
    elif len(tokens) >= 5 and tokens[2] == "funny" and tokens[3] == "up":
        operator = "funny up"
        value = ' '.join(tokens[4:])
    else:
        operator = tokens[2]
        value_tokens = tokens[3:]
        
        # Check if this is an expression with operators
        if len(value_tokens) >= 3 and any(token in MATH_OPERATIONS for token in value_tokens):
            parsed_value = parse_expression(value_tokens)
        else:
            value = ' '.join(value_tokens)
            parsed_value = parse_value(value)
    
    if parsed_value is None:
        print(f"no bizzy bap croski: {value}")
        return
    
    if operator == "fax": # =
        variables[var_name] = parsed_value
    elif operator == "money up": # +=
        if var_name in variables:
            variables[var_name] = MATH_OPERATIONS["addy"](variables[var_name], parsed_value)
        else:
            print(f"fam are you cooked: {var_name} is bare")
    elif operator == "funny up": # -=
        if var_name in variables:
            variables[var_name] = MATH_OPERATIONS["chopped"](variables[var_name], parsed_value)
        else:
            print(f"fam are you cooked: {var_name} is bare")
    elif operator == "cheesed": # *=
        if var_name in variables:
            variables[var_name] = MATH_OPERATIONS["hella"](variables[var_name], parsed_value)
        else:
            print(f"fam are you cooked: {var_name} is bare")
    elif operator == "mandem": # /=
        if var_name in variables:
            variables[var_name] = MATH_OPERATIONS["yute"](variables[var_name], parsed_value)
        else:
            print(f"fam are you cooked: {var_name} is bare")
    elif operator == "steeze": # %=
        if var_name in variables:
            variables[var_name] = MATH_OPERATIONS["nize"](variables[var_name], parsed_value)
        else:
            print(f"fam are you cooked: {var_name} is bare")
    elif operator == "dun": # **=
        if var_name in variables:
            variables[var_name] = MATH_OPERATIONS["mans"](variables[var_name], parsed_value)
        else:
            print(f"fam are you cooked: {var_name} is bare")
    elif operator == "bucktee": # //=
        if var_name in variables:
            variables[var_name] = MATH_OPERATIONS["two-twos"](variables[var_name], parsed_value)
        else:
            print(f"fam are you cooked: {var_name} is bare")
    else:
        print(f"Unknown assignment operator: {operator}")

def handle_comparison(tokens):
    # Syntax: real sh <left> <operator> <right>
    if len(tokens) != 5 or tokens[1] != "sh":
        print(f"Twin, City Boy JJ aint got {len(tokens)} word fam")
        return

    left = tokens[2]
    op = tokens[3]
    right = tokens[4]

    left_val = variables[left] if left in variables else parse_value(left)
    right_val = variables[right] if right in variables else parse_value(right)

    if left_val is None or right_val is None:
        print("Two two my word fam the word is 'real sh # <operator> #'")
        return

    # Try to convert both to float if possible for numeric comparison
    try:
        if (isinstance(left_val, (int, float)) or (isinstance(left_val, str) and left_val.replace('.', '', 1).lstrip('-').isdigit())) and \
           (isinstance(right_val, (int, float)) or (isinstance(right_val, str) and right_val.replace('.', '', 1).lstrip('-').isdigit())):
            left_val = float(left_val)
            right_val = float(right_val)
            # If both are ints, keep as int
            if left_val.is_integer():
                left_val = int(left_val)
            if right_val.is_integer():
                right_val = int(right_val)
    except Exception:
        pass

    if op in COMPARISON_OPERATIONS:
        try:
            result = COMPARISON_OPERATIONS[op](left_val, right_val)
            print(result)
        except TypeError:
            print(f"no bizzy bap croski: can't compare {type(left_val).__name__} and {type(right_val).__name__}")
    else:
        print(f"Are you good fam: {op}")

def handle_logical(tokens):
    # Syntax: real sh <left> <logical_op> <right> or real sh mid <value>
    if len(tokens) == 5 and tokens[1] == "sh":
        left = tokens[2]
        op = tokens[3]
        right = tokens[4]
        left_val = variables[left] if left in variables else parse_value(left)
        right_val = variables[right] if right in variables else parse_value(right)
        if left_val is None or right_val is None:
            print("no bizzy bap croski: logical op")
            return
        if op in LOGICAL_OPERATIONS and op != "mid":
            result = LOGICAL_OPERATIONS[op](left_val, right_val)
            print(result)
        else:
            print(f"Are you good fam: {op}")
    elif len(tokens) == 4 and tokens[1] == "sh" and tokens[2] == "mid":
        value = tokens[3]
        val = variables[value] if value in variables else parse_value(value)
        if val is None:
            print("no bizzy bap croski: logical mid")
            return
        print(LOGICAL_OPERATIONS["mid"](val))
    else:
        print("Twin, City Boy JJ aint got {} word fam".format(len(tokens)))

def handle_identity(tokens):
    # Syntax: real sh <left> <identity_op> <right>
    if len(tokens) == 5 and tokens[1] == "sh":
        left = tokens[2]
        op = tokens[3]
        right = tokens[4]
        left_val = variables[left] if left in variables else parse_value(left)
        right_val = variables[right] if right in variables else parse_value(right)
        if left_val is None or right_val is None:
            print("no bizzy bap croski: identity op")
            return
        if op in IDENTITY_OPERATIONS:
            result = IDENTITY_OPERATIONS[op](left_val, right_val)
            print(result)
        else:
            print(f"Are you good fam: {op}")
    else:
        print("croski are you dess (identity)")

def handle_variable(tokens):
    if len(tokens) >= 3:
        # Check for multi-word assignment operators
        is_assignment = False
        if len(tokens) >= 4 and tokens[2] in ["fax", "cheesed", "mandem", "steeze", "dun", "bucktee"]:
            is_assignment = True
        elif len(tokens) >= 5 and tokens[2] == "money" and tokens[3] == "up":
            is_assignment = True
        elif len(tokens) >= 5 and tokens[2] == "funny" and tokens[3] == "up":
            is_assignment = True
        
        if is_assignment:
            handle_assignment(tokens)
            return
        
        # Check for math expression assignment (e.g., "croski result x addy y")
        if len(tokens) >= 5 and any(token in MATH_OPERATIONS for token in tokens[3:]):
            var_name = tokens[1]
            expression_tokens = tokens[2:]
            result = parse_expression(expression_tokens)
            if result is not None:
                variables[var_name] = result
                return
        
        # Check for function call assignment (e.g., "croski sum run adder 10 20")
        if len(tokens) >= 4 and tokens[2] == "ahlie":
            var_name = tokens[1]
            func_result = handle_function_call(tokens[2:])
            if func_result is not None:
                variables[var_name] = func_result
                return
        
        # Original variable assignment logic
        var_name = tokens[1]
        value = ' '.join(tokens[2:])

        if value.startswith('ting(') and value.endswith(')'):
            inner_value = value[5:-1]
            
            if inner_value in variables:
                actual_value = variables[inner_value]
            else:
                if inner_value.isdigit():
                    actual_value = int(inner_value)
                elif inner_value.replace('.', '', 1).isdigit():
                    actual_value = float(inner_value)
                elif inner_value.startswith('"') and inner_value.endswith('"'):
                    actual_value = inner_value[1:-1]
                else:
                    actual_value = inner_value
            
            if isinstance(actual_value, int):
                result_type = "int"
            elif isinstance(actual_value, float):
                result_type = "float"
            elif isinstance(actual_value, str):
                result_type = "str"
            else:
                result_type = "wasteman"
            
            variables[var_name] = result_type
        elif value.isdigit():
            variables[var_name] = int(value)
        elif value.replace('.', '', 1).isdigit():
            variables[var_name] = float(value)
        elif value.startswith('"') and value.endswith('"'):
            variables[var_name] = value[1:-1]
        else:
            parsed_val = parse_value(value)
            if parsed_val is not None:
                variables[var_name] = parsed_val
            else:
                print(f"no bizzy bap croski: {value}")
    else:
        print("croski what are you doin")

def handle_print(tokens):
    # Support: allow it <var> [operator <var|number>]
    if len(tokens) == 3 and tokens[1] == "it":
        var_name = tokens[2]
        
        # Check if it's a quoted string first
        if var_name.startswith('"') and var_name.endswith('"'):
            print(var_name[1:-1])
            return
        
        # Check if it's a variable
        if var_name in variables:
            print(variables[var_name])
            return
        
        # Try to parse as a literal value
        try:
            val = parse_value(var_name)
            # Only print if it's not a function name (avoid printing function objects)
            if var_name in functions:
                print(f"fam are you cooked: {var_name}")
            else:
                print(val)
        except Exception:
            print(f"fam are you cooked: {var_name}")
            
    elif len(tokens) == 5 and tokens[1] == "it":
        left = tokens[2]
        op = tokens[3]
        right = tokens[4]
        left_val = variables[left] if left in variables else parse_value(left)
        right_val = variables[right] if right in variables else parse_value(right)
        if left_val is None or right_val is None:
            print(f"no bizzy bap croski: {left} {op} {right}")
            return
        if op in MATH_OPERATIONS:
            if op == "addy":
                # Handle string concatenation in print
                if isinstance(left_val, str) or isinstance(right_val, str):
                    print(str(left_val) + str(right_val))
                else:
                    print(MATH_OPERATIONS[op](left_val, right_val))
            else:
                print(MATH_OPERATIONS[op](left_val, right_val))
        else:
            print(f"Are you good fam: {op}")
    else:
        # Instead of error, print the argument as is (fallback)
        if len(tokens) >= 3 and tokens[1] == "it":
            print(' '.join(tokens[2:]))
        else:
            print("croski are you dess")

def handle_operators(tokens):
    if len(tokens) != 5 or tokens[1] != "sh":
        print(f"Twin, City Boy JJ aint got {len(tokens)} word fam")
        return
    
    def is_number(s):
        return s.isdigit() or s.replace('.', '', 1).isdigit()
    
    if not (is_number(tokens[2]) and is_number(tokens[4])):
        print("Two two my word fam the word is 'real sh # <operator> #'")
        return
    
    if '.' in tokens[2]:
        value_1 = float(tokens[2])
    else:
        value_1 = int(tokens[2])

    if '.' in tokens[4]:
        value_2 = float(tokens[4])
    else:
        value_2 = int(tokens[4])

    operator = tokens[3]
    
    if operator in MATH_OPERATIONS:
        result = MATH_OPERATIONS[operator](value_1, value_2)
        print(result)
    else:
        print(f"Are you good fam: {operator}")

def handle_function_definition(tokens):
    """Handle function definition: 'mans <name> takes <param1> <param2> ... does' followed by function body"""
    if len(tokens) < 5 or tokens[2] != "takes":
        print("wagwan fam, function syntax is 'mans <name> takes <params> does'")
        return None
    
    func_name = tokens[1]
    # Find where "does" appears
    does_index = -1
    for i, token in enumerate(tokens):
        if token == "does":
            does_index = i
            break
    
    if does_index == -1:
        print("wagwan fam, need 'does' at the end")
        return None
    
    # Extract parameters between "takes" and "does"
    params = tokens[3:does_index]
    
    functions[func_name] = {
        'params': params,
        'body': []
    }
    
    return func_name

def handle_function_call(tokens):
    """Handle function call: 'ahlie <func_name> <args>'"""
    if len(tokens) < 2:
        print("wagwan fam, need function name")
        return None
    
    func_name = tokens[1]
    args = tokens[2:] if len(tokens) > 2 else []
    
    if func_name not in functions:
        print(f"wagwan fam, function '{func_name}' not found")
        return None
    
    func_def = functions[func_name]
    
    if len(args) != len(func_def['params']):
        print(f"wagwan fam, expected {len(func_def['params'])} args, got {len(args)}")
        return None
    
    # Save current variable state
    saved_vars = variables.copy()
    
    # Set up parameters as local variables
    for param, arg in zip(func_def['params'], args):
        arg_val = parse_value(arg)
        # Ensure numeric strings are converted to numbers
        if isinstance(arg_val, str):
            if arg_val.isdigit():
                arg_val = int(arg_val)
            elif arg_val.replace('.', '', 1).isdigit():
                arg_val = float(arg_val)
        variables[param] = arg_val
    
    # Execute function body
    return_value = None
    for line in func_def['body']:
        tokens = line.split()
        if tokens and tokens[0] == "send":
            # Handle return statement
            if len(tokens) > 1:
                return_expr = ' '.join(tokens[1:])
                return_value = parse_value(return_expr)
                break
            else:
                return_value = None
                break
        else:
            # Execute the line
            execute_line(line)
    
    # Restore variable state
    variables.clear()
    variables.update(saved_vars)
    
    return return_value

def execute_line(line):
    """Execute a single line of code"""
    tokens = line.split()
    if not tokens:
        return
    
    cmd = tokens[0]
    if cmd == "croski":
        handle_variable(tokens)
    elif cmd == "allow":
        handle_print(tokens)
    elif cmd == "real":
        # Check for comparison, logical, or identity operation
        if len(tokens) == 5 and tokens[3] in COMPARISON_OPERATIONS:
            handle_comparison(tokens)
        elif len(tokens) == 5 and tokens[3] in LOGICAL_OPERATIONS and tokens[3] != "mid":
            handle_logical(tokens)
        elif len(tokens) == 4 and tokens[2] == "mid":
            handle_logical(tokens)
        elif len(tokens) == 5 and tokens[3] in IDENTITY_OPERATIONS:
            handle_identity(tokens)
        else:
            handle_operators(tokens)
    elif cmd == "ahlie":
        result = handle_function_call(tokens)
        if result is not None:
            print(result)

def run_varlang(code):
    lines = code.strip().split('\n')
    current_function = None
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        tokens = line.split()
        if not tokens:
            continue
        
        cmd = tokens[0]
        
        # Handle function definition
        if cmd == "mans":
            current_function = handle_function_definition(tokens)
            continue
        
        # Handle end of function
        if cmd == "bet" and current_function:
            current_function = None
            continue
        
        # If we're inside a function definition, add to body
        if current_function:
            functions[current_function]['body'].append(line)
            continue
        
        # Regular command execution
        if cmd == "croski":
            handle_variable(tokens)
        elif cmd == "allow":
            handle_print(tokens)
        elif cmd == "real":
            # Check for comparison, logical, or identity operation
            if len(tokens) == 5 and tokens[3] in COMPARISON_OPERATIONS:
                handle_comparison(tokens)
            elif len(tokens) == 5 and tokens[3] in LOGICAL_OPERATIONS and tokens[3] != "mid":
                handle_logical(tokens)
            elif len(tokens) == 4 and tokens[2] == "mid":
                handle_logical(tokens)
            elif len(tokens) == 5 and tokens[3] in IDENTITY_OPERATIONS:
                handle_identity(tokens)
            else:
                handle_operators(tokens)
        elif cmd == "ahlie":
            result = handle_function_call(tokens)
            if result is not None:
                print(result)
        else:
            print(f"waste man fam: {line}")

### TESTS ###

test_functions = """

mans greet takes name does
    croski greeting eh"Hello, {name}"
    send greeting
bet

ahlie greet "World"

mans g
croski sum ahlie add 10 20
allow it sum
"""

# The correct syntax for assigning the result of a function call to a variable and printing it is:
# croski sum ahlie add 10 20
# allow it sum

# This is already supported by the interpreter:
# - "croski sum ahlie add 10 20" assigns the result of add(10, 20) to variable 'sum'
# - "allow it sum" prints the value of 'sum'

# Example usage:
test_functions = """

mans add takes x y does
    croski result x addy y
    send result
bet

ahlie add 10 20
"""

if __name__ == "__main__":
    run_varlang(test_functions)