import os

from flask import Flask
from cmscore import core, routes
from pluginbase import PluginBase

reg_plugins = {
    'core' : core.CmsCore(),
    'router': routes.CmsRouter(),
}

def register_plugins(app):
    plugin_base = PluginBase(package='cmscore.plugins')
    plugin_source = plugin_base.make_plugin_source(searchpath=[app.config['CMS_PLUGIN_PATH']])
   
    for plugin_name in plugin_source.list_plugins():
        plugin = plugin_source.load_plugin(plugin_name)
        try:
            reg_plugins[plugin_name] =  plugin.register()
            reg_plugins[plugin_name].test()
        except AttributeError:
            pass

    

def create_app(test_config=None):
    # create and configure the app


    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        CMS_PLUGIN_PATH=os.path.dirname(os.path.abspath(__file__)) +'/../plugins',
        CMS_TEMPLATE_PATH=os.path.dirname(os.path.abspath(__file__)) +'/../themes',
    )

    register_plugins(app)
    for name, obj in reg_plugins.items():
        obj.activate(app, reg_plugins)
   
    return app