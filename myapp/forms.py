from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(label='Nome', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Seu nome'}))
    email = forms.EmailField(label='E-mail', widget=forms.EmailInput(attrs={'placeholder': 'Seu e-mail'}))
    message = forms.CharField(label='Mensagem', widget=forms.Textarea(attrs={'placeholder': 'Sua mensagem'}))

    motivo_contato = forms.ChoiceField(label='Motivo do Contato', choices=[
        ('duvida', 'Dúvida'),
        ('sugestao', 'Sugestão'),
        ('reclamacao', 'Reclamação'),
    ])

    def clean_message(self):
        message = self.cleaned_data['message']
        num_palavras = len(message.split())
        if num_palavras < 4:
            raise forms.ValidationError('A mensagem deve conter pelo menos 4 palavras.')
        return message

    class Meta:
        model = Contact
        fields = ['name', 'email', 'motivo_contato', 'message']

