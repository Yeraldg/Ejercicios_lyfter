from decimal import Decimal, InvalidOperation
from datetime import date, datetime
import unicodedata

def validate_amount(amount):
    if amount is None or not str(amount).strip():
        raise ValueError("amount cannot be empty.")
    try:
        amount = Decimal(str(amount))
    except (InvalidOperation, ValueError, TypeError):
        raise ValueError("amount must be a valid number.")
    if not amount.is_finite():
        raise ValueError("amount must be a finite number.")
    if amount <= 0:
        raise ValueError("amount must be greater than zero.")
    return amount

def generate_category_code(categories, last_code_number=0):
    highest_number = last_code_number
    for category in categories:
        try:
            code_number = int(category.code.split("-")[1])
        except(ValueError, IndexError):
            continue
        if code_number > highest_number:
            highest_number = code_number
    return f"CAT-{highest_number + 1:02d}"

def generate_movement_id(movements, last_id_number=0):
    highest_number = last_id_number
    for movement in movements:
        try:
            id_number = int(movement.movement_id.split("-")[1])
        except(ValueError, IndexError):
            continue
        if id_number > highest_number:
            highest_number = id_number
    return f"MOV-{highest_number + 1:03d}"

class Category:
    def __init__(self, code, name, active=True):
        self.code = code
        if not isinstance(name, str) or not name.strip():
            raise ValueError("category name must be a non-empty string")
        self.name = name.strip()
        self.active = active

class Movement:
    def __init__(self, movement_id, title, amount, movement_type, category, movement_date=None):
        self.movement_id = movement_id
        if not isinstance(title, str) or not title.strip():
            raise ValueError("title must be a non-empty string.")
        self.title = title.strip()
        self.amount = validate_amount(amount)
        if movement_type not in ("income", "expense"):
            raise ValueError("movement_type must be 'income' or 'expense'. ")
        self.movement_type = movement_type
        if not isinstance(category, Category):
            raise ValueError("category must be a valid category object.")
        if not category.active:
            raise ValueError("category must be active.")
        self.category = category
        if movement_date is None:
            movement_date = date.today()
        if not isinstance(movement_date, date) or isinstance(movement_date, datetime):
            raise ValueError("movement_date must be a date object")
        if movement_date > date.today():
            raise ValueError("movement_date cannot be in the future.")
        self.movement_date = movement_date

def normalize_text(text):
    normalized_text = unicodedata.normalize("NFD", text.casefold())
    return "".join(character
            for character in normalized_text
            if unicodedata.category(character) != "Mn")

class FinanceGestor:
    def __init__(self):
        self.categories = []
        self.movements = []
        
    def add_category(self, category):
        if not isinstance(category, Category):
            raise ValueError ("category must be a valid category object.")
        for existing_category in self.categories:
            if existing_category.code == category.code:
                raise ValueError("category code already exists.")
            if normalize_text(existing_category.name) == normalize_text(category.name):
                raise ValueError("category name already exists.")
        self.categories.append(category)
    
    def get_active_categories(self):
        return [category 
                for category in self.categories 
                if category.active]
    
    def add_movement(self, movement):
        if not isinstance(movement, Movement):
            raise ValueError("movement must be a valid movement object")
        if movement.category not in self.categories:
            raise ValueError("movement category is not registered")
        self.movements.append(movement)
    
    def calculate_balance(self):
        balance = Decimal("0.00")
        for movement in self.movements:
            if movement.movement_type == "income":
                balance += movement.amount
            elif movement.movement_type == "expense":
                balance -= movement.amount
        return balance

def initialize_finance_manager(categories, movements):
    finance_manager = FinanceGestor()
    for category in categories:
        finance_manager.add_category(category)
    for movement in movements:
        finance_manager.add_movement(movement)
    return finance_manager