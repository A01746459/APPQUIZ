"""
 Final Project: Quiz Application with Microservices
 Date: 30-Nov-2022
 Authors:
        Jeovani Hernandez Bastida A01749164
        José Miguel Garcia Gurtubay Moreno A01373750
        Sebastian Burgos Alanís A01746459
        Sandra Ximena Téllez Olvera A01752142  
"""

### Views Configuration ###

from django.shortcuts import redirect, render, get_object_or_404,HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegistroFormulario, UsuarioLoginFormulario
from .models import QuizUsuario, Pregunta, PreguntasRespondidas, ChooseAnswer
from random import *

# In this Function, we send a request from inicio.html
def inicio(request):
    
    return render(request, 'inicio.html')

# In this Function, we send a request from Usuario/home.html
def HomeUsuario(request):
    return render(request, 'Usuario/home.html')

def seleccionarPreguntas(request):
    if request.method == 'POST':
        cantidad_preguntas = int(request.POST.get('cantidad_preguntas'))    
        return redirect('jugar', cantidad_preguntas=cantidad_preguntas)

    return render(request, 'play/seleccionar_preguntas.html')

# En la función jugar(request, cantidad_preguntas), después de obtener la siguiente pregunta
# y antes de redirigir a los resultados, verifica si se ha alcanzado el número máximo de preguntas respondidas
# In this Function, 
def jugar(request, cantidad_preguntas):
    QuizUser, created = QuizUsuario.objects.get_or_create(usuario=request.user)
    if request.method == 'POST':
        if cantidad_preguntas>0:
            pregunta_pk = request.POST.get('pregunta_pk')
            pregunta_respondida = QuizUser.intentos.select_related('pregunta').get(pregunta__pk=pregunta_pk)
            respuesta_pk = request.POST.get('respuesta_pk')

            try:
                opcion_seleccionada = pregunta_respondida.pregunta.opciones.get(pk=respuesta_pk)
            except ObjectDoesNotExist:
                raise Http404

            QuizUser.validar_intento(pregunta_respondida, opcion_seleccionada)

            # Obtener la siguiente pregunta o redirigir al resultado si no hay más preguntas
            siguiente_pregunta = QuizUser.obtener_nuevas_preguntas(cantidad_preguntas)
            if siguiente_pregunta is not None:
                QuizUser.crear_intentos(siguiente_pregunta)
                return HttpResponseRedirect(f'/resultado/{pregunta_respondida.pk}?cantidad_preguntas={cantidad_preguntas}')
                return redirect('resultado', pregunta_respondida.pk)
            else:
                # return HttpResponseRedirect(f'/resultado/{pregunta_respondida.pk}?cantidad_preguntas={cantidad_preguntas}')
                return redirect('tablero')#pregunta_respondida.pk

    else:
        pregunta = QuizUser.obtener_nuevas_preguntas(cantidad_preguntas)
        if pregunta is not None:
            QuizUser.crear_intentos(pregunta)

        context = {
            'pregunta': pregunta
        }

        return render(request, 'play/jugar.html', context)


# In this Function, 
def resultado_pregunta(request, pregunta_respondida_pk):
      cantidad_preguntas = str(int(request.GET.get('cantidad_preguntas'))-1)
      respondida=get_object_or_404(PreguntasRespondidas, pk=pregunta_respondida_pk)

      context={
            'respondida':respondida,
            'cantidad_preguntas':cantidad_preguntas
      }
      return render(request, 'play/resultados.html', context)


# In this Function, 
def tablero(request):
	total_usaurios_quiz = QuizUsuario.objects.order_by('-puntaje_total')[:10]
	contador = total_usaurios_quiz.count()

	context = {
		'usuario_quiz':total_usaurios_quiz,
		'contar_user':contador
	}
	return render(request, 'play/tablero.html', context)

# In this Function, 
def loginView(request):
    titulo = 'login'
    form = UsuarioLoginFormulario(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        usuario = authenticate(username = username, password = password)
        login(request, usuario)
        return redirect('HomeUsuario')
    
    context = {
        'form' : form,
        'titulo' : titulo
    }
    return render(request, 'Usuario/login.html', context)

# In this Function, 
def registro(request):
    
    titulo = 'Crea una Cuenta'
    if request.method == 'POST':
        form  = RegistroFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistroFormulario()
        
    context = {
        'form':form,
        'titulo': titulo
    }
    
    return render(request, 'Usuario/registro.html', context)

def logout_vista(request):
    logout(request)
    return redirect('/')

"""
def intento(request):
   PreguntasRespondidas.objects.all().delete()
   return redirect(request, 'HomeUsuario')
"""