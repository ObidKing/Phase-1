# Phase 1: Python and Software-Engineering Foundations

## Phase Objective

Progress from no programming experience to being able to:

* Design a medium-sized Python program before coding
* Divide a problem into functions, modules, and classes
* Use Python’s fundamental data structures confidently
* Read and write text, CSV, and JSON data
* Build command-line applications
* Handle errors correctly
* Write unit and integration tests
* Use Git branches, commits, and pull requests
* Debug unfamiliar code
* Explain time and space complexity
* Build reusable game engines
* Complete junior-level Python coding interviews
* Present a project in a technical interview

## Realistic Duration

| Track     | Weekly commitment | Phase 1 duration |
| --------- | ----------------: | ---------------: |
| Intensive |          40 hours |         10 weeks |
| Part-time |          20 hours |         20 weeks |
| Flexible  |          10 hours |      36–40 weeks |

A complete beginner should not try to finish all 15 projects in four or five weeks. The final projects require foundations that must first become automatic.

---

# 1. Core Learning Resources

## Resource R1: CS50’s Introduction to Programming with Python

Use CS50P as the primary video course. It contains lessons on functions and variables, conditionals, loops, exceptions, libraries, unit testing, file input/output, regular expressions, object-oriented programming, and additional Python features. The course is designed for learners with or without prior programming experience.

Complete:

* Week 0: Functions and Variables
* Week 1: Conditionals
* Week 2: Loops
* Week 3: Exceptions
* Week 4: Libraries
* Week 5: Unit Tests
* Week 6: File I/O
* Week 7: Regular Expressions
* Week 8: Object-Oriented Programming
* Week 9: Et Cetera

For every CS50P lesson:

1. Watch the lecture.
2. Watch relevant short videos.
3. Reproduce examples without copying.
4. Complete at least two associated problems.
5. Rewrite one solution from memory after 48 hours.

---

## Resource R2: Official Python Tutorial

Use the official Python tutorial as the language reference beside CS50P. It covers control flow, data structures, modules, files, errors, exceptions, and classes. Because the tutorial assumes some general programming familiarity, read it after watching the corresponding beginner lesson rather than using it as your first explanation.

Complete these chapters:

* Chapter 3: An Informal Introduction to Python
* Chapter 4: More Control Flow Tools
* Chapter 5: Data Structures
* Chapter 6: Modules
* Chapter 7: Input and Output
* Chapter 8: Errors and Exceptions
* Chapter 9: Classes
* Chapter 10: Brief Tour of the Standard Library

Do not attempt to memorize the documentation. Practice locating answers quickly.

---

## Resource R3: Automate the Boring Stuff with Python, Third Edition

Use this as the practical beginner textbook. The third edition provides chapters on Python basics, flow control, loops, functions, debugging, lists, dictionaries, strings, regular expressions, files, command-line applications, and structured data formats.

Required chapters for Phase 1:

1. Python Basics
2. `if`/`else` and Flow Control
3. Loops
4. Functions
5. Debugging
6. Lists
7. Dictionaries and Structuring Data
8. Strings and Text Editing
9. Regular Expressions
10. Reading and Writing Files
11. Organizing Files
12. Designing and Deploying Command-Line Programs
13. CSV, JSON, and XML Files

For every chapter:

* Type each important example manually.
* Change at least three values or conditions.
* Predict the output before running it.
* Complete the practice questions.
* Build one 20–40-line variation not shown in the book.

---

## Resource R4: Pro Git

Use Chapters 1–3 of the freely available Pro Git book for version-control foundations. These chapters cover installation and configuration, creating repositories, tracking changes, commit history, undoing changes, remotes, branches, and merges.

Complete:

* Chapter 1: Getting Started
* Chapter 2: Git Basics
* Chapter 3.1–3.3: Branch fundamentals, merging, and branch management

---

## Resource R5: pytest Documentation

Use the official pytest documentation for creating tests, running test suites, checking expected exceptions, fixtures, parametrized tests, temporary files, and test organization.

Required sections:

* Get Started
* Create your first test
* Run multiple tests
* Assert that an exception is raised
* Assertions
* Parametrized tests
* Fixtures
* Temporary directories and files
* Good integration practices

---

## Resource R6: Python Environments and Packaging

Follow the Python Packaging User Guide to create isolated virtual environments and install dependencies with `pip`.

You must understand:

```text
python -m venv .venv
.venv\Scripts\activate
python -m pip install pytest
python -m pip freeze
```

---

## Resource R7: Command-Line Applications

