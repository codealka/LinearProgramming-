
import numpy as np
import math


Tab = np.loadtxt('input3.txt' ,skiprows=1,comments='#') 

def Simplex(M):
    Mshape = M.shape # for the size of the tableau
    Mrows = Mshape[0]
    Mcolumns = Mshape[1]
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
                index_c = i # getting the index as a location of in the array 

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
        
        #print('this row is used for manipulations: ' + str(temp_row))

        for i in range(Mrows):
            Multiplier = (M[i][index_c])
            #print('opertaing on row: ' + str(i+1))
            #print('Multiplier: ' + str(Multiplier))
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
        print(M)


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
                #print('non-negative')
                pass

        if counter == 0:
            Optimum = True

        #----------------------------------------------------------------
        # step 5: displaying findings in the log.txt file -----------------------
        #-----------------------------------------------------------------
        f = open('log.txt','a')
        f.write(str((M)) + "\n\n")
        f.close()
        


   
Simplex(Tab)
