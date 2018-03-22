from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.welcome,name='welcome'),
    url(r'^accounts/profile$',views.profile,name = 'profile'),
    url(r'^updatedoc',views.welcome,name='updatedoc'),
    url(r'^addpatient',views.addpatient,name='addpatient'),
    url(r'^all/patients',views.allpatient,name='allpatients'),
    url(r'^treatment',views.treatment,name='treatment'),
    url(r'^search$',views.search_results,name='search_patient'),
    url(r'^new/profile/(?P<username>[-_\w.]+)$',views.update_profile, name='updateProfile'),
    # url(r'^single/patient/(\d+)', views.single_patient, name ='singlePatient'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)