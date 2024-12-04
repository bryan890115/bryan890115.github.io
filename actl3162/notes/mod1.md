---
layout: default
title: "Module 1: Fitting Loss Models"
---

# Module 1: Fitting Loss Models

## **Outline**
1. **Introduction to Aggregate Claims and Terminologies**
2. **Candidate Claim Count Distributions**:
   - Binomial Distribution
   - Poisson Distribution
   - Negative Binomial Distribution
3. **Candidate Claim Size Distributions**
4. **Data Analysis and Descriptive Statistics**
5. **Parameter Estimation**:
   - Method of Moments
   - Maximum Likelihood Estimation
6. **Model Selection**

---

## **Introduction to Aggregate Claims and Terminologies**
- **Aggregate Losses**:
  The collective risk model is represented as:
  $$ S = \sum_{i=1}^N X_i $$
  where:
  - *$$ N $$*: Number of claims (integer-valued).
  - *$$ X_i $$*: Individual payment amounts, which are i.i.d. and independent of $$ N $$.

- **Individual Risk Model**:
  If $$ N $$ is a nonrandom constant $$ n $$:
  $$ S = \sum_{i=1}^n X_i $$

- **Actuarial Terminologies**:
  - *$$ N $$*: Claim count (frequency).
  - *$$ X_i $$*: Individual claim amount (severity).
  - *$$ S $$*: Aggregate loss (total loss).

---

## **Candidate Claim Count Distributions**

### **Volume ($$ v $$)**
- **Definition**:
  - The claim count should be understood in relation to the underlying **volume**, denoted by *$$ v > 0 $$*.
  - Examples of volume include:
    - Total number of insureds.
    - Total number of policies in a portfolio.
- **In this context**:
  - *$$ v $$*: Total number of insureds.
  - *$$ N $$*: Total number of claims.
  - *$$ \frac{N}{v} $$*: Claims frequency.

---

### 1. **Binomial Distribution**
- **Parameters**:
  - *$$ v \in \mathbb{N} $$*: Volume (number of insureds).
  - *$$ p \in (0, 1) $$*: Default probability.

- **Distribution**:
  - $$ N \sim \text{Binomial}(v, p) $$
  $$
  P(N = k) = \binom{v}{k} p^k (1-p)^{v-k}, \quad k = 0, 1, \dots, v
  $$

  ***Intuition***: The sum of *$$ v $$* independent Bernoulli random variables.

- **Properties**:
  - *$$ \mathbb{E}[N] = vp $$*: Expected number of claims.
  - *$$ \text{Var}(N) = vp(1-p) $$*: Variance of the number of claims.
  - *$$ \mathbb{E}[N] > \text{Var}(N) $$*: Expected number of claims exceeds variance.

---

### 2. **Poisson Distribution**
- **Parameters**:
  - *$$ v > 0 $$*: Volume (number of insureds).
  - *$$ \lambda > 0 $$*: Expected claims frequency.

- **Distribution**:
  $$
  N \sim \text{Poisson}(\lambda v)
  $$
  $$
  P(N = k) = \frac{e^{-\lambda v} (\lambda v)^k}{k!}, \quad k = 0, 1, 2, \dots
  $$

- **Properties**:
  - *$$ \mathbb{E}[N] = \text{Var}(N) = \lambda v $$*
  - Coefficient of variation:
    $$
    \text{Vco}(N) = \frac{\sqrt{\text{Var}(N)}}{\mathbb{E}[N]} = \frac{1}{\sqrt{\lambda v}}
    $$

- **Link Between Binomial and Poisson Distributions**:
  - As *$$ v \to \infty $$* and *$$ p \to 0 $$* with *$$ vp \to \lambda $$*, the Binomial distribution converges to the Poisson distribution:
    $$
    \text{Binomial}(v, p) \to \text{Poisson}(\lambda)
    $$

---

### 3. **Negative Binomial Distribution**
- **Parameters**:
  - *$$ v > 0 $$*: Volume.
  - *$$ \lambda > 0 $$*: Expected claims frequency.
  - *$$ \gamma > 0 $$*: Dispersion parameter.

- **Distribution**:
  $$
  P(N = n) = \binom{n+\gamma-1}{n} (1-p)^\gamma p^n, \quad n = 0, 1, 2, \dots
  $$
  where:
  $$
  p = \frac{\lambda v}{\gamma + \lambda v}
  $$

