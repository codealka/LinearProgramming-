
Optimization theory and applications assessed assignment 1 : Linear programming
----------------------------------------------------------------------------------

This is a maximisation program for linear programming problems where both the objective function and the constraints of the problem are linear. This program uses the Simplex method to arrive at an optimal solution. For the program to function a linear problem must be properly formulated appropriately into the input text file as the initial tableau of the simplex method.

Example:
The below tableau corresponds to a max problem with objective function Z = x1 + 2x2
Subject to constraints:
x1 <= 7
x2 <= 6
8x1 + 3x2 <= 60
4x1 + 9x2 <= 60

Objective function is rewritten as -x1 -2x2 + Z = 0 and the slack variables (x3,x4,x5,x6) are added.

input.txt should contain:

x1  x2  x3  x4  x5  x6  z   solution
1   0   1   0   0   0   0   7
0   1   0   1   0   0   0   6
8   3   0   0   1   0   0   60
4   9   0   0   0   1   0   60
-1 -2   0   0   0   0   1   0


The program extracts the tableau from text file without headers
the Last column contains the solutions 
the penultimate column contains the objective function
All other columns contain variables and slack variables of the set of equations
while the last row contains the objective function in the form Z - x1 - x2 ... = 0

Any comments written in the input file should be added below the tableau with a # to denote a comment. 
Example:
# comment 1
# comment 2

The Package contains three files:
•   Input.txt 
•   log.txt
•   solution.txt

Input files:

Upon running the program, A command line prompt will ask for the file name which contains the tableau for the problem. The package will contain a example file called “input.txt” For the program to recognise the file it must be in the same directory as the program itself. Alternatively, you can provide the full path name of the file.

To test the program, provide the command line prompt with “input.txt”.

to run the program on any other additional input file, provide the command line with the new file. As an example, “NewInput.txt”. note that an additional input file must be formatted appropriately for the programme to function.

Log.txt file:

This file will display the inner workings of the simplex method, giving the tableau after every pivoting.

Solution.txt file:
Once an optimal solution has been reached, the maximum value of the objective function Z will be stated in this file. Additionally, this file will include the value of each of the variables and slack variables.


Libraries used:
Numpy ==> https://numpy.org