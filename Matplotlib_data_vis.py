import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np


# 1..plot(): line plot; takes 2 lists as arguments, one for x axis, one for y axis
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
x_1 = [1, 2, 3]
y_1 = [4, 5, 6]
x_2 = [9, 5, 2]
y_2 = [3, 6, 4]
plt.plot(x_1, y_1, 'r', label='line 1')
plt.plot(x_2, y_2, 'c', label='line 2')
plt.title('my line plot')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.legend()
plt.show()

# 2..hist(): histogram; plot frequency and visualise data distribution; takes 1 list as argument
values_1 = [10, 15, 20, 10, 10]  # Here we have three 10, one 15 and one 20
plt.hist(values_1, color='b')
plt.show()

# 3..bar(): bar plot; takes 2 lists as arguments, 1st-->xlabel, 2nd-->height of each bar
values_2 = [10, 15, 20]
height_2 = [3, 1, 1]
plt.bar(values_2, height_2, width=2)
plt.show()

# 4..pie(): pie chart; takes 1 list as argument, values of element-->area of sector
plt.pie(values_1, labels=['a-10', 'b-15', 'c-20', 'd-10', 'e-10'], colors=['r', 'b', 'g', 'y', 'c'], explode=[0, 0.2, 0, 0, 0])
plt.show()

# 5..scatter(): scatter plot; takes 2 lists as arguments
plt.scatter(x_1, y_1, c=[1, 2, 3], cmap='Accent')  # Color map: takes a list of integers; maps to color
plt.title('Scatter plot')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()
print(dir(cm))  # Show all kinds of color maps

# 6.log plots
y_3 = [10, 100, 1000]
plt.yscale('log')  # Change y axis from linear to log
plt.plot(x_1, y_3)
plt.show()

# 7..polar(): polar plot; takes 2 arguments, 1st-->angle, 2nd-->distance from center
theta = np.arange(0, (2*np.pi), 0.01)
r = 2
for i in theta:
    plt.polar(i, r)
plt.show()  # ie.plot a circle with radius 2

# 8..xticks(rotation=...): change the direction of x labels, so that long labels wouldn't overlap
dates = ['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04', '2022-01-05', '2022-01-06', '2022-01-07', '2022-01-08']
values_3 = [6, 3, 7, 2, 8, 6, 0, 4]
plt.plot(dates, values_3)
plt.xticks(rotation=90)
plt.show()

# 9. .subplot(nrows, ncols, index): create multiple subplots in one figure
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html
