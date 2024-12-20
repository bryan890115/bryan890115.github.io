---
layout: default
title: "Module 5: Liability Valuations: Ruin Theory Distributions"
---



## **Liability Valuations: Ruin Theory**

### **Insurance Solvency Considerations**

#### **Balance Sheet and Surplus Process**
- **Balance Sheet**:
  - At time $$ t $$:
    - *$$ A_t $$*: Assets at time $$ t $$.
    - *$$ L_t $$*: Liabilities at time $$ t $$.
    - Require: $$ A_t \geq L_t $$.

- **Surplus Process**:
  $$ 
  C_t = A_t - L_t, \quad t \geq 0.
  $$
  - Initial surplus: $$ C_0 > 0 $$.
  - **No Ruin Condition**: Ensure that for a high level $$ q $$:
    $$ 
    1 - \Pr\left[\inf_{t \geq 0} C_t < 0 \mid C_0 = c_0 \right] \geq q.
    $$

#### **Risk Measures**

1. **No Ruin Condition**:
   - For the one-period model, the initial surplus $$ C_0 $$ and asset strategy must satisfy:
     $$ 
     \Pr[A_1 \geq L_1 \mid C_0 = c_0] = \Pr[L_1 - A_1 \leq 0 \mid C_0 = c_0] \geq q.
     $$
   - This implies that the initial surplus $$ C_0 $$ must be at least the **Value-at-Risk (VaR)** at confidence level $$ q $$:
     $$ 
     \text{VaR}_q(L_1 - A_1) = \inf \{c \geq 0 : \Pr[L_1 - A_1 \leq 0 \mid C_0 = c] \geq q\}.
     $$

     - "inf" is the infimum, so we want to find the samllest value of c (or the greatest lower bound of this set) where the probability $$ \Pr[L_1 - A_1 \leq 0]$$ is at least $$ q $$.

2. **Regulatory Risk Measures**:
   - **Solvency II**: Uses $$ \text{VaR}_{99.5\%} $$.
    - **Swiss Solvency Test**: Uses $$ \text{TVaR}_{99\%} $$.

3. **Summary**:
   - **VaR**: Measures the minimum surplus required to ensure that losses exceed assets with a small probability $$ 1-q $$.
   - **TVaR (not covered)**: Accounts for the severity of losses beyond the VaR threshold, providing a more conservative risk assessment.


---

### **Ruin Theory in Discrete Time**

#### **Surplus Process**
- The surplus process over multiple periods:
  $$ 
  C_t = C_0 + \sum_{u=1}^t (\pi_u - S_u), \quad t \in \mathbb{N},
  $$
  where:
  - *$$ C_0 $$*: Initial surplus.
  - *$$ \pi_t $$*: Premium income (i.i.d.).
  - *$$ S_t $$*: Claim payouts (i.i.d.).
  - Assume $$ \pi_t $$ and $$ S_t $$ are independent.

- The net increment is:
  $$ 
  X_t = \pi_t - S_t, \quad t \in \mathbb{N}.
  $$

---

#### **Time of Ruin**
- **Definition**:
  $$ 
  \tau = \inf \{s \in \mathbb{N} : C_s < 0\}.
  $$
  - *$$ \tau $$* is the earliest time step where the surplus $$ C_s $$ becomes negative.
  - If $$ C_s $$ never becomes negative, then $$ \tau = \infty $$.

---

#### **Finite-Time Ruin Probability**
- **Definition**:
  $$ 
  \psi_t(C_0) = \Pr[\tau \leq t \mid C_0 = c_0].
  $$
  - Probability that ruin occurs **within the first $$ t $$ periods**, given initial surplus $$ C_0 = c_0 $$.
  - Useful for analyzing a fixed time horizon.

---

#### **Ultimate Ruin Probability**
- **Definition**:
  $$ 
  \psi(C_0) = \Pr[\tau < \infty \mid C_0 = c_0] = \lim_{t \to \infty} \psi_t(C_0).
  $$
  - Probability that ruin occurs **at any point in the future**, regardless of when.
  - Considers an infinite time horizon.

---

### **Key Difference**:
- **Finite-Time Ruin**: Restricted to a specific $$ t $$.
- **Ultimate Ruin**: Considers ruin over an infinite time horizon.




#### **Behavior of Surplus Process** (Theorem 5.4)
- The behavior of the surplus process $$ C_t $$ depends on the sign of $$ \mathbb{E}[X_1] $$:
  1. **$$ \mathbb{E}[X_1] < 0 $$**: Surplus decreases to $$ -\infty $$ (blows down).
  2. **$$ \mathbb{E}[X_1] = 0 $$**: Surplus oscillates between $$ \infty $$ and $$ -\infty $$.
  3. **$$ \mathbb{E}[X_1] > 0 $$**: Surplus increases to $$ \infty $$ (blows up).

