install:
	pip install pytest
	pip install Pillow
	git clone https://github.com/django/django.git && cd django \
	&& pip install -e . || echo "warning: failed to install version of django"
