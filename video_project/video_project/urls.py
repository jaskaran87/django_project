from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from views import (
                    home_page,
                    about_page,
                    contact_page,
                    login_page,
                    register_page
                )
# from products.views import (
#                             ProductListView,
#                             product_list_view,
#                             product_detail_view,
#                             productDetailView,
#                             ProductFeaturedListView,
#                             ProductFeaturedDetailView,
#                             ProductDetailSlugView,
#                         )
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^homePage/$', home_page, name="home"),
    url(r'^aboutPage/$', about_page, name="about_us"),
    url(r'^contactPage/$', contact_page, name="contact_us"),
    url(r'^loginPage/$', login_page , name="login_url"),
    url(r'^registerPage/$', register_page, name="register_url"),    
    url (r'^products/', include("products.urls" , namespace="products")),
    url (r'^bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
    url (r'^search/', include("search.urls" , namespace="searchs")),
    # url (r'^products/$', ProductListView.as_view()),
    # url (r'^products-fbv/$', product_list_view),
    # url (r'^products/(?P<pk>\d+)/$', productDetailView.as_view()),
    # url (r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),
    # url (r'^featured/$', ProductFeaturedListView.as_view()),
    # url (r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
    # url (r'^products-slug/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view()),

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