---

#### **Implications**
1. **When $$ \mathbb{E}[X_1] \leq 0 $$**:
   - Ruin is certain:
     $$ 
     \psi(C_0) = 1 \quad \text{for any } C_0 \geq 0.
     $$

2. **When $$ \mathbb{E}[X_1] > 0 $$ (Net Profit Condition or NPC)**:
   - Ruin is not certain:
     $$ 
     \psi(C_0) < 1.
     $$
   - The ultimate ruin probability satisfies:
     $$ 
     \psi(C_0) \leq \psi(0) < 1.
     $$
   - This implies that higher initial surplus $$ C_0 $$ reduces the likelihood of ruin.


#### **Summary**
- **Net Profit Condition** ensures the surplus process grows on average, reducing ruin probability.
- Without NPC ($$ \mathbb{E}[X_1] \leq 0 $$), ruin is inevitable regardless of initial surplus.


---

### **Adjustment Coefficient**

#### **Lundberg Coefficient / Adjustment Coefficient**
- The adjustment coefficient $$ R $$ is defined as the positive solution to:
  $$ 
  M_{S_1 - \pi_1}(R) = \mathbb{E}[e^{-R X_1}] = 1.
  $$
  - If $$ R $$ exists, it is unique.

- **Lundberg Upper Bound**:
  $$ 
  \psi(C_0) \leq e^{-R C_0}.
  $$

### **Example Calculation**
- Suppose:
  - Desired tolerance: $$ p = 0.01 $$.
  - Adjustment coefficient: $$ R = 0.05 $$.
- Calculate $$ C_0 $$:
  $$ 
  C_0 = -\frac{\ln(0.01)}{0.05} = \frac{4.605}{0.05} = 92.1.
  $$
- **Result**:
  - An initial surplus of $$ C_0 \geq 92.1 $$ guarantees the ruin probability is less than $$ 1\% $$.

---

## **Ruin Theory in Continuous Time**

### **Surplus Process: The Cramér–Lundberg Model**
The surplus process in continuous time under the Cramér–Lundberg model is defined as:
$$
C(t) = c_0 + \pi t - S(t), \quad t \geq 0,
$$
where:
- *$$ c_0 $$*: Initial surplus of the insurer.
- *$$ \pi t $$*: Premium income collected over time. Premiums are collected at a constant rate, so $$ \pi t $$ represents the cumulative premiums collected over a time interval $$ t $$.
- *$$ S(t) = \sum_{i=1}^{N(t)} Y_i $$*: Aggregate amount of claims up to time $$ t $$.
  - *$$ N(t) $$*: A Poisson process with rate $$ \lambda > 0 $$, modeling the number of claims over time.
  - *$$ \{Y_i\}_{i \in \mathbb{N}} $$*: i.i.d. claim sizes with cdf $$ G $$, independent of $$ N(t) $$.

The equation shows that the insurer's surplus $$ C(t) $$ at any time $$ t $$ is the initial surplus $$ c_0 $$ plus premium income $$ \pi t $$, minus the aggregate claims $$ S(t) $$.

---

The premium rate $$ \pi $$ is set as:
$$
\pi = (1 + \theta) \lambda \mathbb{E}[Y_1],
$$
where:
- *$$ \lambda \mathbb{E}[Y_1] $$*: Expected total claim cost, calculated as the claim frequency ($$ \lambda $$) times the expected claim size ($$ \mathbb{E}[Y_1] $$).
- *$$ (1 + \theta) $$*: Relative security loading, with $$ \theta > 0 $$ ensuring a margin for safety and profitability.

This equation ensures that the premiums collected cover the expected claims and include a safety margin proportional to $$ \theta $$.

---

### **Compound Poisson Process**
Under the Cramér–Lundberg model:

- The aggregate claims $$ S(t) $$ form a compound Poisson process:
  $$
  S(t) = \sum_{i=1}^{N(t)} Y_i, \quad t \geq 0.
  $$
  - Here, $$ S(t) $$ is the total claim amount up to time $$ t $$, summing $$ N(t) $$ independent claim amounts $$ Y_i $$.

- Properties of $$ S(t) $$:
  - **Mean**:
    $$
    \mathbb{E}[S(t)] = \lambda t \mathbb{E}[Y].
    $$
    - The expected total claims are proportional to the claim frequency ($$ \lambda $$), time ($$ t $$), and average claim size ($$ \mathbb{E}[Y] $$).
  - **Variance**:
    $$
    \text{Var}[S(t)] = \lambda t \mathbb{E}[Y^2].
    $$
    - The variance depends on the claim frequency ($$ \lambda $$), time ($$ t $$), and the second moment of the claim size ($$ \mathbb{E}[Y^2] $$).

