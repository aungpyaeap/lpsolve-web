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