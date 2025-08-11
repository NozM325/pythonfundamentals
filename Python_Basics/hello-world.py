name = input("What is your name?\n")

year = int(input("Which year were you born in " + name + " ?\n"))

ageInYears = 2025 - year

ageInDecades = int(ageInYears/10)

print("Hello " + name + " you are " + str(ageInYears) + " years old" + " and " + str(ageInDecades) +" decades old")