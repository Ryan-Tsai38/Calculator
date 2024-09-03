class Calculator:
    def __init__(self):
        self.expression = ""

    def add_to_expression(self, value):
        self.expression += str(value)

    def clear_expression(self):
        self.expression = ""

    def evaluate_expression(self):
        try:
            result = eval(self.expression)
            return result
        except Exception as e:
            return "Error: " + str(e)