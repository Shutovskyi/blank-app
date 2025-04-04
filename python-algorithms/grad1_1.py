import time
import numpy as np
import matplotlib.pyplot as plt

# Define the function f(x) = x^2 - 5x + 5
def f(x):
    return x * x - 5 * x + 5

# Define the derivative f'(x) = 2x - 5
def df(x):
    return 2 * x - 5

N = 20      # Number of iterations for gradient descent
xx = 0      # Initial value of x
lmd = 0.9   # Learning rate (step size)

# Prepare data for plotting the function curve
x_plt = np.arange(0, 5.0, 0.1)
f_plt = [f(x) for x in x_plt]

plt.ion()   # Enable interactive plotting mode
fig, ax = plt.subplots()    # Create a figure and axis for the plot
ax.grid(True)   # Show grid lines on the plot

ax.plot(x_plt, f_plt)                   # Plot the parabola representing f(x)
point = ax.scatter(xx, f(xx), c='red')   # Plot the starting point in red

# Gradient descent loop to minimize the function f(x)
for i in range(N):
    # Update x by moving against the gradient direction (faster descent)
    xx = xx - lmd * df(xx)

    # Update the point's position on the plot
    point.set_offsets([xx, f(xx)])

    # Redraw the canvas and pause for 20 milliseconds to animate the movement
    fig.canvas.draw()
    fig.canvas.flush_events()
    time.sleep(0.02)

plt.ioff()  # Disable interactive plotting mode

print(xx)
ax.scatter(xx, f(xx), c='blue')  # Mark the final point in blue
plt.show()
