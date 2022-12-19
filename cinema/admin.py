from django.contrib import admin
from . models import Programacao, Filme, Cinema,Salas, Sessao
from . models import *

from . models import Add_cat, Add_prod



# Register your models here.

admin.site.register(Programacao)
admin.site.register(Filme)
admin.site.register(Cinema)
admin.site.register(Salas)
admin.site.register(Sessao)
admin.site.register(Add_cat)
admin.site.register(Add_prod)
