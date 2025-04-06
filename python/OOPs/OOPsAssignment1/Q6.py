"""#### 6.Write a code for  Hotel Management System using OOPS :
Create a Room class that has attributes such as room number, room type, rate, and availability (private).
Implement methods to book a room, check in a guest, and check out a guest.
Use encapsulation to hide the room's unique identification number.
Inherit from the Room class to create a SuiteRoom class and a StandardRoom class, each with their own specific attributes and methods.

"""
class Room:
    next_room=201
    def __init__(self,room_type,rate):
        self._room_number= Room.next_room
        self._room_type= room_type
        self._rate=rate
        self._available=True
        Room.next_room+=1
    
    def get_room_number(self):
        return self._room_number
    def get_room_type(self):
        return self._room_type
    def get_room_rate(self):
        return self._rate
    def is_available(self):
        return self._available
    def book_room(self):
        if self.is_available():
            self._available=False
            print(f"Room {self._room_number} type {self._room_type} has been booked")
        else:
            print("The room is not available")
    def check_in(self):
        if not self.is_available():
            print(f"Guest checked in room number {self._room_number} type {self._room_type}")
        else:
            print(f"{self._room_number} type {self._room_type} is not booked")
    def check_out(self):
        if  self.is_available():
            print(f"Guest checked out room number {self._room_number} type {self._room_type}")
        else:
            print(f"{self._room_number} type {self._room_type} is  booked")


class SuiteRoom(Room):
    def __init__(self,rate,has_jacuzzi):
        super().__init__("Suit Room",rate)
        self._has_jacuzzi=has_jacuzzi
    def get_has_jacuzzi(self):
        return self._has_jacuzzi

    def set_has_jacuzzi(self, has_jacuzzi):
        self._has_jacuzzi = has_jacuzzi

class StandardRoom(Room):
    def __init__(self, rate, has_balcony):
        super().__init__("Standard", rate)
        self._has_balcony = has_balcony

    def get_has_balcony(self):
        return self._has_balcony

    def set_has_balcony(self, has_balcony):
        self._has_balcony = has_balcony
# Example usage
def main():
    # Create rooms
    suite_room = SuiteRoom(200.0, True)
    standard_room = StandardRoom(150.0, False)

    # Book and check in/out rooms
    suite_room.book_room()
    suite_room.check_in()
    suite_room.check_out()

    standard_room.book_room()
    standard_room.check_in()
    standard_room.check_out()

if __name__ == "__main__":
    main()

    

      