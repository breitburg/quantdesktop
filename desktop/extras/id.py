from hashlib import md5
from platform import *

generate_id = lambda: md5(f'{system()}{processor()}{platform()}{node()}{machine()}'.encode('utf-8')).hexdigest()
