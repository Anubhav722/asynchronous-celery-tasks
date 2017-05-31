from django.conf.urls import include, url
from django.contrib import admin
from feedback.views import FeedbackView
from photos.views import PhotoView

urlpatterns = [
    # Examples:
    # url(r'^$', 'picha.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', PhotoView.as_view(), name="home"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^feedback/$', FeedbackView.as_view(), name="feedback"),
]
