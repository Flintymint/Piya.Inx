import datetime
import Operation
#to create buying bill in text file
def text_bill(CName,Caddress,Cphone,Total,TQuantity,boughtLaptop,brandoflaptop,buyingPrice,BoughtQuantity):
    printbill = open((str(CName)+(str(datetime.datetime.now().year))+(str(datetime.datetime.now().month))+(str(datetime.datetime.now().day))+(str(datetime.datetime.now().hour))+(str(datetime.datetime.now().microsecond)))+".txt","w")
    printbill.write("-------------------------------------------------------------------------------\n")
    printbill.write("===============================================================================\n")
    printbill.write("\t\t\t\t\tBILL DETAILS  "+"\n")
    printbill.write("Bought Date: "+ str(datetime.datetime.now()) +"\n")
    printbill.write("===============================================================================\n")
    printbill.write("Name of customer: "+ CName+"\n")
    printbill.write("Address of the customer: "+ Caddress+"\n")
    printbill.write("Customer phone no: "+ Cphone+"\n")

    printbill.write("-------------------------------------------------------------------------------\n")
    printbill.write("S.No\tLaptop Name\t\t\tBrand\t\tUnit Price\tQuantity\n")
    printbill.write("-------------------------------------------------------------------------------\n")
    for i in range(len(boughtLaptop)):
        printbill.write(str(i+1)+"\t\t"+boughtLaptop[i]+"\t\t\t"+brandoflaptop[i]+"\t\t"+buyingPrice[i]+"\t\t"+str(BoughtQuantity[i])+"\n")
    printbill.write("-------------------------------------------------------------------------------\n")
    printbill.write("\t\t\t\t\t\t\tTotal quantity: "+ str(TQuantity)+("\n"))
    printbill.write("\t\t\t\t\t\t\tTotal Price: "+"$"+ str(Total)+("\n"))
    printbill.write("-------------------------------------------------------------------------------\n")
    printbill.write("===============================================================================")
    printbill.close()

#to create selling bill in text file
def BILLPRINTtxt(CName,TQuantity,TFine,Ryear,sell_list,sell_brand,sell_price,sell_Quantity):
    BILLPRINTtxt=open((str(CName)+(str(datetime.datetime.now().year)+(str(datetime.datetime.now().month))+(str(datetime.datetime.now().day))+(str(datetime.datetime.now().microsecond))))+".txt","w")
    BILLPRINTtxt.write("----------------------------------------------------------------------------"+"\n")
    BILLPRINTtxt.write("                             Selling Bill"+"\n")
    BILLPRINTtxt.write("\t\t\t\tSelling Date:"+str(datetime.datetime.now())+"\n")
    BILLPRINTtxt.write("----------------------------------------------------------------------------"+"\n")
    BILLPRINTtxt.write("Custoumer Name: "+CName+"\n")
    BILLPRINTtxt.write("============================================================================"+"\n")
    BILLPRINTtxt.write("S.NO\tLaptop Name\t\tQuantity\tBrand\t\tPrice"+"\n")
    BILLPRINTtxt.write("============================================================================"+"\n")
    total_price = 0
    for u in range(len(sell_list)):
        price = float((sell_price[u].replace("$","")))
        quantity = int(sell_Quantity[u])
        total_price += price * quantity
        BILLPRINTtxt.write(str(u+1)+"        "+str(sell_list[u])+"\t\t"+str(sell_Quantity[u])+"\t\t"+str(sell_brand[u])+"\t\t"+str(price*quantity)+"\n")

    BILLPRINTtxt.write("============================================================================"+"\n")
    BILLPRINTtxt.write("\t\t\t\t\t\tTotal Quantity:"+str(TQuantity)+"\n")
    BILLPRINTtxt.write("\t\t\t\t\t\tTotal Fine:"+str(TFine)+"\n")
    BILLPRINTtxt.write("\t\t\t\t\t\tTotal Price :"+str(total_price-TFine)+"\n")
    BILLPRINTtxt.write("============================================================================"+"\n")
    BILLPRINTtxt.write("====================Thankyou for doing business with us====================="+"\n")
    BILLPRINTtxt.write("\n\n")
    BILLPRINTtxt.close()














    
