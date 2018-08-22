import os

from django.core.files.images import get_image_dimensions
import pytest


FILE_NAME = 'img.webp'

here = os.path.dirname(__file__)
file_path = os.path.join(here, FILE_NAME)


def test_webp_parse_error():
    """
    Webp file from douban.com, displays in browser well,
    can be opened by PIL but error occurs while use django parse.
    """
    with pytest.raises(
        RuntimeError,
    ) as info:
        with open(file_path, 'rb') as fp:
            get_image_dimensions(file_or_path=fp, close=True)
    assert str(info.value) == 'could not create decoder object'


def test_the_working_way():
    with open(file_path, "rb") as fp:
        from PIL import Image
        image = Image.open(fp)
        print(image.size)
