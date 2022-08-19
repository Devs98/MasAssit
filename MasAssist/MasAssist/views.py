from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def quienessomos(request):
    return render(request, 'quienessomos.html')

def proveedor(request):
    return render(request, 'proveedor.html')

def reembolsos(request):
    return render(request, 'reembolsos.html')

def pqrs(request):
    return render(request, 'pqrs.html')