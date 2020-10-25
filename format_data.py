import pandas as pd

data = pd.read_csv("myfilteredlog_comma.csv")

user = {}
user['A'] = set()
user['B'] = set()
user_pageload = {}  # map userid to page load
user_timecomplete = {}  # map userid to last interaction
user_checkout = set()  # add userid to the set if they go to page C
return_user = set()

for i in range(len(data)):
    cur_user = data['user id'][i]
    # if first log of cur user
    if cur_user not in user_pageload:
        user_pageload[cur_user] = data['page load'][i]
    # if user lands to the checkout page
    elif data['style'][i] == 'C':
        # 1. add checkout user
        user_checkout.add(cur_user)
        # 2. update time to complete
        user_timecomplete[cur_user] = data['page load'][i]
    # if user clicks items
    elif data['item click'][i] > 0:
        # 1. add user to user[style]
        user[data['style'][i]].add(cur_user)
        # 2. update time to complete
        user_timecomplete[cur_user] = data['item click'][i]
    # if user returns to the page
    elif cur_user in user_checkout and user_pageload[cur_user] != data['page load'][i]:
        # 1. add return user
        return_user.add(cur_user)
        # 2. update time to complete
        user_timecomplete[cur_user] = data['page load'][i]

time_complete_a = []
return_user_a = 0
for cur_user in user['A']:
    time_complete_a.append(
        user_timecomplete[cur_user] - user_pageload[cur_user])
    if cur_user in return_user:
        return_user_a += 1

time_complete_b = []
return_user_b = 0
for cur_user in user['B']:
    time_complete_b.append(
        user_timecomplete[cur_user] - user_pageload[cur_user])
    if cur_user in return_user:
        return_user_b += 1

num_user_a = len(user['A'])
num_user_b = len(user['B'])
print("Number of users visiting version A:", num_user_a)
print("Number of users visiting version B:", num_user_b)
print("Number of return, no return user A: ",
      return_user_a, num_user_a - return_user_a)
print("Number of return, no return user B: ",
      return_user_b, num_user_b - return_user_b)
return_rate_a = [return_user_a, num_user_a - return_user_a]
return_rate_b = [return_user_b, num_user_b - return_user_b]
