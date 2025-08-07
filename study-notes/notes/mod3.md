---
layout: default
title: "Module 3: Aggregate Loss Modeling"
---

# **Module 3: Aggregate Loss Modeling**


## **Outline**
1. **Aggregate Losses and Terminologies**:
   - Collective Risk Model
   - Individual Risk Model
2. **Moments of Aggregate Losses**:
   - Mean and Variance
3. **Moment Generating Function (MGF)**:
   - MGF of Aggregate Losses
4. **Probability Generating Function (PGF)**:
   - PGF of Aggregate Losses
5. **Key Takeaways**

---

## **Aggregate Losses and Terminologies**

1. **Aggregate Losses**:
   - In the collective risk model, the total loss is represented as:
     $$
     S = \sum_{i=1}^N X_i
     $$
     where:
     - *$$ N $$*: Number of claims (integer-valued).
     - *$$ X_i $$*: Individual payment amounts (i.i.d. and independent of $$ N $$).

2. **Individual Risk Model**:
   - If $$ N $$ is a fixed constant $$ n $$:
     $$
     S = \sum_{i=1}^n X_i
     $$

3. **Actuarial Terminologies**:
   - *$$ N $$*: Claim count (frequency).
   - *$$ X_i $$*: Individual claim amount (severity).
   - *$$ S $$*: Aggregate loss (total loss).


---

## **Distribution of Aggregate Losses**

### **1. Determining Distribution of Aggregate Losses**

#### **Using Convolution**
- **Definition**: The sum $$ S = X + Y $$ of two independent random variables is called the convolution of $$ F_X $$ and $$ F_Y $$:
  $$ 
  F_S = F_X \ast F_Y 
  $$

- **Discrete Case**:
  $$ 
  F_S(s) = \sum_x F_Y(s - x) f_X(x), \quad f_S(s) = \sum_x f_Y(s - x) f_X(x) 
  $$

  - $$ F_S(s) = P(X + Y \leq s), \quad f_S(s) = P(X + Y =s )$$


- **Continuous Case**:
  $$ 
  F_S(s) = \int_x F_Y(s - x) f_X(x) dx, \quad f_S(s) = \int_x f_Y(s - x) f_X(x) dx 
  $$

- **Extension to Multiple Random Variables**:
  $$ 
  F_{X+Y+Z} = F_{X+Y} \ast F_Z 
  $$

---

#### **Using Generating Functions**
- **Moment Generating Function (MGF)**:
  $$ 
  M_S(t) = \mathbb{E}[e^{tS}] = \int e^{ts} dF_S(s)
  $$

- **Probability Generating Function (PGF)**:
  $$ 
  Z_S(t) = \mathbb{E}[t^S] = \int t^s dF_S(s) 
  $$

- **Key Insights**:
  - There is a one-to-one correspondence between $$ F_S $$ and $$ M_S $$ or $$ Z_S $$.
  - If $$ M_S(t) $$ or $$ Z_S(t) $$ is recognized, it can identify the distribution of $$ S $$.
  - Alternatively, $$ M_S(t) $$ or $$ Z_S(t) $$ can be expanded numerically to derive moments or probabilities of $$ S $$.

---

### **2. Distribution Function of Aggregate Losses**

#### **Standard Compound Structure**
- Aggregate losses are modeled as:
  $$ 
  S = \sum_{i=1}^N X_i 
  $$
  where:
  - *$$ X_1, X_2, \dots $$* are positive, independent, and identically distributed (i.i.d.).
  - *$$ N $$* is the (integer-valued) number of claims, independent of $$ X_i $$.

---

#### **Conditioning on Claim Count $$ N $$**
- The distribution function:
  $$ 
  F_S(s) = P(S \leq s) = \sum_{n=0}^\infty P\left(\sum_{i=1}^n X_i \leq s \, \big| \, N = n \right) p_N(n)
  $$
  $$ 
  = p_N(0) + \sum_{n=1}^\infty F_X^{\ast n}(s) p_N(n) 
  $$
  where:
  - *$$ p_N(n) $$*: Probability mass function (PMF) of $$ N $$.
    - *$$ P(N=n) $$*
  - *$$ F_X^{\ast n} $$*: n-fold convolution of the distribution $$ F_X $$.
    - *$$ F_X^{\ast n} = (X_1 + X_2 + ... + X_n \leq s) $$*

---

