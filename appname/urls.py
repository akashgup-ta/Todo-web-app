from django.urls import path
from .views import *

urlpatterns = [
    path('sign_in/',sign_in,name='sign_in'),
    path('sign_up/',sign_up,name='sign_up'),
    path('',home,name='home'),
    path('log_out/', log_out, name='log_out'),
    path('delete_item/<int:ak>', deleteItem, name='deleteItem'),
    path('update_item/<int:ak>',updateItem, name='updateItem'),
    



]
