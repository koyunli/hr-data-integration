import requests  
import pandas as pd 

res = requests.get("https://dummyjson.com/users")

data = res.json()

users = data['users']

df_users = pd.DataFrame(users)

print(df_users.head())
df_users.to_csv("data/users.csv", index=False)

import pandas as pd
import random

# 模擬有 30 位員工（因為 dummyjson.com/users 預設回傳 30 筆）
num_employees = 30
data = []

for i in range(1, num_employees + 1):
    data.append({
        "employee_id": i,
        "month": "Jan",
        "hours_worked": random.randint(120, 180)  # 模擬每人打工時數
    })

# 存成 CSV
df = pd.DataFrame(data)
df.to_csv("data/attendance.csv", index=False)

print("✅ 打卡資料已產生完成！")
