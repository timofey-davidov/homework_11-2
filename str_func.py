def input_function():
    """Принимает от пользователя строку, возвращает ее в верхнем регистре"""
    word = input()
    return word.upper()

def capitalize_function():
    """Принимает от пользователя строку, возвращает ее в нижнем регистре с
    первыми буквами в верхнем регистре"""
    word = input()
    return word.lower().capitalize()

# исправляем какие-то баги
