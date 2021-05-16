from time import time
from bookingPortal import BookingPortal
from user import User

if __name__ == '__main__':
    try:
        portal = BookingPortal()
        userId = "MEG"
        secretKey = "MGEHAM__GARG"
        states = ['haryana', 'up', 'punjab']
        flag, msg = portal.registerUser(userId, "Megham", "M", 22, "haryana", "ynr")
        print(flag, msg)
        for state in states:
            print(portal.add_state(secretKey, state))
        print(portal.add_district(secretKey, 'ynr', 'haryana'))
        print(portal.add_ward('NJJJ', 'haryana', 'djk', 48))
        print(portal.add_district(secretKey, 'ynr', 'haryana'))
        print(portal.add_ward(secretKey, 'haryana', 'ynr', 48))
        print(portal.add_ward(secretKey, 'haryana', 'ynr', 788))
        # add_vaccination_center(self, secretKey, state_name, district_name, ward_no, center_id)0
        print(portal.add_vaccination_center(secretKey, 'haryana', 'ynr', 48, "BH2"))
        print(portal.add_vaccination_center(secretKey, 'haryana', 'ynr', 78, "BH2"))
        print(portal.add_vaccination_center(secretKey, 'haryana', 'ynr', 788, "BH22"))
        print(portal.add_vaccination_center(secretKey, 'haryana', 'ynr', 788, "BEH22"))
        # add_slot(self, secretKey, state_name, district_name, ward_no, center_id, capacity,
        #             startTime):
        print("***")
        print(portal.add_slot(secretKey, 'haryana', 'ynr', 48, "BH2", 4, 10))
        print(portal.add_slot(secretKey, 'haryana', 'ynr', 48, "BH2", 4, 12))
        print(portal.add_slot(secretKey, 'haryana', 'ynr', 78, "BH22", 4, 12))
        print(portal.add_slot(secretKey, 'haryana', 'ynr', 48, "BH2", 4, 12))
        print(portal.add_slot(secretKey, 'haryana', 'ynr', 48, "BEH22", 4, 12))
        print(portal.add_slot(secretKey, 'haryana', 'ynr', 48, "BEH22", 4, 16))
        print(portal.add_slot(secretKey, 'haryana', 'ynr', 48, "BEH22", 4, 18))
        print(portal.add_slot(secretKey, 'haryana', 'ynr', 48, "BH2", 4, 12))
        print(portal.add_slot(secretKey, 'haryana', 'ynr', 48, "BH2", 4, 17))
        print(portal.add_slot(secretKey, 'haryana', 'ynr', 48, "H2", 4, 17))
        print(portal.add_slot(secretKey, 'haryana', 'ynr', 4, "BH2", 4, 21))

        print(portal.add_slot(secretKey, 'haryana', 'ynr', 48, "BH2", 4, 15))
        print(portal.add_slot(secretKey, 'haryana', 'ynr', 788, "BEH22", 4, 15))
        print(portal.add_slot(secretKey, 'haryana', 'ynr', 788, "BH22", 4, 15))

        print(portal.listCenters('haryana', 'ynr'))
        print(portal.listCenters('up','dlk'))
        
        print("****")
        print(portal.bookMySlot(userId, "BH2", 10))
        print(portal.bookMySlot(userId, "BH2", 12))
        print(portal.bookMySlot(userId, "BH2", 12))
        print(portal.bookMySlot(userId, "BH2", 12))
        print(portal.bookMySlot(userId, "BH2", 12))
        print(portal.bookMySlot(userId, "BH2", 12))
        print("****")
        print(portal.listBookings("BH2"))
        print(portal.cancelBooking('BH2', userId, 10))
        print(portal.listBookings("BH2"))
        print(portal.search(15, 'ynr', 'haryana'))
        print(portal.search(11, 'ynr', 'haryana'))
        # print(portal.search(15, 'ynr', 'haryana'))
        # print(portal.search(15, 'ynr', 'haryana'))
    except Exception as error:
        print(error)