class VaccineCenter:
    def __init__(self, id):
        self.__id = id
        self.__slots = dict()

    def add_slot(self, capacity, startTime):
        if startTime not in self.__slots.keys():
            self.__slots[startTime]= capacity
        else:
            return False, "slot is already added"

    def checkAvailability(self, atTime):
        # print(self.__slots)
        if atTime in self.__slots.keys() and self.__slots[atTime] > 0:
            return True
        else:
            return False

    def bookSlot(self, atTime):
        self.__slots[atTime]-=1
        return
    
    def cancelBooking(self, atTime):
        if atTime in self.__slots.keys():
            self.__slots[atTime]+=1
        return