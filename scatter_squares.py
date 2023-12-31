import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn")
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

#设置图题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

#设置刻度的样式
ax.tick_params(labelsize=14)

#设置坐标轴的取值范围
ax.axis([0, 1100, 0, 1_100_000])

#覆盖默认的刻度标记样式
#ax.ticklabel_format(style='plain')

#保存绘图
#plt.savefig('square_plot.png', bbox_inches='tight')

plt.show()