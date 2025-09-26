from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string

def enviar_email_cadastro_bem_vindo(email, nome):
    mensagem = render_to_string("send_email_utils/bem_vindo.html", {"mensagem": "Olá " + nome + ", seja bem-vindo ao FindMyPets! Ficamos muito felizes com a seu cadastro"})
    msg = EmailMultiAlternatives(
        "Bem vindo ao FindMyPets!",
        "Olá " + nome + ", seja bem-vindo ao FindMyPets! Ficamos muito felizes com a seu cadastro",
        settings.EMAIL_HOST_USER,
        [email],
    )
    msg.attach_alternative(mensagem, "text/html")
    msg.send()