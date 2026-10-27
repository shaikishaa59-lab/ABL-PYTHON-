# ABL Python Assignment — Test Cases

This file records manual test cases for the ten programs in this repository. Run each program from its own folder with Python 3 and compare the observed output with the expected behaviour below. These are planned test cases; they are not a claim that every test has already been executed.

## General test approach
- Use valid, boundary, and invalid inputs where applicable.
- Check both the displayed result and that the program handles input as documented.
- If a program asks for numeric input, try a non-numeric value only if input validation is implemented; otherwise record that limitation rather than assuming it is handled.

## 01 — Student Grade Calculator
Assumptions: five subjects, each out of 100; a mark below 35 in any subject means Fail. Grade thresholds: A ≥ 90%, B ≥ 75%, C ≥ 60%, D ≥ 35%, otherwise F.

| ID | Input marks (five subjects) | Expected result |
|---|---|---|
| SG-01 | 95, 92, 90, 94, 89 | Total 460/500, 92.00%, Pass, Grade A |
| SG-02 | 80, 75, 78, 76, 81 | 78.00%, Pass, Grade B |
| SG-03 | 60, 62, 65, 61, 62 | 62.00%, Pass, Grade C |
| SG-04 | 40, 45, 50, 35, 55 | 45.00%, Pass, Grade D |
| SG-05 | 80, 80, 80, 80, 34 | Fail and Grade F because one subject is below 35 |
| SG-06 | Enter 101, then re-enter 75 for that subject | Reject 101 and ask for a valid mark; continue with valid marks |
| SG-07 | Enter 0 for all five subjects | 0.00%, Fail, Grade F |

## 02 — Electricity Bill Calculator
The rates are illustrative and must match the slab rates documented in this project's README; they are not presented as official utility tariffs.

| ID | Input | Expected result |
|---|---|---|
| EB-01 | 0 units | Bill is ₹0 (or the documented minimum charge, if the program defines one) |
| EB-02 | 1 unit | Bill follows the first slab |
| EB-03 | A value exactly at the first slab limit | Correct first-slab boundary calculation |
| EB-04 | A value just above the first slab limit | Excess units are charged using the next documented slab |
| EB-05 | A value spanning multiple slabs | Charges from all applicable slabs are added correctly |
| EB-06 | Negative units | Rejected or clearly identified as invalid if validation is implemented |

## 03 — Simple Calculator

| ID | Input / operation | Expected result |
|---|---|---|
| CAL-01 | 12 + 8 | 20 |
| CAL-02 | 12 - 8 | 4 |
| CAL-03 | 12 × 8 | 96 |
| CAL-04 | 12 ÷ 4 | 3 |
| CAL-05 | Any number ÷ 0 | Friendly error; no unhandled division-by-zero crash if guarded |
| CAL-06 | Unsupported operator such as % (if not supported) | Clear invalid-operation message |

## 04 — Attendance Eligibility Checker
Assumption: required attendance is 75%, as documented in the project README.

| ID | Input | Expected result |
|---|---|---|
| AT-01 | 90 classes attended, 100 conducted | 90%; eligible |
| AT-02 | 75 attended, 100 conducted | 75%; eligible at the threshold |
| AT-03 | 74 attended, 100 conducted | 74%; not eligible |
| AT-04 | 0 attended, 100 conducted | 0%; not eligible |
| AT-05 | 10 attended, 0 conducted | Avoid division by zero; report invalid total classes |
| AT-06 | Attended classes greater than conducted | Reject or flag inconsistent input if validation is implemented |

## 05 — Multiplication Table Generator

| ID | Input | Expected result |
|---|---|---|
| MT-01 | Number 5 | Displays 5 × 1 through 5 × 10 with correct products |
| MT-02 | Number 0 | Displays zero for all products |
| MT-03 | Number -3 | Displays mathematically correct negative products if negative input is allowed |
| MT-04 | Number 12 | Displays the table for 12 correctly |
| MT-05 | Non-integer input | Clear validation message if input validation is implemented |

## 06 — String Analyzer

| ID | Input string | Expected result |
|---|---|---|
| SA-01 | `Hello World` | Correct character count and documented counts for vowels/consonants/spaces |
| SA-02 | Empty string | Zero-length result; no crash |
| SA-03 | `Python123!` | Digits and punctuation handled according to the README's counting rules |
| SA-04 | `AEIOU` | Five vowels if vowel counting is case-insensitive |
| SA-05 | `  hi  ` | Spaces counted consistently with the documented rules |

## 07 — Palindrome Checker

| ID | Input | Expected result |
|---|---|---|
| PAL-01 | `madam` | Palindrome |
| PAL-02 | `level` | Palindrome |
| PAL-03 | `python` | Not a palindrome |
| PAL-04 | `Madam` | Result follows documented case-sensitivity rules |
| PAL-05 | `A man, a plan, a canal: Panama` | If punctuation/case are normalized, palindrome; otherwise result follows the README's stated rules |
| PAL-06 | Empty string | Behaviour is handled consistently and documented |

## 08 — List Statistics Calculator

| ID | Input list | Expected result |
|---|---|---|
| LS-01 | `[4, 2, 9, 1]` | Count 4, minimum 1, maximum 9, sum 16, average 4.0 (if these statistics are implemented) |
| LS-02 | `[7]` | Count 1, min/max/sum 7, average 7.0 |
| LS-03 | `[-3, 0, 3]` | Sum 0, average 0.0, min -3, max 3 |
| LS-04 | Empty list | No min/max/average crash; show a clear message or handle empty input |
| LS-05 | Repeated values `[2, 2, 2]` | Statistics reflect all three entries |

## 09 — Duplicate Element Remover

| ID | Input list | Expected result |
|---|---|---|
| DR-01 | `[1, 2, 2, 3, 1]` | Unique values `[1, 2, 3]` if first-occurrence order is preserved |
| DR-02 | `[5, 5, 5]` | `[5]` |
| DR-03 | `[1, 2, 3]` | List remains `[1, 2, 3]` |
| DR-04 | Empty list | Empty result, no crash |
| DR-05 | `[0, -1, 0, -1]` | `[0, -1]` if first-occurrence order is preserved |

## 10 — Student Records Using Lists and Tuples

| ID | Test action | Expected result |
|---|---|---|
| SR-01 | Add one student record | Name and associated fields are stored and displayed correctly |
| SR-02 | Add two different students | Both records are retained |
| SR-03 | Display records when records exist | All stored records display in the documented format |
| SR-04 | Display records before adding any | Clear empty-record message or empty collection display |
| SR-05 | Enter a name containing spaces | Full name is preserved if the program uses line-based input |
| SR-06 | Enter an invalid numeric field (if present) | Clear validation behaviour, if implemented |

## Test execution record

Fill this table after running the programs. Use **Pass**, **Fail**, or **Not run**; include notes for failures.

| Project | Test IDs executed | Status | Notes |
|---|---|---|---|
| 01 Student Grade Calculator | | Not run | |
| 02 Electricity Bill Calculator | | Not run | |
| 03 Simple Calculator | | Not run | |
| 04 Attendance Eligibility Checker | | Not run | |
| 05 Multiplication Table Generator | | Not run | |
| 06 String Analyzer | | Not run | |
| 07 Palindrome Checker | | Not run | |
| 08 List Statistics Calculator | | Not run | |
| 09 Duplicate Element Remover | | Not run | |
| 10 Student Records Using Lists and Tuples | | Not run | |
