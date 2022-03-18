print('''
1. know about numbers binary.
2. calculation in binary.
3. Exit.
''')
select=int(input("input your option: "))

if select == 1:

    fb=int(input("input your first binary number: "))

    print(bin(fb)+" this binary of ",fb)

elif select==2:

    print("1.+ 2.- 3./ 4.*")
    aritop=int(input("input your arithm..: "))
    fb=int(input("input your first binary number: "))


    if aritop==1:
        # fb=int(input("input your first binary number: "))
        sb=int(input("input your second binary number: "))

        print(bin(sb+fb)+" this binary of ",sb+fb)

    if aritop==2:
        # fb=int(input("input your first binary number: "))
        sb=int(input("input your second binary number: "))

        print(bin(sb-fb)+" this binary of ",sb+fb)

    if aritop==3:
        # fb=int(input("input your first binary number: "))
        sb=int(input("input your second binary number: "))

        print(bin(sb/fb)+" this binary of ",sb+fb)

    if aritop==4:
        # fb=int(input("input your first binary number: "))
        sb=int(input("input your second binary number: "))
        print(bin(sb*fb)+" this binary of ",sb+fb)
else:
    exit()
