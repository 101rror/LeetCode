class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.arr  =[big,medium,small]

    def addCar(self, carType: int) -> bool:
        if(self.arr[carType-1]):
            self.arr[carType-1]-=1
            return True
            
        return False