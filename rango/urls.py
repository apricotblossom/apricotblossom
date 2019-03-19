from django.conf.urls import url 
from rango import views

urlpatterns = [ 
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    url(r'^suggest/$', views.suggest_category, name='suggest_category'),
    url(r'^add_category/$', views.add_category, name='add_category'), 
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',
        views.add_page, name='add_page'),
    url(r'^register/$', views.register,name='register'),
    url(r'^login/$', views.user_login, name='login'),  
    url(r'^restricted/', views.restricted, name='restricted'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^game/$', views.singlegamereview, name='singlegamereview'),
    url(r'^grandtheftautovreview/$', views.grandtheftautovreview, name='grandtheftautovreview'),
    url(r'^reddeadredemptionⅡreview/$', views.reddeadredemptionⅡreview, name='reddeadredemptionⅡreview'),
    url(r'^monsterhunterworldreview/$', views.monsterhunterworldreview, name='monsterhunterworldreview'),
    url(r'^devilmaycryvreview/$', views.devilmaycryvreview, name='devilmaycryvreview'),
    url(r'^pokémongoreview/$', views.pokémongoreview, name='pokémongoreview'),
    url(r'^minecraftreview/$', views.minecraftreview, name='minecraftreview'),
    url(r'^nba2k19review/$', views.nba2k19review, name='nba2k19review'),
    url(r'^brawlstarsreview/$', views.brawlstarsreview, name='brawlstarsreview'),
    url(r'^clashroyalereview/$', views.clashroyalereview, name='clashroyalereview'),
    url(r'^boombeachreview/$', views.boombeachreview, name='boombeachreview'),
    url(r'^clashofclansreview/$', views.clashofclansreview, name='clashofclansreview'),
    url(r'^gamereview/$', views.gamereview, name='gamereview'),
    url(r'^gamereview2/$', views.gamereview2, name='gamereview2'),
    url(r'^gamereview3/$', views.gamereview3, name='gamereview3'),
    url(r'^adultgamereview/$', views.adultgamereview, name='adultgamereview'),
    url(r'^negligeelovestoriesreview/$', views.negligeelovestoriesreview, name='negligeelovestoriesreview'),
    url(r'^callofdutyblackops4review/$', views.callofdutyblackops4review, name='callofdutyblackops4review'),
    url(r'^theinvisibleguardianreview/$', views.theinvisibleguardianreview, name='theinvisibleguardianreview'),
    url(r'^dota2review/$', views.dota2review, name='dota2review'),
    url(r'^gamenews/$', views.gamenews, name='gamenews'),
    url(r'^deadbydaylightnews/$', views.deadbydaylightnews, name='deadbydaylightnews'),
    url(r'^conanexiles/$', views.conanexilesnews, name='cononexilesnews'),
    url(r'^ps4news/$', views.ps4news, name='ps4news'),
    url(r'^marionews/$', views.marionews, name='marionews'),
    url(r'^adultgamenews/$', views.adultgamenews, name='adultgamenews'),
    url(r'^senrankaguraburstrenewal/$', views.senrankaguraburstrenewal, name='senrankaguraburstrenewal'),
    url(r'^gta6news/$', views.gta6news, name='gta6news'),
    url(r'^deadoralive6news/$', views.deadoralivenews, name='deadoralive6news'),
    url(r'goto/$', views.track_url, name='goto'),
    url(r'^register_profile/$', views.register_profile, name='register_profile'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^profiles/$', views.list_profiles, name='list_profiles'),
    url(r'^like/$', views.like_category, name='like_category'),
]
