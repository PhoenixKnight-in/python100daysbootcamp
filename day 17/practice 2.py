class classname:
    def __init__(self,key):
        self.seat_no = 0
        self.key = key
    def print_seat(self):
        print("Seat no: ",self.key)
car = classname(15)

car.print_seat()
l = list()
for i in range(0,10):
    l.append(classname(i))

for i in range(0,10):
    item_l = l[i]
    item_l.print_seat()