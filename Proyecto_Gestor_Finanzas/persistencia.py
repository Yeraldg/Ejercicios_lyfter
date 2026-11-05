import csv
from pathlib import Path
from logica import Category, Movement
from datetime import date, datetime
from decimal import Decimal

def get_file_path(file_name):
    return Path(__file__).parent / file_name

def get_reports_folder():
    reports_folder = Path(__file__).parent / "reportes"
    reports_folder.mkdir(exist_ok=True)
    return reports_folder

def export_report(movements, finance_manager):
    report_timestamp = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    report_path = get_reports_folder() / f"reporte_{report_timestamp}.csv"
    total_income = Decimal("0.00")
    total_expenses = Decimal("0.00")
    for movement in movements:
        if movement.movement_type == "income":
            total_income += movement.amount
        elif movement.movement_type == "expense":
            total_expenses += movement.amount
    net_balance = finance_manager.calculate_balance()
    with open(report_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["Fecha", "Título", "Monto", "Categoría", "Tipo"])
        for movement in movements:
            writer.writerow([movement.movement_date.strftime("%d/%m/%Y"),
                        movement.title,
                        movement.amount,
                        movement.category.name,
                        "Ingreso" if movement.movement_type == "income" else "Gasto"])
        writer.writerow([])
        writer.writerow(["Resumen Financiero"])
        writer.writerow(["Total de ingresos", total_income])
        writer.writerow(["Total de gastos", total_expenses])
        writer.writerow(["Saldo Neto", net_balance])
    return report_path

def save_categories(categories):
    file_path = get_file_path("categorias.csv")
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["code", "name", "active"])
        for category in categories:
            writer.writerow([category.code, category.name, category.active])

def load_categories():
    categories = []
    file_path = get_file_path("categorias.csv")
    if not file_path.exists():
        return categories
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if row[0] == "code":
                continue
            category = Category(row[0], row[1], row[2] == "True")
            categories.append(category)
    return categories

def save_movements(movements):
    file_path = get_file_path("movimientos.csv")
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["movement_id", "title", "amount", "movement_type", 
                        "category_code", "category_name", "movement_date"])
        for movement in movements:
            writer.writerow([movement.movement_id, 
                            movement.title, 
                            movement.amount, 
                            movement.movement_type, 
                            movement.category.code, 
                            movement.category.name, 
                            movement.movement_date])

def load_movements(categories):
    movements = []
    file_path = get_file_path("movimientos.csv")
    if not file_path.exists():
        return movements
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if row[0] == "movement_id":
                continue
            category = None
            for existing_category in categories:
                if existing_category.code == row[4]:
                    category = existing_category
                    break
            if category is None:
                raise ValueError(f"Category {row[4]} not found.")
            movement_date = date.fromisoformat(row[6])
            movement = Movement(row[0], row[1], row[2], row[3], category, movement_date)
            movements.append(movement)
    return movements