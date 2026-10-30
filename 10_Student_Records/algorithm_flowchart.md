# Student Records — Algorithm and Flowchart

## Algorithm
1. Start.
2. Read the number of students.
3. If the count is zero or negative, display an error message.
4. Otherwise repeat for each student: read the student's name and marks; store them together as a tuple in the students list.
5. Display every student record.
6. Set the first student record as the current highest scorer.
7. Visit each student record. If the student's marks are greater than the current highest marks, update the highest scorer.
8. Display the highest scorer's name and marks.
9. Stop.

## Flowchart
```mermaid
flowchart TD
 A([Start]) --> B[/Input number of students/]
 B --> C{Count <= 0?}
 C -- Yes --> D[/Display invalid student count/]
 C -- No --> E[Create empty students list]
 E --> F[/Input student name and marks/]
 F --> G[Store name and marks as a tuple]
 G --> H{All students entered?}
 H -- No --> F
 H -- Yes --> I[/Display all student records/]
 I --> J[Set first record as highest scorer]
 J --> K[Check next student record]
 K --> L{More records?}
 L -- No --> M[/Display highest scorer and marks/]
 L -- Yes --> N{Current marks > highest marks?}
 N -- Yes --> O[Update highest scorer]
 N -- No --> K
 O --> K
 D --> P([Stop])
 M --> P
```

*Each record is stored as a tuple containing the student's name and marks.*
