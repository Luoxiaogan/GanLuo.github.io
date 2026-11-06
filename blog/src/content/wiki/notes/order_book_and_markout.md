---
title: Markout and Price Discovery
description: Theory behind the bid-ask spread, adverse selection, stale-quote sniping and the markout
order: 3
updatedDate: 2026-10-27
---

Papers: Glosten–Milgrom (1985) **[GM 1985]**, Glosten (1994) **[G 1994]** , Budish–Cramton–Shim (2015) **[BCS 2015]**, Hasbrouck (1991) **[H 1991]**. Kyle (1985) is background.

Understanding Order Book, theory and empirical study

## 1. Order book, spread and zero profit condition

### 1.1 Order book

The book is the list of standing orders to sell (asks) and to buy (bids), ranked by price.

- **Best bid** $b$: highest price a buyer (provider) is waiting to pay. **Best ask** $a$: lowest price a seller (provider) is waiting to accept.
- **Spread** $= a - b$. **Mid-price** $M = (a+b)/2$. **Half-spread** $= (a-b)/2$.
- A **limit order** names a price and waits; it may never trade. A **market order** trades immediately against the best prices, and a large one walks up the book level by level.

in **[GM 1985]**: a liquidity provider (the specialist) quotes a bid (buy) and an ask (sell). Customers arrive one at a time with market orders. A fraction $\alpha$ are **informed** (they know the value $V$); the rest are **noise** traders who buy or sell at random. The provider cannot tell who is who.

For the provider, his guess of the value $V$ is $M = E[V \mid \text{public info}]$. The provider only trades when someone chooses to trade with his quote, so he must price the quote conditioned on being traded with.

$$
\text{bid} = E[V \mid \text{public}, \text{someone sells}]<M<\text{ask} = E[V \mid \text{public}, \text{someone buys}].
$$

For the bid side, the provider is willing to buy at $b$, "Someone wants to sell" is bad news about $V$, so the provider must buy below $M$. For the ask side, the provider is willing to sell at $a$, "Someone wants to buy" is good news about $V$, so the provider must sell above $M$.

Condider a trade in which a taker buys at the ask (the provider sells) $A=\text{ask}$. Among buyers, let $\alpha$ be the share of informed trader among buyers, and let $I=E[V|\text{public}, \text{informed}]$ be what an informed buyer knows the share is worth. From a noise buyer the provider gains from the half spread $A - M$: the noise trader pays $A$ for something worth $M$ in expectation of public knowledge.

### 1.2 Zero profit condition

**[GM 1985]** assume that liquidity providers compete with each other and this competition drives expected profit to zero (**zero profit condition**) (**Bertrand Competition**: If one provider positive expected profits, other providers will quote a tighter spread and win the order flow, so his profit cannot persist.)

$$
(1-\alpha)\,(A - M) \;=\; \alpha\,(I - A)
\quad\Longleftrightarrow\quad
A = (1-\alpha)\,M + \alpha\, I .
$$

So the spread is what noise traders pay to cover the provider's losses to informed traders. More informed flow means a wider spread. Zero profit is an assumption, not a fact. It comes from competition among providers, and it removes one degree of freedom. In reality market makers earn money: markets are not perfectly competitive.

**[GM 1985]** prices one quote. **[G 1994]**  puts the same logic into a limit order book.

Many patient traders post limit orders; investors send market orders. A market order hits the book **level by level**. Each level is priced at the expected value *given that the order is big enough to reach it*, and big orders are more likely to be informed.
> Small trades pay a positive spread, large trades pay more per share. Limit orders profit on small trades and lose on large informed ones, about zero on average.

## 2. Stale quotes and sniping

Now suppose **nobody has private information**. The provider quotes around the value $M$: bid $= M - S/2$, ask $= M + S/2$. If the value jumps by $J$ and the provider has not yet updated, the ask is **stale**. It can be picked off only when $J > S/2$; the sniper's profit is $J - S/2$.

Value jumps $50 \to 53$, quotes are $49/51$ ($S=2$). There are $N = 4$ trading firms: 1 provider and 3 snipers. All see the news at the same time and the exchange processes messages one at a time in random order. (Here snipers use Immediate-Or-Cancel order i.e. **IOC order**)

| | Provider | Each sniper |
|---|---|---|
| Wins the race | $1/4$ (must beat all three) | $1/4$ each |
| If first | cancels safely | buys at 51 something worth 53: $+2$ |
| If not first | sold at 51 something worth 53: $-2$ | order cancelled: $0$ |
| Expected per jump | $-2 \times \tfrac34 = -1.5$ | $+2 \times \tfrac14 = +0.5$ |

The provider loses on average even though nobody knows more than anybody else. He earns it back from investors through a wider spread. 

In **[BCS 2015]**, free entry makes profit zero after speed costs(expected profits as a sniper minus the costs to speedup), and the cost is **borne**(paid) by investors(noise traders). An informed trader only trades if his edge beats the cost of crossing the spread. Buying at the ask costs $S/2$ above the mid, so an edge below $S/2$ gives negative expected profit and he does not trade.

| | Informed trader (GM, Kyle) | Latency sniper (BCS) |
|---|---|---|
| Knows | private information about fundamentals | the same public information as the provider |
| Edge | knowledge: sees the true value earlier | speed: acts before the provider can cancel |
| Risk | can simply be wrong on a given trade | almost none (IOC order is cancelled if he loses) |

## 3. Who gains, who loses

- **Noise traders** pay the spread to get their trade done right away rather than wait. This is a fee for speed, not a pure loss.
- **Provider** earns the spread from noise traders and pays informed traders **[GM 1985]** and snipers **[BCS 2015]**. Expected profit is about zero under competition (Bertrand Competition).
- **Informed traders / snipers** gain on average when their edge (information or speed) exceeds the half-spread.

For a market to exist some participants must be willing to lose on average. If everyone were rational and equally informed, nobody would trade (**Milgrom–Stokey no-trade theorem**).

## 4. Price discovery, Markout and Price Impact

### 4.1 Price Discovery

**Price discovery is how information enters the price.** A **markout** path is one consequence of price discovery: it measures the **price impact** of trades (4.3), which is only one part of it. Section 5.6 explains the difference.

| | Glosten–Milgrom | Budish et al. |
|---|:--|---|
| Information | held by informed traders, unknown to the provider | public: provider and takers see it at the same time |
| Enters the price through | informed **trades** and the provider's **Bayesian update** | the provider's **cancel**, slow and costly, so stale quotes get sniped |
| A trade tells us | something new | nothing new |

In **[GM 1985]** you (provider) do not know the information; someone (investor) trades and you update. In **[BCS 2015]** you know it already, but it still has to go through trades and cancels, and that is costly.

### 4.2 Markout

For **one trade** with direction $d$ ($+1$ if the taker buys, $-1$ if sells), price $p$, and mid $M_{t+\Delta}$ a time $\Delta$ later, we define the markout of the trader (taker) is:
$$
\text{markout}_{\text{taker}}(\Delta) = d\,\bigl(M_{t+\Delta} - p\bigr) = - \text{markout}_{\text{provider}}(\Delta) .
$$
Here $M_t=E[V|\mathcal{I}_{t}]$, $M_{t+\Delta}=E[V|\mathcal{I}_{t+\Delta}]$, since $\mathcal I_t \cup \{\text{trade}\} \subseteq \mathcal I_{t+\Delta}$(the information at time $t+\Delta$ contains the information at time $t$ and this trade), we have that:
$$
E[M_{t+\Delta}|\mathcal{I}_t, \text{trade}]=E[E[V|\mathcal{I}_{t+\Delta}]|\mathcal{I}_t, \text{trade}]=E[V|\mathcal{I}_t, \text{trade}]
$$
$E[V|\mathcal{I}_{t+\Delta}]$ is random from the view point of $\{\mathcal{I}_t,\text{trade}\}$, but $E[.|\mathcal{I}_t,\text{trade}]$ **averages over the information** that arrives between $t$ and $t+\Delta$ thus integrates out the new information. 

> The future mid $M_{t+\Delta}$ is an **unbiased but noisy** estimate of $E[V \mid \mathcal{I}_t, \text{trade}]$, and the trade price $p$ is known (the trade price). So **one markout of one trade** is one noisy observation of $E[V \mid\mathcal{I}_t, \text{trade}] - p$, and we need many observations (LLN) before the average converges.

| Object | What it is | Example ($M=50$, ask $=60$) |
|---|---|---|
| One trade | a single observation, very noisy | can be positive or negative |
| One trader, all trades | a wallet's average over its trades: that trader's edge | informed wallet $+40$, noise wallet $-10$ |
| All traders | all takers mixed together, $E[V \mid \text{all traders}]$ | $0.8(-10) + 0.2(+40) = 0$ |

Zero profit predicts that only the **last** one is zero. The middle one is what we look for in the data: wallets whose average markout is significantly different from zero.

### 4.3 Price Impact

We can decompose the markout into a part that is known at the time of the trade (the half-spread) and a part that is revealed afterwards (the price impact).
$$
\begin{aligned}
\underbrace{d(M_{t+\Delta} - p)}_{\text{taker markout}}
&= \underbrace{d(M_{t+\Delta} - M_t)}_{\text{price impact}}
- \underbrace{d(p - M_t)}_{\text{half-spread}}, \\[4pt]
\underbrace{d(p - M_t)}_{\text{half-spread}}
&= \underbrace{d(p - M_{t+\Delta})}_{\text{realized spread}}
+ \underbrace{d(M_{t+\Delta} - M_t)}_{\text{price impact}}.
\end{aligned}
$$

When the mid is the efficient price ((1) in 5.2), the price impact contains the information revealed by the trade, $E[V \mid \mathcal I_t, \text{trade}] - M_t$, plus noise from news arriving between $t$ and $t+\Delta$. The noise has mean zero given $\mathcal I_t$ and the trade, so the average price impact over many trades isolates the information content of the trade.
$$
M_{t+\Delta} - M_t
= \underbrace{\bigl(E[V \mid \mathcal I_t, \text{trade}] - M_t\bigr)}_{\text{The information of this trade}}
+ \underbrace{\bigl(M_{t+\Delta} - E[V \mid \mathcal I_t, \text{trade}]\bigr)}_{t\to t+\Delta \text{ new info}}.
$$

## 5. Price Discovery, Closer

### 5.1 Notations

In **[H 1991]** the notation differs from ours. We keep our notation and explain his here.

- **Quote.** The best bid $\cblue{b}=q^b$ and best ask $\cblue{a}=q^a$ of the whole market: posted by the providers (market-maker / specialist), faced by the takers (trader / trading public). We use the equivalent pair (mid, spread): $q^a = q + s/2$, $q^b = q - s/2$, $s = q^a - q^b$.
  - The mid tracks the value and carries the price impact; the spread is the provider's compensation (costs, adverse selection).
  - **$q_t$** is the mid set **after** trade $t$, so a trade meets $q_{t-1}$, which is our $\cblue{M_t}=\cred{q_{t-1}}$.
- **Clock time vs event time.** Our $\cblue{\Delta}$ is in seconds. **[H 1991]** counts events instead: $t$ goes up by one at every trade or quote change in the stock, by anyone, so $k$ steps ahead means $k$ **market events** later.
- **Efficient price.** $E[\cblue{V} \mid \Phi_t]=m_t$($m_t$ in **[H 1991]**), the expected value given public information right after trade $t$. It is not observed. **[H 1991]** first assumes the quotes are symmetric around it, so $q_t = m_t$ (his eq. (1)), which is our $\cblue{M_t = E[V \mid \mathcal I_t]}$; <span class="c-red">he later relaxes it.</span>
- **Quote revision.** $r_t = q_t - q_{t-1}$, the change of the mid. Summing the increments gives the level difference, since the middle terms cancel: $\sum_{k=0}^{K} r_{t+k} = q_{t+K} - q_{t-1}$, our $\cblue{M_{t+\Delta} - M_t}$ with $\cblue{\Delta}$ counted in events.
- **Quote rule.** The 1989 data do not record who initiated a trade, so the sign is **inferred** from the prevailing quotes: above the mid is a buy, below is a sell, at the mid is unknown ($x_t = 0$). **Polymarket records the taker side directly**.
- **Innovation.** A time-series term, not "something new" in the everyday sense: the innovation of a variable is the part the past cannot predict, $y_t - E[y_t \mid \text{past}]$. It has mean zero and is uncorrelated with everything in the past. Example: if buys tend to follow buys and $E[x_t \mid \text{past}] = 0.6$, a buy ($x_t = +1$) has innovation $0.4$ and a sell has $-1.6$. **[H 1991]** has two:
  - $v_{2,t} = x_t - E[x_t \mid \Phi_{t-1}]$, the unexpected part of the trade, our $\cblue{d_t - E[d_t \mid \mathcal I_t]}$;
  - $\cred{v_{1,t}} = r_t - E[r_t \mid \Phi_{t-1}, x_t]$, what is left of the quote revision once the trade is known, read as public news, our $\cblue{R_{t+1} - E[R_{t+1} \mid \mathcal I_t, d_t]}$ (with $\cblue{R_{t+1} = M_{t+1} - M_t}$, defined in 5.2).
  - "The past" is the econometrician's data (past trades and quotes), which may be less than what traders know.

