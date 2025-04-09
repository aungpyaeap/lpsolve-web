from ortools.linear_solver import pywraplp
import re


def solve_linear_program(variables, constraints, objective, method):
    decision_vars = [var.strip() for var in variables.split(",") if var.strip()]
    constraints = [var.strip() for var in constraints.split(",") if var.strip()]

    # Add explicit multiplication to the objective function
    objective = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', objective)

    solution_values = []

    solver = pywraplp.Solver.CreateSolver("GLOP")
    if not solver:
        return

    for decision_variable in decision_vars:
        globals()[decision_variable] = solver.NumVar(0, solver.infinity(), decision_variable)

    for const in constraints:
        # Add explicit multiplication to the constraints
        const = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', const)
        solver.Add(eval(const))

    if method == "max":
        solver.Maximize(eval(objective))
    else:
        solver.Minimize(eval(objective))

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        for decision_variable in decision_vars:
            solution_values.append(globals()[decision_variable].solution_value())
        result_data = {'objective': solver.Objective().Value(),
                       'solution': solution_values,
                       'variables': solver.NumVariables(),
                       'constraints': solver.NumConstraints(),
                       'type': method
                       }
        result_string = f"Optimization Results:\n"
        result_string += f"------------------------\n"
        result_string += f"Optimization Type: {result_data['type']}\n"
        result_string += f"Objective Value: {result_data['objective']}\n"
        result_string += f"Solution:\n"
        for i, var in enumerate(decision_vars):
            result_string += f"  {var}: {result_data['solution'][i]}\n"
        result_string += f"------------------------\n"
        result_string += f"Number of Variables: {result_data['variables']}\n"
        result_string += f"Number of Constraints: {result_data['constraints']}\n"
        return result_string

    else:
        return f"The problem does not have an optimal solution."
