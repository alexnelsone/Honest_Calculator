a = int(input())
b = int(input())
h = int(input())


if h >= a:
    if h <= b:
        print('Normal')
    else:
        print('Excess')
else:
    print('Deficiency')