- **Increments**:
  $$
  S(t + h) - S(t) \sim \text{CompPoi}(\lambda h, G).
  $$
  - Over an interval $$ h $$, the additional claims follow a compound Poisson distribution with rate $$ \lambda h $$ and claim size distribution $$ G $$.

---

### **The Probability of Ruin**

There are multiple methods to calculate the ruin probability:

1. **Analytically**:
   - The ruin probability $$ \psi(c_0) $$ may have a closed-form expression in specific cases, such as:
     - Exponential claim sizes.
     - Mixtures of exponential claim size distributions.

2. **Using Panjer’s Recursion**:
   - By discretizing the continuous distribution of claims, Panjer’s recursion can be applied to compute ruin probabilities.

3. **Monte Carlo Simulation**:
   - Simulate the surplus process to estimate the probability of ruin based on a large number of scenarios.

4. **Finite-Time Ruin Probability**:
   - *$$ \psi_t(c_0) $$*, the ruin probability within a finite time $$ t $$, is often harder to calculate and may require advanced numerical methods.



---

### **Adjustment Coefficient**

#### **Surplus Process**
Over an interval $$ [0, t] $$, the **excess of losses over premiums** is defined as:
$$ 
S(t) - \pi t.
$$

The **adjustment coefficient** $$ R $$ is the first positive solution to:
$$
\mathbb{E}\left[e^{R(S(t) - \pi t)}\right] = 1.
$$

#### **Expectation of Surplus Process**
For the surplus process $$ C(t) $$:
$$ 
\mathbb{E}[e^{-R C(t)}] = e^{-R c_0}.
$$

##### **Derivation:**
1. Start with the surplus equation:
   $$ 
   C(t) = c_0 + \pi t - S(t).
   $$

2. Substitute into the expectation:
   $$ 
   \mathbb{E}[e^{-R C(t)}] = \mathbb{E}[e^{-R(c_0 + \pi t - S(t))}].
   $$

3. Factorize the terms:
   $$ 
   \mathbb{E}[e^{-R C(t)}] = e^{-R c_0} \mathbb{E}[e^{-R (\pi t - S(t))}].
   $$

4. Use the defining property of the adjustment coefficient $$ R $$:
   $$ 
   \mathbb{E}[e^{R(S(t) - \pi t)}] = 1.
   $$

5. Substitute back:
   $$ 
   \mathbb{E}[e^{-R C(t)}] = e^{-R c_0}.
   $$



#### **Lundberg Equation**
The adjustment coefficient $$ R $$ satisfies:
$$
M_Y(R) = \mathbb{E}[e^{R Y}] = 1 + (1 + \theta) \mathbb{E}[Y] R,
$$
where $$ M_Y(R) $$ is the moment generating function (MGF) of $$ Y $$. Below is the derivation.

#### **Derivation**

1. Start with the definition of the adjustment coefficient:
   $$ 
   \mathbb{E}[e^{R(S(t) - \pi t)}] = 1.
   $$

2. Rewrite $$ S(t) $$ as a compound Poisson process:
   $$ 
   S(t) = \sum_{i=1}^{N(t)} Y_i,
   $$
   where $$ N(t) $$ is a Poisson process with rate $$ \lambda $$.

3. Substitute into the expectation:
   $$ 
   \mathbb{E}[e^{R(S(t) - \pi t)}] = e^{-R \pi t} \mathbb{E}[e^{R S(t)}].
   $$

4. Express $$ \mathbb{E}[e^{R S(t)}] $$ for the compound Poisson process:
   $$ 
   \mathbb{E}[e^{R S(t)}] = e^{\lambda t (\mathbb{E}[e^{R Y}] - 1)}.
   $$

   1. **Condition on $$ N(t) $$**:
   $$ 
   \mathbb{E}[e^{R S(t)}] = \mathbb{E}\left[\mathbb{E}\left[e^{R \sum_{i=1}^{N(t)} Y_i} \mid N(t)\right]\right].
   $$

    2. **Independent $$ Y_i $$**:
    $$ 
    \mathbb{E}\left[e^{R \sum_{i=1}^{N(t)} Y_i} \mid N(t) = n\right] = \mathbb{E}[e^{R Y}]^n.
    $$

    3. **Combine with $$ N(t) $$**:
    $$ 
    \mathbb{E}[e^{R S(t)}] = \sum_{n=0}^\infty \mathbb{E}[e^{R Y}]^n \cdot \frac{(\lambda t)^n e^{-\lambda t}}{n!}.
    $$

    4. **Simplify the Series**:
    Recognizing the series as an exponential:
    $$ 
    \mathbb{E}[e^{R S(t)}] = e^{-\lambda t} \cdot e^{\lambda t \mathbb{E}[e^{R Y}]}.
    $$

