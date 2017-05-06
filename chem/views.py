from django.shortcuts import render
from .webChem import main, moleculeSplit, nullMath, out, \
capLowNum, populate, example


def output(request):
    context = {}
    if 'equation' in request.POST:
        equation = request.POST.get('equation')        
        try:
            o = main(equation)
            context['balEquation'] = o[0]
            vals = {}
            for k in o[1].keys():
                #combine dictionaries
                vals[k] = tuple(d[k] for d in [o[1], o[2]])
            context['vals'] = vals
        except: 
            print(equation)
            context['balEquation'] = "Invalid input! \
            Please enter valid chemical symbols with proper capitalization." 
        context['example'] = example()
    else:
        context['example'] = "H + O = H2O" #always first example
      
    return render(request, 'chem/balPage.html', context)

def showMain(request):
    context = {'title': 'Main'}
    return render(request, 'chem/main.html', context)

def showRemove(request):
    context = {'title': 'Remove Coefficients'}
    return render(request, 'chem/remove.html', context)

def showMoleculeSplit(request):
    context = {'title': 'Molecule Split'}
    return render(request, 'chem/moleculeSplit.html', context)

def showNullMath(request):
    context = {'title': 'Null Math'}
    return render(request, 'chem/nullMath.html', context)

def showOut(request):
    context = {'title': 'Out'}
    return render(request, 'chem/out.html', context)

def showCapLowNum(request):
    context = {'title': 'Capital, Lowercase, or Integer'}
    return render(request, 'chem/capLowNum.html', context)

def showPopulate(request):
    context = {'title': 'Populate'}
    return render(request, 'chem/populate.html', context)
                  