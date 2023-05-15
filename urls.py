from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),

    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('site_admin/', views.site_admin, name='site_admin'),
    path('profile/', views.profile, name='profile'),

    path('basket', views.MyBasket, name='basket'),
    path('add-to-basket/<int:pk>', views.addToBasket, name='add-to-basket'),
    path('remove-item/<int:item_id>/', views.remove_item, name='remove_item'),

    path('sign_in/', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout', views.log_out, name='logout'),

    path('profile/edit_profile/', views.edit_profile, name='edit_profile'),
    path('site_admin/user_list', views.user_list, name='user_list'),
    path('site_admin/create_user', views.create_user, name='create_user'),
    path('site_admin/edit_user/<str:username>', views.edit_user, name='edit_user'),
    path('site_admin/delete_user/<str:username>', views.delete_user, name='delete_user'),

    path('product-search/', views.product_search, name='product_search'),
    path('filtered_catalog/', views.filtered_catalog, name='filtered_catalog')
]

