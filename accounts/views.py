
from django.http import HttpResponse
#from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from django.core.mail import EmailMessage, send_mail
from django.conf import settings

from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from projeto import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError

from .helpers import send_forget_password_mail

from . models import Profile








# Create your views here.


def signin(request):

    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            if not username or not password:
                messages.success(request, 'Username e senha são necessários.')
                return redirect('/signin')
            user_obj = User.objects.filter(username = username).first()
            if user_obj is None:
                messages.success(request, 'Usuário não encontrado.')
                return redirect('/signin')
        
        
            user = authenticate(username = username , password = password)
            
            if user is None:
                messages.success(request, 'Senha incorreta.')
                return redirect('/signin')
        
            login(request , user)
            return redirect('/cinesd')

                
            
            
    except Exception as e:
        print(e)
    return render(request , 'cinema/signin.html')


                                         


def Register(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')
            

            try:
                if User.objects.filter(username = username).first():
                    messages.success(request, 'Username já existe')
                    return render(request, 'cinema/signup.html')

                if User.objects.filter(email = email).first():
                    messages.success(request, 'Email já existe')
                    return render(request, 'cinema/signup.html')

                if confirm_password != password:
                    messages.success(request, 'SEnhas não coincidem')
                    return render(request, 'cinema/signup.html')
                
                user_obj = User(username = username , email = email)
                user_obj.first_name = fname
                user_obj.last_name = lname
                user_obj.set_password(password)
                user_obj.is_active = True
                user_obj.save()
                
                subject = "Bem vindo ao CineSD"
                message = "Olá " + user_obj.first_name + "!! \n\n" + "Seja Bem vindo ao clube de amigos CineSD!!  \nObrigado por nos escolher para assistir aos grandes sucessos do Cinema! \n\n\n " 
                from_email = settings.EMAIL_HOST_USER
                to_list = [user_obj.email]
                send_mail(subject, message, from_email, to_list, fail_silently=True)

                profile_obj = Profile.objects.create(user = user_obj)
                profile_obj.save()
                return render(request, 'cinema/signin.html')

            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
    
    return render(request, 'cinema/signup.html')

            

                                                                                                                                                                                                                                                           
def signout(request):
    logout(request)
    messages.success(request, "Você deslogou com sucesso!")
    return render(request, 'cinema/cinesd.html')
    

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


def ChangePassword(request, token):
    context = {}
    
    
    try:
        profile_obj = Profile.objects.filter(forget_password_token = token).first()
        context = {'user_id' : profile_obj.user.id}

        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('reconfirm_password')
            user_id = request.POST.get('user_id')

            if user_id is None:
                messages.success(request, 'Usuário não encontrado.')
                return redirect(f'/change-password/{token}/')
            
            
            if new_password != confirm_password:
                messages.success(request, 'Senhas não coincidem.')
                return redirect(f'/change-password/{token}/')
            
            user_obj = User.objects.get(id = user_id)
            user_obj.set_password(new_password)
            user_obj.save()
            return render(request, "cinema/signin.html" )


        

    except Exception as e:
        print(e)
    return render(request, "cinema/change-password.html",context)


import uuid
def ForgetPassword(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')
            
            if not User.objects.filter(username=username).first():
                messages.success(request, 'Não existe usuário com esse Username')
                return render(request, 'cinema/forget.html')
            
            user_obj = User.objects.get(username = username)
            token = str(uuid.uuid4())
            profile_obj= Profile.objects.get(user = user_obj)
            profile_obj.forget_password_token = token
            profile_obj.save()
            send_forget_password_mail(user_obj.email , token)
            messages.success(request, 'Um email foi enviado.')
            return render(request, 'cinema/forget.html')
                
    
    
    except Exception as e:
        print(e)
    return render(request , 'cinema/forget.html')
