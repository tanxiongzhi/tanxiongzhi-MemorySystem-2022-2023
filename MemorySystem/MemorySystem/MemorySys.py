import os
import shutil
import os.path

MAX_BUF_file_SIZE = 5
DIR_MAX_ELEMS = 5
class Directory:
    def __init__(self):
        self.name = 'New Directory'
        self.path = os.getcwd()
        file_list = os.listdir(self.path)
        self.son_dir = []
        self.son_binary_file = []
        self.son_log_file = []
        self.son_buffer_file = []
        for file in file_list:
            filepath = os.path.join(self.path, file)
            if os.path.isdir(filepath):
                self.son_dir.append(filepath)

    def create_dir(self):
        if len(self.son_dir) + len(self.son_binary_file) + len(self.son_log_file) + len(self.son_log_file) < DIR_MAX_ELEMS:
            path = os.getcwd()
            new_directory_name = input("please input name of new directory:")
            try:
                print(new_directory_name)
                os.mkdir(self.path + '\\' + new_directory_name)
                self.son_dir.append(new_directory_name)
            except:
                print("the directory created failed")
            else:
                print("successfully create directory")
    def delete_dir(self):
        if len(self.son_dir) + len(self.son_binary_file) + len(self.son_log_file) + len(self.son_log_file) <= 0:
            print("no directory to delete")
        else:
            del_directory_name = input("please input the son directory's name that delete:")
            if del_directory_name not in self.son_dir:
                print("failed to find such directory")
            else:
                try:
                    os.rmdir(del_directory_name)
                    print("successfully delete such directory")
                except:
                    print("fail to delete")
    def show_son_file(self):
        print("son directory is below:",end='')
        for s_dir in self.son_dir:
            print(s_dir,end=',')
        print()

        print("son log file is below:",end='')
        for s_log in self.son_log_file:
            print(s_log,end=',')
        print()

        print("son binary file is below:",end='')
        for s_bia in self.son_binary_file:
            print(s_bia,end=',')
        print()

        print("son buffer file is below:",end='')
        for s_buf in self.son_buffer_file:
            print(s_buf,end=',')
        print()
    def change_dir_path(self,path):
        try:
            shutil.move(self.path, path)
        except:
            print('move failed')

    def create_binary_file(self,name):
        if len(self.son_dir) + len(self.son_binary_file) + len(self.son_log_file) + len(self.son_log_file) >= DIR_MAX_ELEMS:
            print('fail to create file')
        try:
            binary = BinaryFile()
            self.son_binary_file.append(binary)

            fp = open(name,'wb')
        except:
            print('create file failed')
        return binary

    def delete_binary_file(self,name):
        try:
            os.remove(name)
        except:
            print("delete binary file failed")

    def create_log_file(self,name):
        if len(self.son_dir) + len(self.son_binary_file) + len(self.son_log_file) + len(self.son_log_file) >= DIR_MAX_ELEMS:
            print('fail to create file')
        try:
            log = LogFile()
            self.son_log_file.append(log)
            fp = open(name,'w')

        except:
            print('create file failed')
        return log

    def delete_log_file(self,name):
        try:
            os.remove(name)
        except:
            print("delete log file failed")

    def update_log_file(self,name,content):
        try:
            with open(name, "a") as f:
                f.write(content)
        except:
            print("write file failed")
    def create_buffer(self,name):
        if len(self.son_dir) + len(self.son_binary_file) + len(self.son_log_file) + len(self.son_log_file) >= DIR_MAX_ELEMS:
            print('fail to create file')
        file = BufferFile(name)
        self.son_buffer_file.append(file)

        return file




class BinaryFile:
    def __init__(self):
        self.name = 'NewFile'

    def read_binary_file(self, name):
        try:
            fp = open(name, 'wb')
        except:
            print("read file failed")
        return fp

class LogFile:
    def __init__(self):
        self.name = 'NewLog'
        
class BufferFile:
    def __init__(self,name):
        self.name = name
        self.items = []
    def push(self,element):
        if len(self.items) == MAX_BUF_file_SIZE:
            raise ValueError("BufferFile size is limited")
        self.items.append(element)
    def pop(self) -> bool:
        if len(self.items) == 0:
            raise ValueError("Can't get items from an empty BufferFile")

        return self.items.pop()

if __name__ == '__main__':
    d = Directory()

    # d.create_dir()
    # d.create_dir()

    d.path = os.getcwd() + '\\1'
    d.create_binary_file("123")
    # # d.delete_binary_file("123")
    d.create_log_file('12')
    d.update_log_file("123",'i am handsome')
    d.update_log_file("123","32424")


