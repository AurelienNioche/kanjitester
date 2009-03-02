# -*- coding: utf-8 -*-
#
#  urls.py
#  kanji_test
# 
#  Created by Lars Yencken on 25-02-2009.
#  Copyright 2009 Lars Yencken. All rights reserved.
#

from django.conf.urls.defaults import *

urlpatterns = patterns('kanji_test.analysis.views',
    url(r'^basic/$', 'basic', name='analysis_basic'),
    url(r'^charts/$', 'chart_dashboard', name='analysis_charts'),
    url(r'^data/$', 'data', name='analysis_data_base'),
    url(r'^data/(?P<name>[a-zA-Z_]+)\.(?P<format>[a-z]+)$', 
        'data', name='analysis_data'),
)

# vim: ts=4 sw=4 sts=4 et tw=78:
