variables = {}

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
    "and": lambda x, y: bool(x) and bool(y),
    "or": lambda x, y: bool(x) or bool(y),
    "not": lambda x: not bool(x),
}

IDENTITY_OPERATIONS = {
    "is": lambda x, y: x is y,
    "aint": lambda x, y: x is not y,
}

def parse_value(value):
    """Parse a value string into the appropriate type"""
    if value.isdigit():
        return int(value)
    elif value.replace('.', '', 1).isdigit():
        return float(value)
    elif value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    elif value in variables:
        return variables[value]
    else:
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
        value = ' '.join(tokens[3:])
    
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

    def is_number(s):
        return s.isdigit() or s.replace('.', '', 1).isdigit()

    left = tokens[2]
    op = tokens[3]
    right = tokens[4]

    left_val = variables[left] if left in variables else parse_value(left)
    right_val = variables[right] if right in variables else parse_value(right)

    if left_val is None or right_val is None:
        print("Two two my word fam the word is 'real sh # <operator> #'")
        return

    if op in COMPARISON_OPERATIONS:
        result = COMPARISON_OPERATIONS[op](left_val, right_val)
        print(result)
    else:
        print(f"Are you good fam: {op}")

def handle_logical(tokens):
    # Syntax: real sh <left> <logical_op> <right> or real sh not <value>
    if len(tokens) == 5 and tokens[1] == "sh":
        left = tokens[2]
        op = tokens[3]
        right = tokens[4]
        left_val = variables[left] if left in variables else parse_value(left)
        right_val = variables[right] if right in variables else parse_value(right)
        if left_val is None or right_val is None:
            print("no bizzy bap croski: logical op")
            return
        if op in LOGICAL_OPERATIONS and op != "not":
            result = LOGICAL_OPERATIONS[op](left_val, right_val)
            print(result)
        else:
            print(f"Are you good fam: {op}")
    elif len(tokens) == 4 and tokens[1] == "sh" and tokens[2] == "not":
        value = tokens[3]
        val = variables[value] if value in variables else parse_value(value)
        if val is None:
            print("no bizzy bap croski: logical not")
            return
        print(LOGICAL_OPERATIONS["not"](val))
    else:
        print("croski are you dess (logical)")

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
            print(f"no bizzy bap croski: {value}")
    else:
        print("croski what are you doin")

def handle_print(tokens):
    # Support: allow it <var> [operator <var|number>]
    if len(tokens) == 3 and tokens[1] == "it":
        var_name = tokens[2]
        if var_name in variables:
            print(variables[var_name])
        else:
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
            print(MATH_OPERATIONS[op](left_val, right_val))
        else:
            print(f"Are you good fam: {op}")
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

def run_varlang(code):
    lines = code.strip().split('\n')
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        tokens = line.split()
        if not tokens:
            continue
        cmd = tokens[0]
        if cmd == "croski":
            handle_variable(tokens)
        elif cmd == "allow":
            handle_print(tokens)
        elif cmd == "real":
            # Check for comparison, logical, or identity operation
            if len(tokens) == 5 and tokens[3] in COMPARISON_OPERATIONS:
                handle_comparison(tokens)
            elif len(tokens) in (4, 5) and (tokens[3] in LOGICAL_OPERATIONS or (len(tokens) == 4 and tokens[2] == "not")):
                handle_logical(tokens)
            elif len(tokens) == 5 and tokens[3] in IDENTITY_OPERATIONS:
                handle_identity(tokens)
            else:
                handle_operators(tokens)
        else:
            print(f"waste man fam: {line}")

### TESTS ###
test = """
# Basic variable assignment

croski hello 10
croski hello bucktee 4
allow it hello

# Comparison tests
real sh 5 word 5
"""

run_varlang(test)
