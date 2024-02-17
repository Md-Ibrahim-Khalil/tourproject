from django.urls import path
from .views import AgencyCreate, AgencyList, AgencyUpdate

urlpatterns = [
    path('create/', AgencyCreate.as_view(), name='create-agency'),
    path('list/', AgencyList.as_view(), name='list-agency'),
    path('update/<int:id>/', AgencyUpdate.as_view(), name='update-agency'),
]
