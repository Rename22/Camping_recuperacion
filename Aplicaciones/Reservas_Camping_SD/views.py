from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario

def iniciar_sesion(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')

        try:
            usuario_obj = Usuario.objects.get(usuario=usuario, contrasena=contrasena)
            request.session['usuario'] = usuario_obj.usuario
            return redirect('/inicio/')
        except Usuario.DoesNotExist:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    return render(request, 'login.html')


def cerrar_sesion(request):
    request.session.flush()
    return redirect('/')

def pagina_inicio(request):
    if 'usuario' not in request.session:
        return redirect('/')
    return render(request, 'inicio.html')

def registro_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        cedula = request.POST.get('cedula')
        celular = request.POST.get('celular')
        usuario = request.POST.get('usuario')
        contrasena = request.POST.get('contrasena')

        if Usuario.objects.filter(usuario=usuario).exists():
            messages.error(request, 'El usuario ya existe.')
            return redirect('/registro/')
        if Usuario.objects.filter(cedula=cedula).exists():
            messages.error(request, 'La cédula ya está registrada.')
            return redirect('/registro/')

        Usuario.objects.create(
            nombre=nombre,
            apellido=apellido,
            cedula=cedula,
            celular=celular,
            usuario=usuario,
            contrasena=contrasena
        )
        messages.success(request, 'Usuario registrado exitosamente.')
        return redirect('/')

    return render(request, 'registro.html')