Within one event $t$, **[H 1991]** fixes the order below. It is a convention about the whole market, not about one trader or one provider. The quote is the best bid / ask of **all providers** and the news is seen by everyone. The trade $x_t$ cannot react to news of the same event; the new quote, and so $r_t$, reacts to both(public news and the trade $x_t$).

```mermaid
block-beta
  columns 3
  S1["1. Quote $$q_{t-1}$$ stands"] space S2["2. A taker trades $$x_t$$"]
  space R["$$r_t = q_t - q_{t-1}$$"] space
  S4["4. Providers set $$q_t$$"] space S3["3. Public news arrives"]
  S1 --> S2
  S2 --> S3
  S3 --> S4
  S4 --> S1
```

### 5.2 Equations

From here on $t$ counts events and $M_t$ is the mid just before event $t$. Define the change of the mid

$$
R_t = M_t - M_{t-1},
$$

so $R_{t+1} = M_{t+1} - M_t$ is the change across trade $t$, and $\sum_{k=1}^{\Delta} R_{t+k} = M_{t+\Delta} - M_t$ is our price impact.

**Equation (1): the mid is always the efficient price.**

$$
M_t = E[V \mid \mathcal I_t] \quad \text{for every } t. \tag{1}
$$

- This is what 4.2 assumed. With $\mathcal I_t \subseteq \mathcal I_{t+\Delta}$, the tower property gives $E[M_{t+\Delta} \mid \mathcal I_t] = E\bigl[E[V \mid \mathcal I_{t+\Delta}] \mid \mathcal I_t\bigr] = E[V \mid \mathcal I_t] = M_t$: the mid is a **martingale**, and its future changes cannot be predicted from $\mathcal I_t$.
- **[H 1991]** starts from (1) and later relaxes it to (3).

**Equation (2): a regression for the change of the mid.**

$$
R_{t+1} = \underbrace{a_1 R_t + a_2 R_{t-1} + \cdots}_{\text{past mid changes}}
+ \underbrace{b_0\, d_t}_{\text{this trade}}
+ \underbrace{b_1 d_{t-1} + b_2 d_{t-2} + \cdots}_{\text{past trades}}
+ \cred{v_{1,t}}. \tag{2}
$$

