---
title: 'Flow matching'
publishDate: 2026-02-09
description: '生成模型初探'
tags:
  - Markdown
  - LLMs
language: 'English'
# Remove or set false to turn draft page into normal ones
draft: false
---

## Rectfied Flow

我们已知噪声分布$\pi_{0}$和目标分布$\pi_{1}$, 根据随机种子$\omega$得到采样$(X_{0}(\omega),X_{1}(\omega))$, 对$t$采样进行线性插值得到$X_{t}=tX_{0}+(1-t)X_{1}$, 可以显式计算导数$\dot{X}_{t}=X_{0}-X_{1}$, 因此在采样过程中, 我们可以得到一个集合$\{(X_{0},X_{1},X_{t},\dot{X}_{t})\}$, 注意这里的导数$\dot{X}_{t}$依赖于选定的端点.

现在回到推理阶段, 已知一个点$x$和时刻$t$, 我们需要一个参数化模型$v_{\theta}(x,t)$来学习此处的速度从而来做更新, 但由于我们采样得到的集合中一个点处的导数可能不唯一, 因此我们是取平均值来拟合: $v^*_{\theta}(x,t)=E[\dot{X}_{t}|X_{t}=x]$, 这个条件期望也是已知$X_{t}=x$的最佳的拟合函数. 因此我们得到:
$$
\dot{Z}_t=v_{\theta}(Z_{t},t)=E[\dot{X}_{t}|X_{t}=Z_{t}]
$$
这里的$\{X_{t}\}$是一个多值的速度场, 我们用条件期望聚合在同一个点$(x,t)$处的速度使得对应唯一速度, 从而可以定义出一个ODE.

现在我们已经训练好了一个模型$v_{\theta}(x,t)$, 采样$Z_{0}\sim\pi_{0}$, 可以用Euler求解一条轨迹得到$(Z_{0},Z_{1})$, 并且上面的构造过程保证了$Z_{1}\sim \pi_{1}$. 但更直的求解轨迹有利于加速推理, 因此可以擦掉中间的轨迹, 只考虑推理得到的对$(Z_{0},Z_{1})$来进行第二次Recitify. 注意这里的$Z_{1}$已经是第一个模型生成的图片了, 而不是原始图片.

## 参考资料
+ [Qiang Liu 老师的 notes](https://www.cs.utexas.edu/~lqiang/PDF/flow_book.pdf)