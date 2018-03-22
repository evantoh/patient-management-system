from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name='welcome'),
    url('^accounts/profile$',views.profile,name = 'profile'),
    url('^updatedoc',views.welcome,name='updatedoc'),
    url('^addpatient',views.addpatient,name='addpatient'),
    url('^all/patients',views.allpatient,name='allpatients'),
    url('^treatment',views.treatment,name='treatment'),

    url(r'^new/profile/(?P<username>[-_\w.]+)$',views.update_profile, name='updateProfile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)