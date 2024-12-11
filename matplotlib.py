import matplotlib.pyplot as plt
#import numpy as np

# Example data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [150, 200, 250, 300, 350, 400]
#finding the median
#median_sales=np.median(sales)
#print ("The median of the sale is:", median_sales)

# Create the bar graph
plt.bar(months, sales, color='skyblue', edgecolor='black')

# Add labels and title
plt.title("Monthly Sales", fontsize=16)
plt.xlabel("Months", fontsize=12)
plt.ylabel("Sales ($)", fontsize=12)

# Add grid for better readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()