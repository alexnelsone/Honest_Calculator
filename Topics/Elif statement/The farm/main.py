CHICKEN = 23
GOAT = 678
PIG = 1296
COW = 3848
SHEEP = 6769

money = int(input())

num_sheep = int(money / SHEEP)
num_cow = int(money / COW)
num_pig = int(money / PIG)
num_goat = int(money / GOAT)
num_chicken = int(money / CHICKEN)

if money < CHICKEN:
    print('None')
else:
    if num_sheep >= 1:
        print(f'{num_sheep} sheep')
    elif num_cow >= 1:
        if num_cow == 1:
            print(f'{num_cow} cow')
        else:
            print(f'{num_cow} cows')
    elif num_pig >= 1:
        if num_pig == 1:
            print(f'{num_pig} pig')
        else:
            print(f'{num_pig} pigs')
    elif num_goat >= 1:
        if num_goat == 1:
            print(f'{num_goat} goat')
        else:
            print(f'{num_goat} goats')
    elif num_chicken >= 1:
        if num_chicken == 1:
            print(f'{num_chicken} chicken')
        else:
            print(f'{num_chicken} chickens')
