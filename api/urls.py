# api/urls.py

from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns

from .views import BucketListCreateView
from .views import DetailsView
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^bucketlist/$', BucketListCreateView.as_view(), name="create"),
    url(r'^bucketlist/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    url(r'^get-token/', obtain_auth_token)
}
# format_suffix_pattern allows us to specify the data format (raw json or even html) when we use the URLs.
# It appends the format to be used to every URL in the pattern.
urlpatterns = format_suffix_patterns(urlpatterns)