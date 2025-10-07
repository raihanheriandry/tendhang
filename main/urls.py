from django.urls import path
from main.views import show_main, show_xml, show_json, show_json_by_id, show_xml_by_id, \
                        add_product, product_detail, register, login_user, logout_user, \
                        edit_product, delete_product, ajax_login, ajax_register, add_product_entry_ajax, \
                        edit_product_ajax, delete_product_ajax

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('add-product/', add_product, name='add_product'),
    path('product/<str:product_id>/', product_detail, name='product_detail'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<uuid:id>/edit', edit_product, name='edit_product'),
    path('product/<uuid:id>/delete', delete_product, name='delete_product'), 
    path('ajax/login/', ajax_login, name='ajax_login'),
    path('ajax/register/', ajax_register, name='ajax_register'),
    path('add-product-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('edit_product_ajax/<uuid:product_id>/', edit_product_ajax, name='edit_product_ajax'),
    path('delete_product_ajax/<uuid:product_id>/', delete_product_ajax, name='delete_product_ajax'), 
]