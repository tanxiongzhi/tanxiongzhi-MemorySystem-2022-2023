from MemorySys import Directory, MAX_BUF_file_SIZE, DIR_MAX_ELEMS
import pytest


@pytest.fixture
def directory() -> Directory:
    fs = Directory()
    fs.create_dir()
    return fs


def test_Directory_creation():
    fs = Directory()
    fs.create_dir()



def test_filesystem_create_multiple_directories():
    fs = Directory()
    fs.create_dir()
    fs.create_dir()

    assert len(fs.son_dir) == 2

def test_delete_directory():
    fs = Directory()
    fs.create_dir()
    fs.create_dir()
    dir_list = fs.son_dir()
    for dir in dir_list:
        fs.delete_binary_file(dir)
    assert len(fs.son_dir) == 0

def test_mov_directory():
    fs = Directory()


def test_create_binary_file():
    fs = Directory()
    fs.create_binary_file('123')
    fs.create_dir()
    fs.create_dir()
    dir_list = fs.son_dir()
    for i in range(0,len(dir_list)):
        fs.change_dir_path(dir_list[i],'D:/')



def test_create_binary_file():
    fs = Directory()
    fs.create_binary_file("123")
    fs.delete_binary_file("123")
    fs.delete_binary_file("12")



def test_create_log_file():
    fs = Directory()
    fs.create_log_file("123")
    fs.update_log_file("123",'stupid')
    fs.delete_log_file("123")
    fs.delete_log_file("12")

def test_create_buffer():
    fs = Directory()
    fs.create_buffer("123")
    fs.son_buffer_file[0].append(1)
    fs.son_buffer_file[0].append(2)

def test_delete_buffer():
    fs = Directory()
    fs.create_buffer("123")
    fs.son_buffer_file[0].push(1)
    fs.son_buffer_file[0].push(2)
    fs.son_buffer_file[0].pop()










