import numpy as np
import matplotlib.pyplot as plt

diasX=["Lun","Mar","Mie","jue","vie"]
califa_va_y=[5,6,3,8,10]
plt.bar(diasX,califa_va_y)
plt.title("Califas en VA de Azul Ramirez NC 0441")
plt.xlabel("dias semana habil")
plt.ylabel("Calificaciones en VA")
plt.grid()
plt.show()