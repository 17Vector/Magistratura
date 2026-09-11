import math
#ax^3 + bx^2 + cx + d = 0 a != 0
a, b, c, d = map(float, input("Введите коэффициенты a, b, c, d, разделенные пробелами: ").split())
#x^3 + Ax^2 + Bx + C = 0
A = b / a
B = c / a
C = d / a
#y^3 + py + q = 0
p = B - (A**2)/3
q = C + 2*(A**3)/27 - A*B/3

w = (-q/2) * (3/-p)**(3/2)
arccos_w = math.acos(w)
omega0 = arccos_w/3
omega1 = (arccos_w - 2*math.pi)/3
omega2 = (arccos_w - 4*math.pi)/3

y0 = 2 * math.sqrt(-p/3) * math.cos(omega0)
y1 = 2 * math.sqrt(-p/3) * math.cos(omega1)
y2 = 2 * math.sqrt(-p/3) * math.cos(omega2)

x0 = y0 - A/3
x1 = y1 - A/3
x2 = y2 - A/3

print(f"Выражение: {a}x^3 + {b}x^2 + {c}x + {d} = 0\n")
print(f"Преобразованное уравнение: y^3 + {p}y + {q} = 0\n")
print(f"Корни исходного кубического уравнения: x0 = {x0:.4f}, x1 = {x1:.4f}, x2 = {x2:.4f}")