from format_data import time_complete_a, time_complete_b, return_rate_a, return_rate_b
from abtesting import *

print("Time to complete")
print("avg time to completion of A: ", get_avg(time_complete_a))
print("avg time to completion of B: ", get_avg(time_complete_b))
print("stddev time to completion of A: ", get_stdev(time_complete_a))
print("stddev time to completion of B: ", get_stdev(time_complete_b))
print("t-score: ", get_t_score(time_complete_a, time_complete_b))
print("t-test: ", perform_2_sample_t_test(time_complete_a, time_complete_b))

print("Return rate")
observed_grid = [return_rate_a, return_rate_b]
print("A (return, no return): ", return_rate_a)
print("B (return, no return): ", return_rate_b)
print("chi2: ", chi2_value(observed_grid))
print("chi2 homogeneity test: ", perform_chi2_homogeneity_test(observed_grid))

'''
Number of users visiting version A: 26
Number of users visiting version B: 18
Number of return, no return user A:  19 7
Number of return, no return user B:  13 5

Time to complete
avg time to completion of A:  89055.84615384616
avg time to completion of B:  106769.11111111111
stddev time to completion of A:  70087.99687803458
stddev time to completion of B:  88059.36463270866
t-score:  -0.7115318865923278
t-test:  0.24103753276363715

Return rate
A (return, no return):  [19, 7]
B (return, no return):  [13, 5]
chi2:  0.003917378917378914
chi2 homogeneity test:  0.9500938144413764

Limitations
Small samples, so a few edge cases have a lot of impact
Different interest in catci
'''
