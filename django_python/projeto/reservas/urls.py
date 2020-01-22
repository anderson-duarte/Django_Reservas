from django.conf.urls import url
from . import views

app_name = 'reservas'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<cliente_id>[0-9]+)/$',views.detalhe, name='detalhe'),
    url(r'^(?P<cliente_id>[0-9]+)/lista/$',views.reservas, name='reservas'),
    url(r'^(?P<cliente_id>[0-9]+)/confirma/$',views.confirma, name='confirma'),
    url(r'^obrigado/$', views.obrigado, name='obrigado'),
    url(r'^contato/$', views.contato, name='contato'),

]