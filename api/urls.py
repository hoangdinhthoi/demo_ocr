from django.urls import path
from api.ocr_view import OcrView

app_name = 'api'
urlpatterns = [
    path('ocr', OcrView.as_view(), name='ocr')
]