#### **Continuous Case**
- If $$ X $$ is continuous:
  - The distribution of $$ S $$ has:
    - A **mass at 0** from $$ p_N(0) $$ (if positive).
    - A **density over $$ (0, \infty) $$** integrating to $$ 1 - p_N(0) $$.

- Summary:
  $$ 
  S \sim 
  \begin{cases} 
  P(S = 0) = p_N(0), & \text{at } 0; \\
  f_S(s) = \sum_{n=1}^\infty f_X^{\ast n}(s) p_N(n), & \text{over } (0, \infty).
  \end{cases}
  $$

---

#### **Discrete Case**

- The probability mass function:
  $$
  p_S(s) = \sum_{n=0}^\infty P\left(\sum_{i=1}^n X_i = s \, \big| \, N = n \right) p_N(n)
  $$
  $$
  = p_X^{\ast 0}(s)p_N(0) + \sum_{n=1}^\infty p_X^{\ast n}(s) p_N(n)
  $$
  where:
  - *$$ p_N(n) $$*: Probability mass function (PMF) of $$ N $$.
    - *$$ P(N=n) $$*
  - *$$ p_X^{\ast n}(s) $$*: n-fold convolution of the PMF of $$ X $$.
    - *$$ P(X_1 + X_2 + ... + X_n) = x$$*
  - *$$ p_X^{\ast 0}(s) $$*: 
    - *$$ p_X^{\ast 0}(0) = 1 $$*
    - *$$ p_X^{\ast 0}(s) = 0 $$* for $$ s > 0 $$.


- If $$ X $$ is discrete, then for $$ s = 0, 1, 2, \dots $$:
  $$ 
  S \sim 
  \begin{cases} 
  P(S = 0) = p_N(0) + \sum_{n=1}^\infty p_X^{\ast n}(0) p_N(n), & \text{at } 0; \\
  p_S(s) = \sum_{n=1}^\infty p_X^{\ast n}(s) p_N(n), & \text{for } s = 1, 2, \dots 
  \end{cases}
  $$

  where:
  $$
p_X^{\ast 0}(x) = P\left(\sum_{i=1}^0 X_i = x\right) = 
\begin{cases} 
1, & x = 0; \\
0, & x \in (0, \infty).
\end{cases}
$$


---

### **3. Compound Poisson**

#### **Aggregation**
- **Theorem**: If $$ S_1, \dots, S_n $$ are independent and follow $$ S_j \sim \text{CompPoi}(\lambda_j v_j, G_j) $$, then:
  $$
  S = \sum_{j=1}^n S_j \sim \text{CompPoi}(\lambda v, G),
  $$
  where:
  - *$$ \lambda v = \sum_{j=1}^n \lambda_j v_j $$* (total claim intensity).

  - *$$ G = \frac{\sum_{j=1}^n \lambda_j v_j G_j}{\lambda v} $$* (weighted average distribution).
  - *$$ S $$* can be represented as:
    $$
    S = \sum_{i = 1}^{N^{\ast}} Y_i, \quad \text{where } N^{\ast} \sim \text{Poi}(\lambda v), \; Y_i \overset{i.i.d.}{\sim} G.
    $$

- **Implication**:
  - Independent compound Poisson portfolios can be aggregated efficiently, resulting in a single compound Poisson process.
  - The aggregated portfolio has:
    - Total claim frequency as the sum of individual frequencies.
    - Claim size distribution as the weighted average of individual distributions.


---

### **Thinning**

- **Theorem (Wüthrich 2014)**:
  If $$ S \sim \text{CompPoi}(\lambda v, G) $$, then for disjoint subsets $$ A_k $$ of the support of $$ Y $$:

  $$
  S_k = \sum_{i=1}^N Y_i \mathbf{1}(Y_i \in A_k), \quad k = 1, \dots, n
  $$

  represents the portion of $$ S $$ corresponding to claims within $$ A_k $$.

- **Result**:
  - The components $$ S_1, \dots, S_n $$ are **independent**.
  - *$$ S_k \sim \text{CompPoi}(\lambda_k v, G_k), $$* where:
    - *$$ \lambda_k = \lambda P(Y \in A_k) $$*: 
      - The new rate $$ \lambda_k $$ adjusts the original rate $$ \lambda $$ by the probability of $$ Y $$ falling into the subset $$ A_k $$.
    - *$$ G_k(y) = P(Y \leq y \mid Y \in A_k) $$*:
      - The conditional distribution of $$ Y $$ restricted to the subset $$ A_k $$.


