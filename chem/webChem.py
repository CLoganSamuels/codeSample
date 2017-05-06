# -*- coding: utf-8 -*-
from sympy import Matrix
import random

def removeCoefficients(molecule):
    #removes any coefficients entered by the user
    for i in range(len(molecule)):
        if capLowNum(molecule[i]) == 'up':
            if molecule[i:] == "H20": return("H2O")
            #fixes a common typo
            return(molecule[i:])

def main(equation):
    #takes input and puts data into a 2d array
    equation = equation.replace('-->', '=').replace('→', '=').replace(' ','')
    subscript = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
    equation = equation.translate(subscript)
    #changes subscripts into normal ints
    react, prod = equation.split('=') 
    #splits the equation into product and reacant sides
    reactants = react.split('+')
    #splits the reactant side into a list of molecules
    products = prod.split('+') 
    #splits product side into a list of molecules
    
    reactants = [removeCoefficients(r) for r in reactants]
    products = [removeCoefficients(p) for p in products]
    
    moleWeights = {}
    atomList = []
    zeros = [] #populated by zeros to fill in missing values in the final matrix
    matrix = [] 
    i = 0 #the total number of molecules counted so far
    
    for reactant in reactants: 
    #add reacant atoms to matrix as positive integers     
        reactant = moleculeSplit(reactant, 1, moleWeights) 
        #splits each molecule into a dictionary of atoms
        #key = atomic symbol, value = the quantity of the atom per molecule        
        for atom in reactant:
            if atom in atomList:
                aIndex = atomList.index(atom)
                populate(matrix[aIndex],i,reactant[atom])
            else:
                atomList.append(atom)
                matrix.append(zeros + [reactant[atom]])
        zeros.append(0)
        i += 1

    for product in products:
    #add product atoms to matrix as negative integers
        product = moleculeSplit(product, -1, moleWeights)
        for atom in product:
            if atom in atomList:
                aIndex = atomList.index(atom)
                populate(matrix[aIndex],i,product[atom])
            else:
                atomList.append(atom)
                matrix.append(zeros + [product[atom]])
        zeros.append(0)
        i += 1

    for x in range(len(matrix)):
        while len(matrix[x]) < i:
            matrix[x].append(0)
            #makes rows have uniform length
            
    return(out(nullMath(matrix, i), reactants, products, moleWeights))

    
def moleculeSplit(mole, sign, moleWeights): 
    #splits molecules into atoms
    subScript = ''
    elem = ''
    elements = {}
    mult = 1        #used to multiply numbers in ()
    i = len(mole)
    moleWeight = 0
    for i in range(len(mole)-1, -1, -1):
        if mole[i] == ')':
            if subScript == '': subScript = 1
            mult = int(subScript)
            subScript = ''
        elif mole[i] == '(':
            mult = 1
        else:
            char = capLowNum(mole[i]) 
            if char == 'digit':
                subScript = mole[i] + subScript
            else:
                elem = mole[i] + elem
                if char == 'up': #elements begin with capital letters
                    if subScript == '': subScript = 1
                    elements[elem] = int(subScript) * sign * mult
                    moleWeight += aw[elem] * mult * int(subScript)
                    subScript = ''
                    elem = ''
    moleWeights[mole] = moleWeight
    return(elements)

    
def nullMath(matrix, i):
    coEffs = Matrix(matrix).nullspace()
    #coefficients in fraction form
    notInts = True
    mult = 1
    
    while notInts:
        intCoEffs = []
        for x in range(i):
            if coEffs[0][x] * mult % 1 == 0: #coefficients must be whole numbers
                intCoEffs.append(coEffs[0][x] * mult)
                notInts = False
            else:
                notInts = True
                mult += 1
                break
    return(intCoEffs)

def out(coEffs, reactants, products, moleWeights):
    coEffDict = {}
    equation = ""
    i = 0
    subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")
    for reactant in reactants:
        r = reactant.translate(subscript)
        moleWeights[r] = moleWeights.pop(reactant)
        coEffDict[r] = coEffs[i]
        if coEffs[i] == 1: coEffs[i] = ''
        equation = equation + str(coEffs[i]) + r + ' + '
        i += 1
    equation = equation[:-2] + "→ "
    for product in products:
        p = product.translate(subscript)
        moleWeights[p] = moleWeights.pop(product)
        coEffDict[p] = coEffs[i]
        if coEffs[i] == 1: coEffs[i] = ''
        equation = equation + str(coEffs[i]) + p + ' + '
        i += 1
    print(coEffDict)
    return((equation[:-2], moleWeights, coEffDict))

