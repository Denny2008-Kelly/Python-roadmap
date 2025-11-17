principle = 0
rate = 0
time = 0

while True:
    principle = float(input(f"Enter your principle :"))
    if principle <= 0:
        print("Your principle can not be less than 1")

while True:
    rate = float(input(f"Enter your interest rate :"))
    if rate <= 0:
        print("Your interest rate can not be less than 1")

while True:
    time = float(input(f"Enter your time :"))
    if time <= 0:
        print("The time can not be less than 1")
print(f"{principle:.2f}$")
print(f"{rate}%")
print(f"{time}yrs")

total = float(pow(principle * (1 + rate/100), time))

print(f"{total:.2f}$")