import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [1,2,3,4,5]

# plt.plot(x,y)
plt.plot(x,y,'ro')            # 'r-', 'g-', 'b-'
plt.show()                    # 'ro', 'go', 'bo'
                              # 'rv', 'gv', 'bv'

# plot()은 b- 옵션이 기본값 : 파란색(b) 라인(-)이라는 뜻
# ro 옵션은 빨간색(r)으로 o표시를 의미함
# bv 옵션은 파란색(b)으로 v표시를 의미함