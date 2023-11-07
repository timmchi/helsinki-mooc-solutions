

def balanced_brackets(my_string: str):
    allowed_symbols = "()[]"
    stringo = "".join(symbol for symbol in my_string if symbol in allowed_symbols)
    if len(stringo) == 0:
        return True
    if not (stringo[0] in '(' and stringo[-1] in ')'):
        
        if not (stringo[0] in '[' and stringo[-1] in ']'):
            return False

    # remove first and last character
    return balanced_brackets(stringo[1:-1])