Use the official `argparse` tutorial when building the task manager and tournament platform. It demonstrates how to define positional arguments, optional arguments, and command-line behavior.

---

## Resource R8: Logging

Use Python’s standard `logging` module instead of filling larger projects with `print()` statements. The standard logging system allows application modules to participate in one consistent logging system.

---

## Resource R9: Paths and Files

Use `pathlib.Path` for most file and directory operations. The official documentation provides platform-aware path objects and file-system operations.

---

## Resource R10: Classes, Dataclasses, Enums, and Type Hints

The official class tutorial explains how classes bundle state and behavior. Use `dataclasses` for simple data-focused objects, `Enum` for fixed values such as suits and ranks, and type hints to communicate expected input and return types. Python does not enforce type annotations at runtime, but development tools can use them to check and explain code.

---

# 2. Daily Study Structure

## Intensive Daily Schedule

| Block                 |        Time | Activity                              |
| --------------------- | ----------: | ------------------------------------- |
| Lesson                |  90 minutes | Course lecture and structured notes   |
| Guided coding         |  90 minutes | Reproduce and modify lesson examples  |
| Interview drill       |  60 minutes | One or two focused problems           |
| Project development   |     3 hours | Build the current project             |
| Testing and debugging |  60 minutes | Tests, bug investigation, refactoring |
| Git and reflection    |  30 minutes | Commit, journal, README, explanation  |
| **Total**             | **8 hours** |                                       |

## Weekly Pattern

### Monday

Learn the core concept and complete small exercises.

### Tuesday

Learn the second concept and begin a small project.

### Wednesday

Add data structures and complete interview exercises.

### Thursday

Refactor, validate inputs, and write tests.

### Friday

Finish the project, demonstrate it, update documentation, and complete a closed-book test.

---

# 3. Project Rules

Before coding any project, create `DESIGN.md` containing:

1. Problem statement
2. Intended user
3. User stories
4. Functional requirements
5. Inputs
6. Outputs
7. Rules
8. Edge cases
9. Data structures
10. Proposed functions
11. Proposed classes
12. Pseudocode
13. Test cases
14. Known limitations
15. Stretch goals

For each major project, include:

```text
project-name/
├── README.md
├── DESIGN.md
├── CHANGELOG.md
├── pyproject.toml
├── src/
├── tests/
└── docs/
```

## AI Usage Rule

You may ask AI to:

* Explain an error message
* Give a hint
* Review code you already wrote
* Generate additional test cases
* Compare two designs
* Explain documentation

You may not ask AI to generate the complete project before attempting it.

Required sequence:

1. Write your design.
2. Write pseudocode.
3. Attempt the implementation.
4. Record the failure.
5. Ask for a hint.
6. Repair the code yourself.
7. Explain the final solution without AI.

---

# 4. Week 0: Environment and Programming Orientation

## Objective

Prepare the computer, terminal, editor, Git, and learning workflow.

## Lessons

* What programming is
* Source code versus program execution
* Python interpreter
* Files and folders
* Terminal commands
* Editor versus terminal
* Syntax errors versus runtime errors
* How to read tracebacks
* Git repositories
* Virtual environments

## Required Reading

* CS50P introduction and course workflow
* Pro Git Chapter 1
* Python Packaging virtual-environment guide

## Windows Setup

Install and verify:

```text
Python
Git
Visual Studio Code
VS Code Python extension
```

Run:

```powershell
python --version
git --version
mkdir python-phase-one
cd python-phase-one
python -m venv .venv
.venv\Scripts\activate
python -m pip install pytest
git init
```

## Day 1

### Lesson

* What code is
* How Python runs a file
* Terminal navigation
* Creating and saving `.py` files

### Coding laboratory

Create:

```python
print("Hello, Python")
print("I am beginning Phase 1")
```

Run it from the terminal.

### Exercises

1. Print your name.
2. Print three separate sentences.
3. Print a simple text menu.
4. Intentionally create a syntax error.
5. Write down what each traceback line means.

### Output

* `hello.py`
* `error_journal.md`
* First Git commit

---

## Day 2

### Lesson

* Git repository
* Working directory
* Staging area
* Commit
* Commit history
* `.gitignore`

### Laboratory

Create a repository and make three separate commits.

```text
chore: initialize Python project
feat: add first Python script
docs: add learning journal
```

### Completion test

Explain the difference between:

* File save
* Git add
* Git commit
* Git push

---

# 5. Week 1: Variables, Types, Functions, and Conditions

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

### Week 1 exit criteria

