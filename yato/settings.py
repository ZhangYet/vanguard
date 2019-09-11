import os

USER_NAME = 'fengxiukeren'
COOKIE = ''
HTML_STORAGE_DIR = './data'


try:
    import settings_local
    if hasattr(settings_local, 'USER_NAME'):
        USER_NAME = settings_local.USER_NAME or USER_NAME
    if hasattr(settings_local, 'COOKIE'):
        COOKIE = settings_local.COOKIE or COOKIE
    if hasattr(settings_local, 'HTML_STORAGE_DIR'):
        HTML_STORAGE_DIR = settings_local.HTML_STORAGE_DIR or HTML_STORAGE_DIR
except ImportError:
    pass

os.makedirs(HTML_STORAGE_DIR, exist_ok=True)
