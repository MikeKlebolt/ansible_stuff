import math
import collections
from ansible import errors

def uppercase_all(arg):
     return arg.upper()

def extract_siteid(arg):
    if len(arg) < 10:
        return FALSE
    site_id = arg[:7]
    return site_id

def extract_datacenter(arg):
    if len(arg) < 10:
        return FALSE
    datacenter = arg[7:10]
    return datacenter

class FilterModule(object):
     def filters(self):
         return {'uppercase_all': uppercase_all, 'extract_siteid': extract_siteid, 'extract_datacenter': extract_datacenter}
