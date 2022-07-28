from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from datetime import datetime

# Create your models here.

# listas de opciones para los formularios
clasificacion = [
    ('A', 'Prioridad Alta'),
    ('B', 'Muy Importante'),
    ('C', 'Importante'),
    ('D', 'Regular'),
]

fase = [
    ('F1', 'Buscar Nuevas Oportunidades de Negocio'),
    ('F2', 'Identificar Necesidades del Prospecto'),
    ('F3', 'Formular la Propuesta'),
    ('F4', 'Negociar el Cierre'),
    ('F5', 'Administrar la Implementación'),
    ('F6', 'Lista Negra')
]


"""class Clasificacion(models.Model):
    tipo_clasif = models.CharField(max_length = 1)
    descripcion_clasif = models.CharField(max_length = 50)

    def __str__(self):
        return self.tipo_clasif"""


"""class Fase(models.Model):
	tipo_fase = models.CharField(max_length = 1)
	descripcion_fase = models.CharField(max_length = 50)

	def __str__(self):
		return self.tipo_fase"""

#modelo resoponsables, tipo tabla en una BD
class Responsable(models.Model):
	nombre_completo = models.CharField(max_length = 200, verbose_name = 'Nombre Completo')

	def __str__(self):
		return self.nombre_completo

	def get_absolute_url(self):
		return reverse('updateResponsable', args = [str(self.id)])

#modelo prospectos(clientes), tipo tabla en una BD
class Prospecto(models.Model):
	razon_social = models.CharField(max_length = 200, verbose_name = 'Razón Social')
	contacto = models.CharField(max_length = 200, verbose_name = 'Contacto')
	num_tel = models.CharField(max_length = 40, verbose_name = 'Número de Teléfono', null = True)
	correo = models.CharField(max_length=70, verbose_name = 'Correo Electronico', null = True)
	nombre_comercial = models.CharField(max_length = 200, verbose_name = 'Nombre Comercial')
	giro = models.CharField(max_length = 200,  verbose_name = 'Giro')
	localidad = models.CharField(max_length = 200, verbose_name = 'Localidad')
	coordenadas = models.CharField(max_length = 100, verbose_name = 'Coordenadas', null = True)
	fechaReg = models.DateField(null = True, blank = True , verbose_name = 'Fecha de Registro', default = now, editable = False )
	clasificacion = models.CharField(max_length = 1, choices = clasificacion, default = '1')
	responsable = models.ForeignKey('Responsable', on_delete = models.SET_NULL, null = True)
	fase = models.CharField(max_length = 2, choices = fase, default = '1')
	observaciones = models.CharField(max_length = 254, verbose_name = 'Observaciones', null = True)

	def __str__(self):
		return '%s, %s, %s, %s, %s' % (self.razon_social, self.responsable, self.fase, self.clasificacion, self.fechaReg)

	def get_absolute_url(self):
		return reverse('updateProspecto', args = [str(self.id)])

	def get_url(self):
		return reverse('detailProspecto', args = [str(self.id)])