5. Combine the terms:
   $$ 
   e^{-R \pi t} e^{\lambda t (\mathbb{E}[e^{R Y}] - 1)} = 1.
   $$

6. Simplify the exponents:
   $$ 
   e^{t(-R \pi + \lambda (\mathbb{E}[e^{R Y}] - 1))} = 1.
   $$

7. Since the exponent must equal zero for the equation to hold:
   $$ 
   -R \pi + \lambda (\mathbb{E}[e^{R Y}] - 1) = 0.
   $$

8. Substitute the premium rate $$ \pi = (1 + \theta) \lambda \mathbb{E}[Y] $$:
   $$ 
   -R (1 + \theta) \lambda \mathbb{E}[Y] + \lambda (\mathbb{E}[e^{R Y}] - 1) = 0.
   $$

9. Rearrange for the MGF of $$ Y $$:
   $$ 
   \mathbb{E}[e^{R Y}] = 1 + (1 + \theta) \mathbb{E}[Y] R.
   $$

10. Conclude with:
   $$ 
   M_Y(R) = \mathbb{E}[e^{R Y}] = 1 + (1 + \theta) \mathbb{E}[Y] R.
   $$

---

### **Adjustment Coefficient**

The adjustment coefficient $$ R $$ is determined by solving the equation:
$$ 
M_Y(R) = 1 + (1 + \theta) \mathbb{E}[Y] R,
$$
where $$ M_Y(R) $$ is the moment generating function (MGF) of the claim size distribution $$ Y $$. 

#### **Key Components**

1. **Moment Generating Function (MGF)**:
   $$ 
   M_Y(R) = \mathbb{E}[e^{R Y}].
   $$
   - The MGF is an increasing and convex function in $$ R $$, as:
     - First derivative: $$ M_Y'(R) = \mathbb{E}[Y e^{R Y}] > 0 $$ (MGF is increasing).
     - Second derivative: $$ M_Y''(R) = \mathbb{E}[Y^2 e^{R Y}] > 0 $$ (MGF is convex).

2. **Linear Function**:
   $$ 
   1 + (1 + \theta) \mathbb{E}[Y] R.
   $$
   - This line starts at $$ 1 $$ when $$ R = 0 $$.
   - Its slope is $$ (1 + \theta) \mathbb{E}[Y] $$, proportional to the loading factor $$ \theta $$.

3. **Intersection Point**:
   - The adjustment coefficient $$ R $$ is the first positive solution where the MGF intersects the linear function:
     $$ 
     M_Y(R) = 1 + (1 + \theta) \mathbb{E}[Y] R.
     $$

#### **Properties**
- The MGF of $$ Y $$ at $$ R = 0 $$ is:
  $$ 
  M_Y(0) = \mathbb{E}[e^{0 \cdot Y}] = 1.
  $$

- The adjustment coefficient $$ R $$ ensures the excess of losses over premiums remains bounded within acceptable probabilities.
 

---
### **Theorem (Lundberg Exponential Upper Bound)**

For $$ c_0 \geq 0 $$:
$$
\psi(c_0) = \Pr[\tau < \infty \mid C(0) = c_0] = \frac{e^{-R c_0}}{\mathbb{E}[e^{-R C(\tau)} \mid \tau < \infty]} \leq e^{-R c_0}.
$$

#### **Explanation**
- **Key Laws**:
  - Derived using the **law of total expectation** and the property of $$ e^{-R C(t)} $$.
  - Since:
    $$
    \mathbb{E}[e^{-R C(t)}] = e^{-R c_0}, \quad \forall t \geq 0.
    $$
  - At the time of ruin ($$ \tau < \infty $$), the surplus $$ C(\tau) < 0 $$, so:
    $$
    \mathbb{E}[e^{-R C(t)}] = \mathbb{E}[e^{-R C(\tau)} \mid \tau < \infty] \Pr[\tau < \infty].
    $$

- **Rearranging**:
  Using the martingale property:
  $$
  \Pr[\tau < \infty] = \frac{\mathbb{E}[e^{-R C(t)}]}{\mathbb{E}[e^{-R C(\tau)} \mid \tau < \infty]}.
  $$

- **Result**:
  Substituting $$ \mathbb{E}[e^{-R C(t)}] = e^{-R c_0} $$:
  $$
  \psi(c_0) = \frac{e^{-R c_0}}{\mathbb{E}[e^{-R C(\tau)} \mid \tau < \infty]}.
  $$

#### **Interpretation**
- The upper bound $$ e^{-R c_0} $$ arises because:
  $$
  \mathbb{E}[e^{-R C(\tau)} \mid \tau < \infty] \geq 1,
  $$
  due to the negativity of $$ C(\tau) $$ at ruin ($$ e $$ to the power of a positive number is also positive).
