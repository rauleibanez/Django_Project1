from django.urls import path
from myapp  import views

urlpatterns = [
    path('', views.index, name='home'),
    path('acerca/', views.acerca, name='about'),
    path('hello/<str:username>', views.saludo, name='hello'),
    path('proyectos/', views.proyectos, name='projects'),
    path('details/<int:id>', views.detalleproyecto, name='details'),
    path('ttareas/', views.ttareas, name='ttasks'),
    path('tareas/<int:id>', views.tareas),
    path('nuevatarea/', views.nuevatarea, name='newtask'),
    path('nuevoproyecto/', views.nuevoproyecto, name='newproject'),
]