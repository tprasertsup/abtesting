from format_data import time_complete_a, time_complete_b, return_rate_a, return_rate_b
from abtesting import *

print("Time to complete")
print("t-score: ", get_t_score(time_complete_a, time_complete_b))
print("t-test: ", perform_2_sample_t_test(time_complete_a, time_complete_b))

print("Return rate")
observed_grid = [return_rate_a, return_rate_b]
print("chi2: ", chi2_value(observed_grid))
print("chi2 homogeneity test: ", perform_chi2_homogeneity_test(observed_grid))

'''
Time to complete
t-score:  -3.262761000839354
t-test:  0.0005964006277157073
Return rate
chi2:  0.044776036743856204
chi2 homogeneity test:  0.8324163867970478
'''
