import re

class GiGaInterpreter:
    def __init__(self):
        self.variables = {}

    def eval(self, source_code):
        lines = source_code.strip().split("\n")
        for line in lines:
            self.evaluate_line(line)

    def evaluate_line(self, line):
        line = line.strip()

        # Ignore comments
        if line.startswith("#"):
            return

        # Variable assignment
        if "=" in line:
            var_name, expr = line.split("=")
            var_name = var_name.strip()
            expr = expr.strip()
            result = self.evaluate_expression(expr)
            self.variables[var_name] = result
        else:
            # Expression evaluation
            result = self.evaluate_expression(line)
            print(result)

    def evaluate_expression(self, expr):
        # Replace variables with their values
        for var_name, var_value in self.variables.items():
            expr = expr.replace(var_name, str(var_value))

        # Evaluate arithmetic expression using eval()
        return eval(expr)

if __name__ == "__main__":
    interpreter = PithonInterpreter()

    source_code = """
        # Pithon Example Code
        x = 10
        y = 5
        z = x + y * 2
        result = (x + y) / z
        result
    """

    interpreter.eval(source_code)
