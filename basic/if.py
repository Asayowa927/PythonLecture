# if文

age = 19
age_alcohol = 20
age_drive = 18
if age >= age_alcohol:
    print("You can drink alcohol!")


elif age < age_drive:
    print("You cannot even drive")

else:
    print("You are too young to drink alcohol")

if not 0 < age < 120:
    print("The value is invalid!!")

# challenge1

balance = 200
withdrawal = 10000
limit = 1000
if withdrawal > limit:
    print("Limit over!! The limit is {}".format(limit))

else:
    if balance < withdrawal:
        print("Short balance!!")
    else:
        balance -= withdrawal
        print("Accepted!! Your new balance is {}".format(balance))

