import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 5, np.nan, 6, 8])  # 一维序列
print(s)

dates = pd.date_range("20130101", periods=6)  # 时间序列
print(dates)

df = pd.DataFrame(
    np.random.randn(6, 4), index=dates, columns=list("ABCD")
)  # 二维数据框

print(df)

print(df.groupby("A").sum())  # 聚合

news = pd.read_csv("news.csv")
print(news)
