---
layout: default
title: "Module 2: Individual Claim Size Modeling"
---

# **Module 2: Individual Claim Size Modeling**

---

## **Outline**
1. **Incomplete Data**:
   - Left-Truncation and Right-Censoring
   - Handling Zero Claims
2. **Coverage Modifications and Reinsurance**:
   - Deductible and Policy Limit
   - Proportional and Non-Proportional Reinsurance
3. **Key Identities and Premium Calculations**:
   - Useful Identity
   - Excess of Loss Premium (Continuous and Discrete Cases)
4. **Example**:
   - Excess of Loss Premium for Exponential Distribution
5. **Likelihood for Right-Censored Data**

---

## **Incomplete Data**
1. **Complete vs. Incomplete Data**:
   - **Complete Data**: Exact values for all observations are available.
   - **Incomplete Data**:
     - Data may be grouped.
     - **Truncation**: Observations below a threshold are not recorded.
     - **Censoring**: Observations above a threshold are limited to a maximum value.

2. **Left-Truncation and Right-Censoring**:
   - **Left-Truncation** at threshold $$ d $$:
     - Values below $$ d $$ are not recorded.
     - Values above $$ d $$ are recorded exactly.
   - **Right-Censoring** at threshold $$ l $$:
     - Values below $$ l $$ are recorded as observed.
     - Values above $$ l $$ are recorded as $$ l $$.
   - Observations may exhibit **both** truncation and censoring.

3. **Zero Claims**:
   - Common when:
     - Final claims do not exceed the deductible.
     - Insurers are not liable for the claim.
     - The insured withdraws the claim.
   - **Handling Zero Claims (assuming a compound Poisson structure)**:
     - Estimate the proportion of zero claims and adjust the distribution $$ G(y) $$ by adding a probability mass at $$ 0 $$. 
        - adding a spike (a probability mass) at $$ 0 $$ in the claim size distribution $$ G(y) $$, the distribution captures the high frequency of zero claims accurately
     - Reduce the expected claim frequency ($$ \lambda $$) to exclude zero claims.

---

## **Coverage Modifications and Reinsurance**

1. **Deductible and Policy Limit**:
   - **Deductible ($$ d > 0 $$)**:
     - The insurer pays claim amounts exceeding $$ d $$.
   - **Policy Limit ($$ l > 0 $$)**:
     - The insurer pays claims up to $$ l $$.
   - Liability for a claim size $$ Y $$:
     $$ 
     \text{Liability} = \min[\max(Y - d, 0), l] 
     $$

2. **Reinsurance**:
   - **Purpose**: Transfers part of the risk from a primary insurer to a reinsurer.
   - Modern financial instruments include catastrophe bonds and insurance-linked securities (ILS).

3. **Proportional Reinsurance**:
   - **Quota Share**: A fixed proportion ($$ \alpha $$) applies to individual claims.
     - Insurer's payment: $$ Y_I = \alpha Y $$
     - Reinsurer's payment: $$ Y_R = (1 - \alpha) Y $$
   - **Surplus Share**: The proportion applies to aggregate claims.
     - Insurer's payment: $$ S_I = \alpha S $$
     - Reinsurer's payment: $$ S_R = (1 - \alpha) S $$

4. **Non-Proportional Reinsurance**:
   - **Excess of Loss (Individual Claims)**:
     - Insurer's payment: $$ Y_I = \min(Y, d) $$
     - Reinsurer's payment: $$ Y_R = \max(Y - d, 0) $$
   - **Stop Loss (Aggregate Claims)**:
     - Insurer's payment: $$ S_I = \min(S, d) $$
     - Reinsurer's payment: $$ S_R = \max(S - d, 0) $$

---

## **Key Identities and Premium Calculations**

1. **Useful Identity**:
$$
(Y \wedge d) + \max(Y - d, 0) = Y
$$ 

- Explanation:
    - *$$ Y \wedge d $$*: The part of $$ Y $$ capped at $$ d $$ (**truncated component**).
    - *$$ \max(Y - d, 0) $$*: The part of $$ Y $$ exceeding $$ d $$ (**excess component**).

- These two components sum to $$ Y $$:
    - If *$$ Y \leq d $$*: 
        - *$$ Y \wedge d = Y $$*
        - *$$ \max(Y - d, 0) = 0 $$*
        - so $$ Y \wedge d + \max(Y - d, 0) = Y $$.
    - If *$$ Y > d $$*: 
        - *$$ Y \wedge d = d $$*
        - *$$ \max(Y - d, 0) = Y - d $$*
        - so $$ d + (Y - d) = Y $$.

