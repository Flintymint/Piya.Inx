
def lapdisplay():#to display Laptops and its details    
    print("")
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("S_No","  ","Laptop Name","\t      ","Company","\t       ","Price","\t    ","Quantity","\t\t", "Processor","\t\t ","GPU")
    print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    txtfile = open("laptop.txt","r")
    SN = 1
    for line in txtfile:        
        print(SN,"\t"+line.replace(",","\t\t"))#to replace "," with a gap
        SN = SN + 1
    print("\n")
    txtfile.close()

def dictionary():#to create dictionary for laptops
    txtfile=open("laptop.txt","r")
    laptops={}
    laptops_SN =1
    for line in txtfile:
        line = line.replace("\n"," ")#to replace "" with"" 
        laptops.update({laptops_SN:(line.split(","))})
        laptops_SN +=1
    txtfile.close()
    return laptops

def validSN():#to check if the S.N is valid or not
    ValidSN=False
    while ValidSN == False:
        try:
            InputSn=int(input("Please!! Input serial no. (S.N) of the Laptop you want to buy : "))
            ValidSN = True
        except:
            print("\n")
            print("Invalid selection please select properly")
            print("\n")
    while InputSn <=0 or InputSn>len(dictionary()):
        print("\n The S.N is not valid please input a proper value")
        InputSn=int(input("Enter the S.N of the laptop you want to buy: "))
    print("\n")
    print("The laptop is available")
    print("\n")
    return InputSn