# noofCars=0
# noofBikes=0
# totalPayment=0
# noofCars=int(input("Enter how many cars parked"))
# noofBikes=int(input("Enter how many bikes parked"))
# totalPayment= noofBikes*20 + noofCars*40;
# print("total amount would be",totalPayment)




# CAMEL casing
# noOfCars = 0
# noOfBikes = 0
# totalPayment = 0
# noOfCars = int(input("No of Cars"))
# noOfBikes = int(input("No of Bikes"))
# totalPayment = noOfBikes*20+noOfCars*40
# print("total payment would be", totalPayment)
# noOfCars="Sanjoy"
#type independent
#Store management Software

#3 variables : Product 1,Product 2, product 3
#product1 =40
#product2=50
#product3=60

# product1=40
# product2=50
# product3=60
#using input function 
product1=int(input("Enter how many kgs you want :"))
product2=int(input("Enter how many kgs you want :"))
product3=int(input("Enter how many kgs you want :"))
# product4=int(input("Enter how many kgs you want"))
# product5=int(input("Enter how many kgs you want"))
price1=int(input("price of product1 :"))
price2=int(input("price of product2 :"))
price3=int(input("price of product3 :"))

#using the list
# products = [product1,product2,product3]
#using for loop 
# for i in products:
#     print(i)
#using If _else statements
if (product1<=0) or (product2<=0) or (product3<=0):
    print("enter a positive number")
else:
    print("product quantity with price")
    totalAmount= product1*price1 + product2*price2+ product3*price3;
    entries ={product1 : price1, product2 : price2, product3 : price3}
    x=open("mydata.txt","a")
    print("the amount of all products")
    print("the amount of all products",file=x)
    # entries1 ={product1 : price1, product2 : price2, product3 : price3}
    for i,p in entries.items():
        print(i,p)
        print(i,p,file=x)
    print("total amount should  be paid by user:")
    print("total amount should  be paid by user:",file=x)
    print(totalAmount)
    print(totalAmount,file=x)


