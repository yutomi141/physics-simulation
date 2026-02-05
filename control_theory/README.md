# Control and Estimation Theory

This directory focuses on state estimation and stochastic control.

このディレクトリでは状態の推定と確率論的制御に着目します。

---

## 1. Bayesian Estimation
General recursive Bayesian update for a constant value.

定数値の一般的なベイズの定理による更新

$Y=cx+V$という信号を得るとき、ガウス分布に従うと仮定した確率変数Xの分布を次の式を用いて更新する。

**平均 $μ_n$ の更新:**
$$\mu_n = \mu_{n-1} + \frac{c\tau_{n-1}}{1+c^2\tau_{n-1}}(y_n - c\mu_{n-1})$$

**分散 $\tau_n$ の更新:**
$$\tau_n = \frac{\tau_{n-1}}{1+c^2\tau_{n-1}}$$

![Bayesian Estimation](../images/bayesian_convergence.png)

---

## 2. Kalman Filter
Extension of Bayesian estimation to dynamical systems.

ベイズ推定の動的システムへの拡張

$X_n=aX_{n-1}+bW_n$というダイナミクスに従って確率変数Xが変化し、それに対して、$Y=cX_{n-1}+V_n$という信号が得られるとき、ガウス分布に従うと仮定した確率変数Xの分布を次の式を用いて更新する。

**カルマンゲイン $K$:**
$$K = \frac{c(a^2\tau_{n-1}+b^2)}{1+c^2(a^2\tau_{n-1}+b^2)}$$

**平均 $\mu_n$ の更新:**
$$\mu_n = a\mu_{n-1} + K(y_n - c\mu_{n-1})$$

**分散 $\tau_n$ の更新:**
$$\tau_n = \frac{a^2\tau_{n-1}+b^2}{1+c^2(a^2\tau_{n-1}+b^2)}$$

![Kalman Filter](../images/kalman_filter.png)