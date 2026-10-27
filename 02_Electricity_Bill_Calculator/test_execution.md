# Test Execution Report — Electricity Bill Calculator

- **Execution method:** Python 3, each test case run with scripted console input.
- **Cases executed:** 6
- **Passed:** 6
- **Failed:** 0
- **Result:** All listed cases passed.

## Results

| Case | Scenario | Status | Observed output / note |
|---|---|---|---|
| EB-01 | 0 units | PASS | Rs. 0.00 |
| EB-02 | 1 unit | PASS | Rs. 2.00 |
| EB-03 | 100-unit boundary | PASS | Rs. 200.00 |
| EB-04 | 101 units | PASS | Rs. 203.00 |
| EB-05 | 350 units across slabs | PASS | Rs. 1350.00 |
| EB-06 | Negative units | PASS | Rejected |

## Evidence

See [test_results.svg](./test_results.svg) for a visual summary of the console test run.


