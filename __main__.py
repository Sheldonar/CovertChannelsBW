import math
import matplotlib.pyplot as plt

bw = 0
n_final = 0

bw_array = []
n_array = []


def bandwidth(n):
    t = (n + 1) / 2
    h = 0
    for n_tmp in range(1, n + 1):
        # h += ((1 / n) * math.log2(1 / n)) * (-1)
        h += ((1 / 2 ** n_tmp) * math.log2(1 / 2 ** n_tmp)) * (-1)
    banw = h / t
    return banw


def bandwidth_with_errors(n):
    t = (n + 1) / 2
    h = 0
    for i in range(1, n + 1):
        h_y_x = 0
        for j in range(1, n + 1):
            h_ex = 0
            if i == j:
                h_ex += 0.6 * math.log2(0.6) * (-1)
            elif i == (j - 1) or i == (j + 1):
                h_ex += 0.2 * math.log2(0.2) * (-1)
            else:
                h_ex += (1/i) * math.log2(1/i) * (-1)
            h_y_x = (-1) * (1/j) * h_ex
        h += ((1 / n) * math.log2(1 / n)) * (-1) - h_y_x
    banw = h / t
    return banw


for n in range(1, 11):
    bw_tmp = bandwidth_with_errors(n)
    if bw_tmp > bw:
        bw = bw_tmp
        n_final = n
    bw_array.append(bw_tmp)
    n_array.append(n)

print("Максимальная пропускная способность = ", bw)
print("Число пакетов = ", n_final)
print(bw_array)

plt.title('График зависимости пропускной способности СК от N')
plt.xlabel('Number of Packets')
plt.ylabel('Bandwidth')
plt.plot(n_array, bw_array, 'g-')
plt.show()