- **$d_t$: the observed trade.** $d_t \in \{+1, -1, 0\}$ is the direction of the taker trade at event $t$: $+1$ for a buy, $-1$ for a sell, $0$ if no trade happens (**[H 1991]**'s $x^0_t$). It is a number at every event. In (2) it enters as a number. In a conditional expectation, "given the trade" means given the value of $d_t$. The **information inside the trade** is the result of that conditioning, how far it moves the expectation of $V$:

  $$
  E[V \mid \mathcal I_t, \text{trade}] - E[V \mid \mathcal I_t]=E[V \mid \mathcal I_t, d_t] - E[V \mid \mathcal I_t].
  $$

  - Given $\mathcal I_t$, knowing $d_t$ is the same as knowing its innovation $d_t - E[d_t \mid \mathcal I_t]$, since the two differ by a known number. So only the innovation can carry information inside the trade; the predictable part (buys tend to follow buys) tells us nothing new.
  - So $b_0 d_t$ is the mid's reaction to the observed trade, not the trade's information content.
- $b_0$ is the immediate reaction of the mid to this trade; $b_1, b_2, \dots$ are delayed reactions to past trades (a slow quote); $a_1, a_2, \dots$ are momentum or reversal in the mid itself (overshoot, then come back if $a_1 < 0$).
- $\cred{v_{1,t}}$ is the part left unexplained, read as public news.
- **Why (2) conflicts with (1).** Under (1) the mid is a martingale, so it can only move on what $\mathcal I_t$ did not know. If any $a_i$ or $b_i$ ($i \ge 1$) is non-zero, past mid changes or past trades predict the next change, and (1) fails. In the data they are non-zero (**[H 1991]** Table II: $a_1 = -0.118$, $b_1 = 0.007$, both significant).

**Equation (3): the mid returns to the efficient price only in the long run.**

$$
\lim_{\Delta \to \infty} E[M_{t+\Delta} \mid \mathcal I_t] = E[V \mid \mathcal I_t]. \tag{3}
$$

- Write $M_t = E[V \mid \mathcal I_t] + u_t$, where $u_t$ is a temporary pricing error (slow quote, inventory, tick size). (1) says $u_t = 0$ always; (3) only says $E[u_{t+\Delta} \mid \mathcal I_t] \to 0$. (1) implies (3), not the other way, which is the sense in which (3) **relaxes** (1).
- Example: after a buy everyone knows $E[V]$ moved from 50 to 53, but the quote steps up one unit per event, $51, 52, 53$. At $M = 51$, $u = -2$: (1) fails, (3) holds.
- Consequence for 4.2: without (1), $E[M_{t+\Delta} \mid \mathcal I_t, \text{trade}] = E[V \mid \mathcal I_t, \text{trade}] + E[u_{t+\Delta} \mid \mathcal I_t, \text{trade}]$, and the last term vanishes only as $\Delta \to \infty$. A short-horizon markout still carries the temporary error, which is why **[H 1991]** measures the persistent impact.
- **Polymarket.** At settlement $M$ is replaced by $V$, so with the horizon running to settlement (3) holds exactly: $E[M_{\text{settle}} \mid \mathcal I_t] = E[V \mid \mathcal I_t]$. Before settlement (1) can fail, for example with a 1¢ tick or a stale book in the last seconds.

**Equation (4): a regression for the trade.**

$$
d_t = \underbrace{\phi_1 d_{t-1} + \phi_2 d_{t-2} + \cdots}_{\text{past trades}}
+ \underbrace{\psi_1 R_t + \psi_2 R_{t-1} + \cdots}_{\text{past mid changes}}
+ \cgreen{v_{2,t}}. \tag{4}
$$

- We write $\phi_i, \psi_i$ for **[H 1991]**'s $d_i, c_i$, which would clash with our $d_t$.
- **Buys tend to follow buys** means $\phi_i > 0$ (**[H 1991]** Table II: $\phi_1 = 0.167$, $\phi_2 = 0.120$, $\phi_3 = 0.078$). Trades also react to past mid changes: $\psi_1 = -3.647$, so after the mid rises a sell is more likely.
- Everything on the right except $\cgreen{v_{2,t}}$ is known at $\mathcal I_t$, so (4) splits the trade into an old and a new part:

  $$
  d_t = \underbrace{E[d_t \mid \mathcal I_t]}_{\text{predictable, old}} + \underbrace{\cgreen{v_{2,t}}}_{\text{innovation, new}} .
  $$

  Example: with only $\phi_1 = 0.167$ and a buy just before, $E[d_t \mid \mathcal I_t] = 0.167$. A buy then has innovation $0.833$, a sell $-1.167$, no trade $-0.167$.
- There is no $R_{t+1}$ on the right: the trade comes before the quote revision it causes, so it cannot react to it (see the timing above). In (2), by contrast, $R_{t+1}$ does depend on $d_t$.
- New is not the same as private. Noise traders also surprise the market, so only part of $\cgreen{v_{2,t}}$ is information: in the linear case the information inside the trade is $\lambda\,\cgreen{v_{2,t}}$, with $\lambda = 0$ if every taker is noise.

**Equation (5): the two innovations are pure surprises.**

$$
\begin{aligned}
&E[\cred{v_{1,t}}] = E[\cgreen{v_{2,t}}] = 0, \\
&E[\cred{v_{1,t}}\,\cred{v_{1,s}}] = E[\cgreen{v_{2,t}}\,\cgreen{v_{2,s}}] = E[\cred{v_{1,t}}\,\cgreen{v_{2,s}}] = 0 \quad (s \ne t).
\end{aligned} \tag{5}
$$

- They also satisfy $E[\cred{v_{1,t}}\,\cgreen{v_{2,t}}] = 0$ at the same $t$, because (2) already contains $d_t$: whatever in $R_{t+1}$ moves with the trade is in $b_0 d_t$, not in $\cred{v_{1,t}}$.
- So a shock to $\cgreen{v_{2,t}}$ can be studied on its own, holding all other shocks at zero. That is what (6) does.

**Equation (6): the information of a trade is the long-run change in the efficient price.**

Start from rest (all past $d$ and $R$ equal to zero), give one unit of trade innovation at $t$, $\cgreen{v_{2,t}} = 1$, set every other shock to zero, and run (2) and (4) forward:

$$
\begin{aligned}
d_t &= 1, \\
R_{t+1} &= b_0, \\
d_{t+1} &= \phi_1 d_t + \psi_1 R_{t+1}, \\
R_{t+2} &= a_1 R_{t+1} + b_0 d_{t+1} + b_1 d_t, \\
&\;\;\vdots
\end{aligned}
$$

These are the expected trades and mid changes that follow one surprise. Add up the mid changes:

$$
\alpha_\Delta = \sum_{k=1}^{\Delta} E\bigl[R_{t+k} \mid \cgreen{v_{2,t}} = 1\bigr] = E\bigl[M_{t+\Delta} - M_t \mid \cgreen{v_{2,t}} = 1\bigr]. \tag{6}
$$

- $\alpha_\Delta$ is the price impact of one unit of **surprise**, not of one raw trade. It includes the follow-on trades that (4) predicts and the slow adjustment of the mid in (2), all caused by this one surprise.
- By (3), as $\Delta \to \infty$ the temporary error $u$ dies out and $\alpha_\Delta$ converges to the change in the **efficient price**:

  $$
  \lim_{\Delta \to \infty} \alpha_\Delta = E[V \mid \mathcal I_t, \cgreen{v_{2,t}} = 1] - E[V \mid \mathcal I_t],
  $$

  the information inside one unit of trade innovation. This limit is **[H 1991]**'s measure of information.
- If (1) holds (no lags, $b_0 = \lambda$), $\alpha_\Delta = \lambda$ at every $\Delta$: the short and long horizons agree. When they disagree, the gap is the temporary part.
- For Ames Department Stores (**[H 1991]** Figure 1) a buy moves the mid by about \$0.014 at once and about \$0.028 after 20 events: the full impact is about twice the immediate one and arrives with a lag.

### 5.3 VAR

(2) and (4) together are a **vector autoregression** (VAR), a standard tool of time-series econometrics (Sims, 1980; see Hamilton, *Time Series Analysis*, ch. 10–11): several series modelled at once, each regressed on the past of all of them, and then simulated forward to see how a shock spreads (the *impulse response*). Macroeconomists use it to trace, say, a rate shock through output and inflation; **[H 1991]** uses it to trace a trade surprise through later trades and the mid. Two regressions, then one forward computation.

**What to regress.** Both equations, truncated at $K$ lags (**[H 1991]** uses $K = 5$), each by OLS on its own. Every regressor is observed data. Below, $a_i, b_i, \phi_i, \psi_i$ are the true coefficients and $\hat a_i, \hat b_i, \hat\phi_i, \hat\psi_i$ their OLS estimates (**[H 1991]**'s tables report the estimates without hats).

$$
R_{t+1} = \sum_{i=1}^{K} a_i\, R_{t+1-i} + \sum_{i=0}^{K} b_i\, d_{t-i} + \cred{v_{1,t}}, \tag{2'}
$$

$$
d_t = \sum_{i=1}^{K} \phi_i\, d_{t-i} + \sum_{i=1}^{K} \psi_i\, R_{t+1-i} + \cgreen{v_{2,t}}. \tag{4'}
$$

- (2') is (2) cut at $K$ lags: the mid change across trade $t$ on the last $K$ mid changes ($R_t, \dots, R_{t-K+1}$), this trade ($d_t$) and the last $K$ trades ($d_{t-1}, \dots, d_{t-K}$). It gives $\hat a_i, \hat b_i$.
- (4') is (4) cut at $K$ lags: the trade on the last $K$ trades and the last $K$ mid changes, with no $R_{t+1}$ on the right. It gives $\hat\phi_i, \hat\psi_i$, and its residual $\hat v_{2,t}$ estimates the trade innovation $\cgreen{v_{2,t}}$.

**Order of computation.**

1. Build $R_t$ and $d_t$ from the data, in event time.
2. Regress (2') to get $\hat a_i, \hat b_i$, and (4') to get $\hat\phi_i, \hat\psi_i$. The two regressions do not depend on each other.
3. Run (6): start from zero, set $d_t = 1$ (that is, $\cgreen{v_{2,t}} = 1$), keep every other shock at zero, and alternate between the two fitted equations, each step using the values already computed:

   $$
   d_t = 1
   \;\xrightarrow{(2')}\; R_{t+1}
   \;\xrightarrow{(4')}\; d_{t+1}
   \;\xrightarrow{(2')}\; R_{t+2}
   \;\xrightarrow{(4')}\; d_{t+2}
   \;\longrightarrow\; \cdots
   $$

   Written out, with every value before the shock set to zero ($d_s = 0$ for $s < t$, $R_s = 0$ for $s \le t$):

   $$
   \begin{aligned}
   R_{t+k+1} &= \sum_{i=1}^{K} \hat a_i\, R_{t+k+1-i} + \sum_{i=0}^{K} \hat b_i\, d_{t+k-i}, && k \ge 0, \\
   d_{t+k} &= \sum_{i=1}^{K} \hat\phi_i\, d_{t+k-i} + \sum_{i=1}^{K} \hat\psi_i\, R_{t+k+1-i}, && k \ge 1.
   \end{aligned}
   $$

   At each step $k$ compute $d_{t+k}$ first (it needs $R_{t+k}$), then $R_{t+k+1}$ (it needs $d_{t+k}$).

4. Add up the mid changes until the sum stops changing (**[H 1991]** stops at $\Delta = 20$):

   $$
   \hat\alpha_\Delta = \sum_{k=1}^{\Delta} R_{t+k}.
   $$

   Its limit as $\Delta \to \infty$ estimates the information of one unit of trade surprise. Since it is built from estimates, $\hat\alpha_\Delta$ is an estimate of $\alpha_\Delta$ in (6) and has sampling error; its standard error needs the delta method or a bootstrap.

**The same computation as a partial derivative.** Why does "give one shock, set the others to zero, run forward" measure the price impact? Substitute one equation into the other and keep expanding.

1. **Substitute (4) into (2).** The trade $d_t$ on the right of (2) is itself given by (4):

   $$
   R_{t+1} = \sum_i a_i R_{t+1-i} + b_0\Bigl(\sum_i \phi_i d_{t-i} + \sum_i \psi_i R_{t+1-i} + \cgreen{v_{2,t}}\Bigr) + \sum_{i \ge 1} b_i d_{t-i} + \cred{v_{1,t}}.
   $$

2. **Keep substituting.** Every past $R$ and $d$ on the right is again given by (2) and (4), with older values and older shocks. Replace them, then replace the older ones, and so on. Each round pushes the lagged terms further into the past; with stable coefficients they shrink to zero. What is left is a sum of shocks only, the **moving-average form** of the VAR:

   $$
   R_{t+1} = \sum_{j \ge 0} \theta_j\, \cgreen{v_{2,t-j}} + \sum_{j \ge 0} \gamma_j\, \cred{v_{1,t-j}},
   \qquad
   M_{t+\Delta} - M_t = \sum_{k=1}^{\Delta} R_{t+k} = \sum_{k=1}^{\Delta} \sum_{j \ge 0} \Bigl(\theta_j\, \cgreen{v_{2,t+k-1-j}} + \gamma_j\, \cred{v_{1,t+k-1-j}}\Bigr).
   $$

   The coefficients $\theta_j, \gamma_j$ are products and sums of $a_i, b_i, \phi_i, \psi_i$, one for every path along which a shock reaches $R$.

3. **Differentiate.** The price impact of one trade surprise is the partial derivative with respect to it:

   $$
   \alpha_\Delta = \frac{\partial\,(M_{t+\Delta} - M_t)}{\partial\, \cgreen{v_{2,t}}} = \sum_{k=1}^{\Delta} \theta_{k-1}.
   $$

   The derivative removes every other term of the expansion: the public news $\cred{v_{1,s}}$ at every date, and the trade surprises $\cgreen{v_{2,s}}$ at other dates $s \neq t$. Only the terms that contain $\cgreen{v_{2,t}}$ survive. Because the system is linear, the derivative does not depend on where it is taken; because the shocks are uncorrelated (5), it also equals the expected response $E[M_{t+\Delta} - M_t \mid \cgreen{v_{2,t}} = 1] - E[M_{t+\Delta} - M_t \mid \cgreen{v_{2,t}} = 0]$. This is (6).

4. **Read off the expansion.** The forward recursion of step 3 computes exactly these coefficients:

   $$
   \theta_0 = b_0, \qquad \theta_1 = a_1 b_0 + b_0(\phi_1 + \psi_1 b_0) + b_1, \qquad \dots
   $$

   $\theta_1$ has three paths: the mid's own lag ($a_1 b_0$), the follow-on trade that the first trade predicts and its impact ($b_0(\phi_1 + \psi_1 b_0)$), and the delayed reaction to the first trade ($b_1$). The **permanent** impact is the full sum $\alpha_\infty = \sum_{j \ge 0} \theta_j$; the **temporary** impact at $\Delta$ is the part not yet added, $\alpha_\Delta - \alpha_\infty = -\sum_{j \ge \Delta} \theta_j$ (5.4). Differentiating with respect to $\cred{v_{1,t}}$ instead gives the impact of public news, $\sum_j \gamma_j$, which is the $\beta_\infty$ of 5.6.

### 5.4 Permanent and temporary price impact

With $M = E[V \mid \mathcal I] + u$ from (3), the impact of one unit of trade surprise splits into two parts:

$$
\alpha_\Delta
= \underbrace{\alpha_\infty}_{\text{permanent}}
+ \underbrace{\bigl(\alpha_\Delta - \alpha_\infty\bigr)}_{\text{temporary} \; = \; E[u_{t+\Delta} \mid \cgreen{v_{2,t}} = 1] \;\to\; 0}.
$$

- **Permanent**: the move in the efficient price, i.e. the information in the trade. It never reverses.
- **Temporary**: the pricing error $u$ (inventory, slow quotes, tick size, split orders). It dies out and can have either sign: overshoot in the toy model of §II ($2 \to 1$), undershoot for Ames Department Stores (\$0.014 → \$0.028). Almost every non-information effect is temporary, so $\Delta \to \infty$ removes them all.
- **Why it matters**: a short-horizon markout mixes the two parts, and only a long horizon splits the half-spread of 4.3 cleanly into realized spread and information. On Polymarket settlement gives the permanent part directly ($M = V$, $u = 0$), without bias but with the noise of the outcome (5.6).

### 5.5 When the reading fails

The VAR reads $\cred{v_{1,t}}$ as public news and $\cgreen{v_{2,t}}$ as private information plus noise. **[H 1991]** §III.B lists how this reading can fail. The estimates stay consistent; only the attribution goes wrong, and the paper offers no fix.

- **Quote setters know things too** (the specialist sees the book). Their information is not measured.
- **Public news leaks into $\cgreen{v_{2,t}}$** when the quote cannot follow it: price smoothing, stale reported quotes, stale limit orders that get picked off. The VAR then counts public news as trade information. Formally the reading needs $E[\cgreen{v_{2,t+k}} \mid \mathcal I^*_t] = 0$ for $k \ge 0$, where $\mathcal I^*_t$ is all public information, news included (his (14)).
- **Misspecification.** Another model gives other innovations, and another split.

**Polymarket.** Stale limit orders are the sniping of section 2: BTC moves on an outside exchange, the Up book lags, takers pick off the stale quotes before the close, and the VAR reports $\hat\alpha > 0$ although nobody has private information. A possible fix (ours, not in **[H 1991]**, in the spirit of Hasbrouck 1995): add the outside BTC price change as a regressor.

### 5.6 Price impact and price discovery

Two different questions about the same price path.

| | Price impact | Price discovery |
|---|---|---|
| Question | How far does one trade move the price, and how much of the move stays? | Through which channels does new information enter the price, and how much through each? |
| Unit | one trade, or one unit of trade surprise $\cgreen{v_{2,t}}$ | every change of the efficient price over a period, with or without a trade |
| Statistic | a mean, as a curve in $\Delta$: $\alpha_\Delta$ in (6) | a share of a variance |
| Split | permanent $\alpha_\infty$ + temporary $\alpha_\Delta - \alpha_\infty$ (5.4) | trades vs. quotes and public news (vs. other markets) |

**Price discovery as a variance share.** Let $w_t$ be the change of the efficient price caused by the shocks of event $t$. It is the long-run response to each shock: $w_t = \alpha_\infty\,\cgreen{v_{2,t}} + \beta_\infty\,\cred{v_{1,t}}$, where $\beta_\infty$ is the cumulative response of the mid to one unit of $\cred{v_{1,t}}$, computed like (6). The two shocks are uncorrelated (5), so their variances add:

$$
\operatorname{Var}(w_t) = \alpha_\infty^2\,\sigma_2^2 + \beta_\infty^2\,\sigma_1^2,
\qquad
IS_{\text{trade}} = \frac{\alpha_\infty^2\,\sigma_2^2}{\alpha_\infty^2\,\sigma_2^2 + \beta_\infty^2\,\sigma_1^2},
$$

with $\sigma_2^2 = \operatorname{Var}(\cgreen{v_{2,t}})$ and $\sigma_1^2 = \operatorname{Var}(\cred{v_{1,t}})$. $IS_{\text{trade}}$ is the share of the efficient-price variance that comes from trades, Hasbrouck's (1991b) summary measure of how informative trades are. **[H 1991]** mentions it (§VII) but does not estimate it. Hasbrouck (1995) applies the same idea across markets that trade one asset; here the other market is Binance.

- Price impact is one input to price discovery, not the same thing. $IS_{\text{trade}}$ also depends on how large and how frequent trade surprises are ($\sigma_2^2$) and on everything that moves the price without a trade ($\beta_\infty^2\sigma_1^2$). In BTC 5-minute markets (section 9) one unit of trade surprise moves the Up mid by about 0.3¢ for good, yet trades explain only about 10–15% of the efficient-price variance: most information enters through the quotes.
- Only the permanent part counts for discovery. The temporary part moves the mid but not $E[V \mid \mathcal I]$.

**Why markouts measure price impact.**

- The price-impact part of a markout, averaged over trades, estimates $E[M_{t+\Delta} - M_t \mid \text{trade}]$ (4.2–4.3): news after the trade averages out. It needs no model and no lag cutoff, one $\Delta$ at a time. The durability $\alpha_\Delta/\alpha_\infty$ and the permanent/temporary split of 5.4 read straight off the curve.
- It is the same object as (6), estimated another way. Regressing $M_{t+\Delta} - M_t$ on the trade at $t$, separately for each $\Delta$, is a *local projection* (Jordà 2005) of the impulse response; the VAR gets it by iterating (2') and (4'). In population the two agree when the VAR has enough lags (Plagborg-Møller and Wolf 2021).
- Two conditions for a clean impact:
  1. **Use the surprise, not the raw trade.** Buys follow buys ($\phi_i > 0$), so the markout of a raw buy also carries the delayed impact of the earlier buys it moves with, and any drift of the mid. Regress on $\hat v_{2,t}$ from (4'), or keep past trades and mid changes as controls.
  2. **Choose the horizon.** On Polymarket the settlement horizon gives the permanent impact without bias ($M = V$), but each trade then carries the noise of the outcome: $\operatorname{Var}(V \mid M) = M(1-M)$, up to $\pm 50$¢ per share. The bands of 6.3 are several cents wide even with 288 cycles. A horizon where the curve has already flattened (about 10 s for the wallet of 8.3) is far less noisy; settlement is then the check.

**Why markouts do not measure price discovery.**

1. **They only look where the trades are.** Discovery has to account for every change of the efficient price, including quotes that market makers move after a Binance move without any trade (the clock-time "quotes" share of section 9, 0.73–0.90 in the full sample). An average taken at trade times says nothing about those.
2. **Markouts of nearby trades overlap, so they do not add up.** The window $[t, t+\Delta]$ of one trade contains the next trades and their impacts: two buys one second apart each get the impact of both in a 10-second markout. Summing markouts over trades counts the same move several times, and the resulting "shares" do not sum to one. Splitting a total needs shocks that are uncorrelated with each other, so that their variances add. That is what (5) provides, and why the VAR innovations are needed.
3. **Impact is not contribution.** A sniper who hits a stale quote after Binance moved has a large markout (section 2, 8.3), but the information was already public and the quote would have moved anyway. The markout credits the trade; discovery asks what the trade added beyond what would have entered the price without it. That needs a counterfactual, here a model that includes the outside price (5.5).

**What a markout can still do.** Condition it on the outside price. In BTC 5-minute markets $V$ depends only on the BTC price at the close, so any information about $V$ is information about where BTC is going. Around a Polymarket trade (Figure 28), the part of its permanent impact that Binance already showed before the trade is public information carried over from Binance. The part that Binance shows only after the trade is information that neither market had yet: private information of the Glosten–Milgrom kind, with Polymarket leading Binance. This splits the impact of a trade into public and private parts, but still says nothing about the price changes without trades. Section 8.3 does this for the fastest wallet, and sections 9.4–9.5 build the full decomposition.

## 6. Example: taker markout in Polymarket BTC 5-minute markets (To Be Edit)

### 6.1 Setup

- **Data.** Pendulum mirror on Oak (`pmxt/v2`, order book and trades with millisecond timestamps), Polymarket data-api (wallets) and gamma (market info, resolution, fee schedule).
- **Sample.** 2026-08-06, 288 five-minute cycles. This is before the switch to 60-second TWAP settlement (2026-08-07), so every cycle settles on the Chainlink closing price.
- **Markout**, in cents per share, always for the **Up** token:
$$
\text{markout}_i(\Delta) = 100 \cdot d_i\,\bigl(M_{t_i+\Delta} - p_i\bigr).
$$
  - $d_i = +1$ for a **taker-long** trade (buy Up or sell Down), $d_i = -1$ for a **taker-short** trade (sell Up or buy Down). The price of a Down trade at $q$ is converted to $1-q$.
  - $M$ is the Up mid-price $(\text{best bid} + \text{best ask})/2$. At $\Delta = 0$ we use the book just before the trade (the trade timestamp minus 180 ms, because trade timestamps in pmxt are about 100–300 ms later than the book). Afterwards we use the last **two-sided** book at $t+\Delta$: a best bid of $0$ or a best ask of $1$ means that side of the book is empty (valid prices are 0.001–0.999), and then the last two-sided mid is carried forward. Once the market has settled (past the last quote of the cycle), $M$ is replaced by the final value $V \in \{0, 1\}$.
  - One taker trade is one transaction: the data-api taker rows and the pmxt trade events both have one row per `transaction_hash`, so the fills of a marketable order that walks the book are already merged, at their volume-weighted price.
- **Taker fee.** On 2026-08-06 every cycle has the gamma fee schedule `crypto_fees_v2` (rate $0.07$, exponent $1$, takers only, 20% rebated to makers). The fee per share is
$$
\text{fee}_i = 100 \cdot 0.07 \cdot p_i\,(1 - p_i) \quad \text{cents},
$$
  with $p_i$ the price of the traded token: $1.75$¢ at $p = 0.5$, $0.63$¢ at $p = 0.1$ or $0.9$. This matches the fee table in the Polymarket documentation; it has not yet been checked against the on-chain `OrderFilled` fee. The **net** markout is $\text{markout}_i(\Delta) - \text{fee}_i$.
- **Averaging.** *Equal-weighted* (blue): every trade counts the same. *Volume-weighted* (orange): weights are shares. In the pooled figures, solid lines are gross of fees and dashed lines (same color) are net of the taker fee; the legend gives the average fee. In the 288-cycle figures the shaded band (equal-weighted) and the thin orange lines (volume-weighted) are 95% **confidence intervals** for the gross lines, clustered by cycle. The net line is the gross line shifted by a fee that barely varies across cycles, so its band is not drawn.
- **Sample filters.** Of the 533,464 taker trades of the 288 cycles we drop those missing from pmxt because of WebSocket drops (5.3%; data-api has them with second timestamps only), those whose price falls on the wrong side of the reference quote (`wrong_side`, 2.4%, mostly in the last seconds before the close) and those with only a one-sided book just before the trade (1.5%). Scripts: `scripts/btc5m/` in the research repo.

### 6.2 One cycle: `btc-updown-5m-1786057200`

2026-08-06 23:00–23:05 UTC, **Up won**. The book was very volatile in the last 10 seconds (Up dropped from about 0.95 to about 0.3) without flipping the outcome. Figures 1–6 are gross of fees.

**One trade (Figure 1).** A taker bought 8 Up shares at 0.18, 102.5 s into the window, with a pre-trade mid of 0.175. The markout at $\Delta = 0$ is about $-0.5$¢ (half-spread). The sharp drop at $\Delta \approx 188$ s is the collapse of the book about 10 s before the close. The dashed line marks the close of the window; after it the curve is flat at $80.5$¢: the Up ask side is empty after the close, so the last two-sided mid ($0.985$) is carried forward. For this trade $t + 300$ s is still before the last quote of the cycle, so the curve never reaches the realized payoff $100\,(1 - 0.18) = 82$¢.

**The first 200 trades (Figure 2).** Gray lines are single trades and the blue line is their equal-weighted mean. The trades run from 298 s before the window opened to 122 s into it (negative time means before the open).

| *Figure 1. Markout of one taker-long trade.* | *Figure 2. First 200 taker-long trades, individual curves and their mean.* |
|:--:|:--:|
| ![One taker-long trade (btc-updown-5m-1786057200)](./assets/btc5m_markout/single_cycle/1_single_long.png) | ![First 200 taker-long trades, equal-weighted](./assets/btc5m_markout/single_cycle/2_first200_long_ew.png) |

**All trades of the cycle**, long and short, equal-weighted and volume-weighted. Figures 3–6 share the same vertical scale.

| *Figure 3. All taker-long trades (853), equal-weighted.* | *Figure 4. All taker-long trades, volume-weighted.* |
|:--:|:--:|
| ![All taker-long trades, equal-weighted](./assets/btc5m_markout/single_cycle/3_all_long_ew.png) | ![All taker-long trades, volume-weighted](./assets/btc5m_markout/single_cycle/4_all_long_vw.png) |

| *Figure 5. All taker-short trades (710), equal-weighted.* | *Figure 6. All taker-short trades, volume-weighted.* |
|:--:|:--:|
| ![All taker-short trades, equal-weighted](./assets/btc5m_markout/single_cycle/5_all_short_ew.png) | ![All taker-short trades, volume-weighted](./assets/btc5m_markout/single_cycle/6_all_short_vw.png) |

**What to take from it.** Up rose and won, so the long curves climb to about $+36$¢ (equal-weighted) or $+44$¢ (volume-weighted), and the short curves fall to about $-47$¢ or $-42$¢. These end values are mostly the realized payoff $100\,d\,(V - p)$ of this one cycle, not evidence that takers had information. Trades from the same cycle share one price path and one outcome, so they are not independent and no confidence band is drawn.

### 6.3 Several cycles pooled

Trades from all cycles are pooled and averaged together (cycles with more trades get more weight). We do not average cycle by cycle first.

#### 5 cycles (23:00–23:25 UTC, Up won 2 of 5)

With only five clusters we do not draw confidence intervals.

| *Figure 7. 5 cycles, all taker-long trades (2,680).* | *Figure 8. 5 cycles, all taker-short trades (3,177).* |
|:--:|:--:|
| ![5 cycles, all taker-long](./assets/btc5m_markout/pooled/5cycles_1_all_long.png) | ![5 cycles, all taker-short](./assets/btc5m_markout/pooled/5cycles_2_all_short.png) |

The equal-weighted and volume-weighted curves already disagree a lot (at $\Delta = 300$ s, long: about $+6.6$¢ vs $+9.4$¢; short: about $-3.2$¢ vs $-7.8$¢). With so few cycles, a handful of large trades decides the picture. The average taker fee is about $1.1$–$1.3$¢ per share, so every net curve sits that much below its gross curve.

Wallet `0xe0229e10…` is the second-largest taker by volume in these 5 cycles, with balanced long and short trades. We follow it for all its taker trades (54), only its long trades (23), and only its short trades (31). Its average fee is about $1.4$¢ per share.

![5 cycles, wallet 0xe0229e10, all trades](./assets/btc5m_markout/pooled/5cycles_3_wallet_all.png)

*Figure 9. Wallet `0xe0229e10…`, all its taker trades.*

| *Figure 10. Wallet `0xe0229e10…`, taker-long trades.* | *Figure 11. Wallet `0xe0229e10…`, taker-short trades.* |
|:--:|:--:|
| ![5 cycles, wallet 0xe0229e10, long](./assets/btc5m_markout/pooled/5cycles_4_wallet_long.png) | ![5 cycles, wallet 0xe0229e10, short](./assets/btc5m_markout/pooled/5cycles_5_wallet_short.png) |

The numbers of trades are tiny, so these curves are mostly noise.

#### 288 cycles (2026-08-06, full day, Up won 133)

| *Figure 12. 288 cycles, all taker-long trades (239,421 trades, 6.72M shares).* | *Figure 13. 288 cycles, all taker-short trades (245,228 trades, 6.76M shares).* |
|:--:|:--:|
| ![288 cycles, all taker-long](./assets/btc5m_markout/pooled/288cycles_1_all_long.png) | ![288 cycles, all taker-short](./assets/btc5m_markout/pooled/288cycles_2_all_short.png) |

| Cents per share | Average fee | $\Delta = 0$ | $\Delta = 10$ s | $\Delta = 60$ s | $\Delta = 300$ s |
|---|---|---|---|---|---|
| Long, equal-weighted: gross → net | 1.22 | −0.77 → −1.98 | +0.01 → −1.21 | −0.14 → −1.36 | −1.03 → −2.25 |
| Long, volume-weighted: gross → net | 1.19 | −0.87 → −2.06 | −0.06 → −1.25 | −0.18 → −1.37 | −1.67 → −2.86 |
| Short, equal-weighted: gross → net | 1.21 | −0.78 → −1.99 | +0.14 → −1.07 | +0.31 → −0.90 | +1.77 → +0.56 |
| Short, volume-weighted: gross → net | 1.18 | −0.89 → −2.07 | +0.12 → −1.05 | +0.35 → −0.82 | +1.47 → +0.29 |

- At $\Delta = 0$ the gross curves start at about $-0.8$¢: the average half-spread paid by a taker.
- **Gross of fees**, within the first seconds the curves return to about $0$ (long about $0$, short about $+0.1$¢ at $\Delta = 10$ s): the price impact roughly offsets the half-spread. This is the qualitative shape the zero-profit model predicts for takers as a group.
- **Net of fees**, takers lose about $1$–$1.4$¢ per share at $\Delta = 10$–$60$ s. The fee (about $1.2$¢) is larger than the half-spread (about $0.8$¢), so nearly all of the net loss at short horizons is the fee. Of the fee, 80% goes to the venue and 20% is rebated to makers.
- At $\Delta = 300$ s, long is about $-1.0$¢ gross (equal-weighted; $-1.7$¢ volume-weighted) and short about $+1.8$¢ ($+1.5$¢). The signs are what we would expect from Down winning more cycles that day (155 of 288), that is, from drift in the outcome, not from information.
- The 95% bands are several cents wide at long horizons (roughly $-5.7$ to $+3.7$¢ for long, equal-weighted, at $\Delta = 300$ s) and always contain $0$. We cannot reject zero, but with a band this wide, relative to a half-spread of about $0.8$¢, the test has little power.

Wallet `0x66b1c3fe…`: among wallets with at least 50 trades in each direction, the one with the largest taker volume (2,949 trades, 611,730 shares, active in 176 cycles).

![288 cycles, wallet 0x66b1c3fe, all trades](./assets/btc5m_markout/pooled/288cycles_3_wallet_all.png)

*Figure 14. Wallet `0x66b1c3fe…`, all its taker trades.*

| *Figure 15. Wallet `0x66b1c3fe…`, taker-long trades (1,363).* | *Figure 16. Wallet `0x66b1c3fe…`, taker-short trades (1,586).* |
|:--:|:--:|
| ![288 cycles, wallet 0x66b1c3fe, long](./assets/btc5m_markout/pooled/288cycles_4_wallet_long.png) | ![288 cycles, wallet 0x66b1c3fe, short](./assets/btc5m_markout/pooled/288cycles_5_wallet_short.png) |

For all trades, the gross equal-weighted curve stays near $0$ (about $+0.2$¢ at $\Delta = 300$ s) and the volume-weighted curve near $-0.3$¢, with bands that contain $0$ throughout (the volume-weighted band is wider). Net of its fee (about $1.2$¢ equal-weighted, $1.0$¢ volume-weighted), the wallet is at about $-1$ to $-2$¢ per share. The long and short curves separate somewhat but their bands are even wider. On this day there is no detectable edge for this wallet before fees. It was chosen by volume, not by its markout, so there is no selection on the outcome.

### 6.4 Caveats and next steps

- **Fee not verified on chain.** The fee follows the gamma fee schedule and the documented formula; it has not been checked against the on-chain `OrderFilled` fee of individual trades. The maker rebate (20% of taker fees, paid daily) is not included in any curve.
- **One day.** Cycles on the same day share one market environment, so clustering by cycle may understate the uncertainty. More days are needed.
- **Long and short are plotted separately.** The zero-profit condition is about all takers together, so the next step is a single curve with long and short pooled, in which the drift of the day largely cancels.
- **Large $\Delta$ is not a pure mid-price markout.** For trades near the close, a large part of the horizon is after settlement, where $M$ is replaced by $V$. The curve then moves toward the unbiased payoff $d\,(V - p)$.
- **Fills vs orders.** One trade is one transaction, so the fills of one marketable order matched in one transaction are merged. An order matched across several transactions, or a remainder that rests and fills later as a maker, still appears as several observations.
- **Dropped trades.** `wrong_side` trades and trades with a one-sided book are concentrated in the most volatile seconds before the close, which are exactly where informed or sniping trades are most likely.

## 7. All takers and all providers (To Be Edit)

Section 6 plots taker-long and taker-short separately. The object the zero-profit condition is about is **all takers together**, and on the other side **all providers**.

### 7.1 Why there is one curve, not four

- In every fill the taker and the maker take opposite positions in the Up token: a taker that goes long Up (buys Up or sells Down) meets a maker that goes short Up (sells Up, or buys Down in a mint), and the other way round. The shares are the same and the Up-equivalent price is the same, so per share
$$
\text{markout}_{\text{maker}}(\Delta) = -\,\text{markout}_{\text{taker}}(\Delta),
$$
  as in 4.2. Summed over fills, the share-weighted provider curve is **exactly** minus the taker curve. It is an accounting identity, not a finding.
- So of the four lines (taker-long, taker-short, maker-long, maker-short) only two are independent, and their share-weighted average is the all-taker curve. In one cycle the long and short curves are dominated by the realized price path (6.2): a common move $D$ enters long with $+$ and short with $-$. Their average cancels most of it; their difference $\approx 2D$ is mostly the path. Splitting by direction is a diagnostic, not the main result.
- **Fees break the mirror.** Takers pay $0.07\,p(1-p)$ per share; makers pay nothing and get 20% of the taker fees back as rebates (see 8.4). Net of fees: taker net + provider net = − the venue's share of the fees.
- Equal-weighted curves differ: per taker trade on one side, per maker fill on the other (one taker trade meets several makers).

### 7.2 Complete fills: 119 cycles

The provider curve is computed directly from every maker fill (data-api `takerOnly=false`), on 2026-08-06 14:05–24:00 UTC. In these cycles the paging limit of data-api (11,000 rows per query) is not hit, so the fills are complete. The six busiest cycles of the day cannot be completed; on-chain fills were not available from Sherlock.

- 210,506 taker trades and 420,700 maker fills. Taker shares = maker shares = 5.67M; the sum of the two volume-weighted curves is zero at every $\Delta$ (largest gap $5\times10^{-7}$¢).
- **Gross**: takers about −0.15¢ per share at $\Delta$ = 10–60 s (−0.6¢ at 300 s); providers the mirror image.
- **Net**: takers about −1.4¢ (fee 1.24¢); providers about +0.4¢ (rebate 0.25¢).

| *Figure 17. 119 cycles, all takers vs all providers, gross.* | *Figure 18. The same, net of fees (providers: plus the rebate).* |
|:--:|:--:|
| ![119 cycles gross](./assets/btc5m_markout/takers_providers/119cycles_1_takers_providers_gross.png) | ![119 cycles net](./assets/btc5m_markout/takers_providers/119cycles_2_takers_providers_net.png) |

### 7.3 Four months: 2026-04-14 to 08-09

Here takers come from the pmxt trade events and providers are the mirror (exact in dollars, see 7.1), which covers every cycle with order books. That is 97 days and 66M taker trades; pmxt has no BTC 5-minute books from about 06-13 to 07-13. CIs are clustered by day.

| Period | Takers, gross ¢/share at Δ = 10 / 60 / 300 s | Takers, net of fee at 60 s | Providers, plus rebate at 60 s |
|---|---|---|---|
| 04-14 to 08-09 (97 days) | −0.60 / −0.68 / −0.56 | −1.79 | +0.90 |
| from 04-28 (83 days) | −0.48 / −0.57 / −0.47 | −1.69 | +0.79 |

By month, the takers' gross loss shrinks from about −1.4¢ (April) to −0.75¢ (May) and −0.06 to −0.3¢ (June–August) (Figure 21).

| *Figure 19. All takers vs all providers, 04-14 to 08-09.* | *Figure 20. The same from 04-28, when fees are paid in USDC (8.2).* |
|:--:|:--:|
| ![four months](./assets/btc5m_markout/takers_providers/full_1_all_takers_providers.png) | ![from April 28](./assets/btc5m_markout/takers_providers/full_1_post_20260428_takers_providers.png) |

![by month](./assets/btc5m_markout/takers_providers/full_6_takers_providers_by_month.png)

*Figure 21. All takers (gross, solid; net of fee, dashed) and all providers (plus rebate, dotted) by month.*

### 7.4 Reading

- **Takers as a group lose even before fees**, and providers earn the mirror image. With fees, takers lose about 1.2–1.8¢ per share. The venue keeps up to 80% of the fees (less the taker rebates of 8.4), so the net gain of providers (about +0.4 to +0.9¢) is much smaller than the takers' net loss.
- Zero profit (1.2) would put the gross provider curve at about 0. It is positive, but it has fallen towards 0 over the months, which is what more competition among providers would do.
- Before 2026-04-28 the taker fee was charged in shares rather than USDC. On the fills of the wallet of section 8 it matches the fee schedule (8.2), so the April "net" lines are about right; most March cycles had an older, lower fee schedule.
- The group average hides who wins: in section 8 one fast taker earns +1¢ per share gross, while the smallest takers lose 8¢ or more.

### 7.5 Price impact by trade size, side, price level and time

Here the object is the **price impact** of 4.3 and 5.6, not the markout: how far the Up mid moves after a taker trade, and how much of the move stays.

- **Sample.** 2026-04-14 to 08-06 (94 days with books, all before the TWAP switch), every taker trade inside the live window $[t_0, t_0 + 300\text{ s})$: 62.6M trades. Dropped: trades before the open (3.0M), `wrong_side` (1.3M), no two-sided book just before the trade (1.0M).
- **Impact** in cents of the Up price, $\text{imp}(\Delta) = 100\, d\,(M_{t+\Delta} - M_t)$, with $M_t$ the mid just before the trade (6.1). At settlement $M = V$, so $\text{imp}(\text{settle})$ is the permanent impact. The durability is $\text{imp}(\Delta)/\text{imp}(\text{settle})$. Equal-weighted per trade; 95% CIs clustered by day. Since the markout is the impact minus the half-spread (4.3), the table also gives the half-spread paid, $100\, d\,(p - M_t)$.
- **Local projection** (5.6): for each $\Delta$, regress $100\,(M_{t+\Delta} - M_t)$ on $d \times$ size bucket and $d \times$ price bucket (the base is a pre-trade mid of 0.3–0.7), with and without controls for the signed taker flow and the mid change in the 1, 5 and 30 seconds before the trade.
- Script: `scripts/btc5m/impact_by_size.py`.

| Trade size (USDC) | Share of trades | Share of shares | Half-spread | $\Delta = 1$ s | 10 s | 60 s | Settle | Durability at 10 s |
|---|---|---|---|---|---|---|---|---|
| < 1 | 14.1% | 1.8% | 0.82 | 0.44 | 0.56 | 0.51 | 0.74 | 0.76 |
| 1–5 | 47.6% | 14.2% | 1.00 | 0.82 | 1.10 | 1.14 | 1.45 | 0.76 |
| 5–20 | 25.7% | 22.9% | 1.30 | 1.36 | 1.67 | 1.60 | 1.99 | 0.84 |
| 20–100 | 10.8% | 32.9% | 1.37 | 1.31 | 1.52 | 1.37 | 1.88 | 0.81 |
| 100–500 | 1.7% | 19.0% | 2.14 | 1.13 | 1.20 | 0.94 | 1.46 | 0.82 |
| 500–2k | 0.2% | 6.8% | 4.58 | 0.96 | 0.49 | 0.00 | 0.18 ± 0.42 | — |
| > 2k | 0.02% | 2.5% | 7.98 | 0.75 | −0.12 | −0.52 | 0.72 ± 0.76 | — |
| **All** | | | 1.11 | 0.96 | 1.22 | 1.19 | 1.53 ± 0.12 | 0.80 |

Cents of the Up price. CIs at 10 s are about ±0.1¢ for trades up to \$500.

| *Figure 22. Price impact by trade size, $\Delta$ = 1 s to settlement.* | *Figure 23. Impact at 10 s, 60 s and settlement, and the half-spread paid, against trade size.* |
|:--:|:--:|
| ![Impact by size](./assets/btc5m_markout/impact/imp_1_by_size.png) | ![Impact vs size](./assets/btc5m_markout/impact/imp_2_vs_size.png) |

| *Figure 24. Local projection: impact by size at a pre-trade mid of 0.3–0.7, raw trade vs. controls for the pre-trade flow and mid changes.* | *Figure 25. Impact by minute of the window.* |
|:--:|:--:|
| ![LP raw vs controls](./assets/btc5m_markout/impact/imp_4_lp_raw_vs_ctrl.png) | ![Impact by minute](./assets/btc5m_markout/impact/imp_7_by_minute.png) |

**Permanent and temporary.** For the typical trade the impact is mostly permanent and arrives late, not early. The average trade moves the mid by about 1.2¢ within 10 s, and nothing comes back: the impact at settlement is 1.5¢. So about 80% of the permanent impact is there after 10 s, and the temporary part is negative (an undershoot, the delayed adjustment of **[H 1991]**'s Ames example), not an overshoot that reverts.

**Size.** The impact of one trade rises with its size up to about \$20 and then falls.

- Per trade it is increasing and concave up to \$5–20 (0.56¢ → 1.67¢ at 10 s while the mean size grows from \$0.8 to \$10), as in **[H 1991]** §VI. Per dollar it falls throughout: a \$1 trade moves the price by about 0.7¢ per dollar traded, a \$200 trade by about 0.006¢.
- Above \$100 the impact *decreases*, and above \$500 it is **temporary**: about 1¢ in the first second, back to about 0 by 60 s, with no permanent part that we can detect. These trades pay a half-spread of 4.6–8¢ because they walk the book, so their gross markout at 10 s is −4 to −8¢ per share. They buy immediacy, not information. **[G 1994]** predicts that larger trades are more likely informed; on Polymarket the largest trades look like the opposite, liquidity demand that the providers absorb and then re-quote.
- The pattern survives the controls (Figure 24): within the same price bucket the coefficient on $d \times$ size goes 1.0 / 1.5 / 2.0 / 1.9 / 1.8 / 1.3 / 1.0¢ at 10 s across the seven buckets.

**Raw trade vs. surprise.** Controlling for the order flow and mid changes of the 30 seconds before the trade changes the impact by at most 0.05¢ (except for trades above \$2k). In clock time the trade a taker sends is barely predictable from the recent history of this market, so condition 1 of 5.6 does not bind here. Recent flow does matter on its own: 1,000 shares of signed flow in the previous second add about 0.7¢ to the move after the trade (the delayed adjustment again).

**Side, price level and time.**

| Group | Half-spread | 10 s | 60 s | Settle |
|---|---|---|---|---|
| Buy Up / buy Down (opening a position) | 1.13 / 1.14 | 1.26 / 1.29 | 1.14 / 1.30 | 1.55 / 1.68 |
| Sell Up / sell Down (closing) | 0.97 / 0.98 | 0.87 / 0.80 | 1.04 / 0.90 | 0.93 / 0.95 |
| Pre-trade mid 0.3–0.7 | 1.25 | 1.62 | 1.65 | 1.86 |
| Pre-trade mid below 0.1 / above 0.9 | 0.75 / 0.74 | 0.27 / 0.26 | 0.07 / 0.03 | 0.74 / 0.79 |
| First four minutes (each) | 0.97–1.02 | 1.06–1.16 | 1.10–1.19 | 1.25–1.39 |
| Last minute | 1.61 | 1.62 | 1.40 | 2.35 |

- Buys, which open a position, move the price about 50% more than sells; Up and Down are symmetric.
- Near 0.5 the impact is large and immediate. Near 0 or 1 almost all of it arrives only by settlement (0.27¢ at 10 s, 0.74¢ at settlement): the trades there are about the outcome, which the book reflects late.
- Trades in the last minute have the largest impact, both immediate and permanent. That is where a small BTC move matters most for the outcome (the sensitivity of the Up price to BTC grows as the time left shrinks), and where the fast takers of section 8 trade.
- In the volume-weighted average of 7.3 (per share, all trades) takers lose 0.6¢ gross at 10 s, while here the average trade gains $1.22 - 1.11 = +0.1$¢. The difference is the weighting: per share, the large trades that lose 4–8¢ count much more.

## 8. Who wins: the wallet JetFadil (To Be Edit)

The wallet `0xe0229e10a858860218b6132f4234602c47bd6603` (profile name JetFadil) is the wallet of 6.3 (five cycles). Its Polymarket profile shows a PnL of **+$281.5K** on $26.2M of volume in 34,072 markets. This section asks whether it really made that money, how, and who paid for it.

### 8.1 Data and accounting

- **Full history** from data-api, 2026-03-26 to 2026-10-27: `activity` (trades, redemptions, rebates), and `/trades` with `takerOnly=true` and `false` (which side of each fill the wallet was on). gamma gives the outcome of all 34,211 markets it traded.
- It traded from 2026-03-26 to **2026-08-20**, and nothing afterwards. 873,633 fills, 26.5M shares. 99.8% of its fills are **taker** fills (1,524 maker fills). It **only buys** (Up or Down) and holds to settlement. Markets: BTC 5-minute (94.5% of shares), BTC 15-minute (3.2%), ETH 5-minute (2.2%).
- **Actual USDC.** For a buy, the activity row's `usdcSize` is the USDC paid; redemptions are the USDC received. Gross PnL = received − price × size; fee = `usdcSize` − price × size.
- **Fee check.** From May to August the USDC it paid above price × size matches $0.07\,p(1-p)$ per share month by month (within 0.4%). This verifies the fee formula of 6.1 with real payments.

### 8.2 Did it make money?

| | USDC |
|---|---|
| Profile PnL (price × `/trades` size, held to settlement) | +281.5K |
| Gross PnL before fees, $\sum (V - p) \times$ ordered size | +289.1K |
| Taker fees paid: in shares (to late April) | −102.0K |
| Taker fees paid: in USDC (from late April) | −240.8K |
| Taker rebates received | +54.6K |
| **Actual net PnL** (cash received − cash paid + rebates) | **+0.9K** |

Gross − fees + rebates = net holds exactly, day by day: $289.1 - 102.0 - 240.8 + 54.6 = 0.9$K. The profile's number is the gross before fees, up to 7K (below).

**Reconciliation.** Earlier versions of this note had an actual gross of +187K and fees of −241K, so profile − fees + rebates (282 − 241 + 55 = 96K) did not match the net (+1K). The 95K gap is the taker fee that was **taken in shares** before late April 2026 (script `scripts/btc5m/wallet_reconcile.py`):

- From May on, the profile and the cash gross agree to the dollar every month, and the USDC fee paid above price × size equals the market's fee schedule $0.07\,p(1-p)$ per share (60,088 vs 59,905 USDC in May, within 0.3% in every month).
- Before that, the wallet paid price × the ordered size in USDC (activity `usdcSize`; no USDC fee), but received fewer shares: of the winning shares it bought in April (2.663M by activity size) it redeemed only 2.592M. The 70.7K winning shares that were never paid out are the fee. The fee schedule (`crypto_fees_v2`, $0.07\,p(1-p)$ USDC, i.e. $0.07\,(1-p)$ shares per share) predicts 70.2K fee shares on those winning tokens: a match within 0.8%.
- In March the fee in shares was lower (31.4K unredeemed winning shares, against 49.8K by the current schedule): most March cycles still had the older schedule `crypto_fees` (rate 0.25, exponent 2, in gamma), which charges less away from $p = 0.5$.
- `/trades` reports buy sizes net of the fee in shares, but in April it deducts it twice: the size gap between activity and `/trades` is exactly $2.02 \times 0.07\,(1-p)$ in every price bucket. The profile adds up $(V - p) \times$ the `/trades` size, so it misses the cost of the fee shares (price × the shares paid for but not shown) and is close to the gross *before* fees. The second deduction makes it 7K lower than the gross.
- Earlier, the activity-based "gross" was cash received − price × size, which before May is already net of the fee in shares. That is why it looked like the wallet earned nothing before fees started in USDC.
- A second, smaller issue: from late April to May, 273 REDEEM rows (75K USDC) have an empty `asset` field and only an `outcomeIndex`; they must be matched by outcome index.

By month (cents per share; net in actual USDC, by the market's window day):

| Month | Shares | Gross | Fee (of which in shares) | Rebates | Net |
|---|---|---|---|---|---|
| 2026-03 | 4.08M | 1.13 | 0.77 (0.77) | 0 | +14.7K |
| 2026-04 | 4.86M | 1.27 | 1.51 (1.46) | 0 | −12.0K |
| 2026-05 | 4.47M | 1.03 | 1.34 | 0 | −14.1K |
| 2026-06 | 3.35M | 0.91 | 1.39 | 0.19 | −9.7K |
| 2026-07 | 4.44M | 1.08 | 1.39 | 0.59 | +12.1K |
| 2026-08 | 5.33M | 1.07 | 1.30 | 0.42 | +9.9K |

| *Figure 26. Cumulative PnL: the profile's number, gross before fees, fees (in shares, then USDC), rebates and net.* | *Figure 27. PnL per share by month.* |
|:--:|:--:|
| ![JetFadil cumulative PnL](./assets/btc5m_markout/wallet/wallet_1_cumulative_pnl.png) | ![JetFadil PnL per share by month](./assets/btc5m_markout/wallet/wallet_10_by_month.png) |

So **before fees it earned about 1.1¢ per share, in every month (0.9–1.3¢); fees took all of it (1.3–1.5¢ from April), and rebates brought it back to about zero.**

### 8.3 Where the gross edge comes from: stale quotes

This is the sniping of section 2 [BCS 2015].

- **Millisecond event study** (Figure 28; Binance BTCUSDT aggTrades around the Polymarket trade time, 2026-07-31 to 08-06). About 0.8 to 0.3 s before its trade, BTC jumps **+0.5 bp in the direction of its bet**; for other takers the move is +0.1 bp. 5.9% of its trades come within one second of a move of 2 bp or more (other takers: 1.9%). Binance moves first, the Up quotes on Polymarket have not been updated, and the wallet hits them.
- **Its markout is realized within seconds** (Figure 29, 97 days with order books). About +1.1¢ at $\Delta = 10$ s and flat up to 300 s, so the edge is a permanent move of the price (5.4), not a temporary error. All takers together: −0.6¢. The edge is stable from month to month (Figure 30).
- **Speed, not a model.** A fair Up probability from spot moneyness and the time left does not predict its settlement markout (Figure 31).
- **When it trades** (Figure 32, May–August). Net of fees it is positive only in the last minute of the window: the fee $0.07\,p(1-p)$ is small when the price is near 0 or 1.
- **By the size of the move** (Figure 33, 2026-07-31 to 08-06). Group the trades by the Binance move in the second before the trade, in the direction of the bet. 19.6% of its volume comes after a move of 1 bp or more; for other takers the share is 5.6%. These trades earn +2.0¢ (1–2 bp) and +4.3¢ (≥ 2 bp) per share at settlement, more than its fee of about 1.36¢. They are 64% of its gross settlement markout. Within one second the Up mid moves +4.1¢ and +7.0¢ its way. After a move against it (≤ 0 bp, 10% of its volume) it loses 1.4¢, the same as other takers (−1.55¢).
- **It hits quotes while they are being repriced.** The quote it hits last changed a median of 49 ms earlier (other takers: 227 ms), and 23 ms earlier after a move of 2 bp or more. Other takers who trade after a large move also earn (+2.5 to +3.0¢). The difference is that the wallet trades there 3.5 times as often, in share of volume.

![JetFadil BTC spot around its trades, ms](./assets/btc5m_markout/wallet/wallet_11_spot_event_study_ms.png)

*Figure 28. Binance BTC price around the wallet's trades and other takers' trades, $10^4\, d \ln(S(t+k)/S(t))$, millisecond resolution.*

| *Figure 29. Taker markout of the wallet vs all takers, 2026-04-14 to 08-09.* | *Figure 30. The wallet's taker markout by month at $\Delta$ = 10, 60, 300 s.* |
|:--:|:--:|
| ![JetFadil taker markout](./assets/btc5m_markout/wallet/full_2_all_wallet_taker.png) | ![JetFadil markout by month](./assets/btc5m_markout/wallet/full_5_wallet_by_month.png) |

| *Figure 31. Settlement markout by model edge (fair value from spot minus price).* | *Figure 32. Settlement markout by time in the window, May–August.* |
|:--:|:--:|
| ![By model edge](./assets/btc5m_markout/wallet/wallet_6_by_model_edge.png) | ![By time in window](./assets/btc5m_markout/wallet/wallet_4_by_time_in_window.png) |

![By the Binance move before the trade](./assets/btc5m_markout/wallet/wallet_12_by_pre_trade_spot_move.png)

*Figure 33. Mid markout at 10 s and settlement markout by the Binance move in the second before the trade, the wallet vs other takers (1 in 5 sampled), 2026-07-31 to 08-06. Percentages: share of each group's volume.*

**Why it is faster: the left part and the right part.** Figure 28 has two sides. Left of the trade, Binance has already moved: that is **public information**, and the wallet carries it to quotes that have not caught up (the sniping of [BCS 2015]). Right of the trade, Binance keeps moving in the wallet's direction: that is information Binance did not have yet when the wallet traded, its **own information** in the Glosten–Milgrom sense. Figure 34 draws both markets in the same units. With $F$ the Binance fair value of Up (9.4) and $M$ the Up mid, it plots $d\,(F_{t+k} - F_t)$ and $d\,(M_{t+k} - M_t)$ around the trade:

- About half a second before the wallet trades, $F$ jumps by about 4¢ of the Up price in its direction; for other takers by under 1¢. The Up mid is already being repriced, jumps at the trade, and is about 2¢ higher within a second. $F$ keeps rising by another 2¢ over the next 5 seconds.
- To split the price impact $d\,(M_{t+\Delta} - M_t)$ into the two sides, regress it, over all taker trades, on the Binance move before the trade, $\text{pre} = d\,(F_t - F_{t-1\,\text{s}})$, and after it, $\text{post} = d\,(F_{t+\Delta} - F_t)$: $\text{impact} = c + \beta_L\, \text{pre} + \beta_R\, \text{post} + e$. The $\beta$'s are Polymarket's pass-through of Binance moves, the same for every taker. Part of the move after the trade is predictable from the move before it (Binance momentum, also public), so also regress $\text{post} = \gamma\, \text{pre} + u$. A group's mean impact then splits exactly into:

| Part | Formula | Meaning |
|---|---|---|
| Public, left | $\beta_L\,\overline{\text{pre}}$ | Binance had already moved |
| Public, continuation | $\beta_R\,\gamma\,\overline{\text{pre}}$ | the Binance move that the move before predicts |
| Own, right | $\beta_R\,(\overline{\text{post}} - \gamma\,\overline{\text{pre}})$ | Binance moves after the trade that the move before does not predict |
| Polymarket only | the rest | not explained by Binance |

Per share, 2026-07-31 to 08-06 (34,866 wallet trades, 3.46M other trades; 95% CI by cycle bootstrap about ±0.1–0.2¢; script `scripts/btc5m/trade_lr_split.py`):

| | Impact | Public, left | Public, continuation | Own, right | Polymarket only |
|---|---|---|---|---|---|
| JetFadil, $\Delta$ = 1 s | 1.97 | 0.57 | 0.07 | 0.21 | 1.12 |
| JetFadil, $\Delta$ = 10 s | 1.71 | 0.31 | 0.31 | 1.25 | −0.17 |
| JetFadil, $\Delta$ = 60 s | 1.81 | 0.28 | 0.39 | 2.03 | −0.90 |
| Other takers, $\Delta$ = 10 s | 0.74 | 0.06 | 0.06 | 0.16 | 0.47 |

| *Figure 34. Binance fair value and Up mid around a taker trade, the wallet vs other takers (per share).* | *Figure 35. The price impact split into public (left) and own (right) parts.* |
|:--:|:--:|
| ![Paths around the trade](./assets/btc5m_markout/formation/lr_1_paths_vw.png) | ![Impact split](./assets/btc5m_markout/formation/lr_2_split_vw.png) |

- **At 1 second** the wallet's impact is mostly the public part and "Polymarket only": it hits quotes that are being repriced at that moment (8.3, 49 ms), by market makers who see the same move or faster venues.
- **At 10 seconds and beyond** the largest part is the right side: Binance keeps moving its way by more than the move before the trade predicts. That part is 8 times larger than for other takers (1.25 vs 0.16¢), and the public left part 5 times (0.31 vs 0.06¢).
- "Own" means: not in Binance spot yet. It can come from faster sources than Binance spot (BTC perpetual futures, other exchanges, the Binance order book) rather than from a private model; the data cannot tell these apart. The Polymarket-only part turns negative at long horizons because the Up mid passes on only part of the later Binance move.
- Section 9.5 does the same split for the price as a whole (price discovery), not for one trade.

### 8.4 Fees, rebates, and when it made money

- **Taker fee**: $0.07\,p(1-p)$ dollars per share, paid by the taker only.
- **Maker rebate**: 20% of the taker fees of a market, paid daily to its makers in proportion to their filled liquidity.
- **Taker rebate program** (from 2026-05-28): a taker gets back a share of the fees it paid, set by a tier based on its weighted volume over the last 30 days. Weighted volume = trade size × (1 − price) × 2.3 for crypto. Tiers: Gold 18%, Platinum 32%, Diamond 44%, Obsidian 50%.
- **JetFadil.** Its first rebate is for 2026-06-19, at 17.5% of that day's fees (Gold). From **2026-07-03 it is 32% (Platinum)** until its last trade on 08-20. There were also two one-off payments ($4.5K on 06-22, $6.6K on 07-07). Total rebates: $54.6K.
- **Timing of the tiers.** If the 30-day rule had applied to its whole history, it would have been Platinum from the launch on 05-28 ($1.86M of weighted volume). The observed dates fit weighted volume counted only from about 06-10. Counted from then, its weighted volume passes $1M at the start of 07-03 ($1.01M), the day Platinum starts. By 06-19 it had $0.55M, which is Gold. One wallet cannot tell whether 06-19 is when payments began or when it joined. Its 30-day weighted volume never reached Diamond's $4M (maximum $3.3M).

Segmented regressions of the daily series (share-weighted, Newey–West SE; Figures 36–38), with the fee in shares counted as a fee (8.2). The shift is the change in the mean at the break:

| Break | Gross ¢/share | Fee ¢/share | Net ¢/share |
|---|---|---|---|
| 2026-04-28, fees start to be paid in USDC | 1.21 → shift −0.18 (t = −1.6) | 1.17 → +0.18 (t = 1.0) | −0.06 (t = −0.3) |
| 2026-07-03, rebate tier 32% | −0.03 (t = −0.3) | +0.08 (t = 0.7) | +0.35 (t = 2.0) |
| 2026-08-07, TWAP settlement | −0.11 (t = −1.1) | −0.02 (t = −0.2) | +0.15 (t = 1.1) |

- **Unknown-break test.** For gross per share there is no break (largest F 2.6; 5% critical value about 8.85). The fee per share has one large break on **2026-04-05** (F = 85: 0.98 → 1.38¢), and so does the volume (F = 92: 567K → 163K shares a day). For net per share no break is significant (largest F 4.1, on 06-21, when the rebates begin).
- **Reading.** The gross edge was about 1.1–1.2¢ per share all along; it did not change when the fee moved from shares to USDC on 04-28 (an earlier version of this table showed a jump of +0.97¢ there, which was the fee in shares being counted as a loss of gross edge). What changed is the cost: when the fee reached its full level in early April, the wallet cut its volume by about 70% and kept a net of about zero. That is the free-entry zero profit of [BCS 2015], with fees as the cost of entry.
- **July–August.** About 1.07¢ gross − 1.35¢ × (1 − 0.32) ≈ +0.15¢ per share, plus the one-off payments. **The rebate tier is what made these months positive.**

![Segmented regression, per share](./assets/btc5m_markout/wallet/seg_1_per_share.png)

*Figure 36. Daily gross, fee and net per share, with the share-weighted mean between breaks.*

| *Figure 37. Daily net PnL and volume.* | *Figure 38. F statistic of a level break at each day.* |
|:--:|:--:|
| ![Daily net and volume](./assets/btc5m_markout/wallet/seg_2_daily_net_and_volume.png) | ![sup-F](./assets/btc5m_markout/wallet/seg_3_supF.png) |

### 8.5 Settlement pushes and the switch to TWAP

This uses the PushIntensity of the settlement-manipulation paper: $|$Binance signed flow in the last 10 s$|$ / median over the first 25 bins. Cycles above the pre-TWAP 90th percentile (26.0) count as pushed. Sample: 2026-07-31 to 08-20.

- **Before TWAP**: there is a spike of flow in the last 10 seconds (Figure 39). In pushed cycles the side of the push wins 72% of the time, against 56% in other cycles (Figure 40).
- **After TWAP** (2026-08-07): the spike is gone, and the push side wins 50% of the time.
- **JetFadil is not the manipulator.** Before TWAP it loses in pushed cycles: −2.5¢ per share gross, −3.9¢ net, about −$5.6K in one week. In other cycles it earns +1.4¢ gross (Figure 41). After TWAP, pushed and other cycles look the same for it. The switch removed a loss it was paying to manipulators.

| *Figure 39. Binance flow by 10 s bin, before vs after TWAP.* | *Figure 40. How often the side of the final-10 s flow wins.* |
|:--:|:--:|
| ![Flow profile](./assets/btc5m_markout/wallet/push_1_flow_profile.png) | ![Push decides](./assets/btc5m_markout/wallet/push_3_push_decides.png) |

![Wallet in pushed vs other cycles](./assets/btc5m_markout/wallet/push_2_wallet_pushed_vs_other.png)

*Figure 41. The wallet's settlement markout in pushed and other cycles, before and after TWAP.*

### 8.6 Who pays

Every share it buys is sold by a maker, so before fees its gain is exactly the makers' loss on those fills. On 2026-08-06 (282 cycles with complete fills) its +$9,255 is matched by −$9,255 for its 1,502 counterparties. 76% of those shares came from market-maker-like wallets (at least 85% maker fills, active in at least 50 cycles).

| Whole history | JetFadil | Makers on the other side | Polymarket |
|---|---|---|---|
| Gross trading PnL (ordered shares) | +289K | −289K | 0 |
| Taker fees: in shares (to late April) | −102K | | +102K |
| Taker fees: in USDC | −241K | | +241K |
| Maker rebates (20% of the USDC fees) | | +48K | −48K |
| Taker rebates | +55K | | −55K |
| **Net** | **+1K** | **≈ −241K** | **≈ +240K** |

The makers sold the full ordered size, so their gross loss is the wallet's gross gain before fees. Whether the fees taken in shares were also rebated to makers (20% would be another 20K) is not checked.

The makers earn their loss back from other takers. In 2026-07-31 to 08-06 (all taker wallets, settlement markout per share):

| Taker wallets ranked by taker volume | Share of volume | Gross ¢/share | Net of fee ¢/share |
|---|---|---|---|
| Smallest 10% (median 1 fill per week) | 0.0% | −8.5 | −9.7 |
| 5th decile | 0.4% | −3.2 | −4.3 |
| 9th decile | 7.6% | −0.0 | −1.0 |
| Largest 10% | 86.5% | +0.3 | −0.8 |
| JetFadil (rank 3 by volume) | 1.6% | +1.1 | −0.2 |

Most of the 15 largest takers have a positive gross markout (+0.3 to +1.45¢) and a net near zero. So there are several fast takers like JetFadil. The chain is: fast takers pick off stale maker quotes; makers recover it through the spread paid by small takers; the venue keeps most of the fees. These are the roles of section 3: the snipers' profit is paid by investors through the spread [BCS 2015].

### 8.7 Caveats

- data-api records only, not on-chain fills. The fees from May on are checked against real payments.
- Before late April the fee was taken in shares. The shares the wallet actually received are known exactly only for winning tokens (from the redemptions); totals use these market-level cash flows, and per-fill splits (Figure 32) use May–August only.
- The event studies, push test and wallet ranking use one or three weeks around the switch; the mid-based curves use 97 days. pmxt has no BTC 5-minute books from about 06-13 to 07-13, nor for 08-10 to 08-17.

## 9. Price discovery in BTC 5-minute markets (To Be Edit)

### 9.1 Setup

- **Event-time VAR**, as in 5.3. An event is a trade or a change of the Up mid within the live window. $d_t$ is the trade direction, $R_{t+1}$ the Up mid change in cents, $K = 10$ lags, and trades are moved back 180 ms so that they come before the quote update they cause (6.1). From (2') and (4') we compute $\alpha_\Delta$ (6) and the information share of trades $IS_{\text{trade}}$ (5.6).
- **Clock-time VAR** in 1-second bins with the outside price, as suggested in 5.5: $y_s = (\text{BTC return (bp)}, \text{signed taker shares}, R_s)$, 5 lags. Structural shocks come from a Cholesky decomposition in all six orderings, which gives bounds on the information shares.
- **Estimates**: the pooled VAR (summed cross products), the mean of per-cycle VARs, and single cycles. Samples: 2026-04-14 to 08-09 (26,248 cycles with order books), the week 07-31 to 08-06, and 08-06 alone.

### 9.2 Results

| Sample | $\alpha_\infty$ pooled | $\alpha_\infty$ mean of cycles | Info share of trades (pooled / median) | BTC | Order flow | Quotes |
|---|---|---|---|---|---|---|
| One cycle (`btc-updown-5m-1786057200`) | 0.48¢ | | 0.06 | 0.04–0.21 | 0.03–0.05 | 0.75–0.92 |
| 2026-08-06, 288 cycles | 0.45¢ | 0.38¢ | 0.15 / 0.12 | 0.03–0.28 | 0.00–0.09 | 0.67–0.97 |
| 07-31 to 08-06, 2,013 cycles | 0.33¢ | 0.25¢ | 0.08 / 0.05 | 0.02–0.23 | 0.00–0.07 | 0.72–0.97 |
| 04-14 to 08-09, 26,248 cycles | 0.33¢ | 0.31¢ | 0.11 / 0.14 | 0.08–0.22 | 0.01–0.06 | 0.73–0.90 |

The last three columns are clock-time information shares, min–max over the six orderings. With the ordering BTC → flow → quotes, the full sample gives 0.22 / 0.05 / 0.73.

| *Figure 42. Impact of a trade surprise, 04-14 to 08-09: pooled, mean of cycles, one cycle.* | *Figure 43. Information share of trades, per cycle.* |
|:--:|:--:|
| ![Trade impact](./assets/btc5m_markout/price_discovery/full_pd_1_trade_impact.png) | ![Info share histogram](./assets/btc5m_markout/price_discovery/full_pd_2_info_share_hist.png) |

| *Figure 44. Clock time: Up mid response to one-sd shocks in BTC, order flow and quotes.* | *Figure 45. Clock-time information shares.* |
|:--:|:--:|
| ![Clock response](./assets/btc5m_markout/price_discovery/full_pd_3_clock_response.png) | ![Clock info shares](./assets/btc5m_markout/price_discovery/full_pd_4_clock_info_shares.png) |

| *Figure 46. Permanent impact $\alpha_\infty$, daily mean of cycles.* | *Figure 47. Information share of trades, daily mean.* |
|:--:|:--:|
| ![alpha by day](./assets/btc5m_markout/price_discovery/full_pd_5a_alpha_by_day.png) | ![share by day](./assets/btc5m_markout/price_discovery/full_pd_5b_share_by_day.png) |

### 9.3 Reading

- A trade surprise moves the Up mid by about **0.3¢ for good**, over 20–40 events. The immediate change is close to 0, because in this event definition the quote reacts at the following events. The full impact is about twice the impact after 10 events, the delayed adjustment of [H 1991] Figure 1.
- **Trades carry only about 10–15% of the information** in the Up price. Most of it enters through the quotes themselves, and in clock time 8–22% of the variation is traced to BTC spot.
- This fits 8.3. Polymarket quotes follow Binance with a delay, and fast takers hit the stale quotes. As 5.5 warns, part of what the event-time VAR counts as trade information is public news (the Binance move) that reaches the price through those trades.
- The daily series (Figures 46–47) has a gap from mid-June to mid-July (no pmxt data). The information share of trades falls to about 0.05 in the first days of August, before the switch to TWAP.

**How to read Figures 42–47** (with the definitions of 5.6):

- Figure 42 is $\alpha_\Delta$ of (6): the cumulative change of the Up mid after one unit of trade surprise, in events. Where it flattens is the permanent impact $\alpha_\infty$. "Pooled" fits one VAR to all cycles; "mean of cycles" averages one VAR per cycle.
- Figure 43 is the histogram over cycles of $IS_{\text{trade}}$, the share of the efficient-price variance that comes from trade surprises. Most of the mass is near 0: in most cycles trades add little information beyond the quotes.
- Figures 44–45 are the clock-time VAR in 1-second bins. A 1-second bin contains the Binance move, the trades and the quote update together, so which comes "first" is an assumption (the Cholesky ordering), and the six orderings give wide bounds (BTC 0.08–0.22, quotes 0.73–0.90). Section 9.4 removes most of this ambiguity with 100 ms bins.

### 9.4 Four channels into the Up price

The question of the 10-27 meeting: when the Up price goes from 0.5 to 1, which part came from traders bringing Binance news, which part from traders' own information, which part from market makers repricing after Binance without any trade, and which part from nothing we can see?

**Setup.**

- **Binance fair value.** $F_t = 100\,\Phi\bigl(\ln(S_t/K)/(\sigma\sqrt{\tau_t})\bigr)$ cents, the Up price if BTC were a driftless random walk and Binance were the only source of news. $S_t$ is the last Binance BTCUSDT trade (aggTrades, millisecond timestamps), $K$ the last Binance price at the open (a proxy for the Chainlink open price), $\sigma$ the standard deviation of 1-second log returns in the 30 minutes before the open, and $\tau_t$ the seconds left (floor 0.5 s).
- **Series**, in 100 ms bins inside the window: $\Delta F_b$, the signed taker flow $x_b$ (thousands of Up-equivalent shares, trades moved back 180 ms as in 6.1), and the Up mid change $\Delta M_b$ (cents).
- **Model.** A recursive VECM: each variable is regressed on a constant, the same-bin values of the variables before it in the order $F \to x \to M$, 10 lags (1 s) of all three, and the gap $z_{b-1} = M_{b-1} - F_{b-1}$ (the error-correction term: $M$ and $F$ both end at the outcome). The residuals are three uncorrelated **structural shocks**: Binance news $e^F$, flow not explained by Binance or the past $e^x$, and quote moves not explained by Binance, flow or the past $e^M$.
- **Exact decomposition.** Run the fitted model forward with only one kind of shock switched on (the historical decomposition of a VAR). By linearity, every cycle's path splits exactly (to $10^{-12}$¢) into five parts:

| Part | What it is | Meeting label |
|---|---|---|
| Binance via quotes | $e^F$ with the flow response shut off: market makers reprice after Binance without a trade | (c) |
| Binance via trades | $e^F$ through the flow it triggers: takers carry Binance news to stale quotes | (b) |
| Flow shocks | $e^x$: trades that Binance and the past do not explain | (a) private information, plus noise |
| Quote shocks | $e^M$: quote moves that Binance, trades and the past do not explain | (d), including market makers trading on other markets |
| Opening gap | constants and the gap at the open | |

- **Shares.** For intervals of length $L$, $\text{share}_j = \sum \text{part}_j \cdot \text{total} / \sum \text{total}^2$ over all intervals and cycles. The shares sum to 1. A part that moves against the total has a negative share.
- **Sample.** The pre-TWAP week 2026-07-31 to 08-06 (2,015 cycles; Binance aggTrades are on Sherlock from 07-30). Robustness: 1-second bins with 1 s Binance klines over 2026-04-14 to 08-06 (25,564 cycles). Script: `scripts/btc5m/price_formation.py`.

**Results.** Shares of the Up mid's moves:

| Interval $L$ | Binance via quotes (c) | Binance via trades (b) | Flow shocks (a) | Quote shocks (d) | Opening gap |
|---|---|---|---|---|---|
| 1 s | 0.28 | 0.01 | 0.01 | 0.71 | 0.00 |
| 10 s | 0.39 | 0.01 | 0.01 | 0.59 | 0.00 |
| 60 s | 0.52 | 0.02 | 0.02 | 0.44 | 0.00 |
| Whole window | 0.59 | 0.02 | 0.04 | 0.36 | 0.00 |
| *1 s bins, 04-14 to 08-06: 10 s / 60 s / whole window* | *0.42 / 0.58 / 0.67* | *0.01 / 0.01 / 0.01* | *0.03 / 0.02 / 0.00* | *0.55 / 0.39 / 0.32* | |

- The order $x \to F \to M$ gives the same shares to the second decimal: within 100 ms, trades and Binance do not move together, so the ordering no longer matters (unlike the 1-second VAR of 9.1). Estimating without the last 10 s of each window changes the whole-window shares by at most 0.05.

Impulse responses to one-standard-deviation shocks (cents; week sample):

| Shock | Up mid after 0.5 s / 1 s / 10 s / 60 s | Binance fair value after 1 s / 10 s / 60 s |
|---|---|---|
| Binance news (+0.67¢ in $F$) | 0.35 / 0.48 / 0.52 / 0.53 | 0.83 / 0.81 / 0.66 |
| … with the trade channel shut off | 0.35 / 0.47 / 0.51 / 0.51 | 0.83 / 0.81 / 0.65 |
| Flow (86 shares) | 0.07 / 0.09 / 0.09 / 0.09 | 0.01 / 0.02 / 0.06 |
| Quote (+0.68¢ in $M$) | 0.70 / 0.71 / 0.72 / 0.70 | 0.06 / 0.15 / 0.44 |

| *Figure 48. Shares of the Up mid's moves by channel, by interval length.* | *Figure 49. Impulse responses of the Up mid, and of $F$, to one-sd shocks.* |
|:--:|:--:|
| ![Shares](./assets/btc5m_markout/formation/form_1_shares_M_week.png) | ![IRF](./assets/btc5m_markout/formation/form_3_irf_week.png) |

| *Figure 50. One cycle (`btc-updown-5m-1785629400`, Up won): the Up mid split by channel.* | *Figure 51. Shares of the Binance fair value's moves: the part Polymarket anticipated.* |
|:--:|:--:|
| ![Example](./assets/btc5m_markout/formation/form_2_example_1785629400_week.png) | ![F shares](./assets/btc5m_markout/formation/form_4_shares_F_week.png) |

**Reading.**

- **Binance news enters the Up price through the quotes, not through trades.** After a Binance move the Up mid follows within half a second, and shutting off the trade channel changes almost nothing (0.51¢ instead of 0.53¢ after 60 s). Takers carrying Binance news to stale quotes, the sniping of 8.3, account for only 1–2% of the price's movement. Sniping is where money changes hands, not where the price is formed.
- **Traders' own information is small:** flow shocks explain 1–4%. The event-time information share of trades in 9.2 (0.08–0.15) is an upper bound, as 5.5 warns: that VAR has no Binance, so it credits the trades with Binance news.
- **The quotes themselves lead Binance.** A quote shock is permanent (0.70¢ after 60 s), and the Binance fair value follows it: 0.15¢ after 10 s, 0.44¢ after 60 s. Polymarket quote shocks explain 13% of $F$'s moves over 60 s and 20% over a whole window (Figure 51). So the market makers have information that Binance spot does not have yet: faster venues such as BTC perpetual futures, and the Chainlink reference that decides the outcome. Two signs of the latter: $F$ ends on the wrong side of the outcome in 4.6% of cycles, the Up mid in only 0.9%. This is the fourth channel of the meeting, market makers moving on other markets; with Binance spot as the only outside price it shows up inside (d).
- **Binance moves are passed through only partly.** After a Binance shock the Up mid moves about 0.6 of the change in $F$, and $F$ itself gives back about a fifth of its move within a minute. The short-run Binance moves are partly noise, and the market makers do not follow them fully.
- **Caveats.** $F$ is a proxy: Binance, not Chainlink; $K$ is the Binance open; $\sigma$ comes from the half hour before. Near the close $F$ is very sensitive to $S$, so in single cycles the Binance and quote parts can be large and offsetting (Figure 50); the shares over 1–60 s are the robust numbers. One week of millisecond data; the full sample uses 1-second bins.

### 9.5 Price discovery with the wallet separated: own information and public information by origin

Section 8.3 split the price impact of the wallet's trades. Here the object is **price discovery** (5.6): of all the moves of the Up price, how much is the wallet's own information, how much is public information, and does that public information come from Binance or from Polymarket?

- **Model.** As in 9.4, with the taker flow split by who trades: $x^w$ the wallet's trades (matched by transaction hash), $x^o$ all other takers. Four series $(\Delta F, x^w, x^o, \Delta M)$, order $F \to x^w \to x^o \to M$, 10 lags of 100 ms, gap term. Four structural shocks:
  - $e^F$: **public information from Binance**;
  - $e^{x^w}$: the wallet's trades that Binance and the past do not explain, its **own information**;
  - $e^{x^o}$: the same for all other takers;
  - $e^M$: quote moves that Binance, all trades and the past do not explain, **public information that originates in Polymarket** (market makers' own sources).
- **Exact decomposition** of every cycle's path (error below $10^{-12}$¢). Binance news is further split by the channel it takes into the Up price: quotes alone (both flows shut off), the wallet's trades (only the other takers' flow shut off, minus quotes alone), and other takers' trades (the rest).
- Sample: 2026-07-31 to 08-06, 2,015 cycles, 34,866 wallet trades (100 ms bins, Binance aggTrades). Rows in italics: 2026-04-14 to 08-06, 25,564 cycles, 423,666 wallet trades, 1-second bins with 1 s Binance klines and 5 lags. Script: `scripts/btc5m/price_discovery_wallet.py`.

Shares of the **Up mid's** moves:

| Interval | Binance → quotes | Binance → wallet's trades | Binance → other trades | **Public from Binance** | Wallet's own | Others' own | **Public from Polymarket** |
|---|---|---|---|---|---|---|---|
| 1 s | 0.261 | 0.015 | 0.005 | **0.281** | 0.009 | 0.007 | **0.703** |
| 10 s | 0.365 | 0.022 | 0.010 | **0.397** | 0.007 | 0.013 | **0.583** |
| 60 s | 0.496 | 0.026 | 0.015 | **0.537** | 0.005 | 0.020 | **0.438** |
| Whole window | 0.567 | 0.023 | 0.018 | **0.608** | −0.006 | 0.033 | **0.363** |
| *1 s bins, 04-14 to 08-06: 10 s* | *0.381* | *0.040* | *0.008* | ***0.429*** | *0.027* | *0.023* | ***0.521*** |
| *1 s bins: 60 s* | *0.533* | *0.049* | *0.010* | ***0.592*** | *0.018* | *0.017* | ***0.373*** |
| *1 s bins: whole window* | *0.624* | *0.046* | *0.012* | ***0.682*** | *−0.005* | *−0.000* | ***0.323*** |

Shares of the **Binance fair value's** moves (who was ahead of Binance):

| Interval | Binance itself | Through trades' feedback | Wallet's own | Others' own | Polymarket quotes |
|---|---|---|---|---|---|
| 10 s | 0.942 | 0.011 | 0.002 | 0.000 | 0.044 |
| 60 s | 0.848 | 0.017 | 0.004 | 0.001 | 0.127 |
| Whole window | 0.754 | 0.029 | 0.002 | 0.006 | 0.193 |
| *1 s bins: 60 s* | *0.855* | *0.028* | *0.010* | *0.002* | *0.104* |
| *1 s bins: whole window* | *0.812* | *0.042* | *0.001* | *−0.003* | *0.140* |

Each row sums to 1 together with the opening gap (at most 0.015).

Responses to one shock, per 1,000 shares of flow (cents; 60 s after the shock):

| Shock | Up mid | Binance fair value | Binance / Up mid |
|---|---|---|---|
| Wallet's own flow | 18.4 | 13.0 | 0.70 |
| Other takers' flow | 1.0 | 0.6 | 0.62 |
| *1 s bins: wallet's own flow* | *58.8* | *43.2* | *0.74* |
| *1 s bins: other takers' flow* | *0.79* | *0.41* | *0.52* |

**Reading.**

- **Public information from Binance** is the largest source over a minute or more (54–61%), and almost all of it enters through quotes. The wallet carries a little of it (1.5–2.6% of the Up price's moves in the week, 4–5% over the four months), more than all other takers together (0.5–1.8%, and about 1%) with 1% of the trades.
- **Public information that originates in Polymarket** is the other large source (36–70%, larger at short intervals). Part of it is ahead of Binance: Polymarket quote shocks explain 13% of the Binance fair value's moves over 60 s and 19% over a window. The market makers watch sources faster than Binance spot.
- **The wallet's own information is small for the price as a whole** (under 1% of the Up price's moves): it trades rarely. **Per share it is the most informative flow in the market:** 1,000 shares of its unexplained flow move the Up mid by 18¢, 18 times more than other takers' flow, and 70% of that move shows up in Binance within a minute (with 1-second bins over four months: about 75 times, and 74%). Over the four months its own information is 1.8–3.7% of the Up price's moves at 1–60 s, about as much as all other takers together, and nothing over a whole window: its information is about the next seconds, not the outcome. This is the right side of Figure 34, seen in the whole price process.
- So the three layers of the meeting: (1) the wallet's own information, large per trade but small in total; (2) public information from Binance, mostly priced by the market makers' quotes, partly carried by takers, the wallet most of all; (3) public information from Polymarket's own quotes, a large part of short-run price moves and partly ahead of Binance.

## References

- **[GM 1985]** Glosten, L. R. and Milgrom, P. R. (1985). Bid, ask and transaction prices in a specialist market with heterogeneously informed traders. *Journal of Financial Economics* 14(1), 71–100. [ScienceDirect](https://www.sciencedirect.com/science/article/pii/0304405X85900443)
- **[G 1994]** Glosten, L. R. (1994). Is the electronic open limit order book inevitable? *The Journal of Finance* 49(4), 1127–1161. [Wiley](https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1994.tb02450.x)
- **[BCS 2015]** Budish, E., Cramton, P. and Shim, J. (2015). The high-frequency trading arms race: Frequent batch auctions as a market design response. *The Quarterly Journal of Economics* 130(4), 1547–1621. [Oxford Academic](https://academic.oup.com/qje/article/130/4/1547/1916146)
- **[H 1991]** Hasbrouck, J. (1991). Measuring the information content of stock trades. *The Journal of Finance* 46(1), 179–207. [Wiley](https://onlinelibrary.wiley.com/doi/10.1111/j.1540-6261.1991.tb03749.x)
- Hasbrouck, J. (1991b). The summary informativeness of stock trades: an econometric analysis. *The Review of Financial Studies* 4(3), 571–595.
- Hasbrouck, J. (1995). One security, many markets: determining the contributions to price discovery. *The Journal of Finance* 50(4), 1175–1199.
- Jordà, Ò. (2005). Estimation and inference of impulse responses by local projections. *American Economic Review* 95(1), 161–182.
- Plagborg-Møller, M. and Wolf, C. K. (2021). Local projections and VARs estimate the same impulse responses. *Econometrica* 89(2), 955–980.
- Kyle, A. S. (1985). Continuous auctions and insider trading. *Econometrica* 53(6), 1315–1335. [JSTOR](https://www.jstor.org/stable/1913210)
