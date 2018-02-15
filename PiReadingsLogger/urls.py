from django.conf.urls import url 
from . import views

urlpatterns = [
	url(r'^insertReadings/',views.insertReadings,name="PiDataInsert"),
	url(r'^getLatestReading/',views.getLatestReading,name="LatestReading"),
	url(r'^getReadingsByDate/',views.getReadingsByDate,name="ReadingsByDate"),

]