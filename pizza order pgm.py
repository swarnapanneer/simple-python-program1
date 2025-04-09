size=input("which size of pizza do you want(s/m/l)?")
bill=0
if size=='S' or size=='s':
    bill+=100
    print("small pizza price is 100r.s")
if size=='M' or size=='m':
    bill+=200
    print("medium pizza price is 200r.s")
if size=='L' or size=='l':
    bill+=300
    print("large pizza price is 300r.s")

add_pepperoni=input("Do you want pepperoni(y/n)?")
if add_pepperoni=='Y' or add_pepperoni=='y':
    if size=='S' or size=='s':
        bill+=30
    else:
        bill+=50
extra_cheese=input("do you want extra cheese(y/n)?")
if extra_cheese=='Y' or extra_cheese=='y':
    bill+=20
print(f"your total bill is {bill}")
      
