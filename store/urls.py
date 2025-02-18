from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
app_name = 'store'
urlpatterns = [
    path('', views.home, name='home'),
    path('khoorsani-hot-chilli-oil/', views.product, name='product'),
    
    path('product_list/<int:category_id>/', views.product_list, name='product_list'),
    path('product_detail/<int:product_id>/', views.product_detail, name='product_detail'),
    
     path('khoorsani-ingrediant/', views.ingrediant, name='ingrediant'),
       path('khoorsni-about/', views.about, name='about'),
       path('khoorsani-recipe/', views.recipe, name='recipe'),
         path('khoorsani-contact/', views.contact, name='contact'),
         path('khoorsani-order/<int:product_id>/', views.order_page, name='order'),
        #  path('start /', views.start, name='start'),
         path('khoorsani-contactc/', views.contactc, name='contactc'),
    path('khoorsani-ordersuccess/', views.success, name='success'),
    path('khoorsani-messagesuccess/', views.messagesuccess, name='success'),
]
