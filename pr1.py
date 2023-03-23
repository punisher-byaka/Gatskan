# Gatskan
Work = False
while Work != True:
    print("\nНачало работы")
    try:
        print("Введите количество операций")
        count = int(input())
        print("Введите первое число")
        first = int(input())
    except:
        print("Ты не прав!")
    while count != 0:
        print("Выберите действие!")
        print("1 - +")
        print("2 - -")
        print("3 - *")
        print("4 - /")
        print("5 - Степень")
        action = input()
        match action:
            case "1":
                print("Введите число для действия с ним")
                try:
                    next = int(input())
                except:
                    print("Ты не прав")
                first = first + next
            case "2":
                print("Введите число для действия с ним")
                try:
                    next = int(input())
                except:
                    print("Ты не прав")
                first = first - next
            case "3":
                print("Введите число для действия с ним")
                try:
                    next = int(input())
                except:
                    print("Ты не прав")
                first = first * next
            case "4":
                print("Введите число для действия с ним")
                try:
                    next = int(input())
                    first = first / next
                except:
                    print("Ты не прав")
            case "5":
                print("Введите число для действия с ним")
                try:
                    next = int(input())
                except:
                    print("Ты не прав")
                first = first ** next
            case _:
                print("Не было такого варианта...\n")
        print(f"\nПромежуточный результат {first}")
        count -= 1
    print(f"Конечный результат {first}")