def capLowNum(char):
    if ord(char) > 96: return('low')
    if ord(char) < 58: return('digit')
    return('up')

def populate(l, most,new):
    while len(l) < most:
        l.append(0)
    l.append(new)
    return(l)

def example():
    choices = ['Fe + H2SO4 = Fe2(SO4)3 + H2', 'Si(OH)4 + NaBr --> SiBr4 + NaOH',\
    'MoS2 + O2 --> MoO3 + SO2', 'C2H4 + O2 = CO2 + H2O',\
    ]

    return(random.choice(choices))


aw = {'Ac': 227.0,
 'Ag': 107.8682,
 'Al': 26.9815,
 'Am': 243.0,
 'Ar': 39.948,
 'As': 74.9216,
 'At': 210.0,
 'Au': 196.9665,
 'B': 10.811,
 'Ba': 137.327,
 'Be': 9.0122,
 'Bh': 264.0,
 'Bi': 208.9804,
 'Bk': 247.0,
 'Br': 79.904,
 'C': 12.0107,
 'Ca': 40.078,
 'Cd': 112.411,
 'Ce': 140.116,
 'Cf': 251.0,
 'Cl': 35.453,
 'Cm': 247.0,
 'Co': 58.9332,
 'Cr': 51.9961,
 'Cs': 132.9055,
 'Cu': 63.546,
 'Db': 262.0,
 'Dy': 162.5,
 'Er': 167.259,
 'Es': 252.0,
 'Eu': 151.964,
 'F': 18.9984,
 'Fe': 55.845,
 'Fm': 257.0,
 'Fr': 223.0,
 'Ga': 69.723,
 'Gd': 157.25,
 'Ge': 72.64,
 'H': 1.0079,
 'He': 4.0026,
 'Hf': 178.49,
 'Hg': 200.59,
 'Ho': 164.9303,
 'Hs': 277.0,
 'I': 126.9045,
 'In': 114.818,
 'Ir': 192.217,
 'K': 39.0983,
 'Kr': 83.8,
 'La': 138.9055,
 'Li': 6.941,
 'Lr': 262.0,
 'Lu': 174.967,
 'Md': 258.0,
 'Mg': 24.305,
 'Mn': 54.938,
 'Mo': 95.94,
 'Mt': 268.0,
 'N': 14.0067,
 'Na': 22.9897,
 'Nb': 92.9064,
 'Nd': 144.24,
 'Ne': 20.1797,
 'Ni': 58.6934,
 'No': 259.0,
 'Np': 237.0,
 'O': 15.9994,
 'Os': 190.23,
 'P': 30.9738,
 'Pa': 231.0359,
 'Pb': 207.2,
 'Pd': 106.42,
 'Pm': 145.0,
 'Po': 209.0,
 'Pr': 140.9077,
 'Pt': 195.078,
 'Pu': 244.0,
 'Ra': 226.0,
 'Rb': 85.4678,
 'Re': 186.207,
 'Rf': 261.0,
 'Rh': 102.9055,
 'Rn': 222.0,
 'Ru': 101.07,
 'S': 32.065,
 'Sb': 121.76,
 'Sc': 44.9559,
 'Se': 78.96,
 'Sg': 266.0,
 'Si': 28.0855,
 'Sm': 150.36,
 'Sn': 118.71,
 'Sr': 87.62,
 'Ta': 180.9479,
 'Tb': 158.9253,
 'Tc': 98.0,
 'Te': 127.6,
 'Th': 232.0381,
 'Ti': 47.867,
 'Tl': 204.3833,
 'Tm': 168.9342,
 'U': 238.0289,
 'V': 50.9415,
 'W': 183.84,
 'Xe': 131.293,
 'Y': 88.9059,
 'Yb': 173.04,
 'Zn': 65.39,
 'Zr': 91.224}