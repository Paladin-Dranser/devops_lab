import re


def calculate(number1: int, number2: int, operation: str) -> int:
    """Calculate result"""
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    elif operation == '/':
        return number1 / number2


def is_correct_equation(equation: str) -> str:
    regex_match = re.match(r'(-?\d+)([*/+-])(-?\d+)=(-?\d+)', equation)
    if regex_match:
        result = calculate(
            int(regex_match.group(1)),
            int(regex_match.group(3)),
            regex_match.group(2)
        )

        if int(regex_match.group(4)) == result:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'ERROR'


if __name__ == '__main__':
    print(is_correct_equation(input('Enter an equation: ')))
