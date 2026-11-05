import unittest
from decimal import Decimal
from logica import validate_amount, Category, Movement, FinanceGestor

class Test_validate_amount(unittest.TestCase):
    def test_valid_amount(self):
        result = validate_amount("12500.50")
        self.assertEqual(result, Decimal("12500.50"))

    def test_negative_amount(self):
        with self.assertRaises(ValueError):
            validate_amount("-5000")
    
    def test_zero_amount(self):
        with self.assertRaises(ValueError):
            validate_amount("0")
    
    def test_invalid_amount(self):
        with self.assertRaises(ValueError):
            validate_amount("abc")
    
    def test_infinite_amount(self):
        with self.assertRaises(ValueError):
            validate_amount("Infinity")

class Test_category(unittest.TestCase):
    def test_category_creation(self):
        category = Category("CAT-01", "Food")
        self.assertEqual(category.code, "CAT-01")
        self.assertEqual(category.name, "Food")
        self.assertTrue(category.active)

class Test_movement(unittest.TestCase):
    def test_movement_creation(self):
        category = Category("CAT-01", "Food")
        movement = Movement("MOV-01", "Groseries", "12500.50", "expense", category)
        self.assertEqual(movement.movement_id, "MOV-01")
        self.assertEqual(movement.amount, Decimal("12500.50"))
        self.assertEqual(movement.category, category)
    
    def test_invalid_movement_type(self):
        category = Category("CAT-01", "Food")
        with self.assertRaises(ValueError):
            Movement("MOV-01", "Groseries", "12500.50", "transfer", category)
    
    def test_empty_title(self):
        category = Category("CAT-01", "Food")
        with self.assertRaises(ValueError):
            Movement("MOV-01", "", "12500.50", "expense", category)
    
class Test_Finance_gestor(unittest.TestCase):
    def test_calculate_balance(self):
        finance_gestor = FinanceGestor()
        category = Category("CAT-01", "Food")
        finance_gestor.add_category(category)
        income = Movement("MOV-01", "Salary", "100000", "income", category)
        expense = Movement("MOV-02", "Groseries", "25000", "expense", category)
        finance_gestor.add_movement(income)
        finance_gestor.add_movement(expense)
        result = finance_gestor.calculate_balance()
        self.assertEqual(result, Decimal("75000"))
        self.assertIsInstance(result, Decimal)
    
if __name__ == "__main__":
    unittest.main()