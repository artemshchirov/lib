from random import randint as rnd
from pprint import pprint


def coin_tosses_variations(times: int) -> list:
    """
    Simulates coin tosses and save all possible outcomes of the toss

    Other way:
    # import itertools
    # for i in itertools.product([1,0], repeat=4):  # repeat: number of coin tosses
    #     print(i)

    :param times: number of coin tosses
    :return: list with all possible options for the result of a coin toss
    on the selected move and previous moves
    """
    results = []
    for toss in range(times):
        results.append([])
        for var in range(2 ** (toss + 1)):  # var=variation toss result
            results[toss].append([])
            coin = rnd(0, 1)  # 0=head, 1=tails
            results[toss][var].append(coin)
            for coin_add in range(toss):
                done = False
                while not done:
                    coin_next = rnd(0, 1)
                    results[toss][var].append(coin_next)
                    unique = True
                    for var_compare in range(len(results[toss]) - 1):
                        if results[toss][var] == results[toss][var_compare]:
                            results[toss][var].remove(coin_next)
                            unique = False
                            break
                    if unique:
                        done = True
                    else:
                        results[toss][var].remove(results[toss][var][len(results[toss][var]) - 1])
                        coin_new = rnd(0, 1)
                        results[toss][var].append(coin_new)
        if results[0][0][0] == results[0][1][0]:  # otherwise they can be the same
            results[0][0][0] = int(not results[0][1][0])
    return results


def count_chance(res: list, seq: str) -> float:
    """

    :param res:
    :param seq:
    :return:
    """
    digits_in = 0
    for symbol in seq:
        if symbol.isdigit():
            digits_in += 1

    seq_all = 0
    seq_in = 0
    for i in range(len(res)):
        if i == len(res) - 1:  # if count in one last toss, elif in all tosses - comment this line
            seq_in += str(res[i]).count(seq)
            for j in range(len(res[i])):
                if len(res[i][j]) >= digits_in:
                    seq_all += 1
                    # print(res[i][j], 'len:', len(res[i][j]))  # TEST

    print(f'\nall sequences: [{seq_all}]')
    print(f'sequence "{seq}"\n in all: [{seq_in}]')

    if seq_in > 0:
        percent = 100 / (seq_all / seq_in)
        if percent > 100:
            return 100
        else:
            return round(percent, 2)
    else:
        return 0


def main():
    """
    :param toss_times: Сколько раз бросить монет?
    :param search_sequence: Какую последовательность искать в результатах? 
    Количество символов не должно превышать количество бросков.
    Последовательность должна быть записана в формате "x, y, z".
    На небольших данных можно легко убедится в точности результатов
    """
    toss_times = 5
    search_sequence = "1, 0, 1, 1, 1"

    tosses = coin_tosses_variations(toss_times)
    chance = count_chance(tosses, search_sequence)

    print(f'chance: [{chance}%]\n')
    # pprint(tosses)


if __name__ == "__main__":
    main()
