name = str(input("What is your name? "))

#age = int(input("How old are you? "))

index_number = int(input("What is your index number? "))

print(f"My name is {name}. Index number is {index_number}.")
year_of_birth = int(input("Enter your year of birth: "))
current_year= 2025
age = current_year - year_of_birth
print(f"You are {age} years old.")
if age < 18:
    print("You are a minor.")
else:
    print("You are an adult.")