from typing import TypedDict

from main import SimplexSolver


class Constraint(TypedDict):
    co: list[int]
    val: int


TestCase = tuple[list[int], list[Constraint], list[list[int]], list[int]]

run_cases: list[TestCase] = [
    (
        [-30, -60, -120],
        [
            {"co": [1, 0, 0], "val": 100},
            {"co": [0, 1, 0], "val": 25},
            {"co": [0, 0, 1], "val": 10},
            {"co": [1, 2, 3], "val": 150},
        ],
        [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 2, 3]],
        [100, 25, 10, 150],
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        [-10, -50, -100],
        [
            {"co": [1, 0, 0], "val": 100},
            {"co": [0, 1, 0], "val": 50},
            {"co": [0, 0, 1], "val": 20},
            {"co": [1, 2, 3], "val": 200},
        ],
        [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 2, 3]],
        [100, 50, 20, 200],
    ),
]


def test(
    coeffs: list[int],
    constraints: list[Constraint],
    expected_rows: list[list[int]],
    expected_constraints: list[int],
) -> bool:
    print("---------------------------------")
    print("- Coefficients:")
    print(
        f" ({coeffs[0]}*basic_subs) + ({coeffs[1]}*pro_subs) + ({coeffs[2]}*enterprise_subs) + profit = 0\n"
    )
    try:
        ss = SimplexSolver(coeffs)
        for constraint in constraints:
            print(f"Constraint:{constraint}")
            cs = []
            if constraint["co"][0] != 0:
                cs.append(f"basic_subs*{constraint['co'][0]}")
            if constraint["co"][1] != 0:
                cs.append(f"pro_subs*{constraint['co'][1]}")
            if constraint["co"][2] != 0:
                cs.append(f"enterprise_subs*{constraint['co'][2]}")
            together = " + ".join(cs)
            print(f" {together} must be less than or equal to {constraint['val']}\n")
            ss.add_constraint(constraint["co"], constraint["val"])

        print("Expected rows:")
        for row in expected_rows:
            print(f" {row}")
        actual_rows = ss.rows
        print("Actual rows:")
        for row in actual_rows:
            print(f" {row}")
        print("\n")
        print(f"Expected constraints: {expected_constraints}")
        actual_constraints = ss.constraints
        print(f"Actual constraints: {actual_constraints}")
        print(f"{ss}\n")
        if actual_constraints != expected_constraints or actual_rows != expected_rows:
            print("Fail")
            return False
        print("Pass")
        return True
    except Exception as e:
        print(f"Error: {e}")
        print("Fail")
        return False


def main() -> None:
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


def simplex_repr(self: SimplexSolver) -> str:
    final = "\nTableau:\n\n"
    for row in self.rows:
        for i in range(len(row)):
            row[i] = float(round(row[i], 1))
        final += " " + str(row) + "\n"
    for i in range(len(self.objective)):
        self.objective[i] = float(round(self.objective[i], 1))
    final += " " + str(self.objective) + "\n"
    return final


SimplexSolver.__repr__ = simplex_repr


test_cases: list[TestCase] = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
