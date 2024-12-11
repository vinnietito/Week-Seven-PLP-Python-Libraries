import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data: House size (sq ft) vs. Price ($1000)
data = {
    'House Size': [750, 800, 850, 900, 950, 1000, 1100, 1200, 1300],
    'Price': [150, 160, 165, 170, 175, 180, 190, 200, 210]
}

# Create a DataFrame from the data dictionary
df = pd.DataFrame(data)

# Plot the scatter plot with a regression line
sns.regplot(x='House Size', y='Price', data=df, scatter_kws={'color':'blue'}, line_kws={'color':'red'})

# Add titles and labels
plt.title("House Size vs. Price")
plt.xlabel("House Size (sq ft)")
plt.ylabel("Price ($1000)")

# Show the plot
plt.tight_layout()
plt.show()
