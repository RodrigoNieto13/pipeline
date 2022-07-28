from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

#Formulario para la creación/edición de los responsables
class ResponsableModelForm(forms.ModelForm):
    class Meta:
        model = Responsable
        fields = '__all__'

#Estilo de los campos dentro del form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('nombre_completo', css_class = 'form-group col-md-12 mb-3 font-weight-bold'),
                css_class = 'form-row'
            ),
            Submit('submit', 'GUARDAR', css_class = 'form-group form-control col-md-3')
        )

#Formulario para la creación/edición de los clientes o prospectos 
class ProspectoModelForm(forms.ModelForm):
	class Meta:
		model = Prospecto
		fields = '__all__'

#Estilo de los campos dentro del form
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False
		self.helper.layout = Layout(
            Row(
                Column('razon_social', css_class = 'form-group col-md-6 mb-3 font-weight-bold'),
                Column('contacto', css_class = 'form-group col-md-6 mb-3 font-weight-bold'),
                css_class = 'form-row'
            ),
            Row(
                Column('num_tel', css_class = 'form-group col-md-3 mb-3 font-weight-bold'),
                Column('correo', css_class = 'form-group col-md-5 mb-3 font-weight-bold'),
                 Column('giro', css_class = 'form-group col-md-4 mb-3 font-weight-bold'),
                css_class = 'form-row'
            ),
            Row(
                Column('nombre_comercial', css_class = 'form-group col-md-4 mb-3 font-weight-bold'),
                Column('localidad', css_class = 'form-group col-md-4 mb-3 font-weight-bold'),
                 Column('coordenadas', css_class = 'form-group col-md-4 mb-3 font-weight-bold'),
                css_class = 'form-row'
            ),
            Row(
                Column('clasificacion', css_class = 'form-group col-md-3 mb-3 font-weight-bold'),
                Column('responsable', css_class = 'form-group col-md-5 mb-3 font-weight-bold'),
                Column('fase', css_class = 'form-group col-md-4 mb-3 font-weight-bold'),
                css_class = 'form-row'
            ),
            Row(
                Column('observaciones', css_class = 'form-group col-md-12 mb-3 font-weight-bold'),
                css_class = 'form-row'
            ),
            Submit('submit', 'GUARDAR', css_class = 'form-group form-control col-md-3')
        )