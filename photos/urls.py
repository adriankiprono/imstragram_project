
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^accounts/register/',views.reg_view,name ='reg_view'),
    url(r'^accounts/login/',LoginView.as_view(),name="login_url"),
    url(r'^logout/',LogoutView.as_view(next_page='home'),name="logout_url"),
    url(r'^new/image$', views.new_image, name='new-image'),
    url(r'^profile$', views.profile, name='my_profile'),
    

    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)