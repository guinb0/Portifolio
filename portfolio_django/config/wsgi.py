"""
WSGI config for portfolio project.
"""
import os
from django.core.wsgi import get_wsgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Run collectstatic automatically if RUN_COLLECTSTATIC=1 is set
if os.environ.get("RUN_COLLECTSTATIC", "0") == "1":
	try:
		from django.core.management import call_command
		call_command("collectstatic", interactive=False, verbosity=0)
	except Exception as e:
		print(f"[collectstatic error] {e}")

application = get_wsgi_application()
