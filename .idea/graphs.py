import matplotlib.pyplot as plt
import numpy as np

plt.title("Bubble sort")
x_points_sorted = np.array([10, 100, 1000, 5000, 10000, 20000, 50000])
y_points_sorted = np.array([45, 4950, 499500, 12497500, 49995000, 199990000, 1249975000])
x_points_reversed = np.array([10, 100, 1000, 5000, 10000, 20000, 50000])
y_points_reversed = np.array([45, 4950, 499500, 12497500, 49995000, 199990000, 1249975000])
x_points_random = np.array([10, 100, 1000, 5000, 10000, 20000, 50000])
y_points_random = np.array([45, 4950, 499500, 12497500, 49995000, 199990000, 1249975000])
plt.plot(x_points_sorted, y_points_sorted, color="green", label="Sorted Array")
plt.plot(x_points_reversed, y_points_reversed, color="red", label="Reversed Array")
plt.plot(x_points_random, y_points_random, color="blue", label="Random Array")
plt.legend()
plt.show()

plt.title("Modified Bubble sort")
x_points_sorted = np.array([10, 100, 1000, 5000, 10000, 20000, 50000])
y_points_sorted = np.array([9, 99, 999, 4999, 9999, 19999, 49999])
x_points_reversed = np.array([10, 100, 1000, 5000, 10000, 20000, 50000])
y_points_reversed = np.array([45, 4950, 499500, 12497500, 49995000, 199990000, 1249975000])
x_points_random = np.array([10, 100, 1000, 5000, 10000, 20000, 50000])
y_points_random = np.array([45, 4895, 499094, 12495015, 49984704, 199934055, 1249564129])
plt.plot(x_points_sorted, y_points_sorted, color="green", label="Sorted Array")
plt.plot(x_points_reversed, y_points_reversed, color="red", label="Reversed Array")
plt.plot(x_points_random, y_points_random, color="blue", label="Random Array")
plt.legend()
plt.show()

plt.title("Comb sort")
x_points_sorted = np.array([10, 100, 1000, 5000, 10000, 20000, 50000])
y_points_sorted = np.array([32, 1003, 18713, 123386, 276739, 613402, 1683412])
x_points_reversed = np.array([10, 100, 1000, 5000, 10000, 20000, 50000])
y_points_reversed = np.array([41, 1102, 19712, 128385, 286738, 633401, 1733411])
x_points_random = np.array([10, 100, 1000, 5000, 10000, 20000, 50000])
y_points_random = np.array([50, 1201, 20711, 133384, 286738, 653400, 1883408])
plt.plot(x_points_sorted, y_points_sorted, color="green", label="Sorted Array")
plt.plot(x_points_reversed, y_points_reversed, color="red", label="Reversed Array")
plt.plot(x_points_random, y_points_random, color="blue", label="Random Array")
plt.legend()
plt.show()
