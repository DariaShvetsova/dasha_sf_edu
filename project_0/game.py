import numpy as np


def game_core(number: int = 1) -> int:
    """Угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 1
    """
    при поиске загаданного числа генерируем 
    """
    predict = np.random.randint(1, 101)
    """
    используется алгоритм как в роботе пылесосе: если число меньше загаданного, прибавляем к нему по 6 каждый шаг, пока не дойдем до искомого числа.
    Если число больше загаданного, отнимаем от него по 7 каждый шаг, пока не дойдем до искомого числа. Вместо 6 и 7 может быть любая пара четного|нечетного чисел,
    однако данная комбинация одна из тех, что дает наименьшее количество итераций цикла.
    """

    while number != predict:
        count += 1
        if number > predict:
            predict += 6
        elif number < predict:
            predict -= 7
        else:
            break

    return count


def score_game(game) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        game ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = []
    np.random.seed(23)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")
    return score


# RUN
if __name__ == '__main__':
    score_game(game_core)
