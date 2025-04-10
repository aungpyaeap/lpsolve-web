import gradio as gr
from solver import solve_linear_program

demo = gr.Interface(
    fn=solve_linear_program,
    inputs=[
        gr.Textbox(label="Enter variables in comma separated format (e.g., x1,x2):"),
        gr.TextArea(label="Enter constraints in comma separated format (e.g., x1+2x2<=14,3x1-x2>=0):"),
        gr.Textbox(label="Enter objective function (e.g., 3x1+4x2):"),
        gr.Radio(["min", "max"], label="Choose optimization method: Min/Max", value="min"),
    ],
    outputs="text",
    title="Linear Programming Solver",
    description="A simple Gradio app for linear programming. To use this app, please follow these steps:\n\n"
                "1. Enter the variables in the first input field, separated by commas (e.g., x1,x2).\n"
                "2. Enter the constraints in the second input field, separated by commas (e.g., x1+2*x2<=14,3*x1-x2>=0).\n"
                "3. Enter the objective function in the third input field (e.g., 3*x1+4*x2).\n"
                "4. Choose the optimization method (Min or Max) using the radio button.\n"
                "5. Click the 'Submit' button to solve the linear programming problem.\n\n"
                "The app will display the optimization results, including the objective value, solution, number of variables, and number of constraints.",
)

demo.launch()
