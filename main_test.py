from main import MinHeap

TestCase = tuple[tuple[tuple[int, str], str], ...]

run_cases: list[TestCase] = [
    (
        ((7, "East Pass"), "East Pass"),
        ((5, "Kingsroad"), "Kingsroad"),
        ((1, "Skirling Pass"), "Skirling Pass"),
        ((3, "The Hook"), "Skirling Pass"),
    ),
    (
        ((5, "Street of Steel"), "Street of Steel"),
        ((3, "Kingsroad"), "Kingsroad"),
        ((7, "Skirling Pass"), "Kingsroad"),
        ((1, "The Hook"), "The Hook"),
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        ((10, "Goldroad"), "Goldroad"),
        ((3, "Kingsroad"), "Kingsroad"),
        ((8, "Godsway"), "Kingsroad"),
        ((6, "East Pass"), "Kingsroad"),
        ((7, "Skirling Pass"), "Kingsroad"),
        ((2, "Boneway"), "Boneway"),
        ((1, "River Row"), "River Row"),
        ((7, "The Hook"), "River Row"),
        ((5, "Street of Steel"), "River Row"),
    ),
]


def test(inputs: TestCase) -> bool:
    print("---------------------------------")
    try:
        min_heap = MinHeap()
        print("Inputs:")
        for input, expected_output in inputs:
            priority, value = input
            print(f'- Pushing "{value}" with priority {priority}')
            min_heap.push(priority, value)
            print("- Peeking Heap:")
            print(f"Expecting: {expected_output}")
            result = min_heap.peek()
            print(f"Actual: {result}\n")
            if result != expected_output:
                print("Fail")
                return False
        print("Pass")
        return True
    except Exception as e:
        print(f"Error: {str(e)}")
        print("Fail")
        return False


def main():
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(test_case)
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
