age = input("How old are you: ")
print("You are " + age + " years old \n =" )
User_age = str(int(age) * 365 * 24 * 60 * 60)
print("Which is " + User_age + " seconds old.")
print("You have lived for " + User_age + " seconds")


def age_program():
    seconds_or_years = input("Give me your age in seconds(s) or years(y): ")
    if seconds_or_years == "s":
        user_age = input("Enter the numbers of seconds you've lived for: ")
        print("You've lived for " + str(int(user_age) / 60 / 60 / 24 / 365) + " years")
    elif seconds_or_years == "y":
        input("Enter the numbers of years you've lived for: ")
        print("You have lived for " + str(int(User_age) * 365 * 24 * 60 * 60) + " seconds")


print(age_program())