- **Properties**:
  - *$$ \mathbb{E}[N] = \lambda v $$*
  - *$$ \text{Var}(N) = \lambda v \left(1 + \frac{\lambda v}{\gamma}\right) $$*
  - *$$ \text{Var}(N) > \mathbb{E}[N] $$*: Variance exceeds the mean.

---

### **Connection Between Negative Binomial and Mixed Poisson Distributions**
For $$ N $$ following a **negative binomial distribution** $$ (\gamma, p) $$, as defined earlier:
- $$ N $$ can be represented as a **mixed Poisson distribution**:
  $$
  N | \Theta \sim \text{Poisson}(\Theta \lambda v),
  $$
  where $$ \Theta \sim \text{Gamma}(\gamma, c) $$, with:
  - *$$ c = \frac{1-p}{p} $$*
  - *$$ \lambda v = p \cdot (\gamma + \lambda v) $$*.

This means the negative binomial distribution arises from a Poisson distribution with a **Gamma-distributed rate parameter**. This property highlights the flexibility of the negative binomial in modeling over-dispersed count data.

---

## **Candidate Claim Size Distributions**


### 1. **Gamma Distribution**
- **Definition**:
  $$ 
  Y \sim \Gamma(\gamma, c)
  $$

- **Density Function**:
  $$
  g(y) = \frac{c^\gamma}{\Gamma(\gamma)} y^{\gamma-1} e^{-cy}, \quad y > 0
  $$

- **Parameters**:
  - *$$ \gamma > 0 $$*: Shape parameter.
  - *$$ c > 0 $$*: Rate parameter.

- **Remarks**:
  - When *$$ \gamma = 1 $$*, it retrieves the exponential distribution.
  - The distribution has a roughly **exponential tail**.
  - **Skewness**:
    $$
    \zeta_Y = \frac{2}{\sqrt{\gamma}} > 0 \text{, positively skewed}
    $$ 

---

### 2. **Weibull Distribution**
- **Definition**:
  $$ Y \sim \text{Weibull}(\tau, c) $$

- **Density Function**:
  $$
  g(y) = (c\tau)(cy)^{\tau-1} e^{-(cy)^\tau}, \quad y > 0
  $$

- **Parameters**:
  - *$$ \tau > 0 $$*: Shape parameter.
  - *$$ c > 0 $$*: Rate parameter.

- **Distribution Function**:
  $$
  G(y) = 1 - \exp\{- (cy)^\tau\}, \quad y > 0
  $$

- **Remarks**:
  - When *$$ \tau = 1 $$*, it retrieves the exponential distribution.
  - When *$$ \tau > 1 $$*, it has a **super-exponential tail**.
  - When *$$ 0 < \tau < 1 $$*, it has a **sub-exponential tail**.

---


### 3. **Log-normal Distribution**
- **Definition**:
  $$
  Y \sim \text{LN}(\mu, \sigma^2), \quad \text{if} \quad \log Y \sim N(\mu, \sigma^2)
  $$


- **Distribution Function**:
  $$
  G(y) = \Phi\left(\frac{\log y - \mu}{\sigma}\right), \quad y > 0
  $$
  where $$ \Phi(\cdot) $$ is the standard normal cumulative distribution function (CDF).

- **Density Function**:
  $$
  g(y) = \frac{1}{\sqrt{2\pi}\sigma y} e^{-\frac{(\log y - \mu)^2}{2\sigma^2}}, \quad y > 0
  $$

- **Parameters**:
  - *$$ \mu \in \mathbb{R} $$*: Mean of *$$ \log Y $$*.
  - *$$ \sigma > 0 $$*: Standard deviation of *$$ \log Y $$*.

- **Remarks**:
  - **Intermediate tail**: Slower than an exponential tail but faster than a power tail.
  - **Skewness**:
    $$
    \zeta_Y = (e^{\sigma^2} + 2)\sqrt{e^{\sigma^2} - 1} > 0
    $$
    Log-normal distributions are positively skewed.


---

### 4. **Log-gamma Distribution**
- **Definition**:
  $$
  Y \sim \text{Log-}\Gamma(\gamma, c), \quad \text{if} \quad \log Y \sim \Gamma(\gamma, c)
  $$

