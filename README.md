# Movie Ticket Booking System 🎬

A beginner-friendly Python program that calculates movie ticket costs and applies discounts based on the total booking amount.

## Overview

The **Movie Ticket Booking System** is a Python project that simulates a basic movie ticket booking process. Users enter the movie name, ticket price, and number of tickets. The program calculates the total cost, determines whether a discount applies, and displays the final amount payable.

## Features

* Accepts movie name, ticket price, and number of tickets.
* Calculates the total booking cost.
* Applies a **10% discount** when the total reaches ₹1,000 or more.
* Displays the discount and final amount.
* Uses functions to organize calculations and improve code readability.

## Discount Rules

| Booking Total  |    Discount |
| -------------- | ----------: |
| ₹1,000 or more |         10% |
| Below ₹1,000   | No discount |

**Formulae:**

* **Total Cost** = Ticket Price × Number of Tickets
* **Discount** = Total Cost × 10% (if the total is at least ₹1,000)
* **Final Amount** = Total Cost − Discount

## Example

**Input**

```text
Enter movie name: Interstellar
Enter ticket price: 250
Enter number of tickets: 5
```

**Output**

```text
===== MOVIE BOOKING =====
Movie: Interstellar
Ticket Price: ₹250
Tickets: 5
Total: ₹1250
Discount: ₹125.0
Final Amount: ₹1125.0
```

## Python Concepts Practiced

* **Variables** — Store movie and booking details.
* **User Input** — Collect information using `input()`.
* **Type Conversion** — Convert numeric inputs using `int()`.
* **Functions** — Separate ticket-cost and discount calculations.
* **Parameters and Return Values** — Pass data to functions and return results.
* **Conditional Statements** — Apply a discount using `if` and `else`.
* **Arithmetic Operations** — Calculate totals, discounts, and final costs.
* **Keyword Arguments** — Call a function using named parameters.
* **f-Strings** — Display booking details in a readable format.

## Getting Started

### Prerequisites

* Python 3.x
* A code editor or terminal

### Run the Program

1. Clone or download the repository.

2. Open the project folder in your terminal.

3. Run the Python file:

   ```bash
   python "movie ticket booking system.py"
   ```

4. Enter the requested booking details.

## Potential Improvements

* Validate ticket prices and ticket quantities.
* Allow users to book tickets for multiple movies.
* Add different discount levels.
* Display a booking confirmation number.
* Format monetary values consistently to two decimal places.

## Project Status

**Completed — Beginner Python Project**

This project demonstrates how Python functions, conditional logic, and arithmetic operations can be combined to solve a practical problem.

## Author
pramod .
