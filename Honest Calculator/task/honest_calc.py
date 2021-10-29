import sys
import operator

loop = True
keep_going = False
VALID_OPERS = '+, -, *, /'
memory = '0'
result = 0.0

message = {
    0: "Enter an equation",
    1: "Do you even know what numbers are? Stay focused!",
    2: "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    3: "Yeah... division by zero. Smart move...",
    4: "Do you want to store the result? (y / n):",
    5: "Do you want to continue calculations? (y / n):",
    6: " ... lazy",
    7: " ... very lazy",
    8: " ... very, very lazy",
    9: "You are",
    10: "Are you sure? It is only one digit! (y / n)",
    11: "Don't be silly! It's just one number! Add to the memory? (y / n)",
    12: "Last chance! Do you really want to embarrass yourself? (y / n)"
 }

msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

msgs = [msg_10, msg_11, msg_12]
msg_index = 0

div_by_zero = False

ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.truediv}


def get_input():
    return input(message[0])


def convert_to_number(num):
    if num.isalpha():
        if num in 'm, M':
            num = memory
        else:
            num = num
    elif '.' in num:
        num = float(num)
    else:
        num = int(num)
    return num


def is_number(num):
    if isinstance(num, (float, int)):
        return True
    else:
        return False


def is_valid_oper(oper):
    if oper in VALID_OPERS:
        return True
    else:
        return False


def store_result(result):
    answer = input(message[4])
    if answer == 'y' or answer == 'Y':
        if is_one_digit(result):
            msg_index = 10
            while msg_index < len(message):
                answer = print_msg(msg_index)
                if answer.lower() == 'y':
                    msg_index += 1
                    if msg_index == len(msgs):
                        memory = str(result)
                else:
                    msg_index = len(msgs) + 1
                    return False
        return True
    else:
        return False


def continue_calc():
    answer = input(msg_5)
    if answer == 'y' or answer == 'Y':
        return True
    else:
        return False


def check_for_m(num):
    if num in 'm, M':
        return memory
    else:
        return num


def is_one_digit(v):
    if v % 1 != 0:
        return False
    elif -10 < v < 10 and isinstance(v, (int, float)):
        return True
    else:
        return False


def check_div_zero(y, oper):
    if oper == '/' and y == 0:
        return True


def calculate(x, y, oper):
    return float(ops[oper](x, y))


def check(x, y, oper):
    msg = ''
    if is_one_digit(x) and is_one_digit(y):
        msg = msg + msg_6
    if x == 1 or y == 1 and oper == '*':
        msg = msg + msg_7
    if x == 0 or y == 0 and (oper in '*, +, -'):
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)
        return True


def print_msg(msg_index):
    return input(message[msg_index])


while loop:
    calc = get_input().split()
    x, oper, y = calc

    x = check_for_m(x)
    y = check_for_m(y)

    x = convert_to_number(x)
    y = convert_to_number(y)

    if not is_number(x) or not is_number(y):
        print(msg_1)
        pass

    if check(x, y, oper):
        if not is_valid_oper(oper):
            print(msg_2)
            pass

        if check_div_zero(y, oper):
            print(msg_3)
            div_by_zero = False
            continue
        else:
            result = calculate(x, y, oper)
            print(result)

        if store_result(result):
            if is_one_digit(result):
                msg_index = 0
                while msg_index < len(msgs):
                    answer = print_msg(msg_index)
                    if answer.lower() == 'y':
                        msg_index += 1
                        if msg_index == len(msgs):
                            memory = str(result)
                    else:
                        msg_index = len(msgs) + 1
                if continue_calc():
                    continue
                else:
                    sys.exit()
            else:
                memory = str(result)

        if continue_calc():
            continue
        else:
            sys.exit()

    result = calculate(x, y, oper)
    print(float(result))
    if store_result(result):
        memory = str(result)
        if continue_calc():
            pass
        else:
            sys.exit()
    else:
        # memory = 0
        if continue_calc():
            pass
        else:
            sys.exit()