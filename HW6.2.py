"""
Confidence intervals
When constructing a confidence interval, we are estimating a population parameter
based on a sample's mean and variance. We don't know if either our sample statistic
is less than, greater than, or equal to the population parameter;
or if our confidence interval contains the population parameter.

Interpreting confidence interval (from Professor Yaesoubui's lecture):
If we repeat the experiments many times to construct a very large number of independent 100(1 − 𝛼)%
confidence intervals, each based on 𝑛 observations, the proportion of these confidence
intervals that cover the unknown but true mean 𝜇 is expected to be
1 − 𝛼. We call this proportion the coverage of the confidence interval.

Interpreting the 95% confidence intervals for the expected value and the probability of the loss:
If we repeat this coin-toss simulation many times to construct a very large number of independent 95%
confidence intervals, each based on 1,000 observations, the proportion of these confidence
intervals that cover the unknown but true mean 𝜇 (of either the expected value or the probability
of loss) is expected to be 0.95.
"""
