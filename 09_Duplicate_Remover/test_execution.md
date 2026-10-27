# Test Execution Report — Duplicate Element Remover

- **Execution method:** Python 3, each test case run with scripted console input.
- **Cases executed:** 5
- **Passed:** 5
- **Failed:** 0
- **Result:** All listed cases passed.

## Results

| Case | Scenario | Status | Observed output / note |
|---|---|---|---|
| DR-01 | 1 2 2 3 1 | PASS | [1, 2, 3] |
| DR-02 | 5 5 5 | PASS | [5] |
| DR-03 | 1 2 3 | PASS | [1, 2, 3] |
| DR-04 | Empty list | PASS | Validation message |
| DR-05 | 0 -1 0 -1 | PASS | [-1, 0] (sorted) |

## Evidence

See [test_results.svg](./test_results.svg) for a visual summary of the console test run.


