import os
import tempfile


class File:
    def __init__(self, file_path):
        self.file = open(file_path, 'a+')
        self.file_name = file_path
    
    def __enter__(self):
        return self.file
    
    def __exit__(self):
        self.file.close()
    
    def __str__(self):
        return os.path.abspath(self.file_name)
    
    def read(self):
        self.file.seek(0)
        return self.file.read()
    
    def write(self, text):
        with open(self.file_name, 'w') as file:
            file.write(text)
    
    def __iter__(self):
        self.value = -1
        return self
    
    def __next__(self):
        self.file.seek(0)
        length = len(self.file.readlines())
        self.file.seek(0)
        if self.value < length - 1:
            self.value += 1
            return self.file.readlines()[self.value]
        else:
            raise StopIteration
        
    def __add__(self, obj):
        if isinstance(obj, File):
            name_path = tempfile.NamedTemporaryFile().name
            new_file = File(name_path)
            new_file.write(self.read()+obj.read())
            return new_file
        else:
            raise 'Wrong type of file'
    