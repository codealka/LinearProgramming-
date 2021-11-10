import numpy as np
import math
#import pandas as pd


#extracting the tableau from text file without headers
#Last column contains the solutions 
#penultimate column contains the objective function variable
#all other columns contain variables and slack variables of the set of equations
# while the last row contains the objective function in the form Z - x1 - x2 ... = 0
Tab = np.loadtxt('input.txt',skiprows=1,comments='#') 


def ProblemParameters(M): #this function outlines the problem parameters
    Mshape = M.shape
    NumVariables  = Mshape[1]-2 #because one column is solutions and a second is the objective function
    NumConstraints = Mshape[0] -1 #because one of the rows holds the objective function

    #ConEquations = np.empty([Mshape[0]-1, Mshape[1]-2] , dtype='str')
    #CEshape = ConEquations.shape
    #for i in range (CEshape[0]):
        #for j in range(CEshape[1]):
            #ConEquations[i][j] = str(M[i][j])
    

    #writing parameter to top of the log.txt file
    #f = open('log.txt','x')
    #f.write('The LP problem has '+ str(NumVariables) + ' variables and ' +
    #        str(NumConstraints) + ' constraint equations.\n \n')
    #f.close()










def Simplex(M):
    Mshape = M.shape # for the size of the tableau
    Mrows = Mshape[0]
    Mcolumns = Mshape[1]
    print(Mshape)
    Optimal = False  # will be used to return solution at the end of simplex method

    print(M)
    #while Optimal == True:

    #step 1 : find pivot column  -----------------------

    index_c = 0
    for i in range(Mcolumns-2):
        if M[Mrows - 1][i] < index_c:
            index_c = M[Mrows - 1][i]
        else:
            pass
    for i in range(Mcolumns-2):
        if M[Mrows - 1][i] == index_c:
            index_c = i # getting the index as a location of in the array 

    print(index_c)

    # step 2: choosing pivot row -----------------------


    index_r = 0
    ratio = []

    for i in range(Mrows-1):
        ratio.append(M[i][Mcolumns-1]/M[i][index_c])
    ratiolen = len(ratio)
    print(ratio)
    
    store = math.inf # setting orginal comaparative value to infinity to find smallest ratio
    for i in range(ratiolen):
        if ratio[i] < store:
            store = ratio[i]
        else:
            pass
    for i in range(ratiolen):
        if store == ratio[i]:
            index_r = i #storing row index
        else:
            pass
    
    print(index_r)
    # step 3: row manipulations for unit vector in pivot column -----------------

    #using index_r and index_c we find our pivot position the focus of the unit vector

    divider = M[index_r][index_c]
    print(divider)

    print(M)

    #Row opertaion to get 1 on pivot
    for i in range(Mcolumns):
        M[index_r][i] = (M[index_r][i])/divider
    
    #Row opertaion to get unit vector on pivot column
    for i in range(Mrows):
        Multiplier = M[i][index_c]
        if i == index_r:
            pass
        else:
            for j in range(Mcolumns):
                if M[i][index_c] == 0:
                    pass
                if M[i][index_c] > 0: 
                     M[i][j] = M[i][j] - M[index_r][index_c]*Multiplier
                elif M[i][index_c] < 0:
                    M[i][j] = M[i][j] - M[index_r][index_c]*Multiplier
                
    print(M)
    print(M[index_r][index_c])



        



    



    
    





    



ProblemParameters(Tab)
Simplex(Tab)
