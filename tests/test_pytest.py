import pytest
from main import YaDiskMakeDir

fixture1 = [
            ("TestDirectory", 201),
            ("TestDirectory", 409)
        ]

@pytest.mark.parametrize("path, code", fixture1)
def test_ya_disk_make_dir(path, code):
    ya_disk = YaDiskMakeDir()
    assert ya_disk.make_dir(path) == code

fixture2 = [
            ("TestDirectory", 200),
            ("DirectoryTest", 404)
        ]

@pytest.mark.parametrize("path, code", fixture2)
def test_ya_disk_check_dir(path, code):
    ya_disk = YaDiskMakeDir()
    assert ya_disk.check_dir(path) == code