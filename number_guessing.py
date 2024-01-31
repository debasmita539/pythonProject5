import random


top_of_range=input("Type a number: ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range<=0:
        print("please type a number large than 0 next time")
        quit()
    else:
        print("please type a number large than 0 next time")
        quit()
r=random.randrange(-5,11)
print(r)