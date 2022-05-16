class Value:
    def __init__(self):
        self.value = None
        
    def __get__(self, obj, obj_type):
        return int(self.value)
    
    def __set__(self, obj, value):
#         print(obj.commission)
        self.value = value - obj.commission * value

        
class Account:
    amount = Value()
    
    def __init__(self, commission):
        self.commission = commission
        