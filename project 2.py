import math
#Python final Project Alex Nygard

#Class for breakfast entries
cBeverages = ["Espresso","Americano","Caffe latte","Mocha","Cappucino","Macchiato"]

#Class for tea
tBeverages = ["White tea,Green tea,Oolong tea,Black tea,Earl Grey,Match"]

#class for pastries
pDesserts = ["Croissant","Cinnamon roll","Banana bread","Pumpkin bread","Sticky bun","Apple turnover"]



#FIRST PROMPT WELCOME
dineWithus=input("Welcome to MC CAFE! Would you like to dine with us today? [Y/N]")
if dineWithus =="N":
  print("Have a nice day!.")
if dineWithus=="Y":
  print("Here is our menu")


#define my breakfast menu
breakfastMenu = ["Pancake 1$, Frech Toast 1$, Chicken Fried Steak 1$, Omlet 1$, Scramble 1$,Eggs 1$, Bacon 1$, Toast, 1$, Fruit 1$, Sausage 1$"]
#define my lunch menu
lunchMenu = ["White tea 1.50$,Green tea,Oolong tea,Black tea,Earl Grey,Matcha"]
#define my drink menu
drinkmenu=["Croissant 5.50$, Cinnamon roll4.50$, Banana bread4.25$, Pumpkin bread3.75$, Sticky bun4.25$, Apple turnover3.75$"]

grandTotal=0

#Possible Counters
orderNumber=1
x=0
y=0
counter = 1
counter2 = 1
drinkOrder = 0


print("Customer Order Number:",orderNumber)
  order=input("Would you like to order breakfast or lunch?[B/L]")
  i=0
  j=0

  #LOOP FOR BREAKFAST ENTRIES
  if order == "B":
    while i < cBeverages)
      print("Breakfast menu is",cBeverages[i])
      i += 1
    entrieB = int(input("Which would you like? "))
    if entrieB == 1:
      print("You have choscBeverages[0])
      grandTotal+=1
    if entrieB == 2:
      print("You have choscBeverages[1])
      grandTotal+=1
    if entrieB == 3:
      print("You have choscBeverages[2])
      grandTotal+=1
    if entrieB == 4:
      print("You have choscBeverages[3])
      grandTotal+=1
    if entrieB == 5:
      print("You have choscBeverages[4])
      grandTotal+=1

    #LOOP FOR BREAKFAST SIDES
    while j < len(bSides):
      print("Breakfast sides are",j+1,bSides[j])
      j += 1
    sideB = int(input("Which would you like? "))
    if sideB == 1:
      print("You have chosen",bSides[0])
      grandTotal+=1
    if sideB == 2:
      grandTotal+=1
      print("You have chosen",bSides[1])
      grandTotal+=1
    if sideB == 3:
      print("You have chosen",bSides[2])
      grandTotal+=1
    if sideB == 4:
      print("You have chosen",bSides[3])
      grandTotal+=1
    if sideB == 5:
      print("You have chosen",bSides[4])
      grandTotal+=1
  
  #LUNCH ENTRIES LOOP
  l = 0
  if order == "L":
    while l < len(lEntries):
      print("Lunch options are",l+1,lEntries[l])
      l += 1
    entrieL = int(input("Which would you like? "))
    if entrieL == 1:
      print("You have chosen",lEntries[0])
      grandTotal+=1
    if entrieL == 2:
      print("You have chosen",lEntries[1])
      grandTotal+=1
    if entrieL == 3:
      print("You have chosen",lEntries[2])
      grandTotal+=1
    if entrieL == 4:
      print("You have chosen",lEntries[3])
      grandTotal+=1
    if entrieL == 5:
      print("You have chosen",lEntries[4])
      grandTotal+=1
    
   

#PRINT TOTAL
print("Your total cost is",grandTotal,"dollars. Thank you for dining with us! Come again!")

