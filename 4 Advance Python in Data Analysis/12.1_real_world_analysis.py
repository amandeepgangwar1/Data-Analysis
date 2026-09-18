import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 11)

sales_in_cr = np.array([12.5, 3.0, 4.2, 5.1, 6.0, 7.8, 8.5, 9.0, 10.2, 11.5])

plt.figure(figsize=(10, 5))
plt.style.use('seaborn-v0_8-darkgrid')

plt.plot(days, sales_in_cr, marker='o', color='b', label='Sales in Crores'
        )

plt.title('Daily Sales Over 10 Days')
plt.grid(True)
plt.xlabel('Days')
plt.ylabel('Sales (in Crores)')
plt.legend()

plt.show()