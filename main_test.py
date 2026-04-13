from main import relax_edge

Input = tuple[dict[str, float], tuple[str, str], float]
Expected = tuple[bool, float]
TestCase = tuple[Input, Expected]

run_cases: list[TestCase] = [
    (
        ({"Cairo": 0, "Tanta": 10, "Alexandria": float("inf")}, ("Cairo", "Tanta"), 5),
        (True, 5),
    ),
    (
        (
            {"Houston": 0, "Austin": 7, "Dallas": float("inf")},
            ("Austin", "Dallas"),
            3,
        ),
        (True, 10),
    ),
    (
        ({"Chicago": 0, "Peoria": 3, "Urbana": float("inf")}, ("Chicago", "Peoria"), 5),
        (False, 3),
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        (
            {"Vienna": 0, "Salzburg": 10, "Graz": float("inf")},
            ("Vienna", "Salzburg"),
            -2,
        ),
        (True, -2),
    ),
    (
        ({"Paris": 0, "Lyon": 8, "Cannes": 5}, ("Lyon", "Cannes"), 3),
        (False, 5),
    ),
    (
        (
            {"Madrid": float("inf"), "Toledo": 5, "Bilbao": float("inf")},
            ("Madrid", "Toledo"),
            2,
        ),
        (False, 5),
    ),
]


def test(input: Input, expected: Expected) -> bool:
    try:
        print("---------------------------------")
        print(f"Current total distances from {next(iter(input[0]))}:")
        for node in input[0]:
            print(f"  - {node}: {input[0][node]}")

        print(
            f"\nChecking new path from {input[1][0]} to {input[1][1]} with distance {input[2]}"
        )

        relaxed = relax_edge(input[0], input[1][0], input[1][1], input[2])

        print(f"\nEdge relaxation expected? {expected[0]}")
        print(f"Edge relaxation found?    {relaxed}")
        if relaxed != expected[0]:
            print("Fail")
            return False

        print(f"\nExpected distance to {input[1][1]}: {expected[1]}")
        print(f"Actual distance to {input[1][1]}:   {input[0][input[1][1]]}")
        if input[0][input[1][1]] != expected[1]:
            print("\nFail")
            return False

        print("\nPass")
        return True

    except Exception as e:
        print(f"\nError: {e}")
        print("Fail")
        return False


def main():
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


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
