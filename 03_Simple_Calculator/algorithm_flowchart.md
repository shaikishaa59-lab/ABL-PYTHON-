# Simple Calculator — Algorithm and Flowchart

## Algorithm
1. Start.
2. Read the first number, an arithmetic operator, and the second number.
3. If the operator is +, add the numbers.
4. Else if it is -, subtract the second number from the first.
5. Else if it is *, multiply the numbers.
6. Else if it is /, check whether the second number is zero. If it is zero, display a division-by-zero error; otherwise divide.
7. If the operator is not supported, display an invalid-operator message.
8. Stop.

## Flowchart
```mermaid
flowchart TD
 A([Start]) --> B[/Input first number, operator, second number/]
 B --> C{Operator is +?}
 C -- Yes --> D[Add numbers]
 C -- No --> E{Operator is -?}
 E -- Yes --> F[Subtract numbers]
 E -- No --> G{Operator is *?}
 G -- Yes --> H[Multiply numbers]
 G -- No --> I{Operator is /?}
 I -- No --> J[Display invalid operator]
 I -- Yes --> K{Second number is zero?}
 K -- Yes --> L[Display division by zero error]
 K -- No --> M[Divide numbers]
 D --> N[/Display result/]
 F --> N
 H --> N
 M --> N
 J --> O([Stop])
 L --> O
 N --> O
```
