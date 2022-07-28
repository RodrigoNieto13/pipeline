from django.urls import path, reverse
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
	path('', login_required(home), name = 'index'),
	path('accounts/logout/', login_required(logout_request), name = 'milogout'),
    path('accounts/login/', index , name = 'index'),
    #Responsables
	path('crearResponsable', ResponsableCreateView.as_view(), name = 'crearResponsable'),
	path('updateResponsable/<pk>/', ResponsableUpdateView.as_view(), name = 'updateResponsable'),
	path('listResponsable', ResponsableListView.as_view(), name = 'listResponsable'),
	#Prospecto
	path('listProspecto', ProspectoListView.as_view(), name = 'listProspecto'),
	path('crearProspecto', ProspectoCreateView.as_view(), name = 'crearProspecto'),
	path('updateProspecto/<pk>/', ProspectoUpdateView.as_view(), name = 'updateProspecto'),
	path('detailProspecto/<pk>/', ProspectoDetailView.as_view(), name = 'detailProspecto'),
	path('marcadores', Marcadores, name = 'marcadores'),
	#Pipeline
	path('grafico', Grafico, name = 'grafico'),
	path('grafico_mensual', GraficoMensual, name = 'grafico_mensual'),
	path('grafico_m/<fecha>/', GraficoM, name = 'grafico_m'),
	#Inicio
	path('inicio', Inicio, name = 'inicio'),
	#SUCCESS
	path('success', SuccessView.as_view(), name='success'),
]
