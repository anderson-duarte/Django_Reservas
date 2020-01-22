from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Cliente, Reservas
from .forms import formContato

# Create your views here.

def index(request):
    ultimos_clientes = Cliente.objects.order_by('-registrado_em')[:5]
    context = {'ultimos_clientes' : ultimos_clientes, }
    return render(request, 'reservas/index.html', context)


def detalhe(request, cliente_id):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
    except Cliente.DoesNotExist:
        raise Http404("Cliente não existe")
    return render(request, 'reservas/detalhe.html', {'cliente': cliente})


def reservas(request, cliente_id):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
    except Cliente.DoesNotExist:
        raise Http404("Cliente não existe")

    return render(request, 'reservas/lista.html', {'cliente': cliente})


def confirma(request, cliente_id):
    try:
        cliente = Cliente.objects.get(pk=cliente_id)
    except Cliente.DoesNotExist:
        raise Http404("Cliente não existe")

    confirmados = request.POST.getlist('confirmacao')
    for reserva_id in confirmados:
        try:
            reserva = cliente.reserva_set.get(pk=reserva_id)
        except (KeyError, Reservas.DoesNotExist):
            return render(request, 'reservas/detalhe.html', {'cliente': cliente,
                                                            'error_message': "Reserva nao encontrada"})
        else:
            reserva.confirmada = True
            reserva.save()
        return HttpResponseRedirect(reverse('reservas:reservas', args=(cliente.id)))

def contato(request):
    if request.method == 'POST':
        form = formContato(request.POST)
        if form.is_valid():
            assunto = form.cleaned_data['assunto']
            comentarios = form.cleaned_data['comentarios']
            remetente = form.cleaned_data['email']
            destinatarios = ['duartelgk4@gmail.com']
            try:
                send_mail(assunto, comentarios, remetente, destinatarios)
            except BadHeaderError:
                return HttpResponse('Cabeçalho Inválido!!!')
            return HttpResponseRedirect('/reservas/obrigado/')

    else:
        form = formContato()

    return render(request, 'reservas/contato.html', {'form': form})

def obrigado(request):
    return render(request, 'reservas/obrigado.html')