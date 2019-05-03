from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from center import views


from django.views.generic.base import TemplateView

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    path('', views.detail, name='detail'),
    path('<int:phong_id>/', views.cacphong, name='cacphong'),
    path('onsite/', views.Onsite, name='Onsite'),
    path('test/', views.Test, name='Test'),
    path('user/', views.user1, name='user'),
    path('about/', views.About, name='About'),
    path('contact/', views.Contact, name='Contact'),
    path('staff/', views.Staff, name='Staff'),
    path('all/<slug:slug>/', views.cacphong1, name='cacphong1'),
    path('BN/update/<slug:slug>/', views.updatetc, name='updatetc'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('admin1/', views.input1, name='input1'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
