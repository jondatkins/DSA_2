# AGENTS.md - DSA_2 Development Guidelines

## Project Overview

This is a Python project for a Boot.dev Data Structures and Algorithms course. It contains
algorithm implementations with a custom test harness.

## Commands

### Running Tests

```bash
python main_test.py
```

Run all test cases in `submit_cases` (the default).

```bash
python -c "__RUN__ = True; exec(open('main_test.py').read())"
```

Run only the `run_cases` test cases for quick iteration.

### Running a Single Test

To run a specific test case, modify `test_cases` in `main_test.py`:

```python
test_cases = [submit_cases[0]]  # Run only the first test
```

Or use the interactive approach:

```bash
python -c "
import sys
sys.path.insert(0, '.')
from main_test import test, submit_cases
test(*submit_cases[0])
"
```

### Development

No build system, linter, or type checker is configured. This is a vanilla Python project.

## Code Style

### General Guidelines

- Python 3.10+ with type hints
- 4-space indentation
- Snake_case for functions, variables, and file names
- PascalCase for classes (if any)
- Maximum line length: 100 characters (soft)

### Type Hints

Use inline type hints for all function parameters and return types:

```python
def get_path(dest: str, predecessors: dict[str, str]) -> list[str]:
```

Use `dict[str, str]` syntax (Python 3.9+), not `Dict[str, str]`.

### Test Structure

This project uses a custom test framework with two test case lists:

```python
run_cases: list[TestCase] = [...]  # Quick tests during development
submit_cases: list[TestCase] = [...] # Full test suite for submission
```

Test case format:

```python
TestCase = tuple[dest: str, predecessors: dict[str, str], expected: list[str]]
```

The `test()` function takes `(dest, predecessors, expected_output)` and prints results.

### Imports

- Standard library imports first
- Third-party imports second (if any)
- Local imports third
- Always use absolute imports: `from main import func`

### Error Handling

Wrap test execution in try/except to catch and report failures gracefully:

```python
try:
    result = function_under_test(*args)
    if result == expected:
        print("Pass")
        return True
except Exception as e:
    print(f"Fail: {e}")
    return False
```

### File Structure

- `main.py` - Main implementation code
- `main_test.py` - Test cases and test runner
- `__pycache__/` - Python bytecode (ignored)
- `myenv/` - Virtual environment (ignored)

## Algorithm Patterns

This is a DSA course, expect implementations of:

- Graph algorithms (traversal, shortest path, etc.)
- Data structure operations
- Backtracking and recursion
- Dynamic programming

The `predecessors` dictionary pattern suggests graph/path reconstruction algorithms,
where keys are nodes and values are their predecessors in a path.

## Notes

- The `.gitignore` is comprehensive but the project has no pyproject.toml or setup.py
- No CI/CD pipeline configured
- Run tests frequently during development to validate correctness
