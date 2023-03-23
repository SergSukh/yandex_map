from constants import QUESTIONS


def get_answer(param):
    sym = input(f'Введите {param}:')
    if sym:
        return sym
    return None


def get_response(param):
    QUESTIONS[param] = []
    w = True
    while w:
        if param != 'заезд':
            w = False
        sym = input(f'Введите {param}:')
        if not sym:
            w = False
        QUESTIONS[param].append(sym)


def get_answer():
    for question in QUESTIONS:
        get_response(question)



if __name__ == '__main__':
    print(get_answer())