
import numpy as np
import math


Tab = np.loadtxt('input3.txt' ,skiprows=1,comments='#') 

def Simplex(M):
    Zmax = []  # stores original objective function 
    Mshape = M.shape # for the size of the tableau

    #number of rows and columns
    Mrows = Mshape[0] 
    Mcolumns = Mshape[1]

    for element in range(Mcolumns):
        Zmax.append(abs((M[Mrows-1][element])))



    print(Mshape)
    print(M)
    Optimum = False
    PC = 0 #pivot count



    while Optimum == False:


        PC+=1
        #-----------------------------------------------------
        #step 1 : find pivot column  -------------------------
        #-----------------------------------------------------

        store = math.inf # storing infinity in a varaible for comparisons
        index_c = int
        b = 0

        last_row = []
        for i in range(Mcolumns-1):
            last_row.append(M[Mrows-1][i])


        for i in range(Mcolumns-2):
            if (M[Mrows - 1][i]) < b :
                b = M[Mrows - 1][i]
            else:
                pass
        for i in range(Mcolumns-2):
            if M[Mrows - 1][i] == b:
                index_c = i # getting the index as a location in the array 

        #-------------------------------------------------------        
        # step 2: choosing pivot row ---------------------------
        #--------------------------------------------------------


        index_r = 0
        ratio = []

        for i in range(Mrows-1):
            ratio.append(M[i][Mcolumns-1]/M[i][index_c])
        #print('these are the ratios: '+str(ratio))
        ratiolen = len(ratio)
        
        for i in range(ratiolen):
            if (ratio[i] < store) & (ratio[i]>0):
                store = ratio[i]
            else:
                pass
        for i in range(ratiolen):
            if store == ratio[i]:
                index_r = i #storing row index
            else:
                pass


        #---------------------------------------------------------------------------
        # step 3: row manipulations for unit vector in pivot column -----------------
        #-----------------------------------------------------------------------------

        #using index_r and index_c we find our pivot position the focus of the unit vector

        divider = M[index_r][index_c]
        #print('divider: '+str(divider))

        #Row opertaion to get 1 on pivot
        for i in range(Mcolumns):
            M[index_r][i] = (M[index_r][i])/divider
        
        #Row opertaion to get unit vector on pivot column


        temp_row = [] # temporary row containing pivot for manipulation
        for j in range(Mcolumns):
            temp_row.append(M[index_r][j])
        

        for i in range(Mrows):
            Multiplier = (M[i][index_c])
            if i == index_r:
                pass
            else:
                for j in range(Mcolumns):

                    if Multiplier == 0:
                        pass   
                    if Multiplier > 0: 
                        M[i][j] = (M[i][j] - (temp_row[j]*Multiplier))
                    else :
                        Multiplier1 = (-1)*Multiplier
                        M[i][j] = (M[i][j] + (temp_row[j]*Multiplier1))
        

        #----------------------------------------------------
        # step 4: Checking if an optimum has been found -------------
        #----------------------------------------------------

        objective = []
        for element in range(Mcolumns):
            objective.append(M[Mrows-1][element])

        counter=0
        for element in objective:
            if element < 0:
                counter += 1
            else:
                pass

        if counter == 0:
            Optimum = True

        #----------------------------------------------------------------
        # displaying findings in the log.txt file -----------------------
        #-----------------------------------------------------------------
        f = open('log.txt','a')
        f.write("The Tableau After pivot number " + str(PC) +" : \n")
        f.write("Pivot Column ==> " + str(index_c+1) + '\n')
        f.write("Pivot Row ==> " + str(index_r+1) + '\n')
        f.write(str((M)) + "\n\n")
        f.write('-----------------------------------\n')
        f.close()
    f = open('log.txt','a')
    f.write('An optimal solution has been reached\n')    
    f.write('-----------------------------------\n')
    f.close


    
   
    #----------------------------------------------------------------
    # displaying findings in the solution.txt file ------------------
    #----------------------------------------------------------------



    # if unit vector set variable value to solution column 
    # if non unit vector set vaiable value to zero

    variableSolution = []
    row_location = int
    for column in range(Mcolumns-1):
        x = 0
        for row in range(Mrows):
            if M[row][column] >= 1 :
                x +=1
                row_location = row
            else:
                pass
        if x != 1:
            variableSolution.append('0')
        else:
            variableSolution.append(str(M[row_location][Mcolumns-1]))

    f = open('solution.txt', 'a')
    f.write('The solution is: \n')
    for i in range(len(variableSolution)-1):
        f.write('X'+str(i+1)+' = '+variableSolution[i]+'\n')
    f.write('Z = '+variableSolution[len(variableSolution)-1]+'\n')   
    f.close()
    

            




   
Simplex(Tab)


