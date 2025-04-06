from utils.environment import Environment
from utils.cases import TestCase2, TestCase
import matplotlib.pyplot as plt
from utils.car import SimpleCar


tc = TestCase2()
env = Environment(obs=tc.obs, lx=20, ly=20)  # use 20x20 to match the map size

# Optional: pass custom start/end if needed
car = SimpleCar(env, start_pos=tc.start_pos, end_pos=tc.end_pos)

# Draw the environment
fig, ax = plt.subplots(figsize=(6, 6))
env.draw(ax)

# Draw start and end points
ax.plot(car.start_pos[0], car.start_pos[1], 'ro', label='Start')
ax.plot(car.end_pos[0], car.end_pos[1], 'go', label='Goal')
ax.legend()

plt.axis("equal")
plt.grid(True)
plt.title("Preview of TestCase Map")
plt.show()