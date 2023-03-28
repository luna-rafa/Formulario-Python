from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm

def contato(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada com sucesso!')
        else:
            messages.error(request, 'Por favor, corrija os erros indicados.')
    else:
        form = ContactForm()

    return render(request, 'contato.html', {'form': form})


