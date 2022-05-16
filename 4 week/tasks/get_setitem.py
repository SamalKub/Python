class GetSetTest:
    def __init__(self, name, val):
        self.name = name
        self.val = val
        self.data = {self.name: self.val}
     
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, val):
        self.data[key] = val
    
    def __str__(self):
        return 'current data: {}'.format(self.data)
    
class PascalList:
    def __init__(self, container_list):
        self.container_list = container_list or []
    def __getitem__(self, index):
        return self.container_list[index-1]
    def __setitem__(self, index, val):
        self.container_list[index-1] = val
    def __str__(self):
        return self.container_list.__str__()
    