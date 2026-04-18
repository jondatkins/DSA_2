class SimplexSolver:
    def solve(self):
        self.add_slack_variables()
        while self.should_pivot():
            pivot_col = self.get_pivot_col()
            pivot_row = self.get_pivot_row(pivot_col)
            self.pivot(pivot_row, pivot_col)

    def pivot(self, pivot_row_idx, pivot_col_idx):
        pivot_val = self.rows[pivot_row_idx][pivot_col_idx]
        # pivot_row = self.rows[pivot_row_idx]
        for i in range(len(self.rows[pivot_row_idx])):
            val = self.rows[pivot_row_idx][i]
            val = val / pivot_val
            self.rows[pivot_row_idx][i] = val
        for i in range(len(self.rows)):
            if i == pivot_row_idx:
                continue
            scalar = self.rows[i][pivot_col_idx]
            for j in range(len(self.rows[i])):
                self.rows[i][j] -= scalar * self.rows[pivot_row_idx][j]
        new_scalar = self.objective[pivot_col_idx]
        for i in range(len(self.objective)):
            self.objective[i] -= new_scalar * self.rows[pivot_row_idx][i]

    def get_pivot_row(self, col_idx):
        last_column = []

        for i, row in enumerate(self.rows):
            value = row[-1]
            last_column.append(value)
        pivot_column = []
        pivot_column_index = self.get_pivot_col()
        for i, row in enumerate(self.rows):
            value = row[pivot_column_index]
            pivot_column.append(value)
        min_ratio = float("inf")
        min_ratio_idx = -1
        for i in range(len(last_column)):
            ratio = float("inf")
            value = pivot_column[i]
            if value != 0:
                ratio = last_column[i] / pivot_column[i]
            if ratio < 0:
                continue
            if ratio < min_ratio:
                min_ratio = ratio
                min_ratio_idx = i
        if min_ratio_idx == -1:
            raise Exception("no non-negative ratios, problem doesn't have a solution")
        return min_ratio_idx

    def get_pivot_col(self):
        min_value = float("inf")
        min_index = -1
        for i in range(len(self.objective) - 1):
            if self.objective[i] < min_value and self.objective[i] < 0:
                min_value = self.objective[i]
                min_index = i
        return min_index

    def should_pivot(self):
        for obj in self.objective[:-1]:
            if obj < 0:
                return True
            return False

    # Don't touch below this line
    #
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
