def main():
    # Drake Bellessa
    print("Python Syntax Guide")
    variables()
    strings()
    loops()
    sequences()

def variables():
    print("-----Variables-----")
    x = 7
    b = "Bob"
    print(x+3)
    print(b+3)
    print(type(x))
    print(type(b))

def strings():
    print("-----Strings-----")
    str1 = "Can't"
    str2 = 'Dave'
    str3 = '''Can use ' or " or even separate lines '''
    print(str1)
    print(str2)
    print(str3)
    x = 42
    str4 = f"x equals {x}. Fun."
    print(str4)

def loops():
    x = 0
    while True:
        x = x + 1
        if x > 5:
            break
    print(f"X is equal to {x}")

    for k in range(5):
        print(k)

    total = 1
    for k in range(1, 101):
        total = total + k
    print(total)

def sequences():
    print("-----Sequences")
    my_list = [4, 5, 6, 7]
    print(my_list)
    my_list[2] = 99
    print(my_list)
    my_list.append(1000)
    print(my_list)
    print(f"The length of the list is {len(my_list)}")
    for k in range(len(my_list)):
        my_list[k] = my_list[k] + 10
        my_list[k] += 10
    print(my_list)

    product = 1
    for k in range(len(my_list)):
        product = product * my_list[k]
    print(product)

    main()