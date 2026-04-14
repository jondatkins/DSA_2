# AGENTS.md - DSA_2 Development Guidelines

## Project Overview

This is a Python project for a Boot.dev Data Structures and Algorithms course. It contains
algorithm implementations with a custom test harness. Current focus: Bellman-Ford algorithm
for finding shortest paths in graphs with negative weights and detecting negative cycles.

## Commands

### Running All Tests

```bash
python main_test.py
```

Runs all test cases in `submit_cases` (the default).

### Running Development Tests Only

```bash
python -c "__RUN__ = True; exec(open('main_test.py').read())"
```

Runs only the `run_cases` test cases for quick iteration.

### Running a Single Test

Option 1 - Edit main_test.py:
```python
test_cases = [submit_cases[0]]  # Run only the first test
```

Option 2 - Inline execution:
```bash
python -c "
import sys
sys.path.insert(0, '.')
from main_test import test, submit_cases
test(*submit_cases[0])
"
```

### Running Specific Tests by Index

```bash
python -c "
import sys
sys.path.insert(0, '.')
from main_test import test, submit_cases
for i in [0, 2]:  # Run tests 0 and 2
    print(f'Test {i}:')
    test(*submit_cases[i])
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
- No comments unless explaining complex logic

### Type Hints

Use inline type hints for all function parameters and return types:

```python
def bellman_ford(
    graph: dict[str, dict[str, int]],
    src: str,
    dest: str
) -> list[str] | str:
```

Use lowercase `dict[str, str]` syntax (Python 3.9+), not `Dict[str, str]`.

### Test Structure

This project uses a custom test framework with two test case lists:

```python
TestCase = tuple[dict[str, dict[str, int]], tuple[list[str | int], ...]]

run_cases: list[TestCase] = [...]  # Quick tests during development
submit_cases: list[TestCase] = run_cases + [...]  # Full test suite for submission
```

Test case format:
- First element: Graph as adjacency list `dict[node, dict[neighbor, weight]]`
- Second element: Tuple of test queries, each `[src, dest, expected]`

The `test()` function takes `(graph, tests)` and prints results.

### Imports

- Standard library imports first
- Third-party imports second (if any)
- Local imports third
- Always use absolute imports: `from main import bellman_ford`
- Blank line between import groups

```python
import heapq


def dijkstra(graph, src, dest):
    ...
```

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

### Naming Conventions

| Element | Convention | Example |
|---------|------------|---------|
| Functions | snake_case | `bellman_ford`, `relax_edge` |
| Variables | snake_case | `distances`, `count_node_visits` |
| Constants | SCREAMING_SNAKE | `FLOAT_INF = float('inf')` |
| Classes | PascalCase | `GraphNode`, `TestCase` |
| Files | snake_case | `main.py`, `dijkstra.py` |

### Function Design

- Keep functions focused and small (< 50 lines preferred)
- Use descriptive names for graph parameters: `graph`, `node`, `neighbor`, `weight`
- Return meaningful values or raise exceptions for error cases

### File Structure

| File | Purpose |
|------|---------|
| `main.py` | Current algorithm implementation to complete |
| `main_test.py` | Test cases and test runner |
| `dijkstra.py` | Reference implementations (Dijkstra algorithm) |
| `notes.md` | Course notes and hints (ignored by git) |

### Algorithm Patterns

This is a DSA course, expect implementations of:

- Graph algorithms (Bellman-Ford, Dijkstra, DFS, BFS)
- Shortest path algorithms
- Negative cycle detection
- Path reconstruction from predecessors

### Common Graph Representations

Adjacency list (most common in this project):
```python
graph = {
    "A": {"B": 5, "C": 2},  # node A connects to B (weight 5) and C (weight 2)
    "B": {"D": 1},
    "C": {},
    "D": {},
}
```

### Development Workflow

1. Read the function signature and understand inputs/outputs
2. Review test cases to understand expected behavior
3. Implement the algorithm
4. Run tests with `python -c "__RUN__ = True; exec(open('main_test.py').read())"`
5. Once all run_cases pass, run full submit_cases

### Notes

- The `.gitignore` ignores `notes.md` (personal notes, not for git)
- No pyproject.toml or setup.py configured
- No CI/CD pipeline configured
- Run tests frequently during development
