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