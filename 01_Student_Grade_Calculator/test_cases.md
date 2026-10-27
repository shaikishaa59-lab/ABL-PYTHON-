# Test Cases — Student Grade Calculator

| Test | Subject marks | Expected output |
|---|---|---|
| 1 — Grade A | 90, 92, 88, 95, 91 | Total 456; 91.20%; Pass; Grade A |
| 2 — Grade B | 75, 76, 78, 80, 77 | Total 386; 77.20%; Pass; Grade B |
| 3 — Grade C | 60, 65, 62, 63, 61 | Total 311; 62.20%; Pass; Grade C |
| 4 — Grade D | 35, 35, 35, 35, 35 | Total 175; 35.00%; Pass; Grade D |
| 5 — Fail in one subject | 80, 70, 30, 90, 85 | Total 355; 71.00%; Fail; Grade F |
| 6 — Invalid high mark | Enter 101, then a valid mark | Program rejects 101 and asks for a valid mark |

## How to run

From this folder, run:

```bash
python main.py
```

Enter one mark at each prompt. For screenshots, capture the terminal showing the entered marks and final result.
