from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing",views.create_listing,name="create_listing"),
    path("categories",views.categories,name="categories"),
    path("categorical_listing/<str:category>",views.categorical_listing,name="categorical_listing"),
    path("watchlist",views.watchlist,name="watchlist"),
    path("listings/<int:id>",views.listings,name="listings"),
    path("alter_watchlist/<int:id>", views.change_watchlist, name="alter-watchlist")
]
