from yogi import read
a1 = read(int)
b1 = read(int)
a2 = read(int)
b2 = read(int)

if b1 < a2:
    print("[]")
elif a1 > a2 :
    if b1 > b2:
        print("[",a1,",",b2,"]", sep="")
    else:
        print("[",a1,",",b1,"]", sep="")
        