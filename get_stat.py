from format_data import time_complete_a, time_complete_b, return_rate_a, return_rate_b
from abtesting import *

print("Time to complete")
print("avg time to completion of A: ", get_avg(time_complete_a))
print("avg time to completion of B: ", get_avg(time_complete_b))
print("t-score: ", get_t_score(time_complete_a, time_complete_b))
print("t-test: ", perform_2_sample_t_test(time_complete_a, time_complete_b))

print("Return rate")
observed_grid = [return_rate_a, return_rate_b]
print("A (return, no return): ", return_rate_a)
print("B (return, no return): ", return_rate_b)
print("chi2: ", chi2_value(observed_grid))
print("chi2 homogeneity test: ", perform_chi2_homogeneity_test(observed_grid))

'''
Time to complete
avg time to completion of A:  22382.411003236244
avg time to completion of B:  18007.76371308017
t-score:  -3.262761000839354
t-test:  0.0005964006277157073
p-value < 0.05 -> statistically significant 
The users use less time to complete in the design B.

Return rate
A (return, no return):  [19, 13]
B (return, no return):  [13, 10]
chi2:  0.044776036743856204
chi2 homogeneity test:  0.8324163867970478
p-value > 0.05 -> statistically insignificant 
There is no difference in return rate between design A and B.

Limitations
Small samples
Different interest in catci
'''
