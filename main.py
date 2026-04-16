class SimplexSolver:
    def __init__(self, func_coefficients):
        self.objective = []
        for coeff in func_coefficients:
            self.objective.append(coeff)
        self.rows = []
        self.constraints = []

    def add_constraint(self, coefficients, value):
        self.rows.append(coefficients)
        self.constraints.append(value)