- Therefore, the ruin probability $$ \psi(c_0) $$ decreases **exponentially** as the initial surplus $$ c_0 $$ increases.

---

### **Examples**
### Example 1: Find $$ R $$ Using the Lundberg Equation

### Question
Let $$ Y_1 \sim \text{Exp}(\beta) $$, where:

- *$$ \mathbb{E}[Y_1] = \frac{1}{\beta} $$*,
- *$$ M_Y(R) = \frac{\beta}{\beta - R} $$*.

The Lundberg equation is given by:

$$
M_Y(R) = 1 + (1 + \theta) \mathbb{E}[Y] R
$$

Solve the Lundberg equation to find $$ R $$ using the quadratic formula.

---

### Solution

Substitute the values for $$ M_Y(R) $$ and $$ \mathbb{E}[Y] $$:

$$
\frac{\beta}{\beta - R} = 1 + (1 + \theta) \frac{1}{\beta} R
$$

Multiply through by $$ \beta (\beta - R) $$ to eliminate denominators:

$$
\beta^2 = \beta (\beta - R) \left( 1 + \frac{(1 + \theta) R}{\beta} \right)
$$

Simplify the right-hand side:

$$
\beta^2 = (\beta - R) \left[ \beta + (1 + \theta) R \right]
$$

Expand:

$$
\beta^2 = \beta^2 - \beta R + (1 + \theta) \beta R - (1 + \theta) R^2
$$

Simplify:

$$
0 = \beta R \theta - (1 + \theta) R^2
$$

Factorize:

$$
R \left( (1 + \theta) R - \beta \theta \right) = 0
$$

Solve for $$ R $$:

$$
R = 0 \quad \text{or} \quad R = \frac{\beta \theta}{1 + \theta}
$$

Since $$ R = 0 $$ is trivial, the solution is:

$$
R = \frac{\beta \theta}{1 + \theta}
$$

---

### Example 2: Find $$ \psi(c₀) $$ Using the Exact Formula

### Question

Using the adjustment coefficient $$ R = \frac{\beta \theta}{1 + \theta} $$ from Example 1, calculate the ruin probability $$ \psi(c₀) $$ using the exact formula:

$$
\psi(c₀) = \frac{e^{-R c₀}}{\mathbb{E}[e^{-R C(\tau)} \mid \tau < \infty]}
$$

- Note: only exponential and negative binomial(?) can be expressed explicitly using exact formula. Thats why we have the Lunberg's lower bound

---

### Solution

1. **Expectation at Ruin:**

At the time of ruin $$ \tau $$, the surplus $$ C(\tau) = -Y_1 $$, where $$ Y_1 > 0 $$ is the deficit. The deficit arises from the claim size $$ Y_1 $$ that exceeds the available surplus.

Given $$ Y_1 \sim \text{Exp}(\beta) $$, the moment-generating function (MGF) of $$ Y_1 $$ is:

$$
\mathbb{E}[e^{R Y_1}] = M_Y(R) = \frac{\beta}{\beta - R}, \quad \text{for } R < \beta.
$$

Thus, the expectation becomes:

$$
\mathbb{E}[e^{-R C(\tau)} \mid \tau < \infty] = \mathbb{E}[e^{R Y_1}] = \frac{\beta}{\beta - R}.
$$

---

2. **Substitute Back into Formula:**

Using the exact formula for $$ \psi(c₀) $$:

$$
\psi(c₀) = \frac{e^{-R c₀}}{\mathbb{E}[e^{-R C(\tau)} \mid \tau < \infty]}
$$

Substitute the expectation:

$$
\psi(c₀) = \frac{e^{-R c₀}}{\frac{\beta}{\beta - R}}.
$$

Simplify:

$$
\psi(c₀) = \left( \frac{\beta - R}{\beta} \right) e^{-R c₀}.
$$

---

3. **Substitute $$ R = \frac{\beta \theta}{1 + \theta} $$:**

Compute $$ \beta - R $$:

$$
\beta - R = \beta - \frac{\beta \theta}{1 + \theta} = \frac{\beta}{1 + \theta}.
$$

Compute $$ \frac{\beta - R}{\beta} $$:

$$
\frac{\beta - R}{\beta} = \frac{\frac{\beta}{1 + \theta}}{\beta} = \frac{1}{1 + \theta}.
$$

Thus:

$$
\psi(c₀) = \frac{1}{1 + \theta} e^{-R c₀}.
$$

---

4. **Lundberg Bound:**

The Lundberg inequality provides an upper bound for $$ \psi(c₀) $$:

$$
\psi(c₀) \leq e^{-R c₀}.
$$

The exact formula satisfies this bound because:

$$
\psi(c₀) = \frac{1}{1 + \theta} e^{-R c₀},
$$

