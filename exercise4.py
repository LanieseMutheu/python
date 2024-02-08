print("grades calculator")

math = int(input("math: "))
eng = int(input("eng: "))
phyc = int(input("phyc: "))
kisw = int(input("kisw: "))
hist = int(input("hist: "))

total = math + eng + phyc + kisw + hist
print(f"total marks = {total} ")

average = total / 5
print(average)

if average >=0 and average <39:
    print("E")
elif average >=40 and average <50:
    print("D")
elif average >=51 and average <60:
    print("C")
elif average >=61 and average <70:
    print("B")
else:
    print("A")




# 0-39 E
# 40-50 D
# 51-60 C
# 61-70 B
# 71-100
