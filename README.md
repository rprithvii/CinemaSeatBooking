# Cinema Seat Booking System 🎬

A Python-based terminal application designed to practice **Object-Oriented Programming (OOP)** principles. This project simulates a cinema theater where users can view a seating layout and book specific seats using a coordinate system.

## 🧠 OOP Concepts Applied

This project was built to demonstrate several core programming patterns:

* **Encapsulation**: The `Seat` class manages its own internal state (`is_booked`), protecting data integrity.
* **Composition**: The `Cinema` class "composes" a grid of `Seat` objects during initialization. The life of the seats is tied directly to the theater.
* **Coordinate Logic**: Uses a 2D grid system (Rows and Columns) to identify and interact with specific objects in a collection.
* **Modularity**: Separation of concerns between the data models (`models.py`) and the execution logic (`main.py`).

## 📁 Project Structure

```text
CinemaSeatBooking/
├── .venv/            # Local virtual environment
├── .gitignore        # Prevents environment and cache files from being uploaded
├── models.py         # Contains Seat and Cinema classes
├── main.py           # Application entry point and testing logic
└── README.md         # Project documentation
```

## 🚀 Getting Started
Prerequisites
Python 3.10+

[Optional] Anaconda/Conda

Installation & Setup
1. Clone the repository:
```
git clone [https://github.com/rprithvii/CinemaSeatBooking.git](https://github.com/rprithvii/CinemaSeatBooking.git)
cd CinemaSeatBooking
```

2. Create and activate the virtual environment:
```
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate
```
3. Run the application:
```
python main.py
```
## 🕹️ Usage
The system initializes a 3x3 grid by default.

[ ] represents an available seat.

[X] represents a booked seat.

The Cinema class provides methods to display the layout and book seats by passing row and column integers.