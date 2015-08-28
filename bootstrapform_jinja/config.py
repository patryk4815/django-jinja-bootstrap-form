from django.conf import settings

BOOTSTRAP_COLUMN_COUNT = getattr(settings, 'BOOTSTRAP_COLUMN_COUNT', 12)
JINJA_FORM_ENGINE = getattr(settings, 'JINJA_FORM_ENGINE', 'backend')
