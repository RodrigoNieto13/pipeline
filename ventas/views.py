from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView, DetailView
from .models import *
from .forms import  *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.db.models import Count, Q
import json
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.utils import timezone

now = timezone.now()

# Create your views here.

def home(request):
    return render(request, "index.html")

#Función de logout
def logout_request(request):
    logout(request)
    return redirect("index")

#Función de login
def index(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Usuario y/o cotraseña erroneos")
        else:
            messages.error(request, "Usuario y/o cotraseña erroneos")
    form = AuthenticationForm()
    return render(request = request, template_name = "login.html")


class SuccessView(TemplateView):
    template_name = 'success.html'


def Inicio(request):
    return render(request, "inicio.html")

#clase para crear responsables
class ResponsableCreateView(CreateView):
	model = Responsable
	form_class = ResponsableModelForm
	template_name = 'responsable.html'

	def get_context_data(self, **kwargs):
		context = super(ResponsableCreateView, self).get_context_data(**kwargs)
		if self.request.POST:
			context['resp'] = ResponsableModelForm(self.request.POST,instance=self.object)
		else:
			context['resp'] = ResponsableModelForm(instance=self.object)
		return context

	def form_valid(self, form):
		context = self.get_context_data(form=form)
		resp = context['resp']
		if resp.is_valid():
		    self.object = form.save()
		    responsable = resp.save(commit = False)
		    #responsable.save()
		    return HttpResponseRedirect(reverse('listResponsable'))
		else:
		    return self.render_to_response(self.get_context_data(form = form))

#clase para editar responsables
class ResponsableUpdateView(UpdateView):
	model = Responsable
	form_class = ResponsableModelForm
	template_name = 'responsable_form.html'
	success_url='/listResponsable'

#clase para editar responsables
class ResponsableListView(ListView):
    model = Responsable
    paginate_by = 10
    template_name = 'responsablelist.html'

#clase para crear un cliente
class ProspectoCreateView(CreateView):
	model = Prospecto
	form_class = ProspectoModelForm
	template_name = 'prospecto.html'
	#success_url = 'listProspecto'

	def get_context_data(self, **kwargs):
		context = super(ProspectoCreateView, self).get_context_data(**kwargs)
		if self.request.POST:
			context['pro'] = ProspectoModelForm(self.request.POST,instance = self.object)
		else:
			context['pro'] = ProspectoModelForm(instance = self.object)
		return context

	def form_valid(self, form):
		context = self.get_context_data(form=form)
		pro = context['pro']
		if pro.is_valid():
		    self.object = form.save()
		    prospecto = pro.save(commit=False)
		    return HttpResponseRedirect(reverse('listProspecto'))
		else:
		    return self.render_to_response(self.get_context_data(form = form))

#clase para editar un cliente
class ProspectoUpdateView(UpdateView):
	model = Prospecto
	form_class = ProspectoModelForm
	template_name = 'prospecto_form.html'
	success_url = '/listProspecto'
	
#clase para listar clientes
class ProspectoListView(ListView):
	model = Prospecto
	paginate_by = 10
	template_name = 'prospectolist.html'

class ProspectoDetailView(DetailView):
	model = Prospecto
	template_name = 'prospecto_detail.html'

#funcion para el gráfico pipeline
def Grafico(request):
	#queryset (consulta a la BD) para obtener las cantidades de cada fase
	fase_uno_series = Prospecto.objects.filter(fase = 'F1', fechaReg__year = str(now.year)).count()
	fase_dos_series = Prospecto.objects.filter(fase = 'F2', fechaReg__year = str(now.year)).count()
	fase_tres_series = Prospecto.objects.filter(fase = 'F3', fechaReg__year = str(now.year)).count()
	fase_cuatro_series = Prospecto.objects.filter(fase = 'F4', fechaReg__year = str(now.year)).count()
	fase_cinco_series = Prospecto.objects.filter(fase = 'F5', fechaReg__year = str(now.year)).count()
	fase_seis_series = Prospecto.objects.filter(fase = 'F6', fechaReg__year = str(now.year)).count()

	cl_uno = Prospecto.objects.filter(fase = 'F1', fechaReg__year = str(now.year))
	cl_dos = Prospecto.objects.filter(fase = 'F2', fechaReg__year = str(now.year))
	cl_tres = Prospecto.objects.filter(fase = 'F3', fechaReg__year = str(now.year))
	cl_cuatro = Prospecto.objects.filter(fase = 'F4', fechaReg__year = str(now.year))
	cl_cinco = Prospecto.objects.filter(fase = 'F5', fechaReg__year = str(now.year))
	cl_seis = Prospecto.objects.filter(fase = 'F6', fechaReg__year = str(now.year))

#Regresar las listas transformadas en json para su uso dentro de la plantilla grafico.html
	return render(request, 'grafico.html', {
        'fase_uno_series': json.dumps(fase_uno_series),
        'fase_dos_series': json.dumps(fase_dos_series),
        'fase_tres_series': json.dumps(fase_tres_series),
        'fase_cuatro_series': json.dumps(fase_cuatro_series),
        'fase_cinco_series': json.dumps(fase_cinco_series),
        'fase_seis_series': json.dumps(fase_seis_series),
        'cl_uno': cl_uno,
        'cl_dos': cl_dos,
        'cl_tres': cl_tres,
        'cl_cuatro': cl_cuatro,
        'cl_cinco': cl_cinco,
        'cl_seis': cl_seis,
    })

def GraficoMensual(request):
	return render(request, "grafico_mensual.html")

def GraficoM(request, fecha):
	fase_uno_series = Prospecto.objects.filter(fase = 'F1', fechaReg__month = str(fecha), fechaReg__year = str(now.year)).count()
	fase_dos_series = Prospecto.objects.filter(fase = 'F2', fechaReg__month = str(fecha), fechaReg__year = str(now.year)).count()
	fase_tres_series = Prospecto.objects.filter(fase = 'F3', fechaReg__month = str(fecha), fechaReg__year = str(now.year)).count()
	fase_cuatro_series = Prospecto.objects.filter(fase = 'F4', fechaReg__month = str(fecha), fechaReg__year = str(now.year)).count()
	fase_cinco_series = Prospecto.objects.filter(fase = 'F5', fechaReg__month = str(fecha), fechaReg__year = str(now.year)).count()
	fase_seis_series = Prospecto.objects.filter(fase = 'F6', fechaReg__month = str(fecha), fechaReg__year = str(now.year)).count()

	cl_uno = Prospecto.objects.filter(fase = 'F1', fechaReg__month = str(fecha), fechaReg__year = str(now.year))
	cl_dos = Prospecto.objects.filter(fase = 'F2', fechaReg__month = str(fecha), fechaReg__year = str(now.year))
	cl_tres = Prospecto.objects.filter(fase = 'F3', fechaReg__month = str(fecha), fechaReg__year = str(now.year))
	cl_cuatro = Prospecto.objects.filter(fase = 'F4', fechaReg__month = str(fecha), fechaReg__year = str(now.year))
	cl_cinco = Prospecto.objects.filter(fase = 'F5', fechaReg__month = str(fecha), fechaReg__year = str(now.year))
	cl_seis = Prospecto.objects.filter(fase = 'F6', fechaReg__month = str(fecha), fechaReg__year = str(now.year))

	return render(request, 'grafico_mes.html', {
        'fase_uno_series': json.dumps(fase_uno_series),
        'fase_dos_series': json.dumps(fase_dos_series),
        'fase_tres_series': json.dumps(fase_tres_series),
        'fase_cuatro_series': json.dumps(fase_cuatro_series),
        'fase_cinco_series': json.dumps(fase_cinco_series),
        'fase_seis_series': json.dumps(fase_seis_series),
        'cl_uno': cl_uno,
        'cl_dos': cl_dos,
        'cl_tres': cl_tres,
        'cl_cuatro': cl_cuatro,
        'cl_cinco': cl_cinco,
        'cl_seis': cl_seis,
    })

def Marcadores(request):
	marcador = Prospecto.objects.values('nombre_comercial','coordenadas')
	return render(request, 'clientes_mark.html', {'marcador': marcador})
