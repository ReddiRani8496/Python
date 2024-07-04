colors1 = {'white', 'red', 'green', 'yellow'}
colors2 = {'blue', 'purple', 'red', 'white'}

# Symmetric difference between colors1 and colors2
colors_sym_diff = colors1.symmetric_difference(colors2)
print( colors_sym_diff)

# Using '^' operator for symmetric difference
colors_sym_diff2 = colors1 ^ colors2
print(colors_sym_diff2)
