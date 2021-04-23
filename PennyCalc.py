print("-------------------------------")
penny = input("How many pennys? ")
print("-------------------------------")
print(str(penny) + " Pennies is equivalent to:")
dollar = int(penny) // 100
penny = int(penny) - int(dollar) * 100
quarter = penny // 25
penny = penny - int(quarter) * 25
Dime = penny // 10
penny = int(penny) - int(Dime) * 10
nickels = penny // 5
penny = int(penny) - int(nickels) * 5
print("--------------------------------")
print("I%5s" % str(dollar) + " Dollars")
print ("I%5s" %str(quarter) + " Quarters")
print("I%5s" %str(Dime) + " Dimes")
print("I%5s" % str(nickels) + " Nickels")
print("I%5s" % str(penny) + " Pennies")
print("-------------------------------")
