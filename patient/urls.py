from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('^updatedoc',views.updatedoc,name='updatedoc'),
    url('^addpatient',views.addpatient,name='addpatient'),
    url('^treatment',views.treatment,name='treatment'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)