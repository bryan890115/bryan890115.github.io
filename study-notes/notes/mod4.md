---
layout: default
title: "Module 4: Approximations for Compound Distributions"
---



# **Approximations for Compound Distributions**

## **Outline**
1. **Approximations using Central Limit Theorem**:
   - Introduction
   - Approximations assuming a symmetrical distribution
   - Approximations allowing for skewness
   - Approximating the IRM by the CRM
2. **Recursion**:
   - The (a, b) family
   - Panjer’s recursion algorithm

---

## **Approximations Using Central Limit Theorem**

### **Compound Distribution**
The total claim amount $$ S $$ is given by the following compound distribution:
$$
S = \sum_{i=1}^N Y_i,
$$
where:
- *$$ N $$*: Nonnegative and integer-valued random variable (number of claims).
- *$$ Y_1, Y_2, \dots $$*: i.i.d. nonnegative random variables (claim sizes) with common distribution $$ G $$.
- *$$ N $$* and $$ Y_i $$ are independent.

### **Why Approximations?**
- Calculating the exact distribution of $$ S $$ is complex due to repeated convolutions.
- Models are prone to inaccuracies due to limited data availability.
- Approximations provide a practical alternative for estimating $$ S $$.

---

### **CLT Approximation (Symmetrical Distribution)**
- Assume $$ S \sim \text{CompPoi}(\lambda v, G) $$, where $$ G $$ has a finite second moment.
- By the Central Limit Theorem (CLT):
    $$
    F_S(s) = P(S \leq s) = P\left(\frac{S - \mathbb{E}[S]}{\sqrt{\text{Var}(S)}} \leq \frac{s - \mathbb{E}[S]}{\sqrt{\text{Var}(S)}}\right) 
    $$
    $$
    \approx P\left(Z \leq \frac{s - \mathbb{E}[S]}{\sqrt{\text{Var}(S)}}\right) 
    = \Phi\left(\frac{s - \mathbb{E}[S]}{\sqrt{\text{Var}(S)}}\right),
    $$

  where:
  - *$$ \Phi(\cdot) $$*: CDF of the standard normal distribution.
  - *$$ \mathbb{E}[S] $$* and $$ \text{Var}(S) $$: Mean and variance of $$ S $$.

#### **When Does It Work Well?**
- *$$ v $$* (frequency) is large.
- *$$ G $$* is not heavy-tailed.

#### **Limitations**
- The normal approximation performs poorly under the following conditions:
  - **Individual Model**: When $$ n $$ (number of components) is small.
  - **Collective Model**:
    - When $$ \lambda $$ (rate parameter in compound Poisson) is small.
    - When $$ r $$ (number of successes in compound negative binomial) is small.
  - **Distribution Skewness**: When $$ G $$ is highly skewed.


---

### **NP2 Approximation (Allowing for Skewness)**
- Incorporates skewness $$ \gamma_1 $$ into the CLT approximation:
  $$
  F_S(s) \approx \Phi(s),
  $$
  where:
  - $$ s = \sqrt{\frac{9}{\gamma_1 ^2} + \frac{6x}{\gamma_1} + 1 } - \frac{3}{\gamma_1} , \quad x = s + \frac{\gamma_1}{6}(s^2 - 1). $$
  - Skewness $$ \gamma_1 $$ is given by:
    $$
    \gamma_1 = \frac{\mathbb{E}[(S - \mathbb{E}[S])^3]}{\text{Var}(S)^{3/2}}.
    $$

#### **When to Use?**
- Effective for values $$ x > \mathbb{E}[S] + \sqrt{\text{Var}(S)} $$.
- Accounts for the skewness often seen in insurance data, improving accuracy in cases where the distribution is not symmetric.



## **Example: Approximation NP2**

### **Key Idea**

The goal is to refine the Central Limit Theorem (CLT) approximation by accounting for skewness $$ \gamma_1 $$ in the distribution of aggregate losses $$ S $$.