#### **Explanation**
- **Thinning Process**:
  - The compound Poisson process $$ S $$ is "thinned" by separating the claims into disjoint subsets $$ A_k $$.
  - Each subset contributes to a separate process $$ S_k $$.

- **Interpretation**:
  1. **Claim Allocation**:
     - The sum $$ S $$ is split based on whether individual claims $$ Y_i $$ belong to a specific subset $$ A_k $$.
     - For instance, if $$ A_k $$ corresponds to claims within a particular range of sizes, then $$ S_k $$ is the sum of claims in that range.
  2. **Independence**:
     - The thinning ensures that the processes $$ S_1, \dots, S_n $$ are independent, as each corresponds to disjoint claim subsets.
  3. **Adjusted Rate and Distribution**:
     - The new claim frequency for $$ S_k $$ is determined by the original frequency $$ \lambda $$, scaled by the probability of claims in $$ A_k $$.
     - The claim size distribution $$ G_k $$ is updated to reflect the conditional distribution of $$ Y $$ within $$ A_k $$.


#### **Use Case**:
- **Portfolio Segmentation**:
  - This theorem is useful for segmenting an insurance portfolio into independent components based on claim size, type, or other attributes.
  - Each segment can be modeled separately as a compound Poisson process, making analysis and pricing more efficient.



## **Moments of Aggregate Losses**

1. **Mean of Aggregate Losses**:
   - Expected value:
     $$
     \mathbb{E}[S] = \mathbb{E}[N] \cdot \mathbb{E}[X]
     $$
   - **Explanation**:
     - The mean of aggregate losses is the product of the expected number of claims ($$ \mathbb{E}[N] $$) and the expected size of individual claims ($$ \mathbb{E}[X] $$).

2. **Variance of Aggregate Losses**:
   - Variance:
     $$
     \text{Var}(S) = \mathbb{E}[N] \cdot \text{Var}(X) + \text{Var}(N) \cdot (\mathbb{E}[X])^2
     $$
   - **Explanation**:
     - The variance consists of:
       - The variability in claim sizes weighted by the expected number of claims.
       - The variability in the number of claims scaled by the square of the expected claim size.

---

## **Moment Generating Function (MGF)**

1. **Definition**:
   - The MGF of aggregate losses $$ S $$, denoted as $$ M_S(t) $$, is defined as:
     $$
     M_S(t) = \mathbb{E}[e^{tS}]
     $$
   - It provides a way to summarize all the moments of $$ S $$ and is useful for identifying the distribution of $$ S $$.

2. **Collective Risk Model**:
   - Aggregate losses $$ S $$ are modeled as:
     $$
     S = \sum_{i=1}^N X_i,
     $$
     where:
     - *$$ N $$* is the number of claims (random variable).
     - *$$ X_1, X_2, \dots, X_N $$* are i.i.d. claim sizes.

   - **Conditioning on $$ N $$**:
     $$
     M_S(t) = \mathbb{E}[e^{tS}] = \mathbb{E}\left[\mathbb{E}[e^{tS} \mid N]\right]
     $$
     - Given $$ N = n $$, the total $$ S $$ is the sum of $$ n $$ independent random variables $$ X_i $$.
     - The MGF of the sum of independent variables is the product of their MGFs:
       $$
       \mathbb{E}[e^{tS} \mid N = n] = \left(M_X(t)\right)^n,
       $$
       where $$ M_X(t) $$ is the MGF of a single claim $$ X $$.

   - Using the **law of total expectation**:
     $$
     M_S(t) = \mathbb{E}\left[(M_X(t))^N\right].
     $$

   - **Using the MGF of $$ N $$**:
     - Recall that for a discrete random variable $$ N $$, the MGF is:
       $$
       M_N(u) = \mathbb{E}[e^{uN}].
       $$
     - By substituting $$ u = \ln M_X(t) $$, we get:
       $$
       M_S(t) = M_N(\ln M_X(t)).
       $$

---

### **Explanation of MGF Derivation**:
- The MGF of aggregate losses $$ S $$ combines:
  - The distribution of the number of claims $$ N $$ (via $$ M_N $$).
  - The distribution of claim sizes $$ X $$ (via $$ M_X $$).
- The nested nature of the formula reflects that $$ S $$ is a compound random variable, dependent on both $$ N $$ and $$ X $$.

