---
title: Linear Programming Solver
emoji: 📈
colorFrom: yellow
colorTo: pink
sdk: gradio
sdk_version: 5.24.0
app_file: app.py
pinned: false
license: mit
short_description: lpsolve
---

# Linear programming solver Gradio app
A simple Gradio app for linear programming. This app solves linear programming problems using the Google OR-Tools library.

To use this app, please follow these steps.
1. Enter the variables in the first input field, separated by commas (e.g., $x1,x2$).
2. Enter the constraints in the second input field, separated by commas (e.g., x1+2*x2<=14, 3*x1-x2>=0).
3. Enter the objective function in the third input field (e.g., 3*x1+4*x2)
4. Choose the optimization method (Min or Max) using the radio button.
5. Click the 'Submit' button to solve the linear programming problem.

The app will display the optimization results, including the objective value, solution, number of variables, and number of constraints.

## Components of Linear Programming
The basic components of a linear programming(LP) problem.
1. Decision Variables: Variables you want to determine to achieve the optimal solution.
2. Objective Function: Mathematical equation that represents the goal you want to achieve.
3. Constraints: Limitations or restrictions that your decision variables must follow.
4. Non-Negativity Restrictions: Decision variables cannot be negative.

## Example
Maximize $3x + 4y$ subject to the following constraints.
1. $x + 2y ≤ 14$
2. $3x - y ≥ 0$
3. $x - y ≤ 2$

**Example usage.**
```
Variables: x, y
Constraints: 
x + 2y <= 14,
3x - y >= 0,
x - y <= 2
Objective function: 3x + 4y
```