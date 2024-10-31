from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    # URLs para Usuarios
    path('Usuarios/', views.UsuariosListCreate.as_view(), name='Usuarios-list'),
    path('Usuarios/<int:pk>/', views.UsuariosDetail.as_view(), name='Usuarios-detail'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

