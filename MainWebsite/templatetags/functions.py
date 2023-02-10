import json
from django import template

register = template.Library()

def jsonToNormal(jsonData):
    return json.loads(jsonData)