"""
URL configuration for SmartInvSalesInt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from .views import (
    index,
    ProductCreateView,
    ProductListView,
    ProductDetailView,
    ProductInventoryMovement,
    ProductUpdateView,
    ProductSoftDeleteView,
)

urlpatterns = [
    path('', index.as_view, name = "index"),
    
    path("Products/",ProductCreateView.as_view(), name = "Products-create"),

    path("Products/list",ProductListView.as_view(), name = "Products-lists"),

    path("product/<int:pk>/",ProductDetailView.as_view(), name = "Products-details"),

    path("product/<int:pk>/inv-movement/",ProductInventoryMovement.as_view(), name = "Inventory-Check"),

    path("product/<int:pk>/update/",ProductUpdateView.as_view(), name = "Products-update"),

    path("product/<int:pk>/delete/",ProductSoftDeleteView.as_view(), name = "Product-Soft-delete"),

]
