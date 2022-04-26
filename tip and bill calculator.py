print("Welcome to the tip calculator ! ")
bill=int(input("Total Bill : $ "))
print(bill)
tip=int(input("What percentage tip would you like to give ? 10 , 12 or 15 ? "))
print(tip)
people=int(input("How many people to spilt the bill ? "))
print(people)
tippercentage=tip/100
totaltip=bill*tippercentage
totalbill=bill+totaltip
billperperson=totalbill/people
finalbill=round(billperperson)
print("Each person should pay : $ ",finalbill)