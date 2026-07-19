Week 1: Variables, Types, Functions, and Conditions

## Projects

1. Interactive Calculator
2. Budget, Tax, and Tip Calculator

## Required Learning

* `print()`
* `input()`
* Variables
* Assignment
* Strings
* Integers
* Floats
* Booleans
* Type conversion
* Arithmetic operators
* Comparison operators
* Boolean operators
* Functions
* Parameters
* Return values
* `if`, `elif`, `else`
* String formatting
* Basic validation

## Required Reading and Viewing

* CS50P Week 0: Functions and Variables
* CS50P Week 1: Conditionals
* Automate Chapters 1, 2, and 4
* Python Tutorial Chapter 3 and Sections 4.1–4.2



## Day 1: Variables and Types

### Lesson objective

Understand how names refer to values and how types affect available operations.

### Guided examples

```python
name = "Ada"
age = 30
hourly_rate = 45.50
is_learning = True
```

### Exercises

1. Store and print a name, age, and city.
2. Convert a string containing `"42"` to an integer.
3. Calculate the area of a rectangle.
4. Calculate the average of three numbers.
5. Predict the result of adding strings versus integers.

### Interview questions

* What is a variable?
* What is the difference between `int` and `float`?
* What happens when `"2" + "3"` executes?
* What happens when `2 + 3` executes?

### Project contribution

Create the calculator repository and implement addition and subtraction.

---

## Day 2: Strings and Input

### Lesson objective

Accept user input and produce readable output.

### Learn

* `input()`
* `strip()`
* `lower()`
* `upper()`
* f-strings
* String indexing
* String length

### Exercises

1. Greeting generator
2. Initials generator
3. Username formatter
4. Sentence word counter
5. Temperature conversion

### Project contribution

Add multiplication, division, and a formatted result.

### Completion test

Build a temperature converter without notes.

---

## Day 3: Functions

### Lesson objective

Separate calculations from terminal interaction.

### Learn

* Function definition
* Parameters
* Arguments
* Return values
* Local scope
* Pure functions
* Function naming
* Docstrings

### Exercises

Write:

```python
def calculate_area(width: float, height: float) -> float:
    ...

def calculate_tip(total: float, rate: float) -> float:
    ...

def is_adult(age: int) -> bool:
    ...
```

### Project contribution

Refactor every calculator operation into its own function.

### Completion test

Explain why this is harder to test:

```python
def add():
    x = float(input("X: "))
    y = float(input("Y: "))
    print(x + y)
```

And why this is easier:

```python
def add(x: float, y: float) -> float:
    return x + y
```

---

## Day 4: Conditions and Validation

### Learn

* `if`
* `elif`
* `else`
* Comparison operators
* `and`
* `or`
* `not`
* Nested conditions
* Guard clauses

### Exercises

1. Positive, negative, or zero
2. Odd or even
3. Largest of three numbers
4. Grade classifier
5. Leap-year checker
6. Password-length validator

### Project contribution

Add:

* Division-by-zero handling
* Unsupported-operation handling
* Continue-or-exit behavior

---

## Day 5: Budget Calculator and Assessment

### Build

Create a second program that calculates:

* Bill subtotal
* Tax
* Tip
* Final total
* Number of people
* Amount per person
* Monthly projection

### Required tests

* Zero tip
* Decimal tax
* One person
* Several people
* Invalid negative bill
* Zero people

### Friday closed-book assessment

Build a program that:

1. Accepts three prices.
2. Rejects negative numbers.
3. Calculates subtotal and tax.
4. Applies a discount when subtotal exceeds a threshold.
5. Prints a formatted receipt.