- Taking expectations:
    $$
    \mathbb{E}[Y \wedge d] = \mathbb{E}[Y] - \mathbb{E}[\max(Y - d, 0)]
    $$
    - **Insurer**:
        - *$$ \mathbb{E}[Y \wedge d] $$*: Expected value of $$ Y $$ capped at $$ d $$ (amount retained by the insurer).
    - **Reinsurer**: 
        - *$$ \mathbb{E}[\max(Y - d, 0)] $$*: Expected value of the excess beyond $$ d $$ (amount covered by the reinsurer).
    - **Loss**:
        - *$$ \mathbb{E}[Y] $$*: Total expected loss (sum of the insurer’s and reinsurer’s shares).


## 2. **Excess of Loss Premium**
   - For a non-negative loss $$ Y $$ with distribution $$ G(y) $$:

     - **Continuous Case**:
       $$ 
       \mathbb{E}[\max(Y - d, 0)] = \int_d^\infty (1 - G(y)) \, dy 
       $$
       - **Derivation**:
         - Start with the definition:
           $$ 
           \mathbb{E}[\max(Y - d, 0)] = \int_d^\infty (y - d) g(y) \, dy 
           $$
         - Apply **integration by parts**:
           $$ 
           \int u \, dv = uv - \int v \, du 
           $$
         - Let:
           - *$$ u = y - d $$*, so $$ du = dy $$
           - *$$ dv = g(y) \, dy $$*, so $$ v = 1 - G(y) $$
         - Substitute into the formula:
           $$ 
           \mathbb{E}[\max(Y - d, 0)] = \left[(y - d)(1 - G(y))\right]_d^\infty - \int_d^\infty (1 - G(y)) \, dy
           $$
         - Simplify:
           - As $$ y \to \infty $$, $$ (y - d)(1 - G(y)) \to 0 $$ (assuming $$ G(y) \to 1 $$ as $$ y \to \infty $$).
           - At $$ y = d $$, $$ (d - d)(1 - G(d)) = 0 $$.
         - Final result:
           $$ 
           \mathbb{E}[\max(Y - d, 0)] = \int_d^\infty (1 - G(y)) \, dy 
           $$

     - **Discrete Case**:
       $$ 
       \mathbb{E}[\max(Y - d, 0)] = \sum_{y = d}^\infty (1 - G(y)) 
       $$
       - **Derivation**:
         - Start with the definition:
           $$ 
           \mathbb{E}[\max(Y - d, 0)] = \sum_{y = d}^\infty (y - d) P(Y = y) 
           $$
         - Express the probability $$ P(Y = y) $$ in terms of the cumulative distribution:
           $$ 
           P(Y = y) = G(y) - G(y-1)
           $$
         - Substitute into the summation:
           $$ 
           \mathbb{E}[\max(Y - d, 0)] = \sum_{y = d}^\infty (1 - G(y)) 
           $$
         - Intuition:
           - For each $$ y \geq d $$, the term $$ (1 - G(y)) $$ represents the cumulative probability that the loss $$ Y $$ exceeds $$ y $$.
           - The summation accounts for the contributions from all excess amounts beyond $$ d $$.



---

## **Example**
- **Exponential Distribution ($$ Y \sim \text{Exp}(\lambda) $$)**:
  - The cumulative distribution function (CDF) is:
    $$
    G(y) = 1 - e^{-\lambda y}, \quad y \geq 0
    $$
  - The probability density function (PDF) is:
    $$
    g(y) = \lambda e^{-\lambda y}, \quad y \geq 0
    $$

### **Method 1: Using the Integral Formula**
- The formula for excess of loss is:
  $$
  \mathbb{E}[\max(Y - d, 0)] = \int_d^\infty (1 - G(y)) \, dy
  $$
- Substitute $$ 1 - G(y) = e^{-\lambda y} $$:
  $$
  \mathbb{E}[\max(Y - d, 0)] = \int_d^\infty e^{-\lambda y} \, dy
  $$
- Evaluate the integral:
  $$
  \int e^{-\lambda y} \, dy = \frac{-1}{\lambda} e^{-\lambda y}
  $$
- Apply the bounds:
  $$
  \mathbb{E}[\max(Y - d, 0)] = \left[ \frac{-1}{\lambda} e^{-\lambda y} \right]_d^\infty = \frac{1}{\lambda} e^{-\lambda d}
  $$

---

