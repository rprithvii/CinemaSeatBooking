from src.seat import Seat

class Cinema:
    def __init__(self, n_rows_cinema, n_cols_cinema):
        self.n_rows_cinema = n_rows_cinema
        self.n_cols_cinema = n_cols_cinema

        self.seats = []
        for i in range(1, n_rows_cinema + 1):
            for j in range(1, n_cols_cinema + 1):
                self.seats.append(Seat(i, j))

    def display_cinema(self):
        print(f"Screen this way\n"
              f"======================")
        for index, j in enumerate(self.seats):
            if (index+1)%self.n_cols_cinema == 0:
                print(j, end = "\n")
            else:
                print(j, end = " ")        
     
    def book_ticket(self, chosen_row, chosen_col):
        for i in self.seats:
            if i.seat_row == chosen_row and i.seat_col == chosen_col and i.is_booked == True:
                print(f"Chose another seat. It is already booked")
            elif i.seat_row == chosen_row and i.seat_col == chosen_col:
                i.is_booked = True
                print(f"You chosen seat is booked. Seat Number: R{chosen_row}C{chosen_col}")    