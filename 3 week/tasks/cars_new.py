import os
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        if not isinstance(brand, str):
            raise ValueError('Brand is incorrect type')
        if len(brand) == 0:
            raise ValueError('Incorrect len for brand')
        self.brand = brand
        
        try:
            self.carrying = float(carrying)
        except ValueError:
            raise ValueError('carrying is wrong')
        
        file_ext = os.path.splitext(photo_file_name)[1]
        expension = ['.jpg','.jpeg','.png','.gif']
        if file_ext in expension:
            self.photo_file_name = photo_file_name
        else:
            raise ValueError('file is incorrect evpension')
            
    def get_photo_file_ext(self):
        try:
            file_ext = os.path.splitext(self.photo_file_name)[1]
            return file_ext
        except ValueError as err:
            print(err.args[0], err.args[1])
        except:
            print('...')

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'car'
        try:
            self.passenger_seats_count = int(passenger_seats_count)
        except ValueError:
            raise ValueError('passenger_seats_count unconvertable to int')

class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        try:
            body_whl_list = list(map(lambda x: float(x), body_whl.split('x')))
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
        self.car_type = 'spec_machine'
        if not isinstance(extra, str):
            raise ValueError('extra is incorrect')
        if len(extra) == 0:
            raise ValueError('Incorrect len for extra')
        self.extra = extra 

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
            car_type = row[0]
            brand = row[1]
            passenger_seats_count = row[2]
            photo_file_name = row[3]
            body_whl = row[4]
            carrying = row[5]
            extra = row[6]
            try:
                if car_type == 'car':
                        car_list.append(Car(brand=brand,
                                 photo_file_name=photo_file_name,
                                 passenger_seats_count=passenger_seats_count,
                                 carrying=carrying))
                elif car_type=='truck':
                        car_list.append(Truck(brand=brand,
                                        photo_file_name=photo_file_name,
                                        body_whl=body_whl,
                                        carrying=carrying)
                                   )
                elif car_type=='spec_machine':
                        car_list.append(SpecMachine(brand=brand,
                                        photo_file_name=photo_file_name,
                                        extra=extra,
                                        carrying=carrying)
                                   )
                else:
                    print('no one')
            except:
                print('something wrong')
    return car_list
