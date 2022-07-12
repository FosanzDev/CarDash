import sys

cars = []
stadiums = []

f = open("stadiumSelection.msm")
for a in f.readlines():
    a = a.split("-")
    stadiums.append(a)

f.close()


f = open("carSelection.msm")
for a in f.readlines():
    a = a.split("-")
    cars.append(a)

f.close()



#Main menu

print ("""
-- Welcome -- 
Select an option:
1 - Play
2 - Exit

Type the number and press enter""")

while True:
    opt = input("--> ")
    if opt == "1":
        break

    elif opt == "2":
        sys.exit()

    else: print("Not an option\n")

#Stadium selection

print("\n\n\n\n\n\n\nSelect an stadium: \n")

for s in stadiums:
    print(s[0], "\n  ", s[1])

stadium = int(input("\n Stadium: "))
stadium = stadiums[stadium-1][0]

#Car selection

print("\n\n\n\n\n\n\nSelect a car: \n")

for c in cars:
    print(c[0], "\n  ", c[1])

car = int(input("\n Car: "))
car = cars[car-1][0]

#Race start

print(f"Race starting with:\n-{stadium[3:]} stadium\n-{car[3:]} car")

f = open("RaceData.rd", "w")
f.write(stadium[:2])
f.write("\n")
f.write(car[:2])
f.close()