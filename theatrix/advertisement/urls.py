"""theatrix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path
from .import views

urlpatterns = [
    path('types', views.types),
    path('typesview', views.typesview),
    path('delete/<type>', views.typedeleteview),
    path('typesupdate/<type>', views.typeupdateview),
    path('items', views.items),
    path('itemsview', views.itemsview),
    path('accounts', views.accounts),
    path('accountsview', views.accountsview),
    path('show', views.show),
    path('showview', views.showview),
    path('delete/<type>', views.typedeleteview)
]
