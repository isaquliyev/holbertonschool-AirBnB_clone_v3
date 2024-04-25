#!/usr/bin/python3
""" Index module """

from api.v1.views import app_views
import json


@app_views.route('/status', strict_slashes=False)
def status():
    """Simple function that returns status: ok"""
    return json.dumps({"status": "OK"})
