from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='Home'),
    path('add_manufacturers/', CreateManufact.as_view(), name='add_manufacturers'),
    path('add_carmodel/', CreateCarModel.as_view(), name='add_carmodel'),
    path('add_owners/', CreateOwners.as_view(), name='add_owners'),
    path('add_car/', CreateCar.as_view(), name='add_car'),
    path('add_price/', CreatePrice.as_view(), name='add_price'),
    path('add_mechanics/', CreateMechanics.as_view(), name='add_mechanics'),
    path('manufacturers/', ListManufact.as_view(), name='manufact_list'),
    path('cars/', ListCars.as_view(), name='cars_view'),
    path('price-list/', ListPrice.as_view(), name='price_list'),
    path('cars/<int:pk>/update', UpdateCar.as_view(), name='car_update'),
    path('price/<int:pk>', UpdatePrice.as_view(), name='price_detail'),
    path('manufacturers/<int:pk>', UpdateManufact.as_view(), name='manufact_update'),
    path('carmodel/<int:pk>', UpdateModelCar.as_view(), name='carmodel_update'),
    path('cars/<int:pk>', DetailCars.as_view(), name='car_detail'),
    path('help/', HelpPage.as_view(), name='help'),
    path('reg/', CreateUser.as_view(), name='reg'),
    path('auth/', auth_user, name='auth'),
    path('logout/', logout_user, name='logout'),
]
