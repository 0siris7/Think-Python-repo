from statistics import mean
from scipy import stats

estimates = [1000,34534,211,777,1,6,3,777888,123,456]

estimates.sort()
"""
tv = int(0.1 * len(estimates))

estimates = estimates[tv:]
estimates = estimates[:len(estimates) - tv]
print(mean(estimates))
"""

#or



m = stats.trim_mean(estimates, 0.1)
print(m)
