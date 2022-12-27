# pandas의 선그래프

import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series([1,2,3,4,5,6,7,8,9,10])
print(s)

s.plot()
plt.show()