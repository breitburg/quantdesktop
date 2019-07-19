from platform import *
from hashlib import md5


generate_id = lambda: md5(f'{system()}{processor()}{platform()}{node()}{machine()}'.encode('utf-8')).hexdigest()