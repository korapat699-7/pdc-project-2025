import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate
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

ln_2x3 = np.log(2 * x[3])
T1 = ln_2x3 / 4
T2 = ln_2x3 / 2
T3 = 3 * ln_2x3 / 4

# ค่าของสัญญาณ
A = 2 * np.log(x[2])
B = 2 / np.sqrt(ln_2x3)

# คำนวณค่า y1s(ln(2x3)), y2s(ln(2x3)), y3s(ln(2x3))
def matched_filter_output(t):
    if 0 <= t < T2:
        return (4 * A / np.sqrt(ln_2x3)) * (t / (ln_2x3 / 4))
    elif T2 <= t <= T3:
        return (4 * A / np.sqrt(ln_2x3)) * (1 - (t - T2) / (ln_2x3 / 4))
    else:
        return 0

y1_val = matched_filter_output(ln_2x3)
y2_val = matched_filter_output(ln_2x3 - T1)
y3_val = matched_filter_output(ln_2x3 - T2)

# แสดงเวกเตอร์ r
r = np.array([y1_val, y2_val, y3_val])
print("Vector r at t = ln(2x3):")
print(r)