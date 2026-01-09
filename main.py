from src.cinema import Cinema
import os
import time

def start_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    max_rows = 5
    max_cols = 5
    c = Cinema(5,5)
    print(f"=======================================================\n"
          f"======Welcome to the Cinema Seat Booking game!=========\n"
          f"=======================================================\n")
    while True:
        c.display_cinema()
        print(f"\nWhat do you what to do? Select from these options:\n"
              f"Book a seat: Enter 1\n"
              f"Clear all seats: Enter 2\n"
              f"Exit the game: Enter 3")  

        selected_value = input()
        if selected_value == '1':
            print(f"Enter the seat row and column you want to book.\n")
            try:
                row_number = int(input(f"Desired seat row number from 1 to {max_rows} inclusive"))
                col_number = int(input(f"Desired seat column number from 1 to {max_cols} inclusive"))
                print(f"You selected seat ({row_number}, {col_number})\n")
                print(f"Booking the seat for you...Hold on...")
                time.sleep(2)
                print(f"Booking completed!\n")
                if row_number >= 1 and row_number <= 5 and col_number >= 1 and col_number <= 5:
                    c.book_ticket(row_number, col_number)
                    # c.display_cinema()
                else:
                    print(f"This is not a valid seat in cinema of size [5, 5]")
                    break
            except:
                print(f"Please enter a valid number between 1 to {max_rows}")
                
        elif selected_value == '2':
            print(f"Resetting the theater")
            os.system('cls' if os.name == 'nt' else 'clear')
            
        else:
            
            print(f"Goodbye!")
            break

if __name__ == "__main__":
    start_game()