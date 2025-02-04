import numpy as np
import matplotlib.pyplot as plt
import os

fig_dir = os.path.join(os.getcwd(), 'src', '0 FIGURER')
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.xlabel('Fra 0 til 10')
plt.ylabel('Sinus')

plt.savefig(os.path.join(fig_dir, 'sinus.pdf'))