* [ ] I can explain all basic Python types.
* [ ] I can write and call functions.
* [ ] I understand return values.
* [ ] I can write conditions without copying.
* [ ] I can validate simple input.
* [ ] Both projects contain tests.
* [ ] I can rebuild the calculator in under 90 minutes.

---

# 6. Week 2: Loops, Lists, Randomness, and Decomposition

## Projects

3. Number-Guessing Tournament
4. Quiz and Flashcard Engine

## Required Learning

* `for`
* `while`
* `range`
* `break`
* `continue`
* Loop counters
* Accumulators
* Lists
* Indexes
* Slices
* List methods
* Nested loops
* Random number generation
* Loop termination
* Function decomposition

## Required Reading and Viewing

* CS50P Week 2: Loops
* Automate Chapters 3, 4, and 6
* Python Tutorial Sections 4.2–4.9 and 5.1
* Python `random` module introduction. The module supplies pseudorandom choices, sampling, shuffling, and seeding useful for games and repeatable tests.

## Day 1: `for` Loops

### Exercises

1. Print numbers 1–20.
2. Print even numbers.
3. Sum numbers 1–100.
4. Print a multiplication table.
5. Count vowels in a string.
6. Find the largest number in a list without using `max()`.

### Project contribution

Create a repeated-round structure for the guessing game.

---

## Day 2: `while` Loops

### Learn

* Condition-controlled repetition
* Sentinel values
* Infinite loops
* Off-by-one errors
* Attempt counters

### Exercises

1. Password retry system
2. Countdown
3. Menu loop
4. Number input validator
5. Savings-goal simulator

### Project contribution

Add limited guesses, higher/lower hints, and replay.

---

## Day 3: Lists

### Learn

* Creating lists
* Index access
* Mutation
* Append and remove
* Slicing
* Iteration
* Membership
* Copying versus aliasing

### Exercises

1. Find second-largest number.
2. Reverse a list manually.
3. Remove duplicates without `set`.
4. Rotate a list.
5. Calculate running totals.
6. Separate positive and negative values.

### Project contribution

Store round scores and show a tournament scoreboard.

---

## Day 4: Quiz Engine

### Build

Represent questions as dictionaries inside a list:

```python
questions = [
    {
        "prompt": "What does len() return?",
        "options": ["A number", "A string", "A list"],
        "answer": "A number",
    }
]
```

### Features

* Random order
* Multiple-choice questions
* Free-text questions
* Score
* Incorrect-answer review
* Percentage result

---

## Day 5: Testing and Review

### Assessment

Build a menu-driven application that:

* Displays five menu options
* Repeats until the user exits
* Records every selection
* Prints a summary
* Rejects invalid choices

### Week 2 exit criteria

* [ ] I know when to use `for` versus `while`.
* [ ] I can identify an infinite loop.
* [ ] I understand list mutation.
* [ ] I can divide a game into functions.
* [ ] I can test seeded random behavior.
* [ ] I can solve easy loop and list problems.

---

# 7. Week 3: Strings, Dictionaries, Sets, and Game State

## Projects

5. Hangman
6. Tic-Tac-Toe

## Required Learning

* Advanced string operations
* Tuples
* Dictionaries
* Sets
* Membership lookup
* Frequency counting
* Nested data
* Grid representation
* Game state
* State transitions
* Win-condition algorithms

## Required Reading and Viewing

* Automate Chapters 6, 7, and 8
* Python Tutorial Chapter 5
* Review CS50P loops and conditionals

## Day 1: Strings

### Exercises

1. Reverse words in a sentence.
2. Check for a palindrome.
3. Count each character.
4. Find the first nonrepeating character.
5. Normalize whitespace.
6. Create a simple password-strength checker.

### Hangman contribution

Implement:

```python
def reveal_word(secret: str, guesses: set[str]) -> str:
    ...

def is_complete(secret: str, guesses: set[str]) -> bool:
    ...
```

---

## Day 2: Dictionaries

### Exercises

1. Character-frequency table
2. Word-frequency table
3. Student-grade lookup
4. Product inventory
5. Two Sum
6. Group words by first letter

### Interview emphasis

Explain why dictionary lookup is generally preferable to repeatedly scanning a list for keyed information.

---

## Day 3: Sets and Tuples

### Exercises

1. Find common values in two lists.
2. Find values present in only one list.
3. Remove duplicates.
4. Track unique guesses.
5. Represent an immutable coordinate with a tuple.

### Hangman contribution

