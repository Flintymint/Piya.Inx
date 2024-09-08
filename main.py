import Operation

Operation.display()
while True:
    Operation.option()
    try:
        options=int(input("enter your choice : "))
    except:
        print("please input the number in interger format")
    if options ==1:
        Operation.buying()
    elif options == 2:
        Operation.Selling()
    elif options ==3:
        Operation.exit()
        break
    else:
        print("Invalid options. please select a correct option.")


