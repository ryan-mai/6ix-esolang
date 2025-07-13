"""
VarLang Operations and Operators
"""

MATH_OPERATIONS = {
    "addy": lambda x, y: x + y,      
    "chopped": lambda x, y: x - y,   
    "hella": lambda x, y: x * y,     
    "yute": lambda x, y: x / y,      
    "nize": lambda x, y: x % y,      
    "mans": lambda x, y: x ** y,     
    "two-twos": lambda x, y: x // y  
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