Complete duplicate-guess handling and attempted-letter tracking.

---

## Day 4: Tic-Tac-Toe State

### Learn

* Flat list representation
* Nested-list representation
* Board coordinates
* Legal moves
* Player turns

### Build

```python
board = [" "] * 9
```

Implement:

```python
def place_move(board: list[str], position: int, symbol: str) -> None:
    ...

def available_moves(board: list[str]) -> list[int]:
    ...

def check_winner(board: list[str]) -> str | None:
    ...
```

---

## Day 5: Win Detection and Review

### Tests

* Every row win
* Every column win
* Both diagonals
* Full-board draw
* Occupied square
* Invalid index
* Turn switching

### Week 3 exit criteria

* [ ] I can select between list, tuple, dictionary, and set.
* [ ] I can represent program state.
* [ ] I can implement game rules separately from input.
* [ ] I can explain Tic-Tac-Toe win detection.
* [ ] I can solve frequency-counting problems.

---

# 8. Week 4: Files, JSON, CSV, Paths, and Text Processing

## Projects

7. Contact Book
8. Text and Log Analyzer

## Required Learning

* Opening and closing files
* Context managers
* Reading line by line
* Writing files
* Character encodings
* `pathlib`
* JSON serialization
* CSV
* Regular expressions
* Data normalization
* Sorting with `key`
* Handling missing files

## Required Reading and Viewing

* CS50P Week 6: File I/O
* CS50P Week 7: Regular Expressions
* Automate Chapters 8, 9, 10, and 18
* Python Tutorial Chapter 7
* Official `pathlib` documentation

## Day 1: Text Files

### Exercises

1. Count file lines.
2. Count file words.
3. Copy a text file.
4. Find lines containing a keyword.
5. Write a Markdown summary.

### Log Analyzer contribution

Read one file line by line without loading the entire file.

---

## Day 2: JSON

### Learn

* Python dictionaries versus JSON objects
* Serialization
* Deserialization
* Missing or corrupt files
* Default application state

### Contact Book contribution

Store contacts in a JSON file.

---

## Day 3: CSV

### Exercises

1. Read transaction records.
2. Calculate totals.
3. Group rows by category.
4. Export a report.
5. Reject malformed rows.

### Contact Book contribution

Add CSV import and export.

---

## Day 4: Regular Expressions

### Learn

* Literal matching
* Character classes
* Repetition
* Groups
* Anchors
* Raw strings
* Validation limitations

### Exercises

1. Extract email-like strings.
2. Parse timestamps.
3. Find error codes.
4. Normalize phone numbers.
5. Detect repeated whitespace.

### Log Analyzer contribution

Extract:

* Timestamps
* Severity levels
* Error codes
* Frequent messages

---

## Day 5: Reporting and Assessment

### Contact Book requirements

* Add
* List
* Search
* Update
* Delete
* JSON persistence
* CSV export
* Duplicate prevention

### Log Analyzer requirements

* Line count
* Severity count
* Word frequency
* Error extraction
* Date grouping
* Markdown report

### Week 4 exit criteria

* [ ] I can read large files one line at a time.
* [ ] I understand JSON and CSV differences.
* [ ] I handle missing and corrupt files.
* [ ] I use `Path` instead of hard-coded separators.
* [ ] I can explain serialization.
* [ ] Both applications preserve data correctly.

---

# 9. Week 5: Exceptions, Modules, CLI Applications, Git, and Logging

## Projects

9. Expense Tracker
10. Command-Line Task Manager

## Required Learning

* Exception types
* `try`, `except`, `else`, `finally`
* Raising exceptions
* Custom exceptions
* Modules
* Packages
* Imports
* Main guard
* Virtual environments
* Dependencies
* `argparse`
* Logging
* Git branches
* Pull requests
* Merge conflicts
* Refactoring

## Required Reading and Viewing

* CS50P Week 3: Exceptions
* CS50P Week 4: Libraries
* Automate Chapters 5, 11, and 12
* Python Tutorial Chapters 6 and 8
* Pro Git Chapters 2 and 3
* Python Packaging virtual-environment guide
* Official argparse tutorial
* Official logging documentation

## Day 1: Exceptions

### Exercises

1. Safe integer parser
2. Safe division
3. Missing-file handler
4. Invalid-date handler
5. Custom `InvalidTransactionError`

### Rule

Never use this without a strong reason:

```python
except:
    pass
```

### Expense Tracker contribution

Validate:

* Amount
* Date
* Category
* Transaction type

---

## Day 2: Modules and Packages