---

## **Probability Generating Function (PGF)**

1. **Definition**:
   - The PGF of aggregate losses $$ S $$, denoted as $$ Z_S(t) $$, is:
     $$
     Z_S(t) = \mathbb{E}[t^S].
     $$
   - It is particularly useful for discrete random variables like $$ S $$, as it directly relates to the probabilities of $$ S $$.

2. **Collective Risk Model**:
   - Aggregate losses $$ S $$ follow the same compound structure:
     $$
     S = \sum_{i=1}^N X_i.
     $$

   - **Conditioning on $$ N $$**:
     $$
     Z_S(t) = \mathbb{E}[t^S] = \mathbb{E}\left[\mathbb{E}[t^S \mid N]\right].
     $$
     - Given $$ N = n $$, the total $$ S $$ is the sum of $$ n $$ independent claims $$ X_i $$.
     - The PGF of the sum is the product of the PGFs:
       $$
       \mathbb{E}[t^S \mid N = n] = \left(Z_X(t)\right)^n,
       $$
       where $$ Z_X(t) $$ is the PGF of a single claim $$ X $$.

   - Using the **law of total expectation**:
     $$
     Z_S(t) = \mathbb{E}[Z_X(t)^N].
     $$

   - **Using the PGF of $$ N $$**:
     - Recall that for a discrete random variable $$ N $$, the PGF is:
       $$
       Z_N(u) = \mathbb{E}[u^N].
       $$
     - By substituting $$ u = Z_X(t) $$, we get:
       $$
       Z_S(t) = Z_N(Z_X(t)).
       $$

---

### **Explanation of PGF Derivation**:
- The PGF of aggregate losses $$ S $$ reflects:
  - The randomness in the claim count $$ N $$, captured via $$ Z_N $$.
  - The randomness in claim sizes $$ X $$, captured via $$ Z_X $$.
- The composition $$ Z_N(Z_X(t)) $$ shows how the distribution of $$ N $$ interacts with $$ X $$ to produce the aggregate loss distribution.

---

### **Comparison: MGF vs PGF**
| Aspect              | MGF ($$ M_S(t) $$)                       | PGF ($$ Z_S(t) $$)                      |
|---------------------|------------------------------------------|-----------------------------------------|
| Definition          | $$ M_S(t) = \mathbb{E}[e^{tS}] $$       | $$ Z_S(t) = \mathbb{E}[t^S] $$          |
| Use Case            | Works for continuous and discrete $$ S $$| Mainly for discrete $$ S $$             |
| Application         | Derives moments and approximates distributions | Derives probabilities directly          |
| Key Formula         | $$ M_S(t) = M_N(\ln M_X(t)) $$          | $$ Z_S(t) = Z_N(Z_X(t)) $$              |



## **Key Takeaways**

1. **Decomposition of Mean**:
   - The mean of aggregate losses separates into contributions from claim frequency ($$ \mathbb{E}[N] $$) and severity ($$ \mathbb{E}[X] $$).

2. **Decomposition of Variance**:
   - Total variance accounts for variability in both the number of claims and the size of claims.

3. **MGF and PGF**:
   - These functions provide tools to identify or approximate the distribution of $$ S $$ by leveraging the properties of $$ N $$ and $$ X $$.

---



### **Premium Calculation Principles**

#### **1. Expected Value Principle**
- **Definition**:
  - (According to Net Profit Condition in Module 5) The premium charged for a risk $$ S $$ should satisfy:
    $$ 
    \pi(S) > \mathbb{E}[S]
    $$ 
    to account for costs like taxes, underwriting, and profit margin.
- **Formula**:
  $$ 
  \pi(S) = (1 + \alpha) \mathbb{E}[S] 
  $$
  where:
  - *$$ \alpha > 0 $$* is a constant margin or loading factor.
- **Criticism**:
  - The premium is **not risk-sensitive**, as it is independent of the variability (or riskiness) of $$ S $$.

---

#### **2. Variance Principle**
- **Definition**:
  - The premium includes a loading based on the variance of $$ S $$:
    $$ 
    \pi(S) = \mathbb{E}[S] + \alpha \text{Var}(S)
    $$
- **Improvements**:
  - **Risk-based**: Accounts for the variability of $$ S $$, making it more reflective of the underlying risk.
