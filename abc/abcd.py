# n=float(input("Enter a number: "))
# cube =n**3
# print(f"The cube of {n} is = ",cube)

# name="prashant"
# greet="Hello\t" + name + "\tWelcome to our service!"
# print(greet)

# user_input="Hello!"
# email="BhattaraiPrashant828@Gmail.Com"
# sentence="dog is a Domestic Animal."
# quotes="Nothing but something."
# uppercase=user_input.upper()
# lower=email.lower()
# capitalize=sentence.capitalize()
# quotese=quotes.title()
# print(uppercase)
# print(lower)
# print(capitalize)
# print(quotes)

# name=str(input("Enter your Full name : "))
# Title=name.title()
# print(Title)

# import random
# print(random.random())#generates a random floating values from 0.0 to 1.0



# Program to Generate OTP code.
# ph_number=(input("Enter your Mobile Number : "))
# import random
# random=random.randint(10,1000000)
# if(len(ph_number)<=10 and ph_number.isdigit()):
#     print("Your number is valid and,")
#     print(f"Your OTP code is : ",random)

# else:
#     print( "Your number is invalid.\n" "Pleasse try again.")


# import random  # Shuffle is used to shuffle the sequence.
# cards=["Joker","Ace","King","Queen","Jack"]
# cards.sort()
# print(cards)
# random.shuffle(cards)
# print(cards)

#   Guessing Game.
# guess=int(input("Guess the number between 1 to 6:  "))
# import random
# game=random.randint(1,6)
# if(guess>6):
#     print("Your guess number is invalid , guess number between 1-6.")
# elif(guess==game):
#     print(f"Your guess is correct. The correct number was {game}.")
    
# else:
#     print(f"Your guess is incorrect. The correct number was {game}.")


# import qrcode
# img=qrcode.make("Prashant Bhattarai")
# type(img)
# img.save("bhattarai.png")

# import qrcode
# img=qrcode.make("https://youtu.be/JgDNFQ2RaLQ?si=4erv4ne9JU8E8I_9")#This line stores QR info
# type(img)
# img.save("QR code.png")


#Toatl in List.
# expenses=[889,788,5656,4455,455,45]
# total=0
# for expense in expenses:
#     total+=expense
#     avg=total/len(expenses)
# print("The total expenses is: ",total)
# print("The Average expenses is: ",avg)

# list=[]
# print("Days =",list)
# list.append("Sunday")
# list.append("Monday")
# list.append("Tuesday")
# list.append("Wednesday")
# list.append("Thursday")
# list.append("Friday")
# list.append("Saturday")
# print("Days=",list)
   
# # Nepali Calendar.
# import nepali_datetime
# def print_nepali_month(year, month):
#     first_day = nepali_datetime.date(year, month, 1)
#     weekday = first_day.weekday() 
#     if month == 12:
#         next_month = nepali_datetime.date(year + 1, 1, 1)
#     else:
#         next_month = nepali_datetime.date(year, month + 1, 1)

#     days_in_month = (next_month - first_day).days

#     print(f"\n  {first_day.strftime('%B %Y')} (B.S.)")
#     print("Su Mo Tu We Th Fr Sa")

#     print("   " * ((weekday + 1) % 7), end="")
#     for day in range(1, days_in_month + 1):
#         print(f"{day:2d} ", end="")
#         if (day + weekday + 1) % 7 == 0:
#             print()
#     print()
# year = int(input("Enter Nepali year (e.g. 2082): "))
# month = int(input("Enter Nepali month (1–12): "))
# print_nepali_month(year, month)



