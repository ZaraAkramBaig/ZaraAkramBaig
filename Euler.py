def f(x, y):
    return x**2 -1 

def euler_method(x0, y0, h, n_steps):
    x = x0
    y = y0
    results = [(x, y)]
    for _ in range(n_steps):
        y += h * f(x, y)  
        x += h  
        results.append((x, y))
    return results

x0 = 0  
y0 = 2  
h = 0.1  
n_steps = 10

solution = euler_method(x0, y0, h, n_steps)

# Print the solution
for x, y in solution:
    print(f"x = {x:.1f}, y = {y:.4f}")
