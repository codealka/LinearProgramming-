
# Simplex Solver CLI

Simplex Solver CLI is a command-line tool designed to solve linear programming problems using the Simplex algorithm. It reads problem specifications from a text file and outputs the optimal solution to the specified linear programming problem. This document explains how to set up and use the Simplex Solver CLI.

## Prerequisites

Before running the Simplex Solver CLI, ensure you have the following installed on your system:
- Python (version 3.6 or newer)
- NumPy

## Installation

To use the Simplex Solver CLI, first, clone this repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/simplexsolvercli.git
cd simplexsolvercli
```

No additional installation steps are required, as the script runs directly in Python.

## Usage

1. **Prepare Your Linear Programming Problem File**

   Create a text file (`name.txt`) containing the tableau of your linear programming problem. The file format should be as follows:

   - The first row (optional) can include comments (starting with `#`).
   - Subsequent rows represent the coefficients of the linear programming problem's tableau.
   - The last column contains the solutions to the equations.
   - The penultimate column contains the coefficients of the objective function variable.
   - The last row contains the objective function in the form `Z - x1 - x2 - ... = 0`.

2. **Run the Simplex Solver CLI**

   Open a terminal or command prompt, navigate to the directory containing `simplex_solver.py`, and run the following command:

   ```bash
   python simplex_solver.py
   ```

   When prompted, enter the name of your problem file (including the `.txt` extension).

3. **View the Results**

   After the script completes, the optimal solution and detailed execution log are available in `solution.txt` and `log.txt` files, respectively, in the same directory.

## Example

Suppose you have a linear programming problem specified in `problem.txt`. Run the Simplex Solver CLI and enter `problem.txt` when prompted. The optimal solution will be printed to `solution.txt`, and the step-by-step log will be available in `log.txt`.

## Contributing

Contributions to the Simplex Solver CLI are welcome! Please feel free to submit pull requests or open issues to suggest improvements or report bugs.
