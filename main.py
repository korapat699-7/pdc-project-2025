# A.653040629-9, 653040699-7 then sum of last to digit is 99 + 97
# B.find parameter x0 with 653040629-9 and 653040699-7 modulo by 100.
def findParameter(student1, student2):
    return (student1 + student2) % 100 # (student1 + student2) mod by 100

x = []
x0 = findParameter(99, 97) # result is 96
x1 = 7 # from document define x1 = 7

# C.find parameter x[n], n is member of (1, 2, 3, ... n)
def findX():
    x.append(x0)
    x.append(x1)
    for i in range(1,5):
        x_temp = (((3 * x[i]) + (2 * x[i-1])) % 19 ) + 2
        x.append(x_temp)
findX()
for i in range(0,5):
    print(f"x{i}: {x[i]}")



