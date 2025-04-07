from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegistroForm, LoginForm


# Create your views here.

def index(request):
    return render (request, 'index.html')

def menujavahtmlcss(request):
    return render (request, 'menujavahtmlcss.html')

def indice_1(request):
    return render (request, 'indice_1.html')

def indice_2(request):
    return render (request, 'indice_2.html')

def indice_3(request):
    return render (request, 'indice_3.html')

def indice_4(request):
    return render (request, 'indice_4.html')

def javascript1(request):
    return render (request, 'javascript1.html')

def encabezados(request):
    return render (request, 'encabezados.html')

def direccionamiento(request):
    return render (request, 'direccionamiento.html')

def atajos_teclado(request):
    return render (request, 'atajos_teclado.html')

def tablas(request):
    return render (request, 'tablas.html')

def imagenes(request):
    return render (request, 'imagenes.html')

def svgywebp(request):
    return render (request, 'imagenes_svg_y_webp.html')

def flexbox(request):
    return render (request, 'flexbox.html')

def margin_padding(request):
    return render (request, 'margin_padding.html')
    
def compra(request):
    return render (request, 'tu_compra.html')

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, "Correo no registrado")
                return redirect('login')
            
            user_auth= authenticate(request, username=user.username, password=password)
            if user_auth is not None:
                login(request, user_auth)
                messages.success(request, "Has iniciado sesión correctamente")
                return redirect('index')
            else:
                messages.success(request, "Contraseña incorrecta")
                return redirect('login')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def registroView(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registro exitoso. Inicia sesión")
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})

def logoutView(request):
    logout(request)
    messages.info(request, "Has cerrado sesión. ¡Vuelve pronto!")
    return redirect('index')

