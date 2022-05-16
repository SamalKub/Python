import os
import csv


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        
        file_ext = os.path.splitext(photo_file_name)[1]
        expension = ['.jpg','.jpeg','.png','.gif']
        if file_ext in expension:
            self.photo_file_name = photo_file_name
        else:
            raise ValueError('File should be in correct expension type')
        try:
            self.carrying = float(carrying)
        except ValueError:
            print('carrying can not convert to float')
        self.car_type = None
    
    def get_photo_file_ext(self):
        try:
            file_ext = os.path.splitext(self.photo_file_name)[1]
            return file_ext
        except AttributeError:
            print('Photo_file_name attribute does not exist')

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        try:
            self.passenger_seats_count = int(passenger_seats_count)
        except ValueError:
            print('passenger_seats_count is required argument for Car')
#         self.passenger_seats_count = int(passenger_seats_count)
    
class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        try:
            body_whl.split('x')
        except TypeError:
            raise 'Type of body_whl is wrong! Should be str of (int, float) numbers concatenated by \'x\'. '
        body_whl_list = body_whl.split('x')
        try:
            body_whl_list = list(map(lambda x: float(x), body_whl_list))
        except ValueError:
            body_whl_list = [0.0, 0.0, 0.0]
                    
        if len(body_whl_list) == 3:
            self.body_length = body_whl_list[0]
            self.body_width = body_whl_list[1]
            self.body_height = body_whl_list[2]
        else:
            self.body_length, self.body_width, self.body_height = 0.0, 0.0, 0.0
        
    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height
        


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra
        self.car_type = 'spec_machine'

def correctness(row):
    arguments = {}
    try:
        row[0] in ['car', 'truck', 'spec_machine']
    except TypeError:
        print('Car type is incorrect!')
    arguments['car_type'] = row[0]
        
    try:
        isinstance(row[1], str)
    except TypeError:
        print('Brand of car is not string')
    arguments['brand'] = row[1]
            
    try: 
        os.path.splitext(row[3]) in ['.jpg', '.jpeg', '.png', '.gif']
    except TypeError:
        print('Image file name is incorrect type')
    arguments['photo_file_name'] = row[3]
        
    try: 
        isinstance(float(row[5]), float)
    except ValueError:
        print('Carrying is float or int type')
    arguments['carrying'] = row[5]
            
    if arguments['car_type'] == 'car':
        try:
            isinstance(row[2], int)
        except ValueError:
            print('Incorrect passenger number')
    elif arguments['car_type'] == 'truck':
        try: 
            row[4].split('x')
        except TypeError:
            raise 'Type of body_whl is wrong! Should be str of (int, float) numbers concatenated by \'x\'. '
    elif arguments['car_type'] == 'spec_machine':
        try:
            len(row[6]) != 0
        except ValueError:
            raise 'extra is required in spec_machine type!'
    else:
        raise 'Wrong type of car!'
    arguments['passenger_seats_count'] = row[2]
    arguments['body_whl'] = row[4]
    arguments['extra'] = row[6]
    return (True, arguments)

def get_car_list(csv_filename):
    list_rows = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            list_rows.append(row)
            
    car_list = []
    for row in list_rows:
        if len(row) == 7:
            correct, args = correctness(row)
            if correct:
                if args['car_type'] == 'car':
                    car = Car(args['brand'], 
                              args['photo_file_name'], 
                              args['carrying'], 
                              args['passenger_seats_count'])
                elif args['car_type'] == 'truck':
                    car = Truck(args['brand'], 
                               args['photo_file_name'], 
                               args['carrying'], 
                               args['body_whl'])
                elif args['car_type'] == 'spec_machine':
                    car = SpecMachine(args['brand'], 
                                      args['photo_file_name'], 
                                      args['carrying'],
                                      args['extra'])
                car_list.append(car)
#                 print(car)
    
    return car_list
