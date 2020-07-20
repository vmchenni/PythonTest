# 5. Let the x axis data points and y axis data points are
# X = [1,2,3,4]
# y = [20, 21, 20.5, 20.8]
# 5.1: Draw a Simple plot
# 5.2: Configure the line and markers in simple plot
# 5.3: configure the axes
# 5.4: Give title of Graph & labels of x axis and y axis
# 5.5: Give error bar if y_error = [0.12, 0.13, 0.2, 0.1]
# 5.6: define width, height as figsize=(4,5) DPI and adjust plot dpi=100
# 5.7: Give a font size of 14

from matplotlib import pyplot as plt
plt.figure(figsize=(4,5),dpi=100,)
X = [1,2,3,4]
Y = [20, 21, 20.5, 20.8]
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("My Graph")
plt.rcParams.update({'font.size': 14})
plt.plot(X, Y)
plt.show()