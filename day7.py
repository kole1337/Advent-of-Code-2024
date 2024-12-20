from itertools import product


def evaluate_expression(numbers, ops):
    result = numbers[0]
    for i, op in enumerate(ops):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        elif op == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result


def is_valid_equation(test_value, numbers):
    ops = ['+', '*', '||']
    for combination in product(ops, repeat=len(numbers) - 1):
        if evaluate_expression(numbers, combination) == test_value:
            return True
    return False


def solve_calibration_from_file(filename):
    valid_sum = 0

    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(': ')
            if len(parts) == 2:
                test_value = int(parts[0])
                numbers = [int(x) for x in parts[1].split()]

                if is_valid_equation(test_value, numbers):
                    valid_sum += test_value

    return valid_sum

print(solve_calibration_from_file('input.txt'))