from scipy import stats
from scipy.stats import t as t_dist
from scipy.stats import chi2

from abtesting_test import *

'''
# You can comment out these lines! They are just here to help follow along to the tutorial.
print(t_dist.cdf(-2, 20))  # should print .02963
# positive t-score (bad), should print .97036 (= 1 - .2963)
print(t_dist.cdf(2, 20))

print(chi2.cdf(23.6, 12))  # prints 0.976
print(1 - chi2.cdf(23.6, 12))  # prints 1 - 0.976 = 0.023 (yay!)
'''

# TODO: Fill in the following functions! Be sure to delete "pass" when you want to use/run a function!
# NOTE: You should not be using any outside libraries or functions other than the simple operators (+, **, etc)
# and the specifically mentioned functions (i.e. round, cdf functions...)


def slice_2D(list_2D, start_row, end_row, start_col, end_col):
    '''
    Splices a the 2D list via start_row:end_row and start_col:end_col
    :param list: list of list of numbers
    :param nums: start_row, end_row, start_col, end_col
    :return: the spliced 2D list (ending indices are exclsive)
    '''
    to_append = []
    for l in range(start_row, end_row):
        to_append.append(list_2D[l][start_col:end_col])

    return to_append


def get_avg(nums):
    '''
    Helper function for calculating the average of a sample.
    :param nums: list of numbers
    :return: average of list
    '''
    # TODO: fill me in!
    return sum(nums)/len(nums)


def get_stdev(nums):
    '''
    Helper function for calculating the standard deviation of a sample.
    :param nums: list of numbers
    :return: standard deviation of list
    '''
    # TODO: fill me in!
    mean = get_avg(nums)
    var = sum((x-mean)**2 for x in nums) / (len(nums)-1)  # variance
    return var**0.5


def get_standard_error(a, b):
    '''
    Helper function for calculating the standard error, given two samples.
    :param a: list of numbers
    :param b: list of numbers
    :return: standard error of a and b (see studio 6 guide for this equation!)
    '''
    # TODO: fill me in!
    stdev_a = get_stdev(a)
    stdev_b = get_stdev(b)
    s_a = stdev_a**2/len(a)
    s_b = stdev_b**2/len(b)
    return (s_a + s_b)**0.5


def get_2_sample_df(a, b):
    '''
    Calculates the combined degrees of freedom between two samples.
    :param a: list of numbers
    :param b: list of numbers
    :return: integer representing the degrees of freedom between a and b (see studio 6 guide for this equation!)
    HINT: you can use Math.round() to help you round!
    '''
    se = get_standard_error(a, b)

    def get_s(nums):
        stddev = get_stdev(nums)
        n = len(nums)
        above = ((stddev**2)/n)**2
        return above/(n-1)

    s_a = get_s(a)
    s_b = get_s(b)
    above = se**4
    return round(above/(s_a + s_b))


def get_t_score(a, b):
    '''
    Calculates the t-score, given two samples.
    :param a: list of numbers
    :param b: list of numbers
    :return: number representing the t-score given lists a and b (see studio 6 guide for this equation!)
    '''
    t = (get_avg(a) - get_avg(b))/get_standard_error(a, b)
    return t if t < 0 else -t


def perform_2_sample_t_test(a, b):
    '''
    ** DO NOT CHANGE THE NAME OF THIS FUNCTION!! ** (this will mess with our autograder)
    Calculates a p-value by performing a 2-sample t-test, given two lists of numbers.
    :param a: list of numbers
    :param b: list of numbers
    :return: calculated p-value
    HINT: the t_dist.cdf() function might come in handy!
    '''
    return t_dist.cdf(get_t_score(a, b), get_2_sample_df(a, b))


# [OPTIONAL] Some helper functions that might be helpful in get_expected_grid().
def row_sum(observed_grid, ele_row):
    return sum(observed_grid[ele_row])


def col_sum(observed_grid, ele_col):
    n_row = len(observed_grid)
    col_ele = [observed_grid[r][ele_col] for r in range(n_row)]
    return sum(col_ele)


def total_sum(observed_grid):
    n_row = len(observed_grid)
    sum_row = [sum(observed_grid[r]) for r in range(n_row)]
    return sum(sum_row)


def calculate_expected(row_sum, col_sum, tot_sum):
    return row_sum*col_sum/tot_sum


