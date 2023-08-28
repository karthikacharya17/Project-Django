"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from signup.views import signaction
from login.views import loginaction
from home.views import homeaction
from upload.views import uploadproduct
from logout.views import logout1
from about.views import aboutaction
from user.views import useraction
from adminpage.views import adminaction
from viewpageus.views import viewaction
from viewpagead.views import viewactionad
from reguser.views import regaction
from deletead.views import deleteaction
from reject.views import rejectaction
from approv.views import approveaction
from adevent.views import adevaction
from winner.views import winneraction
from event.views import eventaction
from django.conf import settings
from django.conf.urls.static import static







urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signaction),
    path('login/',loginaction),
    path('home/',homeaction),
    path('about/',aboutaction),
    path('upload/',uploadproduct),
    path('user/',useraction),
    path('adminpage/',adminaction),
    path('viewpageus/',viewaction),
    path('viewpagead/',viewactionad),
    path('reguser/',regaction),
    path('deletead/',deleteaction),
    path('approv/',approveaction),
    path('reject/',rejectaction),
    path('event/',eventaction),
    path('logout/',logout1),
    path('adevent/',adevaction),
    path('winner/',winneraction),
   
    
    
    
    



    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
