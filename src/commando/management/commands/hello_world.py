import helpers
from django.conf import settings
from typing import Any
from django.core.management.base import BaseCommand

# STATICFILES_VENDOR_DIR = getattr(settings, "STATICFILES_VENDOR_DIR")

# VENDOR_STATICFILES = {
#     "flowbite.min.css":"https://cdn.jsdelivr.net/npm/flowbite@4.0.1/dist/flowbite.min.css",
#     "flowbite.min.js":"https://cdn.jsdelivr.net/npm/flowbite@4.0.1/dist/flowbite.min.js",
# }
class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Downloading vendor static files...")

        # for name, url in VENDOR_STATICFILES.items():
        #     out_path = STATICFILES_VENDOR_DIR / name
        #     helpers.download_file(url, name , out_path)