- **Density Function**:
  $$
  g(y) = \frac{c^\gamma}{\Gamma(\gamma)} (\log y)^{\gamma-1} y^{-(c+1)}, \quad y > 1
  $$

- **Remarks**:
  - Has a **power-like tail** (e.g., $$ x^{-\alpha} $$ for large $$ x $$).
  - When *$$ \gamma = 1 $$*, it retrieves the **Pareto distribution**.

---

### 5. **Pareto Distribution**

- **Definition**:
  - Specifies a (large) threshold $$ \theta > 0 $$ above which it has a power tail with index $$ \alpha > 0 $$.

- **Distribution Function**:
  $$
  G(y) = 1 - \left(\frac{\theta}{y}\right)^\alpha, \quad y > \theta
  $$

- **Density Function**:
  $$
  g(y) = \frac{\alpha}{\theta} \left(\frac{\theta}{y}\right)^{\alpha+1}, \quad y > \theta
  $$

- **Alternative Pareto Type II Distribution**:
  - Another type of Pareto distribution, often used in practice:
    $$
    G(y) = 1 - \left(\frac{\theta}{y + \theta}\right)^\alpha, \quad y > 0
    $$

- **Remarks**:
  - **Power tail**: Heavy-tailed and often used for modeling large claims.
  - Versatile in describing loss distributions with significant skewness.


---


## **Data Analysis and Descriptive Statistics**

### **Graphical Approaches**
- Let $$ \{Y_1, Y_2, \dots, Y_n\} $$ be a sample from an unknown distribution $$ G $$.
- The empirical distribution function is defined as:
  $$
  \hat{G}_n(y) = \frac{1}{n} \sum_{i=1}^n \mathbf{1}\{Y_i \leq y\}
  $$
  where $$ \mathbf{1}\{\cdot\} $$ is the indicator function.

- **Fitted Distribution Function**:
  - *$$ G_0(y) $$* represents the fitted distribution function in a parametric case $$ G(y; \hat{\theta}) $$.
	
	- In the **parametric case**, the distribution $$ G(y) $$ is assumed to belong to a specific family of distributions defined by parameters $$ \theta $$, which are estimated from the data.


- **Graphical Procedures**:
  - Compare the histogram with the fitted density function $$ g_0(y) $$.
  - Compare the empirical distribution function $$ \hat{G}_n(y) $$ with $$ G_0(y) $$.
  - Use:
    - **P–P Plot**: Probability–Probability plot.
    - **Q–Q Plot**: Quantile–Quantile plot.


---

### **P–P Plot**
- A P–P plot shows how well the fitted distribution matches the empirical data by plotting cumulative probabilities against each other.
- Points falling close to the diagonal line indicate a good fit.

#### **Steps**:
1. Order the observations: $$ y_{(1)} \leq y_{(2)} \leq \dots \leq y_{(n)} $$.
2. Compute the fitted distribution at each observation:
   $$
   G_0(y_{(i)})
   $$
3. For $$ i = 1, 2, \dots, n $$, plot the points:
   $$
   \left( \frac{i - 0.5}{n}, G_0(y_{(i)}) \right)
   $$

---

### **Quantile Function**
- For a random variable $$ Y $$ with distribution function $$ G $$, the quantile function is defined as:
  $$
  G^{-1}(1 - q) = \inf \{ y : G(y) \geq q \}, \quad 0 < q < 1
  $$

- **Value at Risk (VaR)**:
  - Denoted as $$ \text{VaR}_q[Y] $$ and equivalent to the quantile function.
  - Represents the threshold such that the probability of exceeding it is $$ 1 - q $$.

---

### **Q–Q Plot**
- A Q–Q plot compares the quantiles of the empirical data and the fitted distribution.
- Points lying close to the diagonal line indicate a good match between the distributions.

#### **Steps**:
1. Order the observations: $$ y_{(1)} \leq y_{(2)} \leq \dots \leq y_{(n)} $$.
2. Calculate the quantile of the fitted distribution for each observed data point:
   $$
   G_0^{-1}\left( \frac{i - 0.5}{n} \right)
   $$
3. Plot the points:
   $$
   \left( y_{(i)}, G_0^{-1}\left(\frac{i - 0.5}{n}\right) \right)
   $$


---


