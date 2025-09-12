from django.urls import path
from main.views import show_main, show_xml, show_json, show_json_by_id, show_xml_by_id, add_product, product_detail

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<str:product_id>/', show_json_by_id, name='show_json_by_id'),
    path('xml/<str:product_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('add-product/', add_product, name='add_product'),
    path('product/<str:product_id>/', product_detail, name='product_detail'),
]