def get_expected_grid(observed_grid):
    '''
    Calculates the expected counts, given the observed counts.
    ** DO NOT modify the parameter, observed_grid. **
    :param observed_grid: 2D list of observed counts
    :return: 2D list of expected counts
    HINT: To clean up this calculation, consider filling in the optional helper functions below!
    '''
    n_row = len(observed_grid)
    if n_row < 1:
        return observed_grid
    n_col = len(observed_grid[0])
    tot_sum = total_sum(observed_grid)
    result = [[0 for x in range(n_col)] for y in range(n_row)]
    row_sums = [row_sum(observed_grid, x) for x in range(n_row)]
    col_sums = [col_sum(observed_grid, x) for x in range(n_col)]
    for r in range(n_row):
        for c in range(n_col):
            result[r][c] = calculate_expected(
                row_sums[r], col_sums[c], tot_sum)
    return result


def df_chi2(observed_grid):
    '''
    Calculates the degrees of freedom of the expected counts.
    :param observed_grid: 2D list of observed counts
    :return: degrees of freedom of expected counts (see studio 6 guide for this equation!)
    '''
    n_row = len(observed_grid)
    if n_row < 1:
        return observed_grid
    n_col = len(observed_grid[0])
    return (n_row-1)*(n_col-1)


def chi2_value(observed_grid):
    '''
    Calculates the chi^2 value of the expected counts.
    :param observed_grid: 2D list of observed counts
    :return: associated chi^2 value of expected counts (see studio 6 guide for this equation!)
    '''
    n_row = len(observed_grid)
    if n_row < 1:
        return observed_grid
    n_col = len(observed_grid[0])
    expected_grid = get_expected_grid(observed_grid)

    def single_chi2_value(observed, expected):
        return ((observed - expected)**2)/expected

    subtracted = [[single_chi2_value(observed_grid[r][c], expected_grid[r][c])
                   for c in range(n_col)] for r in range(n_row)]
    return total_sum(subtracted)


def perform_chi2_homogeneity_test(observed_grid):
    '''
    ** DO NOT CHANGE THE NAME OF THIS FUNCTION!! ** (this will mess with our autograder)
    Calculates the p-value by performing a chi^2 test, given a list of observed counts
    :param observed_grid: 2D list of observed counts
    :return: calculated p-value
    HINT: the chi2.cdf() function might come in handy!
    '''
    return 1 - chi2.cdf(chi2_value(observed_grid), df_chi2(observed_grid))

# These commented out lines are for testing your main functions.
# Please uncomment them when finished with your implementation and confirm you get the same values :)


def data_to_num_list(s):
    '''
      Takes a copy and pasted row/col from a spreadsheet and produces a usable list of nums. 
      This will be useful when you need to run your tests on your cleaned log data!
      :param str: string holding data
      :return: the spliced list of numbers
      '''
    return list(map(float, s.split()))


'''
# t_test 1:
a_t1_list = data_to_num_list(a1)
b_t1_list = data_to_num_list(b1)
print(get_t_score(a_t1_list, b_t1_list))  # this should be -129.500
print(perform_2_sample_t_test(a_t1_list, b_t1_list))  # this should be 0.0000
# why do you think this is? Take a peek at a1 and b1 in abtesting_test.py :)

# t_test 2:
a_t2_list = data_to_num_list(a2)
b_t2_list = data_to_num_list(b2)
print(get_t_score(a_t2_list, b_t2_list))  # this should be -1.48834
print(perform_2_sample_t_test(a_t2_list, b_t2_list))  # this should be .082379

# t_test 3:
a_t3_list = data_to_num_list(a3)
b_t3_list = data_to_num_list(b3)
print(get_t_score(a_t3_list, b_t3_list))  # this should be -2.88969
print(perform_2_sample_t_test(a_t3_list, b_t3_list))  # this should be .005091

# chi2_test 1:
a_c1_list = data_to_num_list(a_count_1)
b_c1_list = data_to_num_list(b_count_1)
c1_observed_grid = [a_c1_list, b_c1_list]
print(chi2_value(c1_observed_grid))  # this should be 4.103536
# this should be .0427939
print(perform_chi2_homogeneity_test(c1_observed_grid))

# chi2_test 2:
a_c2_list = data_to_num_list(a_count_2)
b_c2_list = data_to_num_list(b_count_2)
c2_observed_grid = [a_c2_list, b_c2_list]
print(chi2_value(c2_observed_grid))  # this should be 33.86444
print(perform_chi2_homogeneity_test(c2_observed_grid))  # this should be 0.0000
# Again, why do you think this is? Take a peek at a_count_2 and b_count_2 in abtesting_test.py :)

# chi2_test 3:
a_c3_list = data_to_num_list(a_count_3)
b_c3_list = data_to_num_list(b_count_3)
c3_observed_grid = [a_c3_list, b_c3_list]
print(chi2_value(c3_observed_grid))  # this should be .3119402
# this should be .57649202
print(perform_chi2_homogeneity_test(c3_observed_grid))
'''