## **Parameter Estimation**

### **1. Method of Moments**
- **Concept**: Estimates parameters by equating the theoretical moments to sample moments.
- **Steps**:
  1. Establish moment equations:
     $$
     \mu_1 = \mathbb{E}[X] = g_1(\theta_1, \theta_2, \dots, \theta_k), \quad \dots, \quad \mu_k = \mathbb{E}[X^k] = g_k(\theta_1, \theta_2, \dots, \theta_k)
     $$
  2. Replace theoretical moments with sample moments:
     $$
     \hat{\mu}_1 = g_1(\theta_1, \theta_2, \dots, \theta_k), \quad \dots, \quad \hat{\mu}_k = g_k(\theta_1, \theta_2, \dots, \theta_k)
     $$
  3. Solve for parameter estimates $ \hat{\theta}_1, \dots, \hat{\theta}_k $.

---

### **2. Maximum Likelihood Estimation (MLE)**
- **Concept**: Estimates parameters by maximizing the likelihood function.
- **Likelihood Function**:
  $$
  L(\theta) = \prod_{t=1}^T P(N_t = k; \theta)
  $$
- **Log-Likelihood**:
  $$
  l(\theta) = \sum_{t=1}^T \log P(N_t = k; \theta)
  $$
- Solve the equation:
  $$
  \frac{\partial l(\theta)}{\partial \theta} = 0
  $$
- **MLE Solution**:
  $$
  \hat{\theta}_{\text{MLE}} = \text{argmax}_{\theta} L(\theta) = \text{argmax}_{\theta} l(\theta)
  $$

---

### **Binomial Case**
- $ N_t \sim \text{Binomial}(v_t, p) $

- **Log-Likelihood Function**:
  $$
  l(p) = \sum_{t=1}^T \left[ \log \binom{v_t}{N_t} + N_t \log p + (v_t - N_t) \log (1 - p) \right]
  $$

- **MLE Solution**:
  $$
  \hat{p}_{\text{MLE}} = \frac{\sum_{t=1}^T N_t}{\sum_{t=1}^T v_t}
  $$

#### **Derivation**:
1. Simplify the log-likelihood function (ignoring constants):
   $$
   l(p) = \sum_{t=1}^T \left[ N_t \log p + (v_t - N_t) \log (1 - p) \right]
   $$

2. Differentiate with respect to $p$:
   $$
   \frac{\partial l(p)}{\partial p} = \sum_{t=1}^T \left[ \frac{N_t}{p} - \frac{v_t - N_t}{1-p} \right]
   $$

3. Set the derivative to zero:
   $$
   \sum_{t=1}^T \frac{N_t}{p} = \sum_{t=1}^T \frac{v_t - N_t}{1-p}
   $$

4. Solve for $p$:
   $$
   p \sum_{t=1}^T v_t = \sum_{t=1}^T N_t
   $$

5. Final MLE:
   $$
   \hat{p}_{\text{MLE}} = \frac{\sum_{t=1}^T N_t}{\sum_{t=1}^T v_t}
   $$

---

### **Poisson Case**
- $ N_t \sim \text{Poisson}(v_t \lambda) $

- **Log-Likelihood Function**:
  $$
  l(\lambda) = \sum_{t=1}^T \left[ -\lambda v_t + N_t \log (\lambda v_t) - \log (N_t!) \right]
  $$

- **MLE Solution**:
  $$
  \hat{\lambda}_{\text{MLE}} = \frac{\sum_{t=1}^T N_t}{\sum_{t=1}^T v_t}
  $$

#### **Derivation**:
1. Simplify the log-likelihood function (ignoring constants):
   $$
   l(\lambda) = \sum_{t=1}^T \left[ -\lambda v_t + N_t \log \lambda + N_t \log v_t \right]
   $$

2. Differentiate with respect to $\lambda$:
   $$
   \frac{\partial l(\lambda)}{\partial \lambda} = \sum_{t=1}^T \left[ -v_t + \frac{N_t}{\lambda} \right]
   $$

3. Set the derivative to zero:
   $$
   \sum_{t=1}^T v_t = \sum_{t=1}^T \frac{N_t}{\lambda}
   $$

4. Solve for $\lambda$:
   $$
   \lambda \sum_{t=1}^T v_t = \sum_{t=1}^T N_t
   $$

