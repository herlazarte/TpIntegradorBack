
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Cliente
from apps.cliente.forms import ClienteForm

class ListaClientesView(TemplateView):
    template_name = 'listado_clientes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.all()
        return context

class AltaClientesView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'alta_cliente.html'
    success_url = '/alta_cliente/'

class DashboardClientesView(TemplateView):
    template_name = 'dashboard_cliente.html'

class HomeView(TemplateView):
    template_name = "base.html"


# 1. Crear vistas para cada operación

# Debes crear vistas para cada una de las operaciones que deseas realizar:

# Crear: una vista para crear un nuevo cliente
# Listar: una vista para mostrar la lista de clientes
# Editar: una vista para editar un cliente existente
# Eliminar: una vista para eliminar un cliente

# 2. Crear URLs para cada vista

# Debes crear URLs para cada una de las vistas que creaste en el paso anterior. Por ejemplo:
# # urls.py
# from django.urls import path
# from . import views

# urlpatterns = [
#     path('clientes/', views.ClienteListView.as_view(), name='cliente_list'),
#     path('clientes/crear/', views.ClienteCreateView.as_view(), name='cliente_create'),
#     path('clientes/<int:pk>/editar/', views.ClienteUpdateView.as_view(), name='cliente_update'),
#     path('clientes/<int:pk>/eliminar/', views.ClienteDeleteView.as_view(), name='cliente_delete'),
# ]

# 3. Crear vistas concretas

# Debes crear vistas concretas para cada una de las operaciones. Por ejemplo:

# ClienteListView: una vista que muestra la lista de clientes
# # views.py
# from django.views.generic import ListView
# from .models import Cliente

# class ClienteListView(ListView):
#     model = Cliente
#     template_name = 'clientes/list.html

# ClienteCreateView: una vista que crea un nuevo cliente
# # views.py
# from django.views.generic import CreateView
# from .forms import ClienteForm

# class ClienteCreateView(CreateView):
#     form_class = ClienteForm
#     template_name = 'clientes/crear.html'
#     success_url = reverse_lazy('cliente_list')

# ClienteUpdateView: una vista que edita un cliente existente
# # views.py
# from django.views.generic import UpdateView
# from .forms import ClienteForm

# class ClienteUpdateView(UpdateView):
#     form_class = ClienteForm
#     model = Cliente
#     template_name = 'clientes/editar.html'
#     success_url = reverse_lazy('cliente_list')

# ClienteDeleteView: una vista que elimina un Cliente
# # views.py
# from django.views.generic import DeleteView
# from .models import Cliente

# class ClienteDeleteView(DeleteView):
#     model = Cliente
#     template_name = 'clientes/eliminar.html'
#     success_url = reverse_lazy('cliente_list')

# #################################################################

# {% extends 'base.html' %}

# {% block content %}
#   <h1>Lista de Clientes</h1>
#   <ul>
#     {% for cliente in object_list %}
#       <li>
#         {{ cliente.nombre }} {{ cliente.apellido }} ({{ cliente.email }})
#         <a href="{% url 'cliente_update' cliente.pk %}">Editar</a>
#         <a href="{% url 'cliente_delete' cliente.pk %}">Eliminar</a>
#       </li>
#     {% endfor %}
#   </ul>
#   <a href="{% url 'cliente_create' %}">Crear nuevo cliente</a>
# {% endblock %}   
# ################################################################# 
# {% extends 'base.html' %}

# {% block content %}
#   <h1>Crear nuevo cliente</h1>
#   <form method="post">
#     {% csrf_token %}
#     {{ form.as_p }}
#     <button type="submit">Crear</button>
#   </form>
# {% endblock %}
# #################################################################
# {% extends 'base.html' %}

# {% block content %}
#   <h1>Editar cliente</h1>
#   <form method="post">
#     {% csrf_token %}
#     {{ form.as_p }}
#     <button type="submit">Guardar cambios</button>
#   </form>
# {% endblock %}
# #################################################################
# {% extends 'base.html' %}

# {% block content %}
#   <h1>Eliminar cliente</h1>
#   <p>¿Estás seguro de que deseas eliminar al cliente {{ object.nombre }} {{ object.apellido }}?</p>
#   <form method="post">
#     {% csrf_token %}
#     <button type="submit">Eliminar</button>
#   </form>
# {% endblock %}
# #################################################################