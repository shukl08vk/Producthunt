
from django.urls import path, include
from . import views

urlpatterns = [
    path('create', views.create,name='create'),
    path('prodComment',views.prodComment,name="prodComment"),
    path('<int:product_id>', views.detail,name='detail'),
    path('<int:product_id>/upvote', views.upvote,name='upvote'),
    path('<int:product_id>/delete',views.delete,name='delete'),

    
    
]
