class Seat:
    def __init__(self, seat_row, seat_col):
        self.seat_row = seat_row
        self.seat_col = seat_col
        self.is_booked = False

    def __str__(self):
        if self.is_booked == True:
            return "[X]"
        else:
            return "[ ]"