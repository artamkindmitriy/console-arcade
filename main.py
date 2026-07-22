import random

def rock_paper_scissors():
    """Игра: Камень, Ножницы, бумага"""
    print("\n" * 5)
    choices = {"к": "камень", "н": "ножницы", "б": "бумага"}
    rules = {
        "камень": "ножницы",
        "ножницы": "бумага",
        "бумага": "камень"
    }

    print("\n--- ИГРА: КАМЕНЬ, НОЖНИЦЫ, БУМАГА ---")

    while True:
        key = input("Ваш ход: (к)амень, (н)ожницы, (б)умага или (в)ыход\n> ").lower()

        if key == "в":
            break
        if key not in choices:
            print("[ОШИБКА]: Неверный ввод")
            continue

        user_choice = choices[key]
        system_choice = random.choice(list(choices.values()))

        print(f"\n[ОБРАБОТКА]: Вы — {user_choice}. Система — {system_choice}")

        if user_choice == system_choice:
            res = "Ничья"
        elif rules[user_choice] == system_choice:
            res = "Победа"
        else:
            res = "Поражение"

        print(f"[РЕЗУЛЬТАТ]: {res}\n" + "-" * 35)


def guess_the_number():
    """Игра: Угадай число"""
    print("\n" * 5)
    print("\n --- ИГРА: УГАДАЙ ЧИСЛО --- ")

    system_choice = random.randint(1, 10)
    attempts = 1
    print("Система загадала число от 1 до 10")

    while True:
        print(f"\nПопытка [ {attempts} ]")
        user_input = input("Ваше число (или 'в' для выхода): \n> ").lower()

        if user_input == 'в':
            print("[ИНФО]: Возврат в главное меню...")
            break

        try:
            user_choice = int(user_input)

            if user_choice == system_choice:
                print(f"[УСПЕХ]: Вы угадали число {system_choice} за {attempts} попыток!")
                break

            if user_choice < system_choice:
                print("[ПОДСКАЗКА]: Загаданное число БОЛЬШЕ")
            else:
                print("[ПОДСКАЗКА]: Загаданное число МЕНЬШЕ")

            attempts += 1

        except ValueError:
            print("[ОШИБКА]: Введите число или 'в' для выхода")


def main_menu():
    """Главное меню"""
    print("╔" + "═" * 35 + "╗")
    print("║" + " " * 5 + "АРКАДА: ПАНЕЛЬ УПРАВЛЕНИЯ" + " " * 5 + "║")
    print("╚" + "═" * 35 + "╝")
    print()
    print("     [1] Камень, Ножницы, Бумага \n"
          "     [2] Угадай число\n"
          "     [3] Выход из системы")

    print()

    while True:
        try:
            print()
            choice_game = int(input("Введите номер команды: "))

            if choice_game == 1:
                rock_paper_scissors()
            elif choice_game == 2:
                guess_the_number()
            elif choice_game == 3:
                print("Вы вышли из системы. До скорой встречи!")
                break
            else:
                print("[ОШИБКА]: Введите верный номер (1-3)")
        except ValueError:
            print("[ОШИБКА]: Введите цифру")

main_menu()