- **Criticism**:
  - **Not scale-invariant**: For any $$ c > 0 $$, the property:
    $$ 
    \pi(cS) \neq c \pi(S) 
    $$
    does not hold.

---

#### **3. Standard Deviation Principle**
- **Definition**:
  - The premium includes a loading based on the standard deviation of $$ S $$:
    $$ 
    \pi(S) = \mathbb{E}[S] + \alpha \sqrt{\text{Var}(S)}
    $$
- **Improvements**:
  - **Risk-based**: Reflects variability in $$ S $$.
  - **Scale-invariant**: The property:
    $$ 
    \pi(cS) = c \pi(S)
    $$ 
    holds for any $$ c > 0 $$.
- **Criticism**:
  - **Not monotonic**: If $$ S_1 \leq S_2 $$, it does not guarantee:
    $$ 
    \pi(S_1) \leq \pi(S_2)
    $$
  - This violates a desirable property for premium-setting.



#### **Example: Non-Monotonicity in the Standard Deviation Principle**

- Consider two risks:
  - *$$ S_1 \sim \text{Uniform}(0, 1) $$*
  - *$$ S_2 = 1 $$ (constant risk)*

- Clearly, $$ S_1 \leq S_2 $$ since $$ S_1 $$ is always less than or equal to 1.

##### **Step 1: Compute the Premiums**

1. **For $$ S_1 $$**:
   - Expected value (given):
     $$
     \mathbb{E}[S_1] = \frac{1}{2}
     $$
   - Variance (given):
     $$
     \text{Var}(S_1) = \frac{1}{12}
     $$
   - Standard deviation:
     $$
     \sqrt{\text{Var}(S_1)} = \frac{1}{\sqrt{12}}
     $$
   - Premium (using the Standard Deviation Principle):
     $$
     \pi(S_1) = \mathbb{E}[S_1] + \alpha \sqrt{\text{Var}(S_1)} = \frac{1}{2} + \alpha \cdot \frac{1}{\sqrt{12}}
     $$

2. **For $$ S_2 $$**:
   - Expected value:
     $$
     \mathbb{E}[S_2] = 1
     $$
   - Variance:
     $$
     \text{Var}(S_2) = 0
     $$
   - Premium:
     $$
     \pi(S_2) = \mathbb{E}[S_2] + \alpha \sqrt{\text{Var}(S_2)} = 1
     $$

##### **Step 2: Compare the Premiums**

- Premium for $$ S_1 $$:
  $$
  \pi(S_1) = \frac{1}{2} + \frac{\alpha}{\sqrt{12}}
  $$

- Premium for $$ S_2 $$:
  $$
  \pi(S_2) = 1
  $$

- To determine when $$ \pi(S_1) > \pi(S_2) $$, solve:
  $$
  \frac{1}{2} + \frac{\alpha}{\sqrt{12}} > 1
  $$
  Simplify:
  $$
  \frac{\alpha}{\sqrt{12}} > \frac{1}{2}
  $$
  $$
  \alpha > \frac{\sqrt{12}}{2} = \sqrt{3}
  $$

##### **Conclusion**
- If $$ \alpha > \sqrt{3} $$, the premium for $$ S_1 $$ exceeds the premium for $$ S_2 $$:
  $$
  \pi(S_1) > \pi(S_2),
  $$
  even though $$ S_1 \leq S_2 $$ as a risk. This violates the principle of **monotonicity**.

---

#### **What is the Problem?**

1. **Non-Monotonicity**:
   - Monotonicity requires $$ \pi(S_1) \leq \pi(S_2) $$ if $$ S_1 \leq S_2 $$. However, in this example, the standard deviation principle fails this for $$ \alpha > \sqrt{3} $$.

2. **Cause**:
   - The premium depends on $$ \sqrt{\text{Var}(S)} $$, which can overly inflate premiums for higher variability, even with smaller expected values.

3. **Practical Issue**:
   - A smaller risk ($$ S_1 $$) may be charged a higher premium than a larger risk ($$ S_2 $$), leading to inconsistencies in pricing.

4. **Takeaway**:
   - While risk-based and scale-invariant, the standard deviation principle fails monotonicity, making it unsuitable in critical scenarios.

---

### **Summary**
1. **Expected Value Principle**: Simple but not risk-sensitive.
2. **Variance Principle**: Risk-sensitive but not scale-invariant.
3. **Standard Deviation Principle**: Risk-sensitive and scale-invariant, but not monotonic.
