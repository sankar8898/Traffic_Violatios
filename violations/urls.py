# # from django.urls import path
# # from .views import ingest_violation, get_violations, update_violation_status

# # urlpatterns = [
# #     path('violations/ingest/', ingest_violation, name='ingest_violation'),
# #     path('violations/<str:license_plate>/', get_violations, name='get_violations'),
# #     path('violations/<int:pk>/status/', update_violation_status, name='update_violation_status'),
# # ]
# from django.urls import path
# from .views import ingest_violation, get_violations, update_violation_status

# urlpatterns = [
#     path('ingest/', ingest_violation, name='ingest_violation'),
#     path('<str:license_plate>/', get_violations, name='get_violations'),
#     path('<int:pk>/status/', update_violation_status, name='update_violation_status'),
# ]


from django.urls import path
from .views import ingest_violation, get_violations, update_violation_status

urlpatterns = [
    path('ingest/', ingest_violation, name='ingest_violation'),
    path('<str:license_plate>/', get_violations, name='get_violations'),
    path('<int:pk>/status/', update_violation_status, name='update_violation_status'),
]
 