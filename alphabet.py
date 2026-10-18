def check_alphabet(input_string):
    """
    Checks if the input string contains only alphabetic characters (A-Z, a-z):
    """
    if input_string.isalpha():
        return "The input string contains only alphabetic characters."
    else:
        return "The input string contains non-alphabetic characters."
    