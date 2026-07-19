flowchart TD
    A[Start] --> |Accept input| B
    B{variable a */+- b} --> |True| C 
    B --> |False| D 
    C --> |result| E{return}
    D --> A