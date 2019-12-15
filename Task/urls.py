from django.contrib import admin
from django.urls import path,include
from Vlan import views


from rest_framework_swagger.views import get_swagger_view
schema_view = get_swagger_view(title='welcome')
urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', schema_view),
    path(r'api-auth/', include('rest_framework.urls')),
    path('Vlan/', views.Show.as_view()),
    path('Vlan_switch/', views.show_switch.as_view()),
    path('Vlan/<str:Vlan_id>/<str:Name>/<str:Description>', views.Create.as_view()),
    path('Vlan/<str:Vlan_id>/<str:Name>/', views.Update.as_view()),
    path('Vlan/<str:Vlan_id>/', views.Delete.as_view()),

]



