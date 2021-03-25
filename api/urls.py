from django.urls import path
from .views.business_views import Businesses, MyBusiness, CreateBusiness, BusinessDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword

urlpatterns = [
  	# Restful routing
    path('businesses/', Businesses.as_view(), name='businesses'),
    path('my-business/', MyBusiness.as_view(), name='my_business'),
    path('create-business/', CreateBusiness.as_view(), name='create_business'),
    path('business/<int:pk>/', BusinessDetail.as_view(), name='business_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw')
]
