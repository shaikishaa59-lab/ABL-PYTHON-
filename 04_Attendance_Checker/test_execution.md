# Test Execution Report — Attendance Eligibility Checker

- **Execution method:** Python 3, each test case run with scripted console input.
- **Cases executed:** 6
- **Passed:** 6
- **Failed:** 0
- **Result:** All listed cases passed.

## Results

| Case | Scenario | Status | Observed output / note |
|---|---|---|---|
| AT-01 | 90% attendance | PASS | Eligible |
| AT-02 | 75% threshold | PASS | Eligible |
| AT-03 | 74% attendance | PASS | Not eligible |
| AT-04 | Zero attendance | PASS | Not eligible |
| AT-05 | Zero total classes | PASS | Validation message |
| AT-06 | Attended > total | PASS | Validation message |

## Evidence

See [test_results.svg](./test_results.svg) for a visual summary of the console test run.


