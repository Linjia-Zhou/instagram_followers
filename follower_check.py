import pandas as pd
import openpyxl

"""
INSTRUCTIONS:
In Excel,
1. Import html data into a blank excel file --> command + A shortcut to highlight entire webpage
2. Make sure first row (A1) says "Follow" for both files. 
    This will be the column name and needs to be the same
In Python,
3. Insert file location into following and followers variables
"""
# INSERT EXCEL FILES HERE
following = pd.read_excel('')
followers = pd.read_excel('')

followers = followers.iloc[::2]  # deleting every other row
following = following.iloc[::2]

followers_sorted = followers.sort_values('Follow')  # alphabetical order
following_sorted = following.sort_values('Follow')  # alphabetical order

diff_rows = following.merge(followers, how = 'outer' ,indicator=True)

# left_only = users who don't follow me back, right_only = users I don't follow back
no_follow_back = diff_rows.loc[diff_rows['_merge'] == 'left_only']
i_dont_follow_back = diff_rows.loc[diff_rows['_merge'] == 'right_only']

if __name__ == '__main__':
    print(no_follow_back)
