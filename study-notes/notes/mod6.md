---
layout: default
title: "Module 6: Liability Valuations: Claims Reserving"
---

## **Liability Valuations: Claims Reserving**

### **Overview of the Material**

When an insurer sells a policy, it collects premiums upfront but may have to pay claims well into the future. These future claim payments are uncertain both in timing and amount. Actuaries must estimate these future claims—known as **outstanding loss liabilities**—to ensure the insurer remains financially sound. Over time, various methods have been developed, from simple deterministic algorithms to sophisticated stochastic models, all aimed at providing a clearer picture of future claim development and the insurer’s needed reserves.

---

### **1. Introduction and Background**

**Key Points:**
- **Claims often develop over multiple years:** A claim that occurs in a given accident year may not be reported immediately and can be paid out through several partial payments over subsequent years.
- **Ultimate claim amounts are not known immediately:** Reserves are set because the full settlement cost of claims from past policies is uncertain at the current time.

**Types of Claims:**
- **IBNR (Incurred But Not Reported):** Claims that have happened but have not yet been reported to the insurer.
- **RBNS (Reported But Not Settled):** Claims that have been reported but have not yet been fully paid.

**Short-Tailed vs. Long-Tailed Business:**
- **Short-tailed lines (e.g., property):** Claims settle quickly, making reserving more straightforward.
- **Long-tailed lines (e.g., liability):** Claims may take years to settle and reserve estimates are more uncertain.

**Why Stochastic Reserving?**
- Traditional approaches (like the Chain Ladder) focus on expected values and do not quantify uncertainty.
- Regulators may require reserves at a certain percentile (e.g., 75th), necessitating stochastic models that provide probability distributions, not just point estimates.

---

### **2. Understanding the Run-Off Triangle**

To organize past claim data, we use a **run-off triangle**, which arranges claim amounts by:
- **Accident Year (AY):** The year in which the claim-generating event occurred.
- **Development Year (DY):** How many years after the accident year the payments are made.

**Incremental Run-Off Triangle:**
This shows the actual amounts paid each development year. A typical incremental run-off triangle for, say, 6 accident years might look like this:

| Accident Year (AY) | Dev Year=1 | Dev Year=2 | Dev Year=3 | Dev Year=4 | Dev Year=5 | Dev Year=6 |
|--------------------|------------|------------|------------|------------|------------|------------|
| AY1 (oldest)        | X<sub>1,1</sub> | X<sub>1,2</sub> | X<sub>1,3</sub> | X<sub>1,4</sub> | X<sub>1,5</sub> | X<sub>1,6</sub> |
| AY2                 | X<sub>2,1</sub> | X<sub>2,2</sub> | X<sub>2,3</sub> | X<sub>2,4</sub> | X<sub>2,5</sub> |        |
| AY3                 | X<sub>3,1</sub> | X<sub>3,2</sub> | X<sub>3,3</sub> | X<sub>3,4</sub> |         |        |
| AY4                 | X<sub>4,1</sub> | X<sub>4,2</sub> | X<sub>4,3</sub> |            |         |        |
| AY5                 | X<sub>5,1</sub> | X<sub>5,2</sub> |             |            |         |        |
| AY6 (newest)        | X<sub>6,1</sub> |                |             |            |         |        |

**Interpreting the Triangle:**
- The top-left corner (AY1, DY=1) represents claims paid in the first development year for the oldest accident year.
- As we move to the right (increasing development year), we see how claims for that accident year accumulate over time.
- Lower rows represent more recent accident years, which have fewer development periods of data (hence the "triangle" shape).

**Cumulative Claims:**
Often, it’s easier to work with cumulative amounts rather than annual increments. The cumulative triangle sums the incremental payments row-wise:

$$
C_{i,j} = \sum_{k=1}^j X_{i,k}
$$

Where $$C_{i,j}$$ is the total claims paid for accident year $$i$$ up to development year $$j$$.

If we have incremental data as above, the cumulative form for AY1 would be:
- $$C_{1,1} = X_{1,1}$$
- $$C_{1,2} = X_{1,1} + X_{1,2}$$
- $$C_{1,3} = X_{1,1} + X_{1,2} + X_{1,3}$$, and so forth.

---

### **3. Deterministic Claims Reserving Methods**

#### **Chain Ladder Method**

**Core Idea:**
- Claims tend to develop in a consistent pattern from one development year to the next.
- Use historical proportions of how claims "grow" from one development stage to the next to estimate future values.

**Process:**
1. From the cumulative data, calculate age-to-age development factors.
2. Apply these factors to the latest observed data to project future cumulative values.
3. The difference between the projected ultimate amount and what’s already paid gives the reserve.

**Limitations:**
- Assumes historical patterns continue unchanged into the future.
- No direct measure of uncertainty.

#### **Bornhuetter-Ferguson Method**

**Concept:**
- Combine historical patterns (like in Chain Ladder) with a prior expectation of the ultimate loss (e.g., from pricing assumptions or expert judgment).
- Instead of letting past data fully dictate the ultimate amount, you "start" with a prior guess and then only distribute the *unpaid portion* according to observed patterns.

**Benefits:**
- Less sensitive to early-year volatility.
- Integrates actuarial judgment or external estimates.

---

### **4. Moving Towards Stochastic Reserving**

While Chain Ladder and BF provide point estimates, they don’t give a sense of the variability around those estimates. This is where stochastic models come in.

**Why Stochastic Models?**
- Regulators may require reserves at a certain percentile, not just the mean.
- Stochastic models allow actuaries to quantify the uncertainty in reserve estimates.

**Poisson-Based Models:**
- **Poisson Cross-Classified Model:** Model incremental claims $$X_{ij}$$ as Poisson with parameters depending on accident year and development year.
- **Poisson Mack Model:** Uses a Poisson assumption for cumulative claims development steps, closely mirroring the Chain Ladder factors.

Both yield the same central estimates as Chain Ladder but also provide a framework for calculating prediction intervals and variances.

---

### **Possible Extensions**

- **Adjusting Weights:** Give less importance to older data if claim patterns are changing.
- **Different Distributions:** Move beyond Poisson to other distributions from the exponential dispersion family if data variability doesn’t fit Poisson well.
- **Calendar Year Effects:** Model changes due to inflation, legislation, or operational adjustments by adding trends across calendar years.
- **Micro-Level Data:** Instead of using aggregated triangles, modern computing power allows using individual claim information (claim-by-claim modeling) for more granular reserving.

---

### **Summary**

- **Traditional Methods (Chain Ladder, BF):** Straightforward and intuitive but limited to point estimates.
- **Stochastic Methods:** Provide measures of uncertainty and can satisfy regulatory requirements for setting reserves above a certain percentile.
- **Model Extensions:** Offer flexibility in handling real-world complexities, such as changing claim patterns or incorporating additional data sources.

Overall, the evolution from deterministic algorithms to stochastic and more flexible models reflects the industry’s need for more robust, transparent, and justifiable reserving practices.
