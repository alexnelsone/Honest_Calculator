x = float(input())
y = float(input())




origin = 0

if x == y == origin:
    print("It's the origin!")
elif origin in (x, y):
    print('One of the coordinates is equal to zero!')
else:
    if x < origin and y < origin:
        print('III')
    elif x < origin and y > origin:
        print('II')
    elif x > origin and y > origin:
        print('I')
    else:
        print('IV')