Refactor from:

```text
expense_tracker.py
```

Into:

```text
expense_tracker/
├── cli.py
├── models.py
├── services.py
├── storage.py
├── reports.py
└── exceptions.py
```

### Completion test

Explain:

* Module
* Package
* Import
* Main guard
* Circular import

---

## Day 3: CLI Design

### Task Manager commands

```bash
python -m task_manager add "Study dictionaries"
python -m task_manager list
python -m task_manager complete 3
python -m task_manager search "Python"
python -m task_manager delete 3
```

### Learn

* Positional arguments
* Optional flags
* Subcommands
* Help messages
* Exit codes

---

## Day 4: Logging and Git Branches

### Add logging

```python
logger.info("Task created")
logger.warning("Attempted to complete missing task")
logger.exception("Unable to load task file")
```

### Git exercise

Create branches:

```text
feature/task-search
feature/json-storage
test/task-service
```

Merge each through a pull request.

---

## Day 5: Integration Assessment

### Required functionality

* Task IDs
* Status
* Priority
* Due date
* Search
* Sorting
* JSON persistence
* CLI
* Logging
* Custom exceptions
* At least 25 tests

### Week 5 exit criteria

* [ ] I create a virtual environment for every project.
* [ ] I understand exception flow.
* [ ] I can create modules and packages.
* [ ] I can build a multi-command CLI.
* [ ] I use meaningful Git branches and commits.
* [ ] I can resolve a simple merge conflict.
* [ ] I can explain the Task Manager architecture.

---

# 10. Week 6: Object-Oriented Programming and Card Modeling

## Project

11. Reusable Playing-Card and Deck Library

## Required Learning

* Classes
* Objects
* Instance attributes
* Class attributes
* Methods
* Constructors
* Encapsulation
* Composition
* Inheritance
* Polymorphism
* Dataclasses
* Enums
* Immutability
* Type hints
* Dunder methods

## Required Reading and Viewing

* CS50P Week 8: Object-Oriented Programming
* Python Tutorial Chapter 9
* Official classes tutorial
* Official `dataclasses`, `enum`, and `typing` references

## Day 1: Classes and Objects

Build:

```python
class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.score = 0

    def add_score(self, points: int) -> None:
        self.score += points
```

### Exercises

1. Bank account
2. Rectangle
3. Student
4. Inventory item
5. Dice

---

## Day 2: Dataclasses and Enums

Design:

```python
from dataclasses import dataclass
from enum import Enum


class Suit(Enum):
    CLUBS = "clubs"
    DIAMONDS = "diamonds"
    HEARTS = "hearts"
    SPADES = "spades"


@dataclass(frozen=True)
class Card:
    rank: str
    suit: Suit
```

### Explain

* Why `Card` is immutable
* Why suits are an enum
* Why cards do not inherit from strings
* Why a deck contains cards

---

## Day 3: Composition

Build:

```text
Deck contains Card objects
Hand contains Card objects
Player contains a Hand
Game contains Players and a Deck
```

### Interview question

Why should `Deck` generally use composition rather than inherit directly from `list`?

---

## Day 4: Dunder Methods and Comparison

Implement:

* `__str__`
* `__repr__`
* `__len__`
* `__eq__`

Do not implement ordering until you have defined what card ordering means for the game.

---

## Day 5: Card Library Assessment

### Required tests

* Exactly 52 cards
* All cards unique
* Shuffle preserves membership
* Deal removes cards
* Reset restores deck
* Empty-deck error
* Multiple-deck configuration

### Week 6 exit criteria

* [ ] I can explain class versus object.
* [ ] I understand composition.
* [ ] I use inheritance only when behavior is genuinely shared.
* [ ] I can create immutable data objects.
* [ ] I understand that type hints are not runtime validation.
* [ ] The card library can be reused without terminal input code.

---

# 11. Week 7: Testing, Debugging, and Blackjack

## Project

12. Blackjack

## Required Learning

* Test design
* Arrange-Act-Assert
* Unit tests
* Integration tests
* Parametrized tests
* Fixtures
* Testing exceptions
* Testing randomness
* Dependency injection
* Debuggers
* Breakpoints
* Logging
* Regression tests
* Refactoring

## Required Reading and Viewing

* CS50P Week 5: Unit Tests
* pytest Get Started
* pytest assertions
* pytest parametrization
* pytest fixtures
* pytest temporary paths
* Automate Chapter 5: Debugging

## Day 1: Unit Testing

Write tests for the card library before adding game behavior.

