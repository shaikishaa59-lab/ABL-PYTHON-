# ABL Python Assignment — Test Execution Summary

**Execution date:** 2026-10-27  
**Method:** Each repository program was run under Python 3 with scripted console inputs, and output was checked against expected results. Visual test summaries and per-project Markdown reports are stored in each project folder.

## Overall results

- **Projects executed:** 10
- **Test cases executed:** 57
- **Passed:** 56
- **Failed:** 1
- **Overall:** Most tested behaviour passed; one input-validation issue remains.

| Project | Test cases | Passed | Failed | Evidence |
|---|---:|---:|---:|---|
| [01 Student Grade Calculator](./01_Student_Grade_Calculator/) | 7 | 7 | 0 | [Visual results](./01_Student_Grade_Calculator/test_results.svg) · [Report](./01_Student_Grade_Calculator/test_execution.md) |
| [02 Electricity Bill Calculator](./02_Electricity_Bill_Calculator/) | 6 | 6 | 0 | [Visual results](./02_Electricity_Bill_Calculator/test_results.svg) · [Report](./02_Electricity_Bill_Calculator/test_execution.md) |
| [03 Simple Calculator](./03_Simple_Calculator/) | 6 | 6 | 0 | [Visual results](./03_Simple_Calculator/test_results.svg) · [Report](./03_Simple_Calculator/test_execution.md) |
| [04 Attendance Checker](./04_Attendance_Checker/) | 6 | 6 | 0 | [Visual results](./04_Attendance_Checker/test_results.svg) · [Report](./04_Attendance_Checker/test_execution.md) |
| [05 Multiplication Table](./05_Multiplication_Table/) | 5 | 5 | 0 | [Visual results](./05_Multiplication_Table/test_results.svg) · [Report](./05_Multiplication_Table/test_execution.md) |
| [06 String Analyzer](./06_String_Analyzer/) | 5 | 5 | 0 | [Visual results](./06_String_Analyzer/test_results.svg) · [Report](./06_String_Analyzer/test_execution.md) |
| [07 Palindrome Checker](./07_Palindrome_Checker/) | 6 | 6 | 0 | [Visual results](./07_Palindrome_Checker/test_results.svg) · [Report](./07_Palindrome_Checker/test_execution.md) |
| [08 List Statistics](./08_List_Statistics/) | 5 | 5 | 0 | [Visual results](./08_List_Statistics/test_results.svg) · [Report](./08_List_Statistics/test_execution.md) |
| [09 Duplicate Remover](./09_Duplicate_Remover/) | 5 | 5 | 0 | [Visual results](./09_Duplicate_Remover/test_results.svg) · [Report](./09_Duplicate_Remover/test_execution.md) |
| [10 Student Records](./10_Student_Records/) | 6 | 5 | 1 | [Visual results](./10_Student_Records/test_results.svg) · [Report](./10_Student_Records/test_execution.md) |

## Failed test and recommended fix

**SR-06 — Non-numeric student marks:** entering `abc` for marks raises an unhandled `ValueError`. Add a `try/except ValueError` around numeric conversion and display a friendly validation message before marking this test as passed.

## Important notes

- Electricity-bill rates are illustrative, not official utility tariffs.
- Attendance eligibility uses the documented example threshold of 75%.
- These results reflect the tested input scenarios, not exhaustive proof that every possible input is safe.
