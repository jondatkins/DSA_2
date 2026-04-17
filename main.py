class SimplexSolver:
    def get_solution_from_tableau(self):
        columns = []
        num_rows = len(self.rows)
        num_cols = len(self.rows[0])

        for j in range(num_cols):
            column = [0] * num_rows
            for i in range(num_rows):
                column[i] = self.rows[i][j]
            columns.append(column)
        results = []

        for column in columns[:-1]:
            if column.count(1) == 1 and column.count(0) == len(column) - 1:
                row_index = column.index(1)
                results.append(self.rows[row_index][-1])
            else:
                results.append(0)
        return results, self.objective[-1]

    # Don't touch below this line

    def __init__(self, func_coefficients):
        self.objective = []
        for func_coefficient in func_coefficients:
            self.objective.append(func_coefficient)
        self.rows = []
        self.constraints = []

    def add_constraint(self, coefficients, value):
        row = []
        for coefficient in coefficients:
            row.append(coefficient)
        self.rows.append(row)
        self.constraints.append(value)

    def add_slack_variables(self):
        for i in range(len(self.rows)):
            self.objective.append(0)
            basic_cols = [0] * len(self.rows)
            basic_cols[i] = 1
            basic_cols.append(self.constraints[i])
            self.rows[i] += basic_cols
        self.objective.append(0)