```python
def test_new_deck_contains_52_unique_cards():
    ...

def test_deal_reduces_deck_size():
    ...

def test_empty_deck_raises_error():
    ...
```

---

## Day 2: Blackjack Scoring

Implement score calculation separately from the game loop.

Required cases:

* No ace
* One ace
* Multiple aces
* Blackjack
* Bust
* Ace changes from 11 to 1

### Key tests

```python
def test_ace_and_king_is_blackjack():
    ...

def test_two_aces_and_nine_equals_twenty_one():
    ...

def test_ace_is_reduced_to_avoid_bust():
    ...
```

---

## Day 3: Dealer and Player Behavior

Separate:

* Player choices
* Dealer policy
* Hand scoring
* Round outcome
* Bankroll
* Terminal interface

---

## Day 4: Debugging Laboratory

Plant and repair:

1. A duplicated-card bug
2. Incorrect ace handling
3. Dealer stopping too early
4. Bankroll not updating
5. Round state not resetting

For each bug, record:

```text
Observed behavior
Expected behavior
Reproduction steps
Root cause
Fix
Regression test
```

---

## Day 5: Blackjack Demonstration

### Required tests

At least 35 meaningful tests.

### Demonstration

Explain:

* Class relationships
* Ace logic
* Dealer behavior
* Test strategy
* One difficult bug
* One design refactor

### Week 7 exit criteria

* [ ] I can write tests before code.
* [ ] I can test randomness deterministically.
* [ ] I understand unit versus integration tests.
* [ ] I can reproduce bugs consistently.
* [ ] Every repaired bug has a regression test.
* [ ] I can explain Blackjack without reading the code.

---

# 12. Week 8: Algorithms, Complexity, and Poker Evaluation

## Project

13. Poker Hand Evaluator

## Required Learning

* Time complexity
* Space complexity
* Linear search
* Binary search concept
* Sorting
* Frequency counting
* Hash-table lookup
* Stack and queue concepts
* Combinations
* Comparison keys
* Tie-breaking
* Refactoring long condition chains

## Day 1: Complexity Foundations

Analyze:

```python
for item in items:
    print(item)
```

```python
for left in items:
    for right in items:
        print(left, right)
```

```python
if target in lookup_set:
    ...
```

Explain:

* Input size
* Number of operations
* Additional memory
* Best and worst cases

---

## Day 2: Frequency-Based Algorithms

Using dictionaries, calculate:

```python
{
    14: 2,
    10: 1,
    7: 2
}
```

Use this information to detect:

* Pair
* Two pair
* Three of a kind
* Full house
* Four of a kind

---

## Day 3: Straights and Flushes

Implement and test:

* Standard straight
* Ace-high straight
* Ace-low straight
* Flush
* Straight flush

### Common error

Treating an ace as only high or only low.

---

## Day 4: Comparable Hand Scores

Return a comparison structure such as:

```python
(
    category,
    primary_rank_values,
    kicker_values,
)
```

Two hands should be comparable without a giant collection of special-case statements.

---

## Day 5: Poker Assessment

### Required tests

At least 50 tests covering:

* Every category
* All major tie-breaks
* Ace-low straight
* Equal pairs
* Two-pair ordering
* Kicker ordering
* Invalid duplicates
* Wrong hand size

### Interview questions

* Why use a rank-frequency dictionary?
* What is the complexity of evaluating five cards?
* How are ties broken?
* How would seven-card evaluation change the problem?
* How did you avoid one enormous conditional?

### Week 8 exit criteria

* [ ] I can state basic time and space complexity.
* [ ] I can use counting to simplify classification.
* [ ] I can create sortable comparison keys.
* [ ] I can test difficult boundary cases.
* [ ] I can solve easy dictionary and list interview problems.

---

# 13. Week 9: State Machines, Simulation, and Texas Hold’em

## Project

14. Texas Hold’em Simulator

## Required Learning

* State machines
* Game phases
* Legal-state transitions
* Player actions
* Pot calculation
* Best-five-from-seven evaluation
* Combinations
* Simulation
* Reproducible randomness
* Separation of policy and rules
* Persistence

## Day 1: Game State Design

Define states:

```text
WAITING
PRE_FLOP
FLOP
TURN
RIVER
SHOWDOWN
COMPLETE
```

Define legal transitions between them.

---

## Day 2: Player Actions

Model:

```text
CHECK
CALL
BET
RAISE
FOLD
ALL_IN
```

For each state, define:

* Legal actions
* Required amount
* State changes
* Validation failures

---

