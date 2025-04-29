from django.shortcuts import render
from .forms import LoginForm
from django.contrib.auth import authenticate, login # Aplicacion precargada para hacer autenticacion en Django
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def user_login(request):
    if request.method == 'POST': # verifica el metodo de la peticion
        form = LoginForm(request.POST) # Almacena toda la informacion que llego a LoginForm()
        if form.is_valid():  # Verifica que sean validos los datos 
            cd = form.cleaned_data # Limpia la informacion 
            user = authenticate(request,                    
                                username=cd['username'], # Enviamos los datos a la db para hacer la comprobacion del usuario 
                                password=cd['password']) # Si el usuario que es enviado no se encuntra {user} va retornar None 
            if user is not None: 
                if user.is_active: # Validacion estra, si el usuario esta activo
                    login(request, user) 
                    return HttpResponse('Usuario Autenticado')
                else:
                    return HttpResponse('Usuario Inactivo')
            else:
                return HttpResponse('Usuario no encontrado') # Pertenece a la validacion completa
    else: 
        form = LoginForm() # Si la peticion es GET devolvemos el formulario
    return render(request, 'account/login.html', {'form':form}) # return de la vista completa 

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html', {'section':'dashboard'})