from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('detail/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('list', views.PostList.as_view(), name='post_list'),
    path('category/<int:pk>', views.category_detail,  name='category_detail'),
    path('search', views.search, name='search_posts'),
    path('contactus', views.contact_us, name='contact_us'),
    path('like/<slug:slug>/<int:pk>', views.like, name='like'),
    # path('test', views.test, name='test'),

    # path('test', views.HomPageRedirect.as_view(), name='redirect'),

]