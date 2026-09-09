import math
import matplotlib.pyplot as plt
arr = [0.74, 4.28, 7.10, 7.54, 1.77, 4.53, 5.48, 6.72, 5.38, 0.81,
       6.06, 5.06, 3.79, 9.49, 6.31, 2.44, 3.47, 7.57, 6.17, 4.12,
       5.84, 5.41, 4.36, 5.27, 2.34, 8.18, 4.75, 5.24, 8.22, 4.33,
       3.24, 7.33, 3.13, 6.56, 2.86, 8.39, 5.12, 4.38, 7.64, 7.90,
       5.65, 4.16, 4.84, 7.30, 6.52, 6.20, 6.05, 7.04, 8.96, 4.88,
       1.79, 5.98, 3.17, 5.55, 4.58, 4.33, 5.15, 5.86, 4.64, 6.20,
       6.68, 4.76, 6.46, 6.57, 5.72, 6.36, 2.60, 4.43, 11.10, 2.26,
       3.77, 3.02, 13.18, 9.42, 2.37, 6.70, 2.59, 5.71, 4.76, 1.66,
       7.13, 6.10, 4.84, 0.02, 4.25, 5.46, 7.47, 4.82, 4.87, 6.02, 
       6.89, 6.47, 8.79, 2.70, 7.81, 2.04, 2.81, 3.97, 8.01, 4.75]

arr.sort()
n = len(arr)

k = round(1 + 3.322 * math.log10(n))
x_min = arr[0]
x_max = arr[-1]
h = math.ceil((x_max - x_min) / k * 100) / 100

edges = [round(x_min + i * h, 2) for i in range(k + 1)]
counts = [0] * k
for x in arr:
    for i in range(k):
        left_ok = x >= edges[i] if i == 0 else x > edges[i]
        if left_ok and x <= edges[i + 1]:
            counts[i] += 1
            break

w = []
x_mids = []
nixi = 0
nixi2 = 0
for i in range(k):
    w.append(counts[i] / n)
    x_mids.append((edges[i] + edges[i + 1]) / 2)
    nixi += counts[i] * x_mids[i]
    nixi2 += counts[i] * x_mids[i] ** 2

x_mean = nixi / n
x_q_mean = nixi2 / n

sigma_q = x_q_mean - x_mean ** 2
sigma = sigma_q ** 0.5

s_x2 = n/(n-1) * sigma_q
s_x = s_x2 ** 0.5

print(f"Отсортированный массив: {arr}\n")

for i in range(k):
    print(f"({edges[i]:.4f}; {edges[i+1]:.4f}]  n_i = {counts[i]}  "
          f"w_i = {w[i]:.4f}  x~ = {x_mids[i]:.4f}  "
          f"n*x~ = {counts[i]*x_mids[i]:.4f}  " 
          f"x~^2 = {x_mids[i]**2:.4f}  "
          f"n*x~^2 = {counts[i]*x_mids[i]**2:.4f}  "
          f"w_i/h = {w[i]/h:.4f}")

print(f"\nРазмер шага: {h:.4f}\n")
print(f"Среднее значение: {x_mean:.4f}\n")
print(f"Среднее значение квадратов: {x_q_mean:.4f}\n")
print(f"Сумма: {nixi:.4f}, Сумма квадратов: {nixi2:.4f}\n")
print(f"Дисперсия: {sigma_q:.4f}\n")
print(f"Среднее квадратичное отклонение: {sigma:.4f}\n")
print(f"Несмещенная дисперсия: {s_x2:.4f}\n")
print(f"Несмещенное среднее квадратичное отклонение: {s_x:.4f}\n")

heights = [w[i] / h for i in range(k)]

plt.bar(x_mids, heights, width=h, edgecolor='black', color='lightsteelblue')

plt.xticks(edges, rotation=45)
plt.xlabel('x_i')
plt.ylabel('w_i / h')
plt.title('Гистограмма')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()