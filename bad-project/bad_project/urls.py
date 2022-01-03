from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from fix_me import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('<category_slug>', views.list),
    path('<category_slug>/<id>', views.detail),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
