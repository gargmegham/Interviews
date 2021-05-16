class User:
    def __init__(self, id, name, gender, age, current_state, current_district):
        self.id = id
        self.__name = name
        self.__gender = gender
        self.__age = age
        self.__current_state = current_state
        self.__current_district = current_district
        self.__center = None
        self.__isVaccinated = False
        self.__bookedSlot = None
    
    def vaccinationStatus(self):
        return self.__isVaccinated

    def getAge(self):
        return self.__age

    def getStateDistrict(self):
        return self.__current_state, self.__current_district
    
    def vaccinate(self, slot_time, center):
        self.__isVaccinated = True
        self.__center = center
        self.__bookedSlot = slot_time

    def getName(self):
        return self.__name
    
    def getBookingTime(self):
        return self.__bookedSlot

    def cancelBooking(self):
        self.__isVaccinated = False
        self.__bookedSlot = None
        self.__center = None
    
    def getCenter(self):
        return self.__center