5. Final MLE:
   $$
   \hat{\lambda}_{\text{MLE}} = \frac{\sum_{t=1}^T N_t}{\sum_{t=1}^T v_t}
   $$

---

### **Grouped Data**
- Assume $n$ intervals $(c_{i-1}, c_i)$.
- Observations: $m_i$ (number of losses in $(c_{i-1}, c_i)$).
- **Likelihood Function**:
  $$
  L = \prod_{i=1}^n \left[ G(c_i) - G(c_{i-1}) \right]^{m_i}
  $$

- **Log-Likelihood Function**:
  $$
  l = \sum_{i=1}^n m_i \log \left[ G(c_i) - G(c_{i-1}) \right]
  $$


---

## **Model Selection**

### **Hypothesis Testing**
1. **Steps**:
   - State hypotheses $ H_0 \leftrightarrow H_1 $.
   - Construct a test statistic $ T_n $.
   - Determine its distribution under $ H_0 $.
   - Choose significance level $ \alpha $ (e.g., 5%).
   - Compute the observed $ T_n $ and critical value $ C $.
   - Decision:
     - Reject $ H_0 $ if $ T_n > C $.
     - Otherwise, fail to reject $ H_0 $.

2. **Errors**:
   - **Type I**: Reject $ H_0 $ when true.
   - **Type II**: Fail to reject $ H_0 $ when false.

---

### **Goodness-of-Fit Tests**
1. **Kolmogorov–Smirnov (K–S) Test**:
   - **Statistic**:
     $$
     D_n = \sup_y | \hat{G}_n(y) - G_0(y) |
     $$
   - Convergence under $ H_0 $:
     $$
     \sqrt{n} D_n \xrightarrow{d} K
     $$
   - Reject $ H_0 $ if:
     $$
     D_n > \frac{K^{-1}(1 - \alpha)}{\sqrt{n}}
     $$

    note: not work for grouped data

2. **Anderson–Darling (A–D) Test**:
   - **Statistic**:
     $$
     A_n = n \int \frac{\left[ \hat{G}_n(y) - G_0(y) \right]^2}{G_0(y)(1 - G_0(y))} \, dG_0(y)
     $$

    note: not work for grouped data


3. **$ \chi^2 $ Test**:
   - Partition data into $ K $ intervals:
     $$
     \chi^2_{n,K} = \sum_{k=1}^K \frac{(E_k - O_k)^2}{E_k}
     $$
   - Distribution:
     $$
     \chi^2_{n,K} \xrightarrow{d} \chi^2_{K-1-d}
     $$


### **Comparison of Goodness-of-Fit Tests**

1. **Kolmogorov–Smirnov (K-S) Test**:
   - Measures the maximum absolute difference between the empirical and model distribution functions.
   - Emphasizes overall fit but does not prioritize specific regions like the tails.

2. **Anderson–Darling (A-D) Test**:
   - Measures the squared difference between the empirical and model distribution functions.
   - Weighted average with greater emphasis on the tails compared to the K-S test.

3. **Chi-Square ($\chi^2$) Test**:
   - Compares the observed and expected frequencies across intervals of the data range.
   - Adjusts the degrees of freedom to account for the number of parameters estimated in the model.

---

#### **Key Comparisons**:
- **Focus**:
  - K-S focuses on absolute differences.
  - A-D gives more importance to the tails.
  - $\chi^2$ evaluates differences over defined intervals.

- **Model Complexity**:
  - K-S and A-D tests do not adjust for the increase in parameters, often favoring more complex models.
  - $\chi^2$ adjusts degrees of freedom for the number of parameters, penalizing over-complexity.

- **Sample Size**:
  - Larger samples increase the likelihood of rejecting all models for both K-S and A-D tests.
  - $\chi^2$ can handle larger samples better by considering parameter estimation.



---

### **Information Criteria**
1. **Akaike Information Criterion (AIC)**:
   $$
   AIC = -2\hat{\ell} + 2d
   $$
2. **Bayesian Information Criterion (BIC)**:
   $$
   BIC = -2\hat{\ell} + \log(n)d
   $$

  remarks:
  - Smaller AIC, BIC $$ \to $$ the better
  - BIC penalise number of paramers (d) more strongly by $$ \log{n} $$ for large $$ n $$. 


---
