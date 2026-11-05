Personal Finance Manager

A desktop application developed in Python to manage personal finances through a graphical user interface. It allows users to record income and expenses, organize transactions by categories, track their balance, and export financial reports.

This project was developed as part of my programming training, applying fundamental software development concepts through a practical application.

Features

- Income Management: Register and track income transactions.
- Expense Management: Record expenses and associate them with categories.
- Category Management: Create and manage transaction categories.
- Balance Calculation: Automatically calculate the current financial balance.
- Date Filtering: Filter transactions using a custom date range.
- CSV Data Persistence: Save and load categories and transactions using CSV files.
- Report Export: Generate financial reports in CSV format, including income, expenses, and net balance.
- Input Validation: Validate amounts, dates, descriptions, and category selections.

Technologies Used

- Python 3.14
- FreeSimpleGUI
- CSV
- Decimal
- Unittest

Project Structure

Proyecto_Gestor_Finanzas/
│
├── main.py
├── interfaces.py
├── logica.py
├── persistencia.py
├── test_logica.py
├── requirements.txt
└── README.md

Installation

1. Clone the repository:

git clone https://github.com/Yeraldg/Ejercicios_lyfter.git

2. Navigate to the project directory:

cd Ejercicios_lyfter/Proyecto_Gestor_Finanzas

3. Create and activate a virtual environment:

python -m venv .venv

Windows:

.venv\Scripts\activate

4. Install the dependencies:

pip install -r requirements.txt

How to Run

Start the application with:

python main.py

Running Unit Tests

Execute the unit tests with:

python -m unittest test_logica.py -v

The project includes 10 unit tests covering core business logic and input validation.

Concepts Applied

- Object-Oriented Programming (OOP)
- Modular programming
- File handling
- Data validation
- Exception handling
- Unit testing
- Separation of business logic and user interface

Currency

The application uses Costa Rican colones (CRC), displaying amounts with the ₡ symbol and two decimal places.

Author

Yerald Mauricio Garcia Arguedas

Developed as a practical programming project.