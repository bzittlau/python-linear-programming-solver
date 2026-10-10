# Beckett Zittlau-Johnson
# Linear Programming Solver
# This program compares each variable by itself with the balanced solution.

import numpy as np

# Used this so I do not have to repeat the same input check every time.
def get_values(prompt, count):
    while True:
        values = input(prompt).split()

        if len(values) != count:
            print(f"Please enter exactly {count} values.")
            continue

        try:
            return [float(value) for value in values]
        except ValueError:
            print("Please enter numbers only.")


# The number of variables and constraints are the same.
# Makes sure the number of variables is a valid positive number.
while True:
    try:
        n = int(input("How many variables/constraints are in the problem? "))
        if n > 0:
            break
        print("Please enter a positive integer.")
    except ValueError:
        print("Please enter a valid integer.")

# Coefficients used in the objective function.
objective = get_values(
    f"Enter the {n} objective function coefficients separated by spaces: ", n
)

A = []
print("\nEnter the constraint matrix one row at a time.")
for i in range(n):
    row = get_values(
        f"Constraint {i + 1}, enter {n} coefficients separated by spaces: ", n
    )
    A.append(row)

# Limits for each constraint.
b = get_values(
    f"Enter the {n} constraint limits separated by spaces: ", n
)

# Convert A and b to NumPy arrays to solve Ax = b.
A_np = np.array(A, dtype=float)
b_np = np.array(b, dtype=float)

# Print a simple chart to see the setup before solving it.
print("\nPROBLEM SETUP")
header = f"{'Variable':<12}"
for i in range(n):
    header += f"{'Constraint ' + str(i + 1):>15}"
header += f"{'Objective':>15}"
print(header)

for j in range(n):
    line = f"{'x' + str(j + 1):<12}"
    for i in range(n):
        line += f"{A[i][j]:>15.2f}"
    line += f"{objective[j]:>15.2f}"
    print(line)

limit_line = f"{'Limit':<12}"
for value in b:
    limit_line += f"{value:>15.2f}"
print(limit_line)

# Find how much can be made with one variable.
# If a coefficient is zero, that constraint does not limit that variable.
solo_options = []

for j in range(n):
    possible_amounts = []

    for i in range(n):
        if A[i][j] > 0:
            possible_amounts.append(b[i] / A[i][j])

    if possible_amounts:
        units = min(possible_amounts)
    else:
        units = 0.0

    profit = units * objective[j]

    option = [0.0] * n
    option[j] = units

    solo_options.append((option, profit))

# Balanced option is where all of the constraint equations meet.
try:
    inverse_A = np.linalg.inv(A_np)
    balance = inverse_A.dot(b_np)
    balance_profit = np.dot(objective, balance)

    # A negative answer would not make sense for the examples in this assignment.
    balance_valid = np.all(balance >= -1e-9)

except np.linalg.LinAlgError:
    balance = None
    balance_profit = None
    balance_valid = False

# Show every solo option to compare all of them.
print("\nSOLO OPTIONS")
for i, (option, profit) in enumerate(solo_options):
    print(
        f"Only x{i + 1}: "
        f"{option[i]:.2f} units, "
        f"objective value = {profit:.2f}"
    )

# Show the balanced result and the value of every variable.
print("\nBALANCED OPTION")
if balance is not None and balance_valid:
    for i in range(n):
        print(f"x{i + 1} = {balance[i]:.2f}")
    print(f"Balanced objective value = {balance_profit:.2f}")
else:
    print("A usable balanced solution could not be found.")

# Compare everything and keep the option with the highest objective value.
best_name = ""
best_values = None
best_profit = float("-inf")

for i, (option, profit) in enumerate(solo_options):
    if profit > best_profit:
        best_name = f"Only x{i + 1}"
        best_values = option
        best_profit = profit

if balance is not None and balance_valid and balance_profit > best_profit:
    best_name = "Balanced option"
    best_values = balance
    best_profit = balance_profit

print("\nBEST OPTION")
print(best_name)
for i in range(n):
    print(f"x{i + 1} = {best_values[i]:.2f}")
print(f"Best objective value = {best_profit:.2f}")

# Results output from Chemical Test Case
"""
How many variables/constraints are in the problem? 3
Enter the 3 objective function coefficients separated by spaces: 3000 2000 2000                               

Enter the constraint matrix one row at a time.
Constraint 1, enter 3 coefficients separated by spaces: 2 4 5
Constraint 2, enter 3 coefficients separated by spaces: 1 2 4
Constraint 3, enter 3 coefficients separated by spaces: 8 0 3
Enter the 3 constraint limits separated by spaces: 300 200 300

PROBLEM SETUP
Variable       Constraint 1   Constraint 2   Constraint 3      Objective
x1                     2.00           1.00           8.00        3000.00
x2                     4.00           2.00           0.00        2000.00
x3                     5.00           4.00           3.00        2000.00
Limit                300.00         200.00         300.00

SOLO OPTIONS
Only x1: 37.50 units, objective value = 112500.00
Only x2: 75.00 units, objective value = 150000.00
Only x3: 50.00 units, objective value = 100000.00

BALANCED OPTION
x1 = 25.00
x2 = 20.83
x3 = 33.33
Balanced objective value = 183333.33

BEST OPTION
Balanced option
x1 = 25.00
x2 = 20.83
x3 = 33.33
Best objective value = 183333.33
"""