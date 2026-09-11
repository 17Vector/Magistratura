#f(x, y) = Ax^2 + Bxy + Cy^2 + Dx + Ey + F
A, B, C, D, E, F = map(float, input("Введите коэффициенты A, B, C, D, E и F через пробел: ").split())
print(f"Полученное уравнение: {A}x^2 + {B}xy + {C}y^2 + {D}x + {E}y + {F} = 0")
#x' = 2Ax + By + D = 0
#y' = Bx + 2Cy + E = 0
# [2A B] = [-D]
# [B 2C] = [-E]
detM = 4*A*C - B**2
x_star = (B*E - 2*C*D)/detM
y_star = (B*D - 2*A*E)/detM
print(f"Координаты критической точки: ({x_star}, {y_star})")
f = A*x_star**2 + B*x_star*y_star + C*y_star**2 + D*x_star + E*y_star + F
print(f"Значение функции в критической точке: {f}")