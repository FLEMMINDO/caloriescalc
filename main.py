
from colorama import init, Fore, Back, Style
init(autoreset=True)


def solve(whateat, weight60d, weight90d, dictionary):
    for a in whateat:
        weight60d -= dictionary[a]
        weight90d -= dictionary[a]
    if weight60d <= 0:
        print(Fore.GREEN + 'выполнил норму за 60 дней')
    else:
        print(Fore.RED + 'козёл, для 60 дней,' + ' употреби ещё ' + str(weight60d))
    if weight90d <= 0:
        print(Fore.GREEN + 'выполнил норму за 90 дней')
    else:
        print(Fore.RED + 'козёл, для 90 дней,' + ' употреби ещё ' + str(weight90d))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    food = {
        'пельмени': 275,
        'дошик': 440,
        'макпоф': 196,
        'пицца': 2000,
        'эрмигурт': 117,
        'кола': 42,
        'вода': 200,
        'йогурт': 68,
        'цезарьролл': 552,
        'картподер': 331,
        'бутикиз5': 260,
        'сырокчудо': 423,
        'кирики': 380,
        'сидр': 50,
        'сосискавтесте': 270,
        'сэндвичсамокат': 267,
        'котспюрсамокат': 375,
        'гуляшсамокат': 512,
        'сыроксамокат': 390,
    }

    print('-----------------')
    print(Fore.BLUE + 'СПИСОК')
    for a in food:
        print(a)
    print('-----------------')

    to60by90days = 3150
    to60by60days = 3550

    print('-----------------')

    print(Fore.RED + 'че ёл?')
    print('')

    whatdidieat = [str(i) for i in input().split()]

    print('-----------------')
    print(Fore.BLUE + '-----------------')

    solve(whatdidieat, to60by60days, to60by90days, food)

    print(Fore.BLUE + '-----------------')
    print('-----------------')