where the prefactor $$ \frac{1}{1 + \theta} < 1 $$, ensuring $$ \psi(c₀) \leq e^{-R c₀} $$.

---

### Final Expression:

1. **Exact Ruin Probability:**

$$
\psi(c₀) = \frac{1}{1 + \theta} \exp\left( -\frac{\beta \theta}{1 + \theta} c₀ \right).
$$

2. **Lundberg Bound:**

$$
\psi(c₀) \leq e^{-R c₀}.
$$


---

## Final Answers

1. **Adjustment Coefficient:**
   $$
   R = \frac{\beta \theta}{1 + \theta}
   $$

2. **Ruin Probability:**
   $$
   \psi(c₀) = \frac{1}{1 + \theta} \exp\left( -\frac{\beta \theta}{1 + \theta} c₀ \right)
   $$

---

### **Key Points**
- The **adjustment coefficient** $$ R $$ plays a central role in quantifying ruin probabilities and their bounds.
- The **Cramér–Lundberg model** provides a framework to model the surplus process and estimate ruin probabilities analytically or numerically.








---

## **Applications to Reinsurance**

### **Key Formula for Ruin Probability**
From Theorem 13.4.1:
- The ruin probability under reinsurance satisfies:
  $$ 
  \psi(c_0) = e^{-R c_0} \mathbb{E}\left[e^{-R C(\tau)} \mid \tau < \infty \right] \leq e^{-R c_0}.
  $$
  - The **adjustment coefficient** $$ R $$ is the positive solution to:
    $$ 
    \mathbb{E}\left[e^{R Y}\right] = 1 + (1 + \theta)\mathbb{E}[Y] R.
    $$
  - **Goal**:
    - Increase $$ R $$ by designing reinsurance strategies (e.g., proportional or excess-of-loss reinsurance) to reduce the risk retained by the insurer, thus lowering $$ \psi(c_0) $$. 
      - Reduce ruin probability and upper bound directly
    - Select reinsurance with the smallest possible premium that ensures $$ \psi(c_0) $$ remains below a given tolerance level.



---
### **Modified Surplus Process**
With reinsurance, the surplus process becomes:
$$
C(t) = c_0 + (\pi - \pi_h)t - \sum_{i=1}^{N(t)} \{Y_i - h(Y_i)\},
$$
where:
- *$$ c_0 $$*: Initial surplus of the insurer.
- *$$ \pi $$*: Premium rate (income from direct policies).
- *$$ \pi_h $$*: Reinsurance premium:
  $$
  \pi_h = (1 + \xi) \lambda \mathbb{E}[h(Y)],
  $$
  where $$ \xi \geq 0 $$ is the reinsurance loading factor (profit margin for the reinsurer).
- *$$ Y_i $$*: Size of a claim (loss amount for each policy), which is a random variable following the claim size distribution $$ G $$.
- *$$ h(Y_i) $$*: Portion of each claim $$ Y_i $$ paid by the reinsurer, satisfying $$ 0 \leq h(Y_i) \leq Y_i $$.

#### **Key Details**
1. **Claim Size ($$ Y $$)**:
   - Represents the **total loss or claim** amount for an insurance policy.


2. **Reinsurer's Share ($$ h(Y) $$)**:
   - The **portion of the claim $$ Y $$ that is covered by the reinsurer**, reducing the insurer's exposure.
   - Types of reinsurance:
     - **Proportional Reinsurance**:
       $$ 
       h(Y) = \alpha Y, 
       $$
       where $$ \alpha $$ is the retention percentage covered by the reinsurer.
     - **Excess-of-Loss Reinsurance**:
       $$ 
       h(Y) = (Y - d)^+, 
       $$
       where $$ d $$ is the retention limit (the insurer pays up to $$ d $$, and the reinsurer covers the excess).

#### **Practical Observations**
- *$$ \xi > \theta $$*: Reinsurance loading ($$ \xi $$) is typically higher than the insurer's original loading ($$ \theta $$).
- *$$ \pi > \pi_h $$*: The insurer's premium income exceeds the reinsurance costs.

---

### **Adjustment Coefficient for Reinsurance**
The adjustment coefficient $$ R_h > 0 $$ satisfies:
$$
\lambda \left(\mathbb{E}[e^{r (Y - h(Y))}] - 1\right) = (\pi - \pi_h) r.
$$

#### **Key Intuition**
1. **Left-Hand Side (LHS):**
   - **$$ \lambda $$:** The arrival rate of claims.
   - **$$ \mathbb{E}[e^{r (Y - h(Y))}] $$:** The moment-generating function (MGF) of the retained claim $$ Y - h(Y) $$, where $$ h(Y) $$ is the portion of the claim covered by reinsurance.
   - **$$ \mathbb{E}[e^{r (Y - h(Y))}] - 1 $$:** Represents the net growth factor contributed by the retained claims.

   This term quantifies the contribution of retained losses to the ruin probability.

