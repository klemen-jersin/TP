import random

x=random.randrange(0,30)
s_poskusov=5

while s_poskusov > 0:
    poskus = input("Vnesi številko: ")
    poskus = int(poskus)
    if x==poskus:
            print("Zmaga")
            break
    if x!= poskus and s_poskusov==1:
            print("PORAZ")
            if poskus < x:
                 print("Vnesli ste premajhno številko")
            else:
                    print("Vnesli ste preveliko številko")
            break
    elif poskus < x:
         print("Vnesli ste premajhno številko")
    else:
            print("Vnesli ste preveliko številko")
    s_poskusov-=1




print(f'''
---------------------------
Correct answer: {x}
---------------------------
''')