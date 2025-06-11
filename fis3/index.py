import numpy as np
import matplotlib.pyplot as plt

# Dados
comprimento_cm = np.array([60, 55, 50, 45, 40, 35, 30, 25, 20, 15, 10, 5])
resistencia_ohm = np.array([2.2, 2.0, 1.8, 1.7, 1.5, 1.3, 1.2, 1.1, 0.9, 0.7, 0.6, 0.4])

# Ajuste pelo método dos mínimos quadrados (reta: y = ax + b)
# Convertendo comprimento para metros
comprimento_m = comprimento_cm / 100.0

# Ajuste linear com numpy (reta: y = ax + b)
a, b = np.polyfit(comprimento_m, resistencia_ohm, 1)
reta_ajustada = a * comprimento_m + b

# Plotando os dados e a reta ajustada
plt.figure(figsize=(8, 5))
plt.scatter(comprimento_m, resistencia_ohm, color='blue', label='Dados experimentais')
plt.plot(comprimento_m, reta_ajustada, color='red', label=f'Ajuste linear: y = {a:.4f}x + {b:.4f}')

plt.xlabel('Comprimento (m)')
plt.ylabel('Resistência (Ω)')
plt.title('Resistência vs Comprimento - Ajuste Linear')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