### **Method 2: Using Probability and Conditional Expectation**
- Decompose the expectation using the **Law of Total Expectation**:
  $$ 
  \mathbb{E}[X] = \mathbb{E}[\mathbb{E}[X \mid A]]
  $$
  - Here, $$ A $$ is the event $$ Y > d $$ (i.e., exceeding the deductible $$ d $$).
  - Applying this to $$ \mathbb{E}[\max(Y - d, 0)] $$, we get:
    $$
    \mathbb{E}[\max(Y - d, 0)] = P(Y > d) \cdot \mathbb{E}[Y - d \mid Y > d]
    $$

- **Step 1: Compute $$ P(Y > d) $$**:
  - The probability of exceeding the deductible is:
    $$
    P(Y > d) = 1 - G(d) = e^{-\lambda d}
    $$

- **Step 2: Compute $$ \mathbb{E}[Y - d \mid Y > d] $$**:
  - Given that $$ Y > d $$, the conditional distribution of $$ Y $$ shifts by $$ d $$ and remains exponential. For the exponential distribution:
    $$
    \mathbb{E}[Y - d \mid Y > d] = \frac{1}{\lambda}
    $$

- Combine the results:
  - Substituting $$ P(Y > d) $$ and $$ \mathbb{E}[Y - d \mid Y > d] $$:
    $$
    \mathbb{E}[\max(Y - d, 0)] = e^{-\lambda d} \cdot \frac{1}{\lambda} = \frac{1}{\lambda} e^{-\lambda d}
    $$

---

### **Explanation of Method 2**
- **Decompose the Expectation**:
  - The expectation is split into two parts:
    1. The probability that the deductible is exceeded: $$ P(Y > d) $$.
    2. The expected amount of loss above the deductible: $$ \mathbb{E}[Y - d \mid Y > d] $$.
  - The **Law of Total Expectation** ensures that the product of these two quantities gives the total contribution of excess loss.
  
- **Key Components**:
  - $$ P(Y > d) $$: Represents the **frequency** of losses exceeding the deductible $$ d $$.
  - $$ \mathbb{E}[Y - d \mid Y > d] $$: Represents the **severity** of losses above the deductible.

- By multiplying these terms, this method provides a clear and intuitive breakdown of excess loss into its frequency and severity components.

---


## **Proportional (Quota Share) Premium**

For proportional reinsurance, the reinsurer and insurer share claims in a fixed proportion, denoted by $$ \alpha $$ (reinsurer's share) and $$ 1 - \alpha $$ (insurer's share).

### **Premium Formula**
The net premium under a proportional reinsurance arrangement is a fraction of the total premium based on the reinsurer's share:
$$
\text{Net Premium (Reinsurer)} = \alpha \cdot \mathbb{E}[Y]
$$
where:
- *$$ Y $$*: The loss random variable.
- *$$ \mathbb{E}[Y] $$*: The expected value of the claim size.

---

## **Example**
- **Exponential Distribution ($$ Y \sim \text{Exp}(\lambda) $$)**:
  - The cumulative distribution function (CDF) is:
    $$
    G(y) = 1 - e^{-\lambda y}, \quad y \geq 0
    $$
  - The probability density function (PDF) is:
    $$
    g(y) = \lambda e^{-\lambda y}, \quad y \geq 0
    $$

### **Step 1: Compute Total Expected Value**
- The expected value of $$ Y $$ for an exponential distribution is:
  $$
  \mathbb{E}[Y] = \frac{1}{\lambda}
  $$

### **Step 2: Reinsurer's Premium**
- Using the proportional formula:
  $$
  \text{Net Premium (Reinsurer)} = \alpha \cdot \mathbb{E}[Y]
  $$
  Substituting:
  $$
  \text{Net Premium (Reinsurer)} = \alpha \cdot \frac{1}{\lambda}
  $$

### **Step 3: Insurer's Premium**
- The insurer's premium is the remaining share of the total premium:
  $$
  \text{Net Premium (Insurer)} = (1 - \alpha) \cdot \mathbb{E}[Y]
  $$
  Substituting:
  $$
  \text{Net Premium (Insurer)} = (1 - \alpha) \cdot \frac{1}{\lambda}
  $$

---

### **Explanation**
- **Sharing Mechanism**:
  - Each individual claim is split proportionally between the insurer and reinsurer.
  - For a claim $$ Y $$:
    - Reinsurer pays: $$ \alpha Y $$
    - Insurer pays: $$ (1 - \alpha) Y $$

- **Key Insights**:
  - Proportional premiums simplify risk-sharing by maintaining the same proportional split across all claims.
  - The reinsurer’s premium reflects their proportion $$ \alpha $$ of the total expected claim value, while the insurer retains $$ 1 - \alpha $$ of the premium.


