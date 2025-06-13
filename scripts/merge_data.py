import pandas as pd

# 讀進來：users 員工資料 + attendance 出勤資料
df_users = pd.read_csv("data/users.csv")
df_attend = pd.read_csv("data/attendance.csv")

# 合併兩份資料：用 employee_id 對上 id
df_merged = pd.merge(df_attend, df_users, left_on='employee_id', right_on='id')

# 看看合併後的資料長怎樣
print(df_merged.head())

# 可以把結果存起來
df_merged.to_csv("data/merged_users_attendance.csv", index=False)