1. **Standardized Approximation**:
   - Standardize the aggregate losses:
     $$
     \tilde{S} = \frac{S - \mathbb{E}[S]}{\sqrt{\text{Var}(S)}} \approx Z + \frac{\gamma_1}{6}(Z^2 - 1),
     $$
     where:
     - *$$ Z \sim \text{Normal}(0, 1) $$*.
     - The skewness adjustment term $$ \frac{\gamma_1}{6}(Z^2 - 1) $$ captures the asymmetry of the distribution.

2. **Key Checks for Moments**:
   - To validate this approximation, we check the moments of the left-hand side (LHS) and right-hand side (RHS) for $$ k = 1, 2, 3 $$:
     - **For $$ k = 1 $$ (Mean)**:
       - *$$ \mathbb{E}[\text{LHS}] = 0 $$*.
       - *$$ \mathbb{E}[\text{RHS}] = 0 $$*.
       - These match perfectly.
     - **For $$ k = 2 $$ (Variance)**:
       - *$$ \mathbb{E}[\text{LHS}^2] \approx 1 $$*.
       - *$$ \mathbb{E}[\text{RHS}^2] \approx 1 + \frac{\gamma_1^2}{36} $$*.
       - The variance is slightly adjusted due to the skewness term.
     - **For $$ k = 3 $$ (Skewness)**:
       - *$$ \mathbb{E}[\text{LHS}^3] \approx \gamma_1 $$*.
       - *$$ \mathbb{E}[\text{RHS}^3] \approx \gamma_1 + \frac{\gamma_1^3}{27} $$*.
       - The skewness approximation is accurate for small $$ \gamma_1 $$.

3. **Bounds for $$ Z $$**

   #### 3.1 **Approximating $$ P(\tilde{S} \leq s) $$**
   - When incorporating skewness $$ \gamma_1 $$ into the approximation, we have:
     $$
     P\left(\tilde{S} \leq s\right) = P\left(Z + \frac{\gamma_1}{6}(Z^2 - 1) \leq s\right),
     $$
     where:
     - *$$ Z \sim \text{Normal}(0, 1) $$*.
     - *$$ \frac{\gamma_1}{6}(Z^2 - 1) $$* is the skewness adjustment term.

   #### 3.2 **Why Bounds are Needed**
   - Unlike the standard normal CLT approximation, the inclusion of $$ \frac{\gamma_1}{6}(Z^2 - 1) $$ introduces a **non-linear transformation**.
   - To approximate this probability:
     - We need to determine the range of $$ Z $$ (denoted by $$ s_- $$ and $$ s_+ $$) where this condition holds.

   #### 3.3 **Deriving the Bounds $$ s_- $$ and $$ s_+ $$**
   - Rearrange the inequality:
     $$
     Z + \frac{\gamma_1}{6}(Z^2 - 1) \leq s.
     $$
   - Multiply both sides by 6 to eliminate fractions:
     $$
     6Z + \gamma_1(Z^2 - 1) \leq 6s.
     $$
   - Bring all terms to one side:
     $$
     \gamma_1 Z^2 + 6Z - \gamma_1 - 6s \leq 0.
     $$
   - This is a quadratic in $$ Z $$:
     $$
     \gamma_1 Z^2 + 6Z - (\gamma_1 + 6s) = 0.
     $$
   - Solve for $$ Z $$ using the quadratic formula:
     $$
     Z = \frac{-6 \pm \sqrt{36 + 4\gamma_1(\gamma_1 + 6s)}}{2\gamma_1}.
     $$
     - Simplify:
       $$
       Z = -\frac{3}{\gamma_1} \pm \sqrt{\frac{9}{\gamma_1 ^2} + \frac{6x}{\gamma_1} + 1 }.
       $$

   #### 3.4 **Interpreting $$ s_- $$ and $$ s_+ $$**
   - The solutions represent the bounds:
     $$
     s_- = -\frac{3}{\gamma_1} - \sqrt{\frac{9}{\gamma_1 ^2} + \frac{6x}{\gamma_1} + 1 }, \quad s_+ = -\frac{3}{\gamma_1} + \sqrt{\frac{9}{\gamma_1 ^2} + \frac{6x}{\gamma_1} + 1 }.
     $$
   - These bounds define the adjusted range of $$ Z $$ that satisfies the inequality, incorporating skewness.
   - The probability is then:
     $$
     P\left(Z + \frac{\gamma_1}{6}(Z^2 - 1) \leq s\right) = P(s_- \leq Z \leq s_+).
     $$



