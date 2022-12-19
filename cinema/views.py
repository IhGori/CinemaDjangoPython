from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse
#from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from django.core.mail import EmailMessage, send_mail
from django.conf import settings



from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from projeto import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from . tokens import generate_token

from .models import *
from . models import Post, Programacao, Sessao



# Create your views here.
def home(request):
    return render(request, "cinema/cinesd.html")


def snackbar(request):
    return render(request, "cinema/snackbar.html")

def promocoes(request):
    return render(request, "cinema/promocoes.html")

def corporativo(request):
    return render(request, "cinema/corporativo.html")

def info_filmes(request):
    return render(request, "base_filmes.html")

def info_movies(request):
    return render(request, "base_filmes2.html")
#Sessões detalhadas
def sessao_detail_view_oAuto(request, pk = None, *args, **kwargs):
    instance = Sessao.objects.filter(filme__titulo__icontains="O Auto")
    #instance = Sessao.objects.get(pk=pk)
    context = {
        'object':instance,
        
    }
    return render(request, "cinema/sessao.html", context)

def sessao_detail_view_batman(request, pk = None, *args, **kwargs):
    instance = Sessao.objects.filter(filme__titulo__icontains="Batman")
    context = {
        'object':instance,
        
    }
    return render(request, "cinema/sessao.html", context)

def sessao_detail_view_belfast(request, pk = None, *args, **kwargs):
    instance = Sessao.objects.filter(filme__titulo__icontains="Belfast")
    context = {
        'object':instance,
        
    }
    return render(request, "cinema/sessao.html", context)

def sessao_detail_view_belfast(request, pk = None, *args, **kwargs):
    instance = Sessao.objects.filter(filme__titulo__icontains="Belfast")
    context = {
        'object':instance,
        
    }
    return render(request, "cinema/sessao.html", context)

def sessao_detail_view_caras(request, pk = None, *args, **kwargs):
    instance = Sessao.objects.filter(filme__titulo__icontains="Os Caras")
    context = {
        'object':instance,
        
    }
    return render(request, "cinema/sessao.html", context)

def sessao_detail_view_ritual(request, pk = None, *args, **kwargs):
    instance = Sessao.objects.filter(filme__titulo__icontains="Ritual")
    context = {
        'object':instance,
        
    }
    return render(request, "cinema/sessao.html", context)

def sessao_detail_view_sword(request, pk = None, *args, **kwargs):
    instance = Sessao.objects.filter(filme__titulo__icontains="Sword")
    context = {
        'object':instance,
        
    }
    return render(request, "cinema/sessao.html", context)

def sessao_detail_view_uncha(request, pk = None, *args, **kwargs):
    instance = Sessao.objects.filter(filme__titulo__icontains="Uncharted")
    context = {
        'object':instance,
        
    }
    return render(request, "cinema/sessao.html", context)

def sessao_detail_view_animais(request, pk = None, *args, **kwargs):
    instance = Sessao.objects.filter(filme__titulo__icontains="Animais")
    context = {
        'object':instance,
        
    }
    return render(request, "cinema/sessao.html", context)

def sessao_detail_view_doutor(request, pk = None, *args, **kwargs):
    instance = Sessao.objects.filter(filme__titulo__icontains="Doutor")
    context = {
        'object':instance,
        
    }
    return render(request, "cinema/sessao.html", context)

def sessao_detail_view_jujutsu(request, pk = None, *args, **kwargs):
    instance = Sessao.objects.filter(filme__titulo__icontains="Jujutsu")
    context = {
        'object':instance,
        
    }
    return render(request, "cinema/sessao.html", context)

def sessao_detail_view_morbius(request, pk = None, *args, **kwargs):
    instance = Sessao.objects.filter(filme__titulo__icontains="Morbius")
    context = {
        'object':instance,
        
    }
    return render(request, "cinema/sessao.html", context)

def sessao_detail_view_sonic(request, pk = None, *args, **kwargs):
    instance = Sessao.objects.filter(filme__titulo__icontains="Sonic")
    context = {
        'object':instance,
        
    }
    return render(request, "cinema/sessao.html", context)

#Tela de Venda
def venda(request, pk = None, *args, **kwargs):
    sess = Sessao.objects.get(pk=pk)
    context = {
        'object': sess,
    }
    return render(request, "cinema/venda.html", context)



#Telas de Vendas
def venda_batman(request):
    return render(request, "cinema/vendas/venda_batman.html")

def venda_autodacompadecida(request):
    return render(request, "cinema/vendas/venda_autodacompadecida.html")

