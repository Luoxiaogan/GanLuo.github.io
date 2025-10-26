---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<style>
ul {
  line-height: 1.5;
}
</style>

<span class='anchor' id='about-me'></span>

- Gan Luo(<font face=STKaiti>罗淦</font>)
- Undergraduate Student
- [[School of Mathematical Sciences, Peking University](https://www.math.pku.edu.cn)]
- Email: luogan [at] stu [dot] pku [dot] edu [dot] cn
- [[Curriculum Vitae](../CV_GanLuo/cv.pdf)], [[Google Scholar](https://scholar.google.com/citations?user=wNnV8vsAAAAJ&hl=en)]

I am currently a senior undergraduate at School of Mathematical Sciences, Peking University, where I am very fortunate to be advised by Prof. [[Kun Yuan](https://kunyuan827.github.io/)]. I have the privilege of working with Prof. [[David Simchi-Levi](https://slevi1.mit.edu)] at MIT, Prof. [[Wotao Yin](https://wotaoyin.mathopt.com)] at the [[Decision Intelligence Lab, DAMO Academy](https://damo.alibaba.com/labs/decision-intelligence)] and Prof. [[Bin Dong](http://faculty.bicmr.pku.edu.cn/~dongbin/)] at PKU. Throughout my research journey, I have been fortunate to learn from and collaborate with [[Liyuan Liang](https://scholar.google.com/citations?user=uPVoCcwAAAAJ&hl=en)], [[Ruicheng Ao](https://www.mit.edu/~aorc/index.html)] and [[Zihan Qin](https://openreview.net/profile?id=~Zihan_Qin5)].

<span style="background-color: #ffff0082; padding: 2px 4px;">I am seeking PhD opportunities starting in Fall 2026</span>. Please feel free to reach out!

<span class='anchor' id='publications'></span>

## 📝 Publications and PrePrints
- **Achieving Linear Speedup and Optimal Complexity for Decentralized Optimization over Row-stochastic Networks** [[Arxiv](https://arxiv.org/abs/2506.04600)]\\
Liyuan Liang\*, Xinyi Chen\*, **<u>Gan Luo*</u>**, Kun Yuan (*equal contribution)\\
**_ICML 2025 Spotlight (top 2.6%)_**

- **MetaFlow: A Meta Approach of Training LLMs into Generalizable Workflow Generators**\\
($\alpha$-$\beta$) **<u>Gan Luo*</u>**, Zihan Qin\*, Bin Dong, Wotao Yin\\
Work during internship in Prof. [[Wotao Yin](https://wotaoyin.mathopt.com)]'s group at Alibaba\\
As project lead, coming soon to Arxiv

- **Optimizing LLM Inference: Fluid-Guided Online Scheduling with Memory Constraints** [[Arxiv](https://arxiv.org/abs/2504.11320)] [[SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5195463)] [[Code1](https://github.com/Luoxiaogan/vidur_or)] [[Code2: vLLM Simulator](https://github.com/Luoxiaogan/vllm_simulation)]\\
($\alpha$-$\beta$) Ruicheng Ao\*, **<u>Gan Luo*</u>**, David Simchi-Levi, Xinshang Wang\\
**_Submitted to Operations Research_**\\
Preliminary version accepted at **_NeurIPS 2025 MLxOR Workshop_**

- **On the Linear Speedup of the Push-Pull Method for Decentralized Optimization over Digraphs** [[Arxiv](https://arxiv.org/abs/2506.18075)] [[Code: Linear Speedup](https://github.com/pkumelon/PushPull)]\\
Liyuan Liang\*, **<u>Gan Luo*</u>**, Kun Yuan (*equal contribution)\\
**_Submitted to Siam Optimization_**
  <details style="margin-top: -0.5em; margin-bottom: 0;"><summary>We propose a novel multi-step descent analysis framework and first to prove that the [<a href="https://arxiv.org/abs/1810.06653">Push-Pull algorithm</a>] achieves linear speedup over arbitrary strongly connected digraphs.</summary><br>This is my first research project, started in December 2023, advised by Prof. Kun Yuan and in collaboration with Liyuan Liang, whom I am fortunate to learn from. At first, we wanted to use the [<a href="https://arxiv.org/abs/2312.04928">traditional approach</a>] to analyze the problem, but after several months we found that this would give a non-vanishing noise term in the upper bound. We further found that this was because we first analyzed the single-term noise and then added them together, which motivated us to try a multi-step descent analysis framework, and finally we succeeded at about October 2024. You can see how we analyze the multi-step term step by step in the [<a href="../PDFs/new_proof.pdf">notes</a>].<br><br>For the empirical experiments, we struggled when validating the linear speedup properties of neural networks on the MNIST dataset. The challenge was in correctly measuring the gradient norm: we needed to compute the normalized gradient norm by averaging the gradients from all <i>n</i> nodes (where each node computes its gradient on its own batch) and then normalizing by the square root of the total parameter count, rather than using the average of the individual node gradient norms. See the [<a href="https://github.com/pkumelon/PushPull/blob/main/neural_network_experiments/training/training_track_grad_norm.py#L27">implementation</a>].
  <!-- <ul>
  <li>test</li>
  </ul> -->
  </details>

## 🎖 Slected Honors and Awards
- **Applied Mathematics Elite Program**, the program accepted only 15 people this year.
- **Silver Medal**, 35th Chinese Chemical Olympiad (**National Final**). The prize is awarded to the top 150 high school students in chemical throughout China.
<span class='anchor' id='educations'></span>

## 📖 Educations and Experiments
- *2023.04 - 2026.06 (expected)*, Undergraduate Student, School of Mathematical Sciences, Peking University
- *2025.07 - 2025.09*, Intern, DAMO Academy, Hangzhou, China
- *2022.09 - 2023.04*, Undergraduate Student, College of Environmental Sciences and Engineering, Peking University
- *2019.09 - 2022.06*, Senior High School Student, Chongqing Nankai Secondary School


<span class='anchor' id='miscs'></span>

## 😉 Miscs
- My nickname is little_wolf, which comes from a Chinese pun on my name.
<!-- - My nickname is <span style="background-color: #ffff0082; padding: 2px 4px;">little_wolf</span>, which comes from a Chinese pun on my name. -->
- <span style="color: rgb(99,142,201)">My favorite color is light blue, rgb(99,142,201)</span>.
- I sometimes write blogs on [[Zhihu](https://www.zhihu.com/people/zou-chu-dong-xue-16)].

<!-- <div class="clustrmaps-container" style="width: 300px; height: 180px; overflow: hidden; margin: 1em 0; border: 1px solid #ccc; /* Optional: border helps visualize the container */">
  <script type="text/javascript" id="mapmyvisitors" src="//mapmyvisitors.com/map.js?d=wXhj3VMV8ErHKlAkznvwdiZom4zFOwbyHEAM86vXFIM&cl=ffffff&w=a"></script>
</div> -->