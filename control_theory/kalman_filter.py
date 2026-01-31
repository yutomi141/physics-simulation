import numpy as np
import matplotlib.pyplot as plt

a = 0.8
b = 3.1
c = 1.0
x = 10
m = 2 #平均値μ
t = 10 #分散τ
X = [x] #xをリスト化
M = [m] #平均値をリスト化
T = [np.sqrt(t)] #標準偏差をリスト化
K = 0 # カルマンゲイン

np.random.seed(0)

for n in range(1,51):
  x = a * x + b * np.random.randn() #xの更新式
  y = c * x + np.random.randn() #yの更新式
  K = c * (a**2 * t + b**2) / (1 + a**2 * c**2 * t + b**2 * c**2) #カルマンゲインの更新
  m = a * m + K * (y - a * c * m) #平均値の更新式
  t = (a**2 * t + b**2)/(1 + a**2 * c**2 * t + b**2 * c**2) #分散の更新式
  X.append(x)
  M.append(m)
  T.append(np.sqrt(t))

# グラフ1: 真の状態 X と 推定値 M
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1) # 横に2つ並べる左側
plt.plot(X, color='gray', lw=3, label='True state X')
plt.plot(M, color='red', lw=1, label='Estimate M')
plt.title('State Estimation')
plt.legend()

# グラフ2: 推定値 M と エラーバー T (標準偏差)
plt.subplot(1, 2, 2) # 右側
steps = range(len(M))
plt.errorbar(steps, M, yerr=T, fmt='-b', ecolor='r', capsize=2) 
plt.title('Estimation with Error Bars')

plt.tight_layout()
plt.show()
