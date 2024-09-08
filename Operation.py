import datetime
import write
import read
def display():#to display the welcome message
    print("")
    print("")
    print("\t\t\t\t\tPIYA.Inx")
    print("----------------------------------------------\t\t\t\t-----------------------------------------------------")
    print("\t\t\t\t     Welcome to PIYA.Inx")
    print("")  

def option():#to display the options
    print("Please select one option:")
    print("If you want to buy any of our laptops? Press 1 ")
    print("If you want to sell your Laptop? Press 2 ")
    print("You would like to leave? Press 3")
    print("\n")

def buying():#to buy the laptop
    print("Let the buying begin")
    print("\n")
    read.lapdisplay()
    moreBuying =True
    boughtLaptop=[]
    brandoflaptop=[]
    buyingPrice=[]
    BoughtQuantity=[]
    Total=0
    TQuantity=0
    while moreBuying :
        InputSn=read.validSN()
        try:
            Quantity=int(input("Enter the quantity of Laptops : "))
            BoughtQuantity.append(Quantity)
            print("\n")
        except:
            print("Enter a valid quantity")
        laptops=Quantity_updater(InputSn,Quantity)
        file_update(laptops)
        
        TQuantity += Quantity
        price=float((laptops[InputSn][2].replace("$","")))
        Total +=price*Quantity
        print("The unit price is:",price)
        print("\n")
        
        boughtLaptop.append(laptops[InputSn][0])
        brandoflaptop.append(laptops[InputSn][1])
        buyingPrice.append(laptops[InputSn][2])
        
        print("--------------------------------------------------------------------------------------------------------------------------------")
        print("Do you want to buy other laptops too?")
        print("If you want please press 'YES' otherwise you can press any other key ")
        print("--------------------------------------------------------------------------------------------------------------------------------")
        wantMorelaptops=input("Do you want to buy more? :")
        print("\n")
        if wantMorelaptops.upper()=="YES":
            read.lapdisplay()
            print("\n")
        else:
            moreBuying =False
            CName=input("Enter your name : ")
            Caddress =input("Enter your address : ")
            Cphone=input("Enter your phone number : ")
    createbill(CName,Caddress,Cphone,Total,TQuantity,boughtLaptop,brandoflaptop,buyingPrice,BoughtQuantity)
    display()
    
#to update the file
def file_update(laptops): 
    txtfile = open("laptop.txt","w")
    for key,value in laptops.items():
        txtfile.write(value[0]+","+ value[1] +","+ value[2] +","+ value[3]+","+ value[4] +","+ value[5])
        txtfile.write("\n")
    txtfile.close()
    
#to update the quantity of laptops
def Quantity_updater(InputSn,Quantity):
    laptops =read.dictionary()
    quantity=int(laptops[InputSn][3])
    while Quantity<=0 or Quantity>quantity:
        print("Please enter a valid quantity.")
                      
        print("\n")
        try:
            Quantity=int(input("Enter the quantity to buy: "))
        except:
            print("enter the valid quantity")
        print("\n")
    laptops[InputSn][3]=str(quantity-Quantity)
    return laptops
    
#to create bill in cmd shell
def createbill(CName,Caddress,Cphone,Total,TQuantity,boughtLaptop,brandoflaptop,buyingPrice,BoughtQuantity):
    print("------------------------------------------------------------------------------------------")
    print("==========================================================================================")
    print("\t\t\t\t\tBILL DETAILS  " )
    print("Bought Date: ", str(datetime.datetime.now()))
    print("==========================================================================================")
    print("Name of customer: ", CName)
    print("Address of the customer: ", Caddress)
    print("Customer phone no: ",Cphone)

    print("------------------------------------------------------------------------------------------")
    print("S.No\tLaptop Name\t\t\tBrand\t\tUnit Price\tQuantity")
    print("------------------------------------------------------------------------------------------")
    for i in range(len(boughtLaptop)):
        print(str(i+1)+"\t"+boughtLaptop[i]+"\t\t\t"+brandoflaptop[i]+"\t\t"+buyingPrice[i]+"\t\t"+str(BoughtQuantity[i]))
    print("------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\t\tTotal quantity: "+ str(TQuantity))
    print("\t\t\t\t\t\t\tTotal Price: "+"$"+ str(Total))
    print("------------------------------------------------------------------------------------------")
    print("==========================================================================================")
    print("\n\n")
    write.text_bill(CName,Caddress,Cphone,Total,TQuantity,boughtLaptop,brandoflaptop,buyingPrice,BoughtQuantity)

