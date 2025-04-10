---
title: My Gradio App
emoji: 🚀  # Optional: Add an emoji to represent your app
colorFrom: "red"  # Optional: Starting color for the gradient
colorTo: "green"    # Optional: Ending color for the gradient
sdk: gradio            # The SDK you are using
sdk_version: "5.24.0"  # Specify the version of Gradio you are using
app_file: app.py      # The main file for your Gradio app
pinned: false          # Set to true if you want to pin the Space
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