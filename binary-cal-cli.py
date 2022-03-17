print('''
1. know about numbers binary.
2. calculation in binary.
> Exit (press the (ctrl + ^c / cmd+^c) from the keyboard).
''')
select=int(input("input your option: "))

fb=int(input("input your first binary number: "))

if select == 1:

    print(bin(fb)+" this binary of ",fb)

elif select==2:

    print("1.+ 2.- 3./ 4.*")

    aritop=int(input("input your arithm..: "))

    if aritop==1:

        sb=int(input("input your second binary number: "))

        print(bin(sb+fb)+" this binary of ",sb+fb)

    if aritop==2:

        sb=int(input("input your second binary number: "))

        print(bin(sb-fb)+" this binary of ",sb+fb)

    if aritop==3:

        sb=int(input("input your second binary number: "))

        print(bin(sb/fb)+" this binary of ",sb+fb)

    if aritop==4:

        sb=int(input("input your second binary number: "))

        print(bin(sb*fb)+" this binary of ",sb+fb)
else:
    print("you are exiting from the tool...(because your have written wrong option)")
    exit()