#for selling section
def Selling():
    display()
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print("====================================================== SELLING SECTION =========================================================")
    sell_list=[]
    sell_brand=[]
    sell_price=[]
    sell_Quantity=[]
    print("--------------------------------------------------------------------------------------------------------------------------------")
    print("\n")
    CName=input("Enter your name : ")
    TQuantity=0
    TFine=0
    Ryear=0

    more_selling=True
    while more_selling == True:
        read.lapdisplay()
        SN=0
        while True:
            try:
                SN = int(input("Enter the serial no. of laptop you want to sell : "))
                break
            except:
                print("please input the valid serial number")
                SN = int(input("Enter the serial no. of laptop you want to Selling: "))
                print("\n")
                
        while True:
            try:
                Quantity = int(input("Selling Quantity: "))
                if Quantity < 1:
                    print("Please enter a valid input.")
                    Quantity =int(input("No.of laptop to be sold: "))
                print("\n")
                break
            except:
                print("Please input valid Quantity ")
                Quantity =int(input("No.of laptop to be sold: "))
        sell_Quantity.append(Quantity)
        laptop=read.dictionary()
        Inventory=int(laptop[SN][3])
        Amount=float(laptop[SN][2].replace("$",""))

        laptop[SN][3]=str(Inventory+Quantity)
        file_update(laptop)
        TQuantity+= Quantity

        sell_list.append(laptop[SN][0])
        sell_brand.append(laptop[SN][1])
        sell_price.append(laptop[SN][2])

        print("--------------------------------------------------------------------------------------------------------------------------------")
        print("Do you want to sell other laptops too?")
        print("If you want please press 'YES' otherwise you can press any other key ")
        print("--------------------------------------------------------------------------------------------------------------------------------")
        more =input("You want to sell more? ")
        if more.upper()=="YES":
            more_selling=True
        else:
            more_selling=False
            print("Your laptop has been accepted. Thanks for doing business with us")
            while True:
                try:
                   NoOfyear= int(input("Number of year the laptop was used for: "))
                   break
                except:
                    print("Enter the year in number format" )
                        
             
    BILLPRINT(CName,TQuantity,TFine,Ryear,sell_list,sell_brand,sell_price,sell_Quantity)
    
#to create bill in cmd shell
def BILLPRINT(CName,TQuantity,TFine,Ryear,sell_list,sell_brand,sell_price,sell_Quantity):
    print("----------------------------------------------------------------------------")
    print("                             Selling Bill")
    print("\t\t\t\tSelling Date:",str(datetime.datetime.now()))
    print("----------------------------------------------------------------------------")
    print("Custoumer Name: ", CName)
    print("============================================================================")
    print("S.NO\tLaptop Name\t\tQuantity\tBrand\t\tPrice")
    print("============================================================================")
    total_price = 0
    for u in range(len(sell_list)):
        price = float((sell_price[u].replace("$","")))
        quantity = int(sell_Quantity[u])
        total_price += price * quantity
        print(str(u+1)+"\t"+str(sell_list[u])+"\t\t"+str(sell_Quantity[u])+"\t\t"+str(sell_brand[u])+"\t\t"+str(price*quantity))

    print("============================================================================")
    print("\t\t\t\t\t\tTotal Quantity:"+str(TQuantity))
    print("\t\t\t\t\t\tTotal Fine:",str(TFine))
    print("\t\t\t\t\t\tTotal Price :",str(total_price-TFine))
    print("============================================================================")
    print("====================Thankyou for doing business with us=====================")
    print("\n\n")
    write.BILLPRINTtxt(CName,TQuantity,TFine,Ryear,sell_list,sell_brand,sell_price,sell_Quantity)
#to exit the program
def exit():
    print("----------------------------------------------------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\t\tThank you!! for choosing us")
    print("----------------------------------------------\t\t\t\t------------------------------------------------")
    print("\t\t\t\t\t\tHope to see you again")
    print("----------------------------------------------------------------------------------------------------------------------------------------------")




































    
