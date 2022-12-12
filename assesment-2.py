car={}
file=open("output2.txt","a")
brand_Name=input("Enter brand name of the car: ")
color=input("Enter color of the car: ")
car[brand_Name]=color
print(car)
file.write(str(car))
file.close()