## Day 3: Best Hand from Seven Cards

Start with the simple correct method:

1. Generate every five-card combination from seven cards.
2. Evaluate each five-card hand.
3. Select the maximum score.

After it works, discuss performance improvements.

---

## Day 4: Reproducible Simulation

Create seeded simulations for:

* Two players
* Six players
* Repeated games
* Win-frequency estimates
* Tie-frequency estimates

Keep computer-player strategy separate from game rules.

---

## Day 5: Hold’em Assessment

### Required demonstration

* Deal hole cards
* Reveal flop, turn, and river
* Accept legal actions
* Reject illegal actions
* Evaluate winners
* Print hand history
* Reproduce a game from a fixed seed

### Week 9 exit criteria

* [ ] I can model a state machine.
* [ ] I can explain every legal game transition.
* [ ] I separate rules from player strategy.
* [ ] I can evaluate seven-card poker hands.
* [ ] I can produce deterministic simulations.
* [ ] I can explain current limitations, including side pots.

---

# 14. Week 10: Architecture, Capstone, and Interviews

## Project

15. Card-Game Tournament Platform

## Required Learning

* Application architecture
* Interfaces
* Abstract responsibilities
* Reuse
* Dependency direction
* Configuration
* Persistence
* Integration tests
* Benchmarking
* CLI design
* Documentation
* Technical demonstrations
* Interview communication

## Day 1: Architecture Design

Create:

```text
cards/
games/
players/
tournament/
storage/
cli/
tests/
```

Define the responsibility of every directory before implementation.

---

## Day 2: Shared Game Interface

Design common operations:

```python
class Game:
    def start(self) -> None:
        ...

    def take_turn(self) -> None:
        ...

    def is_complete(self) -> bool:
        ...

    def get_result(self):
        ...
```

Do not force unrelated games into an interface that does not fit. Document where the abstraction works and where it becomes awkward.

---

## Day 3: Tournament and Leaderboard

Implement:

* Player registration
* Match scheduling
* Match results
* Wins
* Losses
* Draws
* Points
* Leaderboard sorting
* Tournament persistence

---

## Day 4: Integration Testing

Write tests for:

1. Registering several players
2. Starting a tournament
3. Running multiple game types
4. Recording results
5. Saving the tournament
6. Reloading it
7. Continuing the tournament
8. Producing a final leaderboard

---

## Day 5: Final Demonstration and Interview

### Demonstration structure

1. Problem
2. Requirements
3. Architecture
4. Data model
5. Game abstraction
6. Testing strategy
7. Difficult bug
8. Performance
9. Limitations
10. Next version

### Final capstone requirements

* 300–500 or more lines of application code
* 50 or more tests
* Type hints
* Logging
* Custom exceptions
* JSON persistence
* CLI
* Unit tests
* Integration tests
* Architecture diagram
* Benchmark
* README
* Design document
* Changelog
* Demo video

---

# 15. Coding Interview Plan

## Weekly Problem Targets

| Week      | Focus                           | Problems |
| --------- | ------------------------------- | -------: |
| 1         | Conditions, arithmetic, strings |        6 |
| 2         | Loops and lists                 |        8 |
| 3         | Dictionaries, sets, game state  |        8 |
| 4         | Files and text processing       |        6 |
| 5         | Errors, modules, CLI debugging  |        6 |
| 6         | Object-oriented design          |        6 |
| 7         | Testing and debugging           |        8 |
| 8         | Arrays, hashing, sorting        |       10 |
| 9         | Simulations and state machines  |        6 |
| 10        | Mixed mock interviews           |        8 |
| **Total** |                                 |   **72** |

## Required Coding Patterns

You must be able to recognize and use:

* Counter
* Accumulator
* Boolean flag
* Frequency dictionary
* Membership set
* Running minimum or maximum
* Two pointers
* Stack
* Queue
* Sorting with a key
* Grid traversal
* State machine
* Simulation loop
* Validation guard
* Comparison tuple

---

# 16. Weekly Lesson Assessment

At the end of every week, complete these seven assessments.

## 1. Vocabulary test

Define 10–15 concepts without notes.

## 2. Code tracing

Predict the output of five programs before running them.

## 3. Coding test

Build one small program in 60–90 minutes.

## 4. Debugging test

Repair three deliberately broken functions.

## 5. Project demonstration

Demonstrate the week’s project without reading the README.

## 6. Oral explanation

Explain:

* Program inputs
* Outputs
* State
* Data structures
* Important functions
* Test strategy
* Complexity
* Limitations

