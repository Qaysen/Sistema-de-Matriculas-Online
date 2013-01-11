from django.db import models

class Alumno(models.Model):
	nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=100)
	telefono = models.DecimalField(max_digits=6,decimal_places=0)
	correo= models.EmailField()

	def __unicode__(self):
		return self.nombre


class Profesor(models.Model):
	nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=100)
	telefono = models.DecimalField(max_digits=6,decimal_places=0)
	correo= models.EmailField()

	def __unicode__(self):
		return self.nombre


class Curso(models.Model):
	nombre = models.CharField(max_length=50)
	num_creditos=models.IntegerField()

	def __unicode__(self):
		return self.nombre

class Matricula(models.Model):

	IMP_CHOICES=(
			('1','regular'),
			('2','irregular'),
			('3','extemporaneo'),
		)

	fecha = models.DateField() 
	tipo = models.CharField(max_length=10,choices=IMP_CHOICES)
	alumno =models.ForeignKey(Alumno)
	curso =models.ForeignKey(Curso)

	def __unicode__(self):
		return '%s y %s' %(self.alumno,self.curso)

class Dictar(models.Model):
	fecha_ini = models.DateField() 
	fecha_ter = models.DateField() 
	profesor =models.ForeignKey(Profesor)
	curso =models.ForeignKey(Curso)

	def __unicode__(self):
		return '%s y %s' %(self.profesor,self.curso)

class Nota(models.Model):
	IMP_CHOICES=(
			('1','I'),
			('2','II'),
			('3','III'),
		)
	valor =models.IntegerField()
	fecha = models.DateField() 
	trimestre= models.CharField(max_length=5,choices=IMP_CHOICES)
	matricula=models.ForeignKey(Matricula)

	def __unicode__(self):
		return '%s y %s' %(self.valor,self.trimestre)


