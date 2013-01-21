# Create your views here.
from principal.models import Alumno, Profesor, Curso, Matricula, Dictar, Nota
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect 
from django.template import RequestContext
from principal.forms import AlumnoForm, CursoForm, ProfesorForm, ContactoForm, MatriculaForm
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def lista_alumnos(request):
	alumnos = Alumno.objects.all()
	return render_to_response('lista_alumnos.html',{'alumnos':alumnos},context_instance = RequestContext(request))

def lista_cursos(request):
	cursos = Curso.objects.all()
	return render_to_response('lista_cursos.html',{'cursos':cursos},context_instance = RequestContext(request))

def lista_profesores(request):
	profesores = Profesor.objects.all()
	return render_to_response('lista_profesores.html',{'profesores':profesores},context_instance = RequestContext(request))

def dato_alumno(request, id_alumno):	
	dato = Alumno.objects.get(pk=id_alumno)
	dato2 = Matricula.objects.filter(alumno=id_alumno)
	return render_to_response('dato_alumno.html',{'alumno':dato,'cursos_matriculados':dato2},context_instance = RequestContext(request))

def dato_curso(request, id_curso):
	dato = Curso.objects.get(pk=id_curso)
	dato2 = Matricula.objects.filter(curso=id_curso)	
	return render_to_response('dato_curso.html',{'curso':dato,'alumnos_matriculados':dato2},context_instance = RequestContext(request))

def dato_profesor(request,id_profesor):
	dato = Profesor.objects.get(pk =id_profesor)
	dato2 = Dictar.objects.filter(profesor= id_profesor)
	return render_to_response('dato_profesor.html',{'profesor':dato,'cursos_dictados':dato2},context_instance = RequestContext(request))

def nuevo_alumno(request):
	if request.method=='POST':
		formulario=AlumnoForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/alumnos')
	else: 
		formulario=AlumnoForm()
	return render_to_response('alumnoform.html',{'formulario':formulario}, context_instance=RequestContext(request))


def nuevo_curso(request):
	if request.method=='POST':
		formulario=CursoForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/cursos')
	else: 
		formulario=CursoForm()
	return render_to_response('cursoform.html',{'formulario':formulario}, context_instance=RequestContext(request))

def nuevo_profesor(request):
	if request.method=='POST':
		formulario=ProfesorForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/profesores')
	else: 
		formulario=ProfesorForm()
	return render_to_response('profesorform.html',{'formulario':formulario}, context_instance=RequestContext(request))
	

def contacto(request):
	if request.method=='POST':
		formulario=ContactoForm(request.POST)
		if formulario.is_valid():
			titulo='Mensaje desde el recetario de Maestros del Web'
			contenido=formulario.cleaned_data['mensaje']+"\n"
			contenido+='Comunicarse a:'+ formulario.cleaned_data['correo']
			correo=EmailMessage(titulo, contenido, to=['destinatario@gmail.com'])
			correo.send()
			return HttpResponseRedirect('/')
	else: 
			formulario=ContactoForm()
	return render_to_response('contactoform.html',{'formulario':formulario}, context_instance=RequestContext(request))

def nueva_matricula(request):
	alumnos=Alumno.objects.all()
	cursos=Curso.objects.all()
	if request.method=='POST':
		formulario=MatriculaForm(request.POST, request.FILES)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/matriculas')
	else: 
		formulario=MatriculaForm()
	return render_to_response('matriculaform.html',{'formulario':formulario,'alumnos':alumnos,'cursos':cursos}, context_instance=RequestContext(request))

def nuevo_usuario(request):
	if request.method=='POST':
		formulario=UserCreationForm(request.POST)
		if formulario.is_valid():
			formulario.save()
			return HttpResponseRedirect('/usuario/nuevo')
	else:
		formulario=UserCreationForm()
	return render_to_response('nuevousuario.html',{'formulario':formulario}, context_instance=RequestContext(request))

def mylogin(request):
  if request.method == 'POST':
  	username = request.POST['username']
  	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponseRedirect("/privado/")
		else:
			return render_to_response('noactivo.html', context_instance=RequestContext(request))
	else:
		return render_to_response('nousuario.html', context_instance=RequestContext(request))

def ingresar(request):	
	if not request.user.is_anonymous():
		return HttpResponseRedirect('/privado')
	if request.method == 'POST':
		formulario = AuthenticationForm(request.POST)
		if formulario.is_valid:
			usuario = request.POST['username']
			clave = request.POST['password']
			acceso = authenticate(username=usuario, password=clave)
			if acceso is not None:
				if acceso.is_active:
					login(request, acceso)
					return HttpResponseRedirect('/privado')
				else:
					return render_to_response('noactivo.html', context_instance=RequestContext(request))
			else:
				return render_to_response('nousuario.html', context_instance=RequestContext(request))
	else:
		formulario = AuthenticationForm()
	return render_to_response('ingresar.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def privado(request):
	usuario=request.user
	return render_to_response('privado.html',{'usuario':usuario},context_instance=RequestContext(request))

@login_required(login_url='/ingresar')
def cerrar(request):
	logout(request)
	return HttpResponseRedirect('/cerrar')

def perfil(request, username):
	usuario = request.user
	usuario_no_logueado = User.objects.get(username=username)
	if usuario == User.objects.get(username=username):
		return render_to_response('perfil.html', {'usuario':usuario}, context_instance=RequestContext(request))
	else:
		return render_to_response('perfil_no_logueado.html', {'usuario':usuario_no_logueado}, context_instance=RequestContext(request)) 
		
@login_required
def editar_alumno(request, object_id):
    try:
        alumno = Alumno.objects.get(id = object_id)

    except Alumno.DoesNotExist:
        pass

    if request.POST:
        form = EditarAlumno(request.POST, instance = alumno)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/alumnos/')
        else:
            form = EditarAlumno(instance = alumno)

    return render_to_response("editar_alumno.html", {"alumno": alumno, 'form': form})