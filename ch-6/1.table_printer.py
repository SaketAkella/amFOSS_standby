tableData=[['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
'''
for k in range (len(tableData)):
    l=len(tableData[k])
    for i in range (l):
        print(tableData[k][i], end=",")
        '''
        
def printTable(table):
    colwidth=[0]*len(table)
    l=int(len(table[0])) #lenght of each list
    for i in range (len(table)):
        newlist=sorted(table[i], key=len) #sort our original list using len as our characterstic.
        colwidth[i]=len(newlist[-1])
    #print(colwidth) (checking if the codition is met.) 
    
    for i in range (l):
        print()
        for j in range(len(table)):
            string=table[j][i]
            print(string.rjust(colwidth[j]),end=" ")

printTable(tableData)