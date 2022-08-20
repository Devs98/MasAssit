from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def home(request):
    return render(request, 'index.html')

def quienessomos(request):
    return render(request, 'quienessomos.html')

def proveedor(request):
    if request.method == 'POST':
        subject = "Web Mas Assist - Quiero Ser Proveedor"
        message = "Nombre: " + request.POST['name'] +" Correo Electronico:  " + request.POST['email'] + " Telefono: " + request.POST['phone'] + " Comentario: " +  request.POST['comment']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['desarrollodigitalaa@gmail.com', 'dtecnologia99@gmail.com', 'valen330042@gmail.com']
        send_mail(subject, message, email_from, recipient_list)
        messages.success(request, 'Correo Enviado')
        return redirect('proovedor')
    return render(request, 'proveedor.html')

def reembolsos(request):
    return render(request, 'reembolsos.html')

def pqrs(request):
    if request.method == 'POST':
        subject = "Web Mas Assist - PQRS"
        message = "Tipo de Peticion: " + request.POST['peticion'] + " Telefono: " + request.POST.get('telefono', 'False')  + " Producto: " + request.POST['productos']  + " Celular: " + request.POST['celular'] + " Medio de Respuesta:  " + request.POST['medio-respuesta'] + " Comentario:  " + request.POST['comentario'] + " Tipo de Documento:  " + request.POST['tipo-documento'] + " Numero de documento:  " + request.POST['num-documento']+ " Registro Solicitud en nombre de otra empresa o persona:  " + request.POST.get('persona-empresa', 'No') + " Acepta Politicas:  " + request.POST['politica'] + " Primer Nombre:  " + request.POST['primer-nombre'] + " Segundo Nombre " + request.POST.get('segundo-nombre', 'Ninguno') + "Acepta Autorización Voluntaria: " + request.POST['autorizacion-voluntaria'] + " Primer Apellido:  " + request.POST['primer-apellido'] + " Segundo Apellido:  " + request.POST.get('segundo-apellido', 'Ninguno') + " Correo Electronico:  " + request.POST['email']
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['desarrollodigitalaa@gmail.com']
        send_mail(subject, message, email_from, recipient_list)
        messages.success(request, 'Correo Enviado')
        return redirect('pqrs')
    return render(request, 'pqrs.html')

def contacto(request):
    if request.method == 'POST':
        subject = "Web Mas Assist - Contacto"
        message = " Correo Electronico: " + request.POST['email']  + " Nombre: : " + request.POST['name'] + " Telefono: " + request.POST['phone'] + " Comentario: " +  request.POST['comment'] + " Productos de interes:  Adulto Mayor: " +  request.POST.get('adulto', 'False') + " Legal: " + request.POST.get('legal', 'False') + " Garantia Extendida: " +  request.POST.get('garantia', 'False') + " Medico:  " +  request.POST.get('medico', 'False') + " Funerario:  " +  request.POST.get('funerario', 'False') + " Mascotas: " +  request.POST.get('mascotas', 'False') + " Hogar:  " +  request.POST.get('hogar', 'False') + " Turismo: " + request.POST.get('turismo', 'False')
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['desarrollodigitalaa@gmail.com']
        send_mail(subject, message, email_from, recipient_list)
        messages.success(request, 'Correo Enviado')
        return redirect('contacto')
    return render(request, 'contacto.html')