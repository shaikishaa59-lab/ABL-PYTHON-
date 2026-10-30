# List Statistics Calculator — Algorithm and Flowchart

## Algorithm
1. Start.
2. Read numbers separated by spaces and split the input into parts.
3. If no numbers were entered, display a message asking for at least one number.
4. Otherwise convert each part to a number and store the values in a list.
5. Initialize total to 0, and largest and smallest to the first list item.
6. Visit each number: add it to total; update largest if it is greater; update smallest if it is smaller.
7. Calculate average = total ÷ number of items.
8. Display the list, sum, average, largest, and smallest values.
9. Stop.

## Flowchart
```mermaid
flowchart TD
 A([Start]) --> B[/Input numbers separated by spaces/]
 B --> C[Split input into parts]
 C --> D{Any values entered?}
 D -- No --> E[/Ask user to enter at least one number/]
 D -- Yes --> F[Convert parts into a number list]
 F --> G[Initialize total, largest and smallest]
 G --> H[Read next number]
 H --> I{More numbers?}
 I -- Yes --> J[Add to total and update largest and smallest]
 J --> H
 I -- No --> K[Calculate average]
 K --> L[/Display list, sum, average, largest and smallest/]
 E --> M([Stop])
 L --> M
```

*The algorithm assumes each entered item can be converted to a number.*
