from django.conf.urls import include, url
from django.contrib import admin
from ask_app.views import *
from ask_project import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^$', QuestionListView.as_view(), name='home-page'),
    # authentication
    url(r'^login/', 'django.contrib.auth.views.login', name='login-page'),
    url(r'^logout/', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout-page'),

    # question pages
    url(r'^question/(?P<pk>\d+)/$', QuestionDetailView.as_view(), name='question-page'),
    url(r'^question/(?P<pk>\d+)/update/$', UserUpdateView.as_view(), name='question-update-page'),
    url(r'^questions/$', QuestionListView.as_view(), name='question-list-page'),
    url(r'^question/create/$', QuestionCreateView.as_view(), name='question-create-page'),
    url(r'^question/(?P<pk>\d+)/delete/$', QuestionDeleteView.as_view(), name='question-delete-page'),

    # answers pages
    url(r'^answer/(?P<pk>\d+)/$', AnswerDetailView.as_view(), name='answer-page'),
    url(r'^answer/(?P<pk>\d+)/update/$', UserUpdateView.as_view(), name='answer-update-page'),
    url(r'^answers/$', AnswerListView.as_view(), name='answer-list-page'),
    url(r'^answer/create/$', AnswerCreateView.as_view(), name='answer-create-page'),
    url(r'^answer/(?P<pk>\d+)/delete/$', AnswerDeleteView.as_view(), name='answer-delete-page'),

    # user pages
    url(r'^user/(?P<pk>\d+)/$', UserDetailView.as_view(), name='user-page'),
    url(r'^user/(?P<pk>\d+)/update/$', UserUpdateView.as_view(), name='user-update-page'),
    url(r'^users/$', UserListView.as_view(), name='user-list-page'),
    url(r'^user/create/$', UserCreateView.as_view(), name='user-create-page'),
    url(r'^user/(?P<pk>\d+)/delete/$', UserDeleteView.as_view(), name='user-delete-page'),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^img/(?P<path>.*)$', 'django.views.static.serve', name='image-page')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)