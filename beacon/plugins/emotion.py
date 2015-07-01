from __future__ import absolute_import
from emotion.config.beacon_backend import create_objects_from_config_node, create_object_from_cache
import emotion.controllers
from jinja2 import Template
import os
import pkgutil

def get_html(cfg):
    with file(os.path.join(os.path.dirname(__file__), "emotion.html")) as f:
      html_template = Template(f.read())
    vars = dict(cfg.items())
    vars["controller"] = cfg.parent.get("class")
    controllers = list()
    vars["controllers"] = controllers
    pkgpath = os.path.dirname(emotion.controllers.__file__)
    for _, controller_name, _ in pkgutil.iter_modules([pkgpath]):
       controllers.append({"class": controller_name})
    return html_template.render(**vars)
    
    
