from input_data import get_answer
from main import main


def pars_rourte():
    start, finish, int_stop = get_answer()
    return main(start, finish)


if __name__ == '__main__':
    pars_rourte()
