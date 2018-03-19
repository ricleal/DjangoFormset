from django.urls import include, path, re_path
from django.contrib import admin

from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^app1/', include(('app1.urls', 'app1'), namespace='app1')),
    re_path(r'^app2/', include(('app2.urls', 'app2'), namespace='app2')),
    re_path(r'^app3/', include(('app3.urls', 'app3'), namespace='app3')),
    re_path(r'^$', RedirectView.as_view(pattern_name='app1:listmusician',
                                        permanent=False),
            name='index')
]
