from django.conf.urls import url
from api.views import userviews
from api.views import billviews
from api.views import elementviews
from api.views import inventoryviews
from api.views import requestquotationviews
from api.views import statusviews
from api.views import taskviews

urlpatterns = [
    url(r'^user/$', userviews.user_list),
    url(r'^user/(?P<pk>[0-9]+)/$', userviews.user_detail),

    url(r'^bill/$', billviews.bill_list),
    url(r'^bill/(?P<pk>[0-9]+)/$', billviews.bill_detail),

    url(r'^element/$', elementviews.element_list),
    url(r'^element/(?P<pk>[0-9]+)/$', elementviews.element_detail),

    url(r'^inventory/$', inventoryviews.inventory_list),
    url(r'^inventory/(?P<pk>[0-9]+)/$', inventoryviews.inventory_detail),

    url(r'^quotation/$', requestquotationviews.quotation_list),
    url(r'^quotation/(?P<pk>[0-9]+)/$', requestquotationviews.quotation_detail),

    url(r'^status/$', statusviews.status_list),
    url(r'^status/(?P<pk>[0-9]+)/$', statusviews.status_detail),

    url(r'^task/$', taskviews.task_list),
    url(r'^task/(?P<pk>[0-9]+)/$', taskviews.task_detail),
]