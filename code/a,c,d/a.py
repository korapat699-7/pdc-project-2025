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
B = 2 / np.sqrt(ln_2x3)

# สร้างช่วงเวลา (0 ถึง T3)
t = np.linspace(0, T3, 1000)

# สร้างฟังก์ชันพื้นฐาน ψ1, ψ2, ψ3 ตามช่วงเวลา
psi1 = np.where((t >= 0) & (t <= T1), B, 0)
psi2 = np.where((t >= T1) & (t <= T2), B, 0)
psi3 = np.where((t >= T2) & (t <= T3), B, 0)

# คำนวณ impulse response ของ matched filters โดยใช้ time-reversal ของ ψ
h1 = psi1[::-1]
h2 = psi2[::-1]
h3 = psi3[::-1]

# พลอตกราฟ h1
plt.figure(figsize=(8, 4))
plt.plot(t, h1, label=r'$h_1(t)$', color='blue')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.title('Impulse Response h1(t)')
plt.legend()
plt.grid(True)
plt.show()

# พลอตกราฟ h2
plt.figure(figsize=(8, 4))
plt.plot(t, h2, label=r'$h_2(t)$', color='green')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.title('Impulse Response h2(t)')
plt.legend()
plt.grid(True)
plt.show()

# พลอตกราฟ h3
plt.figure(figsize=(8, 4))
plt.plot(t, h3, label=r'$h_3(t)$', color='red')
plt.xlabel('Time (t)')
plt.ylabel('Amplitude')
plt.title('Impulse Response h3(t)')
plt.legend()
plt.grid(True)
plt.show()