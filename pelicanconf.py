AUTHOR = "Joe Moon Whitehead"
SITENAME = "Joe Moon Whitehead"
SITEURL = ""

PATH = "content"

TIMEZONE = "Europe/London"

DEFAULT_LANG = "en"

THEME = "themes/classy-software"
THEME_STATIC_DIR = "themes/classy-software/static"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("LinkedIn", "https://www.linkedin.com/in/joe-moon-whitehead/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
)

# Social widget
SOCIAL = (
    ("LinkedIn", "https://www.linkedin.com/in/joe-moon-whitehead/"),
    ("GitLab", "https://gitlab.com/joemoonwhitehead"),
    ("GitHub", "https://github.com/M-Moon"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

ARTICLE_PATHS = ("articles",)
ARTICLE_URL = "articles/{slug}.html"
ARTICLE_SAVE_AS = "articles/{slug}.html"

STATIC_PATHS = ("images", "css")

USE_SHORTCUT_ICONS = True
