from django.contrib import admin
from django.urls import path
from store import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/",views.SignUpView.as_view(),name="signup"),
    path("",views.SignInView.as_view(),name="signin"),
    path("index/",views.IndexView.as_view(),name="index"),
    path("products/<int:pk>/",views.ProductDetailView.as_view(),name="product_detail"),
    path("home/",views.HomeView.as_view(),name="all"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)