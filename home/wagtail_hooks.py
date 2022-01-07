from django.templatetags.static import static
from django.utils.html import format_html

from wagtail.core import hooks


# Register a custom css file for the wagtail admin.
@hooks.register("insert_global_admin_css", order=100)
def global_admin_css():
    """Add /static/home/assets/css/custom_admin.css."""
    return format_html('<link rel="stylesheet" href="{}">', static("home/assets/css/custom_admin.css"))