"""capstone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from auth_app.views import LoginFormView, LogoutView, signup
from backend.views import UploadView, file_list, favorite, favorites, SearchView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", file_list, name="file_list"),
    path("login/", LoginFormView.as_view(), name="Login"),
    path("logout/", LogoutView.as_view(), name="Logout"),
    path("signup/", signup, name="Signup"),
    path("upload/", UploadView.as_view(), name="Upload"),
    path("favorites/", favorites, name="Favorites"),
    path("favorite/<int:upload_id>/", favorite, name="favorite"),
    path("search/", SearchView.as_view(), name='search'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'backend.views.handler404'
handler500 = 'backend.views.handler500'
