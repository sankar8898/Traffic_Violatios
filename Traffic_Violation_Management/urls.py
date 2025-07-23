from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  # ✅ Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('violations/', include('violations.urls')),
    path('', RedirectView.as_view(url='/admin/', permanent=False)),  # ✅ Redirect root to /admin/
]
