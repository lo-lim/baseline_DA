import pandas as pd

tbl = pd.DataFrame([
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"]
])

print(tbl)

print("데이터 반전: 행과 열이 바뀜")
print(tbl.T)