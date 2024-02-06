import pandas as pd
import openpyxl

"""
INSTRUCTIONS:
Request to download Instagram information from: https://accountscenter.instagram.com/info_and_permissions/
In Excel,
- Copy HTML data into a blank Excel file --> command + A shortcut to highlight entire webpage

In Python,
- Insert file location into "following" and "followers" variables

TO VIEW WHO DOESN'T FOLLOW YOU BACK:
- uncomment print statement 
"""
# INSERT EXCEL FILES HERE
following = pd.read_excel('')
followers = pd.read_excel('')

#delete the blankspace
followers = followers.drop([0, 1, 2])
following = following.drop([0, 1, 2, 3])

followers = followers.iloc[::2]  # deleting every other row
following = following.iloc[::2]

followers_sorted = followers.sort_values(by='Unnamed: 0')  # alphabetical order
following_sorted = following.sort_values(by='Unnamed: 0')  # alphabetical order

diff_rows = following.merge(followers, how = 'outer' ,indicator=True)

# left_only = users who don't follow me back, right_only = users I don't follow back
no_follow_back = diff_rows.loc[diff_rows['_merge'] == 'left_only']
i_dont_follow_back = diff_rows.loc[diff_rows['_merge'] == 'right_only']

if __name__ == '__main__':
    # uncomment to see who doesn't follow you back
    # print(no_follow_back)
    # uncomment to see who you don't follow back
    # print(i_dont_follow_back)
