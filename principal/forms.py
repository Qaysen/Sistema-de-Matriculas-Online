#encoding:utf-8
from principal.models import Alumno, Profesor, Curso, Matricula, Dictar, Nota
from django import forms
from django.forms import ModelForm



class AlumnoForm(ModelForm):
	class Meta:
		model=Alumno

class CursoForm(ModelForm):
	class Meta:
		model=Curso

class ProfesorForm(ModelForm):
	class Meta:
		model=Profesor

class ContactoForm(forms.Form):
	correo = forms.EmailField(label='Tu correo electronico')
	mensaje = forms.CharField(widget=forms.Textarea)

class MatriculaForm(ModelForm):
	class Meta:
		model=Matricula