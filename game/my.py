def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        raise ValueError("Error: Too many problems.")
    if check(problems):
        pass

    return problems


def check(problems):
    for problem in problems:
        if not problem.index("+") or not problem.index("-"):
            pass


print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')