### **Summary**
- This approach incorporates skewness $$ \gamma_1 $$ to refine the normal approximation of aggregate losses.
- For small values of $$ \gamma_1 $$ (low skewness), the approximation is effective, and moments align well between LHS and RHS.
- The bounds $$ s_- $$ and $$ s_+ $$ illustrate how skewness shifts the range of $$ Z $$, improving accuracy for skewed data.
- This provides a more accurate representation of the distribution, particularly for skewed data.


---

## **Approximating IRM by CRM**

 **Individual Risk Model (IRM)**
- **Definition**:
  $$ 
  \tilde{S} = \sum_{i=1}^n I_i b_i 
  $$
  - *$$ I_i $$*: Indicator variable for policy $$ i $$ with:
    $$ 
    P(I_i = 1) = q_i, \quad P(I_i = 0) = 1 - q_i.
    $$
  - *$$ b_i $$*: Claim size for policy $$ i $$.
  
- **Characteristics**:
  - Models claims at an individual level.
  - Probability $$ q_i $$ determines if a claim occurs for policy $$ i $$.


**Collective Risk Model (CRM)**
- **Definition**:
  $$ 
  S = \sum_{i=1}^n N_i b_i
  $$
  - *$$ N_i \sim \text{Poisson}(\lambda_i) $$*: Number of claims for policy $$ i $$.
  - *$$ b_i $$*: Claim size for policy $$ i $$.

- **Characteristics**:
  - Models aggregate claims by assuming a compound Poisson process.
  - *$$ \lambda_i $$* reflects the expected number of claims.

---

### **Relationship Between IRM and CRM**
- The aggregate loss $$ S $$ in CRM can approximate $$ \tilde{S} $$ in IRM:
  $$ 
  \tilde{S} = \sum_{i=1}^n I_i b_i \approx \sum_{i=1}^n N_i b_i = S.
  $$

- **Distributions**:
  - *$$ I_i $$* in IRM is replaced by $$ N_i \sim \text{Poisson}(\lambda_i) $$ in CRM.

---

### **The Distribution of Aggregate Losses**

#### **Compound Poisson Representation**
- In CRM:
  $$ 
  S = \sum_{i=1}^n S_i, \quad S_i \sim \text{CompPoi}(\lambda_i, G_i),
  $$
  where:
  - *$$ G_i(x) = \mathbb{1}[b_i, \infty)(x) $$*: Indicator distribution for $$ b_i $$.
  - $$ \lambda = \sum_{i=1}^n \lambda_i, \quad G(x) = \frac{\sum_{i=1}^n \lambda_i G_i(x)}{\lambda}. $$

**Key Points**:
1. The sum of independent compound Poisson distributions remains a compound Poisson.
2. Parameters:
   - Total intensity: $$ \lambda = \sum \lambda_i $$.
   - Weighted distribution: $$ G(x) $$.

---

### **Approximations of IRM by CRM**

#### **Expected Value and Variance**
- **IRM**:
  $$ 
  \mathbb{E}[\tilde{S}] = \sum_{i=1}^n q_i b_i, \quad \text{Var}(\tilde{S}) = \sum_{i=1}^n q_i (1 - q_i) b_i^2.
  $$
- **CRM**:
  $$ 
  \mathbb{E}[S] = \sum_{i=1}^n \lambda_i b_i, \quad \text{Var}(S) = \sum_{i=1}^n \lambda_i b_i^2.
  $$

