"""
URL configuration for stremyfy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

def admin_redirect(request):
    if request.user.is_superuser:
        return redirect('/admin/')
    else:
        return redirect('/')

admin.site.site_header = "Streamify Admin Panel"
admin.site.site_title = "Streamify Watch Unlimited"
admin.site.index_title = "Welcome to Streamify Online Watching Platform"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('live_streaming.urls')),
    path('', admin_redirect),  # Redirect root URL to admin panel for superusers
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
