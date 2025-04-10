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
    description="A simple Gradio app for linear programming.",
)

demo.launch()
