print('Welcome to "This is You".\n')
name = input("What's your name?: \n")
age = input("Your age?: \n")
city = input("What city do you live in?: \n")
gender = input("Your gender?: \n")

print(f"Hello {name.title()}, You are a {age} year old "
      f"{gender.lower()} living in {city.title()}.")