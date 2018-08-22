install:
	pip install pytest
	pip install Pillow
	pip show django || git clone https://github.com/django/django.git && cd django && pip install -e .
