# Attendance Eligibility Checker — Algorithm and Flowchart

## Algorithm
1. Start.
2. Read total classes held and classes attended.
3. If total classes are zero or negative, display an error.
4. Else if attended classes are negative or greater than total classes, display invalid attendance.
5. Otherwise calculate attendance percentage = attended classes ÷ total classes × 100.
6. If percentage is at least 75, display Eligible; otherwise display Not eligible.
7. Stop.

## Flowchart
```mermaid
flowchart TD
 A([Start]) --> B[/Input total classes and attended classes/]
 B --> C{Total classes <= 0?}
 C -- Yes --> D[Display total classes error]
 C -- No --> E{Attended < 0 or attended > total?}
 E -- Yes --> F[Display invalid attendance]
 E -- No --> G[Calculate attendance percentage]
 G --> H{Percentage >= 75?}
 H -- Yes --> I[Display Eligible]
 H -- No --> J[Display Not eligible]
 D --> K([Stop])
 F --> K
 I --> K
 J --> K
```

*Note: The 75% eligibility threshold is an example used by this project.*
