AUTHOR = 'Edward Gomez'
SITENAME = 'Robotic Telescopes for Education'
#SITEURL = 'https://www.zemogle.net/robotic-telescopes/'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

THEME = 'themes/bulma_profile/'

# Blogroll
LINKS = (
        ('Home','/'),
        ('Telescopes & Networks', '/telescopes/'),
         ('Survey', '/survey/'),
)

DEFAULT_PAGINATION = False

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

READERS = {"html": None}

STATIC_PATHS = ['images',]

DIRECT_TEMPLATES = ['index', 'telescopes']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True