## 7. Rebuild exercise

Rebuild one important component from memory.

Passing score: **80%**, with no category below 70%.

---

# 17. Phase 1 Final Examination

## Section A: Python Knowledge — 45 Minutes

Topics:

* Types
* Mutability
* Functions
* Scope
* Conditions
* Loops
* Collections
* Files
* Exceptions
* Classes
* Imports
* Testing

## Section B: Coding — 60 Minutes

Solve:

1. One string or list problem
2. One dictionary or set problem

Required process:

* Clarify
* Give examples
* Explain approach
* Write code
* Test
* State complexity

## Section C: Debugging — 30 Minutes

Repair code containing:

* Mutable-state bug
* Off-by-one error
* Incorrect condition
* Missing edge case
* Incorrect exception handling

## Section D: Object-Oriented Design — 30 Minutes

Design one:

* Card game
* Parking garage
* Vending machine
* Library checkout system
* Restaurant ordering system

## Section E: Project Deep Dive — 30 Minutes

Present either:

* Poker Hand Evaluator
* Texas Hold’em Simulator
* Card-Game Tournament Platform

---

# 18. Final Phase 1 Portfolio

## Pinned Repositories

### 1. Poker Hand Evaluator

Demonstrates:

* Algorithms
* Dictionaries
* Sorting
* Comparison logic
* Edge-case testing

### 2. Texas Hold’em Simulator

Demonstrates:

* State modeling
* Object-oriented design
* Simulation
* Reusable components

### 3. Command-Line Task Manager

Demonstrates:

* CLI design
* Persistence
* Modules
* Exceptions
* Logging

### 4. Card-Game Tournament Platform

Demonstrates:

* Application architecture
* Reuse
* Testing
* Integration
* Technical communication

## Smaller Project Repository

Keep Projects 1–8 together:

```text
python-foundations-projects/
├── calculator/
├── budget-calculator/
├── guessing-game/
├── quiz-engine/
├── hangman/
├── tic-tac-toe/
├── contact-book/
└── log-analyzer/
```

---

# 19. Phase 1 Advancement Checklist

You may proceed to Phase 2 only when all required items are complete.

## Programming

* [ ] I can write functions without copying examples.
* [ ] I understand parameters and return values.
* [ ] I can use conditions and loops correctly.
* [ ] I understand strings, lists, tuples, dictionaries, and sets.
* [ ] I can choose an appropriate data structure.
* [ ] I can read and write files.
* [ ] I can work with JSON and CSV.
* [ ] I can raise and handle exceptions.
* [ ] I can organize code into modules.

## Object-Oriented Programming

* [ ] I can design classes from requirements.
* [ ] I understand object state.
* [ ] I understand composition.
* [ ] I can explain inheritance and its risks.
* [ ] I can use dataclasses and enums.
* [ ] I can explain every card-game class.

## Testing and Debugging

* [ ] I can write unit tests.
* [ ] I can write integration tests.
* [ ] I can test expected exceptions.
* [ ] I can test randomness deterministically.
* [ ] I can use fixtures and parametrization.
* [ ] I can reproduce a bug before fixing it.
* [ ] I write regression tests.
* [ ] I can use breakpoints and logging.

## Software Engineering

* [ ] I use virtual environments.
* [ ] I maintain readable repository structures.
* [ ] I use meaningful Git commits.
* [ ] I use feature branches.
* [ ] I can resolve a basic merge conflict.
* [ ] I write README and design documentation.
* [ ] I can refactor without breaking tests.

## Interviews

* [ ] I can solve two easy problems in 60 minutes.
* [ ] I can explain time and space complexity.
* [ ] I can trace code manually.
* [ ] I can debug unfamiliar code.
* [ ] I can design a small object-oriented system.
* [ ] I can explain one project for 20–30 minutes.
* [ ] I can rebuild the Poker Hand Evaluator from memory.
* [ ] I can discuss failures honestly.

## Portfolio

* [ ] I completed all five major repositories.
* [ ] My core projects have tests.
* [ ] My repositories contain architecture diagrams.
* [ ] My README files explain setup and use.
* [ ] I recorded at least two demonstrations.
* [ ] I published a technical write-up about one difficult bug.
* [ ] I can explain every major function in my code.

Passing Phase 1 means you are ready to begin deeper data structures, algorithms, computer systems, networking, databases, concurrency, and software architecture. It does not yet mean that you are ready for an advanced engineering interview, but you should have genuine Python foundations and credible evidence that you can design and finish software.
