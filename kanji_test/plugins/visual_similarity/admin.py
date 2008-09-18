# -*- coding: utf-8 -*-
# 
#  admin.py
#  kanji_test
#  
#  Created by Lars Yencken on 2008-09-16.
#  Copyright 2008 Lars Yencken. All rights reserved.
# 

from django.contrib import admin

from plugins.visual_similarity import models

class GraphAdmin(admin.ModelAdmin):
    list_display = ('label', 'neighbour_label', 'weight')

admin.site.register(models.SimilarityEdge, GraphAdmin)