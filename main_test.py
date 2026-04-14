from main import PriorityQueue

TestCase = tuple[list[tuple[int, str]], list[str]]

run_cases: list[TestCase] = [
    (
        [
            (1, "Goldroad"),
            (5, "Kingsroad"),
            (10, "Prince's Pass"),
        ],
        [
            "Goldroad",
            "Kingsroad",
            "Prince's Pass",
        ],
    ),
    (
        [
            (7, "Kingsroad"),
            (5, "Godsway"),
            (2, "East Pass"),
        ],
        [
            "East Pass",
            "Godsway",
            "Kingsroad",
        ],
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        [
            (10, "Kingsroad"),
            (1, "Prince's Pass"),
            (3, "Goldroad"),
            (2, "Godsway"),
            (8, "Skirling Pass"),
            (7, "Boneway"),
            (6, "River Row"),
            (7, "The Hook"),
            (7, "Street of Steel"),
            (5, "East Pass"),
        ],
        [
            "Prince's Pass",
            "Godsway",
            "Goldroad",
            "East Pass",
            "River Row",
            "Boneway",
            "The Hook",
            "Street of Steel",
            "Skirling Pass",
            "Kingsroad",
        ],
    ),
]


def test(push_inputs: list[tuple[int, str]], expected_pops: list[str]) -> bool:
    try:
        print("---------------------------------")
        print("- Pushing inputs:")
        for delay, street in push_inputs:
            print(f"  - Delay: {delay}, Street: {street}")
        print("\n")
        print(f"Expected Pop Order: {expected_pops}")
        pq = PriorityQueue()
        for delay, street in push_inputs:
            pq.push(delay, street)
        results = []
        while not pq.empty():
            results.append(pq.pop())
        print(f"Actual: {results}\n")
        if results == expected_pops:
            print("Pass")
            return True
        print("Fail")
        return False
    except Exception as e:
        print(f"Error: {e}")
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
