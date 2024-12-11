from scipy.optimize import fsolve

# Define the quadratic equation
def quadratic(x):
    # Example equation: x^2 - 5x + 6 = 0
    return x**2 - 5*x + 6

# Solve the equation
roots = fsolve(quadratic, [0, 5])  # Initial guesses for the roots

# Display the results
print("Roots of the equation:")
print(roots)
