import subprocess
import sys
from pathlib import Path

# Find the original Python program.
PROGRAM = (
    Path(__file__).resolve().parents[1]
    / "Zittlau-Johnson_Mod5_Assignment02.py"
)


def run_solver(user_input):
    # Run the solver and send it the test inputs.
    return subprocess.run(
        [sys.executable, str(PROGRAM)],
        input=user_input,
        text=True,
        capture_output=True,
        timeout=10
    )


def test_chemical_problem():
    # Test the chemical example from class.
    user_input = (
        "3\n"
        "3000 2000 2000\n"
        "2 4 5\n"
        "1 2 4\n"
        "8 0 3\n"
        "300 200 300\n"
    )

    result = run_solver(user_input)

    assert result.returncode == 0
    assert "Balanced option" in result.stdout
    assert "Best objective value = 183333.33" in result.stdout


def test_invalid_variable_count():
    # The program should reject zero variables.
    user_input = (
        "0\n"
        "1\n"
        "10\n"
        "2\n"
        "20\n"
    )

    result = run_solver(user_input)

    assert result.returncode == 0
    assert "Please enter a positive integer." in result.stdout


def test_singular_matrix():
    # A singular matrix cannot be inverted.
    user_input = (
        "2\n"
        "10 20\n"
        "1 1\n"
        "2 2\n"
        "10 20\n"
    )

    result = run_solver(user_input)

    assert result.returncode == 0
    assert (
        "A usable balanced solution could not be found."
        in result.stdout
    )


def test_invalid_coefficient_input():
    # The program should reject letters as coefficients.
    user_input = (
        "1\n"
        "abc\n"
        "5\n"
        "2\n"
        "10\n"
    )

    result = run_solver(user_input)

    assert result.returncode == 0
    assert "Please enter numbers only." in result.stdout
