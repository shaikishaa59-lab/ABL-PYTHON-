# Test Execution Report — Student Records Using Lists and Tuples

- **Execution method:** Python 3, each test case run with scripted console input.
- **Cases executed:** 6
- **Passed:** 5
- **Failed:** 1
- **Result:** At least one case exposed a validation gap; see below.

## Results

| Case | Scenario | Status | Observed output / note |
|---|---|---|---|
| SR-01 | One student record | PASS | Record and highest scorer displayed |
| SR-02 | Two student records | PASS | Highest scorer Ravi |
| SR-03 | Display stored records | PASS | Records and highest marks displayed |
| SR-04 | Zero students | PASS | Validation message |
| SR-05 | Name with spaces | PASS | Full name preserved |
| SR-06 | Non-numeric marks | FAIL | FAIL: unhandled ValueError |

## Evidence

See [test_results.svg](./test_results.svg) for a visual summary of the console test run.

> **Follow-up needed:** The non-numeric marks test raises an unhandled `ValueError`. Add input validation before considering the project fully robust.