def venda_belfast(request):
    return render(request, "cinema/vendas/venda_belfast.html")

def venda_carasmalvados(request):
    return render(request, "cinema/vendas/venda_carasmalvados.html")

def venda_oritual(request):
    return render(request, "cinema/vendas/venda_oritual.html")

def venda_swordart(request):
    return render(request, "cinema/vendas/venda_swordart.html")

def venda_uncharted(request):
    return render(request, "cinema/vendas/venda_uncharted.html")

def venda_animaisfantasticos(request):
    return render(request, "cinema/vendas/venda_animaisfantasticos.html")

def venda_drstrange2(request):
    return render(request, "cinema/vendas/venda_drstrange2.html")

def venda_jujutsu(request):
    return render(request, "cinema/vendas/venda_jujutsu.html")

def venda_morbius(request):
    return render(request, "cinema/vendas/venda_morbius.html")

def venda_sonic2(request):
    return render(request, "cinema/vendas/venda_sonic2.html")

def venda_belfast(request):
    return render(request, "cinema/vendas/venda_belfast.html")




#Telas de Filmes em Cartaz
def batman(request):
    return render(request, "cinema/cartaz/batman.html")

def autodacompadecida(request):
    return render(request, "cinema/cartaz/autodacompadecida.html")

def belfast(request):
    return render(request, "cinema/cartaz/belfast.html")

def carasmalvados(request):
    return render(request, "cinema/cartaz/carasmalvados.html")

def oritual(request):
    return render(request, "cinema/cartaz/oritual.html")

def swordart(request):
    return render(request, "cinema/cartaz/swordart.html")

def uncharted(request):
    return render(request, "cinema/cartaz/uncharted.html")


#Telas de Filmes em Breve
def morbius(request):
    return render(request, "cinema/embreve/morbius.html")

def sonic2(request):
    return render(request, "cinema/embreve/sonic2.html")

def jujutsu(request):
    return render(request, "cinema/embreve/jujutsu.html")

def animaisfantasticos(request):
    return render(request, "cinema/embreve/animaisfantasticos.html")

def drstrange2(request):
    return render(request, "cinema/embreve/drstrange2.html")

def spider2(request):
    return render(request, "cinema/embreve/spider2.html")

def avatar2(request):
    return render(request, "cinema/embreve/avatar2.html")


#def contato(request):

 #   if request.method == 'POST':
  #      subject = request.POST.get('subject')
   #     message = request.POST.get('message')
    #    email = request.POST.get('email')
     #   email_cinesd = 'cinesdcontact@gmail.com'
      #  message_cinesd = 'Mensagem recebida com sucesso'
       # send_mail(subject, message, settings.EMAIL_HOST_USER,
        #          [email_cinesd], fail_silently=False)
        #return render(request, 'cinema/email_sent.html', {'email': email})

    #return render(request, 'cinema/home.html', {})



def contato(request):

    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        subject_cinesd = 'CineSD'
        email_cinesd = 'cinesdcontact@gmail.com'
        message_cinesd = 'Obrigado por entrar em contato com a redes de cinemas, CineSD. \n\n Em breve retornaremos com a sua solicitação.'        
        datatuple = (
                (subject, message, email, ['cinesdcontact@gmail.com']),
                (subject_cinesd, message_cinesd, email_cinesd, [email]),
            )
        send_mass_mail(datatuple)
        

    return render(request, 'cinema/contato.html', {})




#def activate(request, uidb64, token):
 #   try:
  #      uid = force_text(urlsafe_base64_decode(uidb64))
   #     myuser = User.objects.get(pk=uid)
    #except (TypeError, ValueError, OverflowError, User.DoesNotExist):
     #   myuser = None

    #if myuser is not None and generate_token.check_token(myuser, token):
     #   myuser.is_active = True
      #  myuser.save()
       # login(request, myuser)
        #return redirect("cinema/home.html")
                                 #return HttpResponse('Obrigado por fazer confirmação a de cadastro! Agora faça o login')
    #else:
     #   return render(request, 'cinema/activation_failed.html')
                                      #return HttpResponse('O link de ativação é invalido')


        #Postagem
def programacao(request):
    pics = Post.objects.all()
    return render(request, 'cinema/programacao.html',{"pics":pics})


def welcome_user(request):      
    if 'cat_name' in request.GET:
       filter_category = request.GET.getlist('cat_name')
       my_products = Add_prod.objects.filter(cat__in=filter_category) 
       context = { "products":my_products}
    else:
       my_products = Add_prod.objects.all()     
       context = { "products":my_products}
    return render(request,"teste.html",context)
