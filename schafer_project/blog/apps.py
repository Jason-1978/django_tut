from django.apps import AppConfig


# Add this to INSTALLED_APPS in "project/settings.py" using its relative path
#   blog.app.BlogConfig
class BlogConfig(AppConfig):
    name = 'blog'
