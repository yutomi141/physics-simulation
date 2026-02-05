import numpy as np
from scipy import integrate

# ---厳密解の計算---

# 1.関数の定義
def f(x):
  return np.sin(x)

# 2.積分範囲の設定
a, b = 0, np.pi

# 3.積分の実行
ans_scipy, err = integrate.quad(f, a, b)
print(f"Scipyによる厳密解:{ans_scipy}")

# ---モンテカルロ法---
N = 100000 #サンプリング数
np.random.seed(0) #シード値の固定

# 積分範囲 [a, b] 内でランダムに X を N 個選ぶ
x_samples = np.random.uniform(a, b, N)

# 選んだ X を関数に放り込んで Y を計算する
y_values = f(x_samples)

# 「区間の幅」 × 「Yの平均値」 が積分の近似値になる
ans_mc = (b - a) * np.mean(y_values)

print(f"モンテカルロ法: {ans_mc}")
print(f"真の値との差: {abs(ans_scipy - ans_mc)}")