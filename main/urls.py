import os

from django.conf.urls.defaults import *
from django.contrib import admin

import settings
import main.views
#import passreset
admin.autodiscover()

urlpatterns = patterns('main.views',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$',
        'example',
        name='index'),
        url(r'^index2/$',
        'example2',
        name='index2'),
    url(r'^example/$',
        'example',
        name='example'),
                       )
if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(.*)$', 'django.views.static.serve',
                             {'document_root': os.path.join(os.path.dirname(__file__), 'media')}),
    )

