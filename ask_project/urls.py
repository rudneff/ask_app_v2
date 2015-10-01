from django.conf.urls import include, url
from django.contrib import admin
from ask_app.views import *

urlpatterns = [

    url(r'^$', AskAppTemplateView.as_view(), name='home-page'),
    # registration
    url(r'^login/', 'django.contrib.auth.views.login', name='login-page'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout-page'),

    # question page; change views
    url(r'^question/(?P<pk>\d+)/$', AskAppTemplateView.as_view(), name='question-page'),

    url(r'^admin/', include(admin.site.urls)),
]
