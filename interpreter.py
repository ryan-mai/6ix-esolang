"""
VarLang Interpreter Core
"""

from exceptions import VarLangError, throw_error
from operations import COMPARISON_OPERATIONS, LOGICAL_OPERATIONS, IDENTITY_OPERATIONS, MATH_OPERATIONS
from state import variables, functions
from handlers import (
    handle_variable, handle_print, handle_comparison, handle_logical, 
    handle_identity, handle_operators, handle_throw
)
from functions import handle_function_definition, handle_function_call

def handle_try_catch(lines, start_index):
    """Handle try-catch blocks: 'trust' ... 'nah' ... 'safe'"""
    try_body = []
    catch_body = []
    current_section = "try"
    i = start_index + 1

    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith('#'):
            i += 1
            continue

        tokens = line.split()
        if not tokens:
            i += 1
            continue

        if tokens[0] == "nah":
            current_section = "catch"
            i += 1
            continue
        elif tokens[0] == "safe":
            break

        if current_section == "try":
            try_body.append(line)
        elif current_section == "catch":
            catch_body.append(line)

        i += 1

    try:
        for line in try_body:
            execute_line(line)
    except VarLangError as e:
        variables['error_message'] = e.message
        variables['error_type'] = e.error_type
        for line in catch_body:
            execute_line(line)

    return i

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
    elif cmd == "waste":
        handle_throw(tokens)

def run_varlang(code):
    """Main interpreter function"""
    lines = code.strip().split('\n')
    current_function = None
    i = 0

    while i < len(lines):
        line = lines[i].strip()
        if not line or line.startswith('#'):
            i += 1
            continue

        tokens = line.split()
        if not tokens:
            i += 1
            continue

        cmd = tokens[0]

        if cmd == "trust":
            i = handle_try_catch(lines, i)
            i += 1
            continue

        if cmd == "mans":
            current_function = handle_function_definition(tokens)
            i += 1
            continue

        if cmd == "bet" and current_function:
            current_function = None
            i += 1
            continue

        if current_function:
            functions[current_function]['body'].append(line)
            i += 1
            continue

        try:
            if cmd == "croski":
                handle_variable(tokens)
            elif cmd == "allow":
                handle_print(tokens)
            elif cmd == "real":
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
            elif cmd == "waste":
                handle_throw(tokens)
            else:
                throw_error(f"Unknown command: {line}", "generic")
        except VarLangError as e:
            print(f"ERROR [{e.error_type}]: {e.message}")

        i += 1