2. **Right-Hand Side (RHS):**
   - **$$ \pi - \pi_h $$:** The net premium rate after subtracting the reinsurance premium $$ \pi_h $$.
   - **$$ r $$:** The adjustment coefficient $$ R_h $$, representing the exponential decay rate of ruin probability.

   This term represents the surplus growth due to net premium income.

3. **Balance of Risk and Income:**
   - The equation ensures the balance between:
     - The risk of ruin from retained claims (LHS).
     - The surplus growth from net premiums (RHS).
   - Solving this equation for $$ r $$ gives the adjustment coefficient $$ R_h $$, which measures how effective reinsurance is in reducing the risk of ruin.


---

### **Proportional Reinsurance**

- **Setup**:
  - Let $$ Y \sim \text{Exp}(\beta = 1) $$, $$ \theta = 0.25 $$, and $$ \xi = 0.4 $$.
  - The reinsurer covers a proportion $$ (1 - \alpha) $$ of claims:
    $$ 
    h(Y) = (1 - \alpha)Y.
    $$

- **Adjustment Coefficient Calculation**:
  1. **Expected exponential term**:
     - Using the moment generating function (MGF) of an exponential random variable:
       $$ 
       M_Y(r) = \mathbb{E}[e^{rY}] = \frac{1}{1 - r}, \quad \text{for } r < 1.
       $$
     - Substituting $$ Y - h(Y) = \alpha Y $$:
       $$ 
       \mathbb{E}[e^{r(Y - h(Y))}] = \mathbb{E}[e^{r \alpha Y}] = M_Y(\alpha r) = \frac{1}{1 - \alpha r}, \quad \text{for } \alpha r < 1.
       $$

  2. **Premium difference between insurer and reinsurer**:
     $$ 
     \pi - \pi_h = 1.25\lambda - 1.4\lambda(1 - \alpha) = \lambda(1.4\alpha - 0.15).
     $$

  3. **Equation for $$ R_h $$**:
     $$ 
     \frac{\alpha}{1 - \alpha R_h} = 1.4\alpha - 0.15.
     $$

  4. **Solve for $$ R_h $$**:
     $$ 
     R_h = \frac{1}{\alpha} \cdot \frac{0.4\alpha - 0.15}{1.4\alpha - 0.15}.
     $$

- **Optimal Retention**:
  - Maximize $$ R_h $$ with respect to $$ \alpha $$:
    $$ 
    \alpha^* = 0.691933 \approx 70\%.
    $$
  - Resulting adjustment coefficient:
    $$ 
    R_h^* = 0.223787.
    $$

- **Remark**: Transforming **30%** of losses reduces expected profit by approximately **48%**, not 60.5%.

  - **Profit Reduction Formula**:
    $$ 
    \text{Profit Reduction} = 1 - \frac{\text{Profit (With Reinsurance)}}{\text{Profit (No Reinsurance)}} = 1 - \frac{\pi - \pi_h - \lambda \mathbb{E}[\alpha Y]}{\pi - \lambda \mathbb{E}[Y]}.
    $$

  - **Calculation**:
    Substituting:
    - *$$ \pi = 1.25\lambda $$*,
    - *$$ \pi_h = 1.4\lambda(1 - \alpha) $$*,
    - *$$ \mathbb{E}[Y] = 1 $$* (since $$ Y \sim \text{Exp}(1) $$),
    - *$$ \alpha = 0.7 $$*,
    $$ 
    \text{Profit Reduction} = 1 - \frac{1.25\lambda - 1.4\lambda(1 - 0.7) - 0.7\lambda}{1.25\lambda - \lambda}.
    $$

    Simplify the numerator:
    $$
    1.25\lambda - 1.4\lambda(0.3) - 0.7\lambda = 1.25\lambda - 0.42\lambda - 0.7\lambda = (1.25 - 0.42 - 0.7)\lambda = 0.13\lambda.
    $$

    Simplify the denominator:
    $$
    1.25\lambda - \lambda = 0.25\lambda.
    $$

    Compute the profit reduction:
    $$
    \text{Profit Reduction} = 1 - \frac{0.13\lambda}{0.25\lambda} = 1 - \frac{0.13}{0.25} = 1 - 0.52 = 0.48.
    $$

    So, the profit reduction is **48% (CHECK AGAIN, LECTURE SLIDE SAYS 60.5%)**.

  - **Explanation**:
    The **48%** reduction occurs because introducing reinsurance reduces the insurer's retained profit due to the reinsurer's higher premium loading ($$ \xi = 0.4 $$). The insurer passes **30%** of the losses to the reinsurer (since $$ \alpha = 0.7 $$, the insurer retains 70% of the claims), which significantly reduces the profit margin.