#### **Choices for $$ \lambda_i $$**
1. **$$ \lambda_i = q_i $$**:
   - Matches the expected number of claims:
     $$ 
     \mathbb{E}[\tilde{S}] = \mathbb{E}[S].
     $$
   - *$$ \text{Var}(\tilde{S}) < \text{Var}(S). $$*

2. **$$ \lambda_i = -\ln(1 - q_i) $$**:
   - Matches the probability of no claims:
     $$ 
     P[S = 0] = P[\tilde{S} = 0].
     $$
   - *$$ \mathbb{E}[\tilde{S}] < \mathbb{E}[S], \quad \text{Var}(\tilde{S}) < \text{Var}(S). $$*



---




## **Recursion**

### **The (a, b) Family**
For a nonnegative integer-valued random variable $$ N $$ with probability function $$ p_n = P(N = n) $$:
$$
p_n = \left(a + \frac{b}{n}\right)p_{n-1}, \quad n \geq 1,
$$
with initial value $$ p_0 $$.

#### **Examples**:
| Distribution      | $$ a $$    | $$ b $$               | $$ p_0 $$                |
|-------------------|------------|-----------------------|--------------------------|
| Poisson($$ \lambda $$) | $$ 0 $$    | $$ \lambda $$         | $$ e^{-\lambda} $$       |
| Neg Bin($$ r, p $$) | $$ 1 - p $$ | $$ (r-1)(1-p) $$       | $$ p^r $$                |
| Binomial($$ m, p $$) | $$ -\frac{p}{1-p} $$ | $$ (m+1)\frac{p}{1-p} $$ | $$ (1-p)^m $$ |

---

### **Panjer's Recursion Algorithm**

#### **General Formula**:
For $$ S = \sum_{j=1}^N Y_j $$, with:
- *$$ N $$*: Panjer distribution ($$ a, b $$).
- *$$ Y $$*: Discrete with PMF $$ g_m = P(Y = m) $$.

Recursive formula:
$$
f_r = 
\begin{cases} 
p_0, & \text{if } r = 0, \\ 
\sum_{k=1}^r \left(a + \frac{b \cdot k}{r}\right) g_k f_{r-k}, & \text{if } r \geq 1.
\end{cases}
$$

#### **Special Case: Compound Poisson**
When $$ N \sim \text{Poisson}(\lambda) $$:
$$
f_r = 
\begin{cases} 
e^{-\lambda}, & \text{if } r = 0, \\ 
\frac{\lambda}{r} \sum_{k=1}^r k g_k f_{r-k}, & \text{if } r \geq 1.
\end{cases}
$$

---

### **Properties and Applications**
1. **Key Properties**:
   - The algorithm is **stable** for:
     - *$$ N \sim \text{Poisson} $$*.
     - *$$ N \sim \text{Negative Binomial} $$*.
   - It is **less stable** for $$ N \sim \text{Binomial} $$.
   - Discretization is required for continuous distributions $$ G $$.

2. **Use Cases**:
   - Efficient calculation of aggregate claims distributions when $$ Y $$ is discrete.
   - Useful for models where $$ N $$ follows distributions in the (a, b) family.

3. **Extensions**:
   - For continuous $$ Y $$, approximate $$ G $$ using discretization methods to apply Panjer's recursion.

4. **Benefits**:
   - Avoids direct convolution for calculating $$ S $$.
   - Recursively builds the probabilities $$ f_r $$.

5. **Limitations**:
   - Sensitive to choice of distribution for $$ N $$ and $$ G $$.
   - Approximation accuracy decreases with increasing complexity in $$ G $$.


---

## **Key Takeaways**
- **Approximations**:
  - CLT is effective for large $$ v $$ and symmetrical $$ G $$.
  - NP2 incorporates skewness for more accurate results.
- **CRM Approximation**:
  - Effective alternative to IRM, with manageable parameters.
- **Panjer's Recursion**:
  - Efficient method for calculating aggregate loss distributions for discrete $$ Y $$. Stable for Poisson and Negative Binomial $$ N $$.
