# Student Grade Calculator — Algorithm and Flowchart

## Algorithm
1. Start.
2. Create an empty list to store marks.
3. Repeat for five subjects: read a mark; while it is below 0 or above 100, ask again; add the valid mark to the list.
4. Add all five marks to get the total and divide the total by 5 to calculate the percentage.
5. If any subject mark is below 35, display Fail and grade F.
6. Otherwise, assign grade A for 90% or above, B for 75% or above, C for 60% or above, and D for 35% or above.
7. Display total, percentage, result, and grade.
8. Stop.

## Flowchart
```mermaid
flowchart TD
 A([Start]) --> B[Create empty marks list]
 B --> C[Read mark for next subject]
 C --> D{Mark between 0 and 100?}
 D -- No --> E[Ask for mark again]
 E --> D
 D -- Yes --> F[Add mark to list]
 F --> G{Five marks entered?}
 G -- No --> C
 G -- Yes --> H[Calculate total and percentage]
 H --> I{Any mark below 35?}
 I -- Yes --> J[Display Fail and grade F]
 I -- No --> K{Percentage >= 90?}
 K -- Yes --> L[Display Pass, grade A]
 K -- No --> M{Percentage >= 75?}
 M -- Yes --> N[Display Pass, grade B]
 M -- No --> O{Percentage >= 60?}
 O -- Yes --> P[Display Pass, grade C]
 O -- No --> Q[Display Pass, grade D]
 J --> R([Stop])
 L --> R
 N --> R
 P --> R
 Q --> R
```
