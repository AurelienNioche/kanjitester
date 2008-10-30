# -*- coding: utf-8 -*-
# 
#  plugin_api.py
#  kanji_test
#  
#  Created by Lars Yencken on 2008-10-24.
#  Copyright 2008 Lars Yencken. All rights reserved.
# 

import consoleLog

from kanji_test import settings

class UserModelPlugin(object):
    """
    A plugin which provides one or more prior distributions across a form
    of user error.
    """
    
    def provides_dists(self):
        """
        Returns a list of tags as strings, where each tag is the name
        of an error distribution generated by this plugin.
        """
        raise Exception('not implemented')
    
    def build_dists(self, force=False):
        """
        Builds the prior distributions that this error model provides.
        """
        raise Exception('not implemented')

def load_plugins():
    """
    Loads the list of plugin classes specified in USER_MODEL_PLUGINS in the
    project settings.
    
    >>> from kanji_test import settings
    >>> len(load_plugins()) == len(settings.USER_MODEL_PLUGINS)
    True
    """
    plugin_classes = []
    for plugin_path in settings.USER_MODEL_PLUGINS:
        path_parts = plugin_path.split('.')
        base_module = __import__('.'.join(path_parts[:-1]))
        plugin_class = reduce(getattr, path_parts[1:], base_module)
        plugin_classes.append(plugin_class)
    
    return plugin_classes

def load_priors(syllabus):
    "Loads the prior distributions represented by each plugin."
    log = consoleLog.default
    log.start('Loading prior distributions', nSteps=2)
    
    log.log('Loading plugins')
    plugins = load_plugins()
  
    log.start('Initialising prior distributions', nSteps=len(plugins))
    for plugin_class in plugins:
        plugin_obj = plugin_class()
        
        plugin_obj.init_priors(syllabus)
    log.finish()

    log.finish()