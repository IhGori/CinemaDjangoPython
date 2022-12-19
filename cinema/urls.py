from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url


app_name = 'cinema'

urlpatterns = [
   path('cinesd', views.home, name="home"),
   path('contato', views.contato, name="contato"),
   path('programacao', views.programacao, name="programacao"),
   path('snackbar',views.snackbar,name="snackbar"),
   path('promocoes',views.promocoes,name="promocoes"),
   path('info_filmes', views.info_filmes,name="info_filmes"),
   path('info_movies', views.info_movies,name="info_movies"),
   path('autodacompadecida', views.autodacompadecida, name="autodacompadecida"),
   path('batman',views.batman,name="batman"),
   path('belfast', views.belfast,name="belfast"),
   path('carasmalvados',views.carasmalvados,name="carasmalvados"),
   path('oritual',views.oritual,name="oritual"),
   path('swordart',views.swordart,name="swordart"),
   path('uncharted',views.uncharted,name="uncharted"),
   path('morbius',views.morbius,name="morbius"),
   path('sonic2',views.sonic2,name="sonic2"),
   path('jujutsu',views.jujutsu,name="jujutsu"),
   path('animaisfantasticos',views.animaisfantasticos,name="animaisfantasticos"),
   path('drstrange2',views.drstrange2,name="drstrange2"),
   path('spider2',views.spider2,name="spider2"),
   path('avatar2',views.avatar2,name="avatar2"),
   path('detailOAuto/<str:pk>', views.sessao_detail_view_oAuto, name="detailOAuto"),
   path('detailbatman/<str:pk>', views.sessao_detail_view_batman, name="detailbatman"),
   path('detailbelfast/<str:pk>', views.sessao_detail_view_belfast, name="detailbelfast"),
   path('detailcaras/<str:pk>', views.sessao_detail_view_caras, name="detailcaras"),
   path('detailritual/<str:pk>', views.sessao_detail_view_ritual, name="detailritual"),
   path('detailsword/<str:pk>', views.sessao_detail_view_sword, name="detailsword"),
   path('detailuncha/<str:pk>', views.sessao_detail_view_uncha, name="detailuncha"),
   path('detailanimais/<str:pk>', views.sessao_detail_view_animais, name="detailanimais"),
   path('detaildoutor/<str:pk>', views.sessao_detail_view_doutor, name="detaildoutor"),
   path('detailjujutsu/<str:pk>', views.sessao_detail_view_jujutsu, name="detailjujutsu"),
   path('detailmorbius/<str:pk>', views.sessao_detail_view_morbius, name="detailmorbius"),
   path('detailsonic/<str:pk>', views.sessao_detail_view_sonic, name="detailsonic"),
   path('venda/<str:pk>', views.venda, name="venda"),
   path('venda_batman', views.venda_batman,name="venda_batman"),
   path('venda_animaisfantasticos',views.venda_animaisfantasticos,name="venda_animaisfantasticos"),
   path('venda_autodacompadecida',views.venda_autodacompadecida,name="venda_autodacompadecida"),
   path('venda_belfast',views.venda_belfast,name="venda_belfast"),
   path('venda_carasmalvados',views.venda_carasmalvados,name="carasmalvados"),
   path('venda_drstrange2',views.venda_drstrange2,name="drstrange2"),
   path('venda_jujutsu',views.venda_jujutsu,name="venda_jujutsu"),
   path('venda_morbius',views.venda_morbius,name="venda_morbius"),
   path('venda_oritual',views.venda_oritual,name="venda_oritual"),
   path('venda_sonic2',views.venda_sonic2,name="venda_sonic2"),
   path('venda_swordart',views.venda_swordart, name="venda_swordart"),
   path('venda_uncharted',views.venda_uncharted, name="venda_uncharted"),

   
   url(r'^welcome_user/$',views.welcome_user,name='welcome_user'),
]

'''path('venda_batman',views.venda_batman,name="venda_batman"),
   path('venda_animaisfantasticos',views.venda_animaisfantasticos,name="animaisfantasticos"),
   path('venda_autodacompadecida',views.venda_autodacompadecida,name="venda_autodacompadecida"),
   path('venda_belfast',views.venda_belfast,name="venda_belfast"),
   path('venda_carasmalvados',views.venda_carasmalvados,name="carasmalvados"),
   path('venda_drstrange2',views.venda_drstrange2,name="drstrange2"),
   path('venda_jujutsu',views.venda_jujutsu,name="venda_jujutsu"),
   path('venda_morbius',views.venda_morbius,name="venda_morbius"),
   path('venda_oritual',views.venda_oritual,name="venda_oritual"),
   path('venda_sonic2',views.venda_sonic2,name="venda_sonic2"),
   path('venda_swordart',views.venda_swordart, name="venda_swordart"),
   path('venda_uncharted',views.venda_uncharted, name="venda_uncharted"),'''
   