import os

USER_NAME = 'fengxiukeren'
COOKIE = ''
HTML_STORAGE_DIR = './data'
OUT_DIR = './output'
TOTAL_PAGES = 84


try:
    import settings_local
    if hasattr(settings_local, 'USER_NAME'):
        USER_NAME = settings_local.USER_NAME or USER_NAME
    if hasattr(settings_local, 'COOKIE'):
        COOKIE = settings_local.COOKIE or COOKIE
    if hasattr(settings_local, 'HTML_STORAGE_DIR'):
        HTML_STORAGE_DIR = settings_local.HTML_STORAGE_DIR or HTML_STORAGE_DIR
    if hasattr(settings_local, 'OUT_DIR'):
        OUT_DIR = settings_local.OUT_DIR or OUT_DIR
    if hasattr(settings_local, 'TOTAL_PAGES'):
        TOTAL_PAGES = settings_local.TOTAL_PAGES or TOTAL_PAGES
except ImportError:
    pass

os.makedirs(HTML_STORAGE_DIR, exist_ok=True)
os.makedirs(OUT_DIR, exist_ok=True)