---

### **Excess of Loss Reinsurance**
- **Setup**:
  - Let $$ Y \sim \text{Exp}(1) $$, $$ \theta = 0.25 $$, and $$ \xi = 0.4 $$.
  - The reinsurer covers losses above a threshold $$ d $$:
    $$ 
    h(Y) = \max(Y - d, 0).
    $$

- **Adjustment Coefficient Calculation**:

  1. **Reinsurance Premium**:
     - The reinsurance premium $$ \pi_h $$ is calculated as:
       $$ 
       \pi_h = (1 + \xi)\lambda \mathbb{E}[h(Y)],
       $$
       where:
       - *$$ \mathbb{E}[h(Y)] $$* is the expected portion of claims paid by the reinsurer:
         $$ 
         \mathbb{E}[h(Y)] = \int_d^\infty (Y - d)e^{-Y}dx.
         $$
     - **Why $$ \mathbb{E}[h(Y)] $$?**
       - This integral represents the **average payment made by the reinsurer** for claims $$ Y > d $$:
         - When $$ Y > d $$, the reinsurer pays $$ Y - d $$, so the integrand becomes $$ (Y - d)f_Y(Y) $$, where $$ f_Y(Y) = e^{-Y} $$ is the PDF of the exponential distribution.

         - To computer $$ \mathbb{E}[h(Y)] $$, we sum up all possible payments $$ h(Y) = (Y-d)$$, weighted by their probabilities $$ f_Y(Y) = e^{-Y}$$ (Y ~ exp(1)).
        
         - The integration starts at $$ d $$ because for $$ Y \leq d $$, the reinsurer pays nothing ($$ h(Y) = 0 $$).




     - **Simplify $$ \mathbb{E}[h(Y)] $$**:
       - Split the integral into two parts:
         $$ 
         \mathbb{E}[h(Y)] = \int_d^\infty x e^{-x} dx - \int_d^\infty d e^{-x} dx.
         $$
       - First term $$ \int_d^\infty x e^{-x} dx $$:
         - Use integration by parts:
           $$ 
           \int_d^\infty x e^{-x} dx = \left[-x e^{-x}\right]_d^\infty + \int_d^\infty e^{-x} dx = d e^{-d} + e^{-d}.
           $$
       - Second term $$ \int_d^\infty d e^{-x} dx $$:
         - Since $$ d $$ is a constant:
           $$ 
           \int_d^\infty d e^{-x} dx = d \int_d^\infty e^{-x} dx = d e^{-d}.
           $$
       - Combine results:
         $$ 
         \mathbb{E}[h(Y)] = (d e^{-d} + e^{-d}) - d e^{-d} = e^{-d}.
         $$
     - **Final Formula for $$ \pi_h $$**:
       $$ 
       \pi_h = (1 + \xi)\lambda e^{-d} = 1.4\lambda e^{-d}.
       $$
     - **Explanation**:
       - The reinsurance premium depends on the expected portion of claims paid by the reinsurer. As $$ d $$ increases, fewer claims exceed $$ d $$, reducing $$ \pi_h $$.

  2. **Expected Exponential Term**:
     $$ 
     \mathbb{E}[e^{r(Y - h(Y))}] = \int_0^d e^{r x} e^{-x} dx + \int_d^\infty e^{r d} e^{-x} dx.
     $$
     - **$$ \mathbb{E}[e^{r (Y - h(Y))}] $$:** The moment-generating function (MGF) of the retained claim $$ Y - h(Y) $$
     - The first term corresponds to claims $$ Y \leq d $$ (no reinsurance coverage).
     - The second term corresponds to claims $$ Y > d $$ (reinsurer pays $$ h(Y) = Y - d $$, insurers pays $$ d $$).
     - Simplify:
       $$ 
       \mathbb{E}[e^{r(Y - h(Y))}] = \frac{1 - r e^{-d(1 - r)}}{1 - r}.
       $$

  3. **Solve for $$ R_h $$**:
     - Substitute the premium difference $$ \pi - \pi_h $$ into the adjustment coefficient equation:
       $$ 
       1 + (1.25 - 1.4e^{-d})R_h - \frac{1 - R_h e^{-d(1 - R_h)}}{1 - R_h} = 0.
       $$

  4. **Optimal Threshold**:
     - Use numerical methods to solve for $$ d $$ and $$ R_h $$:
       $$ 
       d^* = 0.9632226, \quad R_h^* = 0.3493290.
       $$

- **Remark**:
  - The higher $$ R_h^* $$ compared to proportional reinsurance demonstrates the greater effectiveness of excess of loss reinsurance in reducing ruin probabilities.
