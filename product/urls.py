
from django.urls import path
from .views import HomeScreen,AllProducts,ProductDetails,SearchProductListView


app_name = "product"
urlpatterns = [
    path("", SearchProductListView.as_view(),name="home"),
    path("products/", AllProducts.as_view(),name="products"),
    path("products/<int:pk>/", ProductDetails.as_view(),name="products-details"),

    path('search/', SearchProductListView.as_view(), name='search-products'),
]
