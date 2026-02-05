import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

c = 0.3 #S/N比
true = 1 #未知変数の真値
x = 2 #平均値
X =[x]
t = 3 #分散
T = [t]

for n in range(1, 2001):
  y = c * true + np.random.randn()
  x = x + c * t * (y - c * x)/(1 + c ** 2 * t)
  t = t/(1 + c ** 2 * t)
  X.append(x)
  T.append(t)

plt.figure(figsize=(10, 5))
plt.plot(X, label=r'Estimated Value $x_n$ ($\mu_n$)', color='blue', lw=1)
plt.plot(T, label=r'Uncertainty $t_n$ ($\tau_n$)', color='red', lw=1.5)
plt.axhline(true, color='black', linestyle='--', label='True Value')
plt.title('Bayesian Estimation Process')
plt.xlabel('Steps (n)')
plt.ylabel('Value')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
