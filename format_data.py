import pandas as pd

''' Time to completion
'''
# data = pd.read_csv("myfilteredlog-comma.csv")
data = pd.read_csv("myfilteredlog_comma.csv")
# rowA = data["A: Time to complete"].copy().dropna().reset_index(drop=True)
# rowB = data["B: Time to complete"].copy().dropna().reset_index(drop=True)
# time_complete = pd.concat([rowA, rowB], axis=1, ignore_index=True)
# time_complete.columns = ['A', 'B']
time_complete_a = []
time_complete_b = []
for i in range(len(data)):
    if data['time to complete'][i] > 0:
        if data['style'][i] == 'A':
            time_complete_a.append(data['time to complete'][i])
        elif data['style'][i] == 'B':
            time_complete_b.append(data['time to complete'][i])

''' Return rate
'''
visited_userid = set()
visited_pageclick_userid = set()
return_user = {}
return_user['A'] = set()
return_user['B'] = set()
user = {}
user['A'] = set()
user['B'] = set()
for i in range(len(data)):
    cur_user = data['user id'][i]
    pageclick_userid = (data['page load'][i], cur_user)
    if pageclick_userid not in visited_pageclick_userid:
        visited_pageclick_userid.add(pageclick_userid)
        style = data['style'][i]
        if style != 'C':
            if cur_user not in user[style]:
                user[style].add(cur_user)
            else:
                return_user[style].add(cur_user)

# [return_rate, no_return_rate]
return_rate_a = [len(return_user['A']), len(user['A']) - len(return_user['A'])]
return_rate_b = [len(return_user['B']), len(user['B']) - len(return_user['B'])]
