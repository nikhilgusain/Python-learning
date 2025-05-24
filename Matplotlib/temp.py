import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(0,11, 5)


fig, axs = plt.subplots(2, 2)
axs[0,0].grid(True)
axs[0,0].legend(["data"])
axs[0,0].bar(['a', 'b', 'c', 'd', 'e'], x)
plt.tight_layout()
axs[0,0].set_title("Practice")

plt.show()