from django.urls import path

from .views import dashboard, faturamentomes, clienteatendidosmes, totalestudiomes, TotalFuncionarioList

app_name = 'dashboard'

urlpatterns =[
    #path('', dashboard, name='dashboard'),
    path('dashboard', faturamentomes, name='dashboard-cliente'),
    path('dashboard-cortes-tatuagens', clienteatendidosmes, name='dashboard-cortes-tatuagens'),
    path('dashboard-total-mes', totalestudiomes, name='dashboard-total-mes'),
    path('', TotalFuncionarioList.as_view(), name='dashboard'),
]