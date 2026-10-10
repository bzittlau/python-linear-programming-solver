
# Python Linear Programming Solver

A Python application developed as part of my graduate
Computer Science coursework at Merrimack College.

## Overview

This program evaluates linear programming problems by
comparing individual variable solutions with a balanced
solution calculated using NumPy.

## Features

- Accepts user-defined variables and constraints
- Performs matrix calculations using NumPy
- Validates user input and handles invalid entries
- Evaluates individual variable solutions
- Calculates a balanced solution when possible
- Compares candidate solutions

## Technologies

- Python
- NumPy
- Pytest
- GitHub Actions

## Installation

Install the required packages:

```bash
python -m pip install numpy pytest
```

## Running the Program

Run the application from the repository directory:

```bash
python Zittlau-Johnson_Mod5_Assignment02.py
```

Follow the prompts to enter the objective coefficients,
constraint matrix, and constraint limits.

## Automated Testing

The project includes four automated integration tests
using Pytest.

Tests cover:

- Expected results for a sample optimization problem
- Invalid variable counts
- Singular matrices
- Invalid coefficient inputs

Run the tests using:

```bash
python -m pytest -v
```

## Continuous Integration

GitHub Actions automatically installs the dependencies
and runs the Pytest suite whenever changes are pushed
to the repository.

The initial workflow successfully completed all four
tests.

## Project Purpose

This project demonstrates Python programming, numerical
computation, input validation, error handling,
automated testing, and continuous integration.
