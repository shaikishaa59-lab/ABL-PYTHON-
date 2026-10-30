# Electricity Bill Calculator — Algorithm and Flowchart

## Algorithm
1. Start.
2. Read the number of electricity units consumed.
3. If units are negative, display an error message.
4. Otherwise calculate the bill using the illustrative slabs: ₹2 per unit for the first 100 units; ₹3 per unit for units 101–200; ₹5 per unit for units 201–300; and ₹7 per unit above 300. Earlier slabs are charged cumulatively.
5. Display the units and bill amount.
6. Stop.

## Flowchart
```mermaid
flowchart TD
 A([Start]) --> B[/Input units consumed/]
 B --> C{Units < 0?}
 C -- Yes --> D[Display invalid units]
 C -- No --> E{Units <= 100?}
 E -- Yes --> F[Bill = units * 2]
 E -- No --> G{Units <= 200?}
 G -- Yes --> H[Bill = 200 + (units - 100) * 3]
 G -- No --> I{Units <= 300?}
 I -- Yes --> J[Bill = 500 + (units - 200) * 5]
 I -- No --> K[Bill = 1000 + (units - 300) * 7]
 F --> L[/Display bill/]
 H --> L
 J --> L
 K --> L
 D --> M([Stop])
 L --> M
```

*Note: These are illustrative assignment rates, not a statement of official electricity tariffs.*
