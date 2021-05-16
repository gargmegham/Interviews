from user import User
from vaccineCenter import VaccineCenter

class BookingPortal:
    def __init__(self, userIdLength=3):
        self.__registeredUsers = dict()
        self.__registeredCenters = dict()
        self.__adminSceretKey = "MGEHAM__GARG"
        self.__bookings = dict()
        self.__userIdLength = userIdLength

    # ADD USER <unique_identification> <name> <gender> <age> <current_state> <current_district> 
    # Eg: ADD USER pan12345 Ramesh Yadav Male 35 karnataka Bangalore Urban 
    def registerUser(self, id, name, gender, age, current_state, current_district):
        if id in self.__registeredUsers.keys():
            return False, "can't register twice"
        if not isinstance(id, str) or len(id) != self.__userIdLength:
            return False, "invalid user id"
        try:
            newUser = User(id, name, gender, age, current_state, current_district)
            self.__registeredUsers[id]=newUser
            return True, "success"
        except Exception as ee:
            return False, str(ee)

    # ADD STATE <state_name> 
    # Eg: ADD STATE Karnataka
    # Output: Added state Karnataka into the system.
    def add_state(self, secretKey, name):
        name = str(name)
        if secretKey == self.__adminSceretKey:
            if name not in self.__registeredCenters.keys():
                self.__registeredCenters[name]=dict()
                return True, "Success"
            else:
                return False, "state already present"
        else:
            return False, "you are not admin"

    # ADD DISTRICT <state_name> <district_name> 
    # Eg. ADD DISTRICT Karnataka Bangalore Urban
    def add_district(self, secretKey, district_name, state_name):
        district_name = str(district_name)
        if secretKey == self.__adminSceretKey:
            if state_name not in self.__registeredCenters.keys():
                return False, "invalid state"
            if district_name not in self.__registeredCenters[state_name].keys():
                self.__registeredCenters[state_name][district_name] = dict()
                return True, "Success"
            else:
                return False, "district already present"
        else:
            return False, "you are not admin"

    # ADD WARD <state_name> <district_name> <ward_no>
    # Eg. ADD WARD Karnataka Bangalore Urban 58
    def add_ward(self, secretKey, state_name, district_name, ward_no):
        try:
            ward_no = int(ward_no)
        except Exception as ee:
            return False, "invalid ward number"
        if secretKey == self.__adminSceretKey:
            if state_name not in self.__registeredCenters.keys():
                return False, "invalid state"
            if district_name not in self.__registeredCenters[state_name].keys():
                return False, "invalid district"
            if ward_no not in self.__registeredCenters[state_name][district_name].keys():
                self.__registeredCenters[state_name][district_name][ward_no]=dict()
                return True, "success"
            else:
                return False, "ward already present"
        else:
            return False, "you are not admin"

    # ADD VACCINATION_CENTER <state_name> <district_name> <ward_no> <center_id>
    # Eg: ADD VACCINATION_CENTER Karnataka Bangalore Urban 58 KABU12334
    def add_vaccination_center(self, secretKey, state_name, district_name, ward_no, center_id):
        try:
            center_id = str(center_id)
        except Exception as ee:
            return False, "invalid cente id"
        if secretKey == self.__adminSceretKey:
            if state_name not in self.__registeredCenters.keys():
                return False, "invalid state"
            if district_name not in self.__registeredCenters[state_name].keys():
                return False, "invalid district"
            if ward_no not in self.__registeredCenters[state_name][district_name].keys():
                return False, "invalid ward"
            if center_id not in self.__registeredCenters[state_name][district_name][ward_no].keys():
                self.__registeredCenters[state_name][district_name][ward_no][center_id]=VaccineCenter(center_id)
                return True, "success"
            else:
                return False, "center already present"
        else:
            return False, "you are not admin"

    # ADD SLOT<center_id> <slot> <capacity>
    # Eg :  ADD SLOT KABU12334 2021-05-01 10:00 3
    def add_slot(self, secretKey, state_name, district_name, ward_no, center_id, capacity,
                    startTime):
        # if validateTime(startMonth, startYear, startDate, startHr, startMin,
        #             endMonth, endYear, endDate, endHr, endMin):
        #     return False, "invalid slot added"
        if secretKey == self.__adminSceretKey:
            if state_name not in self.__registeredCenters.keys():
                return False, "invalid state"
            if district_name not in self.__registeredCenters[state_name].keys():
                return False, "invalid district"
            if ward_no not in self.__registeredCenters[state_name][district_name].keys():
                return False, "invalid ward"
            if center_id in self.__registeredCenters[state_name][district_name][ward_no].keys():
                self.__registeredCenters[state_name][district_name][ward_no][center_id].add_slot(capacity, startTime)
                self.__bookings[center_id]=list()
                return True, "success"
            else:
                return False, "center invalid"
        else:
            return False, "you are not admin"

    # LIST CENTER <state_name> <district_name> 
    # E.g LIST CENTER Karnataka Bangalore Urban
    # List down all the centres in Bangalore Urban eg : KABU12334 , KABU12335
    def listCenters(self, state_name, district_name):
        if state_name not in self.__registeredCenters.keys():
            return False, "invalid state"
        if district_name not in self.__registeredCenters[state_name].keys():
            return False, "invalid district"
        allCenters = set()
        for wardNo in self.__registeredCenters[state_name][district_name].keys():
            for centerId in self.__registeredCenters[state_name][district_name][wardNo].keys():
                allCenters.add(centerId)
        return allCenters

    # BOOK <center_id> <slot_time> <user_id> 
    # Books the given vaccination center for a given slot,
    # Eg: BOOK KABU12334 1:15  pava.k
    def bookMySlot(self, userId, center_id, atTime):
        if userId not in self.__registeredUsers.keys():
            return False, "invalid userId"
        user= self.__registeredUsers[userId]
        state, district = user.getStateDistrict()
        userAge = user.getAge()
        if user.vaccinationStatus():
            return False, "you are already vaccinated"
        if userAge < 18:
            return False, "you're underage"
        for ward in self.__registeredCenters[state][district].values():
            for cId, center in ward.items():
                flag = center.checkAvailability(atTime)
                if flag:
                    center.bookSlot(atTime)
                    user.vaccinate(atTime, center)
                    # <SLOT> <user_name> <center_id> <district>
                    self.__bookings[cId].append("{} {} {} {} {}".format(userId, atTime, user.getName(), cId, district))
                    return True, "success"
        return False, "slot not available"

    # LIST BOOKING <center_id> 
    # Should list down all the bookings made user 
    # Output format:  <SLOT> <user_name> <center_id> <district>
    def listBookings(self, center_id):
        if center_id in self.__bookings.keys():
            return self.__bookings[center_id]
        return False, "no booking on this"

    def deleteBooking(self, center_id, user_id, slot_time):
        user= self.__registeredUsers[user_id]
        state, district = user.getStateDistrict()
        center = user.getCenter()
        center.cancelBooking(slot_time)
        listings = self.__bookings[center_id]
        for key in range(len(listings)):
            if listings[key][:3] == user_id:
                del self.__bookings[center_id][key]
                break
        return

    def validCancel(self, bookTime, cancelTime):
        pass

    def cancelBooking(self, center_id, user_id, slot_time):
        if center_id in self.__bookings.keys() and user_id in self.__registeredUsers.keys():
        # if validCancel(self.__registeredUsers[user_id].getBookingTime(), slot_time):
            self.deleteBooking(center_id, user_id, slot_time)
            self.__registeredUsers[user_id].cancelBooking()
            return True, "success"
        return False, "invalid details"

    def search(self, atTime, district_name, state_name):
        allCenters = set()
        if state_name in self.__registeredCenters.keys():
            if district_name in self.__registeredCenters[state_name].keys():
                for ward in self.__registeredCenters[state_name][district_name].values():
                    for cId, center in ward.items():
                        # print(cId)
                        if center.checkAvailability(atTime):
                            allCenters.add(cId)
        if len(allCenters)==0:
            return self.recommendFutureSlots(atTime, district_name, state_name)
        return allCenters

    def recommendFutureSlots(self, atTime, district_name, state_name):
        allCenters = set()
        if state_name in self.__registeredCenters.keys():
            if district_name in self.__registeredCenters[state_name].keys():
                while atTime < 24 and len(allCenters) <= 3:
                    atTime+=1
                    for ward in self.__registeredCenters[state_name][district_name].values():
                        if len(allCenters) > 3:
                            break
                        for cId, center in ward.items():
                            if center.checkAvailability(atTime):
                                if len(allCenters) > 3:
                                    break
                                print(len(allCenters))
                                allCenters.add(str(cId)+" "+str(atTime))
        print(len(allCenters))
        return allCenters