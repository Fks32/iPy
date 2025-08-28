from yogi import read

temp = read(int)

if temp <= 30:
    if temp < 10:
        print("it's cold")
        if temp <= 0:
            print("water would freeze")
    else: print("it's ok")
else: 
    print("it's hot")
    if temp > 99:
        print("water would boil")

