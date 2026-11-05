from datetime import datetime
import FreeSimpleGUI as sg
from persistencia import load_categories, load_movements, save_categories, save_movements, export_report
from logica import initialize_finance_manager, generate_category_code, Category, Movement, generate_movement_id

def convert_movement_date(date_text):
    try:
        return datetime.strptime(date_text, "%d/%m/%Y").date()
    except ValueError:
        raise ValueError("La fecha ingresada no es valida.")

def format_amount(amount, movement_type=None):
    formatted_amount = f"{abs(amount):,.2f}"
    formatted_amount = formatted_amount.replace(",", "X")
    formatted_amount = formatted_amount.replace(".", ",")
    formatted_amount = formatted_amount.replace("X", " ")
    if movement_type == "expense" or (movement_type is None and amount < 0):
        return f"-₡{formatted_amount}"
    return f"₡{formatted_amount}"

def prepare_movement_rows(movements):
    rows = []
    for movement in movements:
        row = [movement.movement_date.strftime("%d/%m/%Y"), movement.title, format_amount(movement.amount, movement.movement_type), movement.category.name, 
            "Ingreso"  if movement.movement_type == "income"
            else "Gasto"]
        rows.append(row)
    return rows

def filter_movements_by_date(movements, start_date, end_date):
    filtered_movements = []
    for movement in movements:
        if start_date <= movement.movement_date <= end_date:
            filtered_movements.append(movement)
    return filtered_movements

    
def main_window():
    categories = load_categories()
    movements = load_movements(categories)
    finance_manager = initialize_finance_manager(categories, movements)
    balance = finance_manager.calculate_balance() 
    movement_rows = prepare_movement_rows(movements)
    
    layout = [[sg.Text("Gestor de Finanzas Personales", font=("Arial", 20, "bold"), justification="center", expand_x=True)], 
            [sg.Column([[sg.Button("Categorias", key="-CATEGORIES-"), 
            sg.Button("Agregar ingreso", key="-ADD_INCOME-"), 
            sg.Button("Agregar gasto", key="-ADD_EXPENSE-"), 
            sg.Button("Exportar reporte", key="-EXPORT_REPORT-")]],element_justification="center", expand_x=True, pad=(0, 10))], 
            [sg.Text("Saldo", font=("Arial", 15, "bold"), justification="center", expand_x=True)], 
            [sg.Text(format_amount(balance), font=("Arial", 22, "bold"), justification="center", expand_x=True, key="-BALANCE-")], 
            [sg.Text("Filtrar movimientos por fecha", font=("Arial", 11, "bold"))], 
            [sg.Text("Desde:"), sg.Input(key="-START_DATE-", size=(12, 1)), sg.Text("Hasta:"), sg.Input(key="-END_DATE-", size=(12, 1))], 
            [sg.Button("Filtrar", key="-FILTER_DATES-"), sg.Button("Mostrar Todo", key="-SHOW_ALL-")], 
            [sg.Table(values = movement_rows, headings=["Fecha", "Descripcion", "Monto", "Categoria", "Tipo"], 
            key="-MOVEMENTS_TABLE-", auto_size_columns=False, col_widths=[12, 25, 18, 20, 12], justification="center", 
            expand_x=True, expand_y=False, num_rows=5)]]
    window = sg.Window("Gestor de Finanzas Personales", layout, size=(800, 500))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "-CATEGORIES-":
            print("Categories button pressed")
            categories_window(finance_manager)
        elif event == "-ADD_INCOME-":
            print("add_income button pressed")
            if add_movement_window(finance_manager, "income"):
                balance = finance_manager.calculate_balance()
                window["-BALANCE-"].update(format_amount(balance))
                movement_rows = prepare_movement_rows(finance_manager.movements)
                window["-MOVEMENTS_TABLE-"].update(values=movement_rows)
        elif event == "-ADD_EXPENSE-":
            print("Add_expense button pressed")
            if add_movement_window(finance_manager, "expense"):
                balance = finance_manager.calculate_balance()
                window["-BALANCE-"].update(format_amount(balance))
                movement_rows = prepare_movement_rows(finance_manager.movements)
                window["-MOVEMENTS_TABLE-"].update(values=movement_rows)
        elif event == "-EXPORT_REPORT-":
            if not finance_manager.movements:
                sg.popup_error("No hay movimientos para exportar.")
                continue
            try:
                report_path = export_report(finance_manager.movements, finance_manager)
                sg.popup(f"El reporte se exportó correctamente. \nUbicacion: \n{report_path}")
            except OSError:
                sg.popup_error("No se pudo generar el reporte.", title="Error de exportacion")
        elif event == "-FILTER_DATES-":
            start_date_text = values["-START_DATE-"].strip()
            end_date_text = values["-END_DATE-"].strip()
            if not start_date_text or not end_date_text:
                sg.popup_error("Debe ingresar ambas fechas.")
                continue
            try:
                start_date = convert_movement_date(start_date_text)
                end_date = convert_movement_date(end_date_text)
            except ValueError as error:
                sg.popup_error(str(error))
                continue
            if start_date > end_date:
                sg.popup_error("La fecha inicial no puede ser posterior a la fecha final.")
                continue
            filtered_movements = filter_movements_by_date(finance_manager.movements, start_date, end_date)
            filtered_rows = prepare_movement_rows(filtered_movements)
            window["-MOVEMENTS_TABLE-"].update(values=filtered_rows)
        elif event == "-SHOW_ALL-":
            movement_rows = prepare_movement_rows(finance_manager.movements)
            window["-MOVEMENTS_TABLE-"].update(values=movement_rows)
            window["-START_DATE-"].update("")
            window["-END_DATE-"].update("")
    
    window.close()


def categories_window(finance_manager):
    active_categories = finance_manager.get_active_categories()
    category_rows = [[category.code, category.name]
        for category in active_categories]
    layout = [[sg.Text("Categorías", font=("arial", 16, "bold"))], 
    [sg.Table(values=category_rows, headings=["Código", "Nombre"], key="-CATEGORY_TABLE-", auto_size_columns=True, justification="center",num_rows=10)], 
    [sg.Button("Agregar categoría", key="-ADD_CATEGORY-"), sg.Button("Cerrar", key="-CLOSE-")]]
    window = sg.Window("Categorías", layout, size=(250, 280), modal=True)
    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "-CLOSE-"):
            break
        elif event == "-ADD_CATEGORY-":
            category_added =add_category_window(finance_manager)
            if category_added:
                active_categories = finance_manager.get_active_categories()
                category_rows = [[category.code, category.name]
                for category in active_categories]
            window["-CATEGORY_TABLE-"].update(values= category_rows)
                
    window.close()

def add_category_window(finance_manager):
    layout = [[sg.Text("Nombre de la Categoría:")], 
            [sg.Input(key="-CATEGORY_NAME-")], 
            [sg.Button("Guardar", key="-SAVE_CATEGORY-"), sg.Button("Cancelar", key="-CANCEL-")]]
    window =sg.Window("Agregar categoría", layout, size=(350, 100), modal=True)
    while True:
        event, values = window.read()
        if event in(sg.WIN_CLOSED, "-CANCEL-"):
            window.close() 
            return False
        elif event == "-SAVE_CATEGORY-":
            category_name = values["-CATEGORY_NAME-"].strip()
            if not category_name:
                sg.popup_error("Debe ingresar el nombre de la categoría", title="Campo obligatorio")
                continue
            try:
                category_code = generate_category_code(finance_manager.categories)
                category = Category(category_code, category_name)
                finance_manager.add_category(category)
                save_categories(finance_manager.categories)
            except ValueError as error:
                if str(error) == "category name already exists.":
                    sg.popup_error("Ya existe una categoría con ese nombre.", title="Categoría duplicada.")
                else:
                    sg.popup_error("No se pudo agregar la categoría.", title="Error")
                continue
            sg.popup("La Categoría se agrego correctamente.", title="Operacion exitosa")
            window.close()
            return True
            
    window.close()

def translate_error(error):
    error_messages = {"amount cannot be empty.": "El monto no puede estar vacío.", 
                    "amount must be a valid number.": "El monto debe de ser un numero valido.", 
                    "amount must be a finite." : "El monto debe ser un numero valido.", 
                    "amount must be greater than zero.": "El monto debe ser mayor a cero.", 
                    "movement_date cannot be in the future.": "la fecha del movimiento no puede ser en el futuro."}
    return error_messages.get(str(error), str(error))

def add_movement_window(finance_manager, movement_type):
    if movement_type == "income":
        window_title = "Agregar ingreso"
    else:
        window_title = "Agregar gasto"
    layout = [[sg.Text("Descripción del movimiento:")], 
            [sg.Input(key="-MOVEMENT_TITLE-")], 
            [sg.Text("Monto en colones")], 
            [sg.Input(key="-MOVEMENT_AMOUNT-")], 
            [sg.Text("Categoría:")], 
            [sg.Combo(values=[category.name
                        for category in finance_manager.get_active_categories()],
                            key="-MOVEMENT_CATEGORY-", readonly=True)], 
            [sg.Text("Fecha (dd/mm/aaaa):")], 
            [sg.Input(default_text=datetime.today().strftime("%d/%m/%Y"), key="-MOVEMENT_DATE-")],
            [sg.Button("Guardar", key="-SAVE_MOVEMENT-"), sg.Button("Cancelar", key="-CANCEL_MOVEMENT-")]]
    window = sg.Window(window_title, layout, size=(400, 350), modal=True)
    while True:
        event, values= window.read()
        if event in (sg.WIN_CLOSED, "-CANCEL_MOVEMENT-"):
            window.close()
            return False
        elif event == "-SAVE_MOVEMENT-":
            movement_title = values["-MOVEMENT_TITLE-"].strip()
            amount_text = values["-MOVEMENT_AMOUNT-"].strip()
            category_name = (values["-MOVEMENT_CATEGORY-"] or "").strip()
            date_text = values["-MOVEMENT_DATE-"].strip()
            if not movement_title:
                sg.popup_error("La descripcion del movimiento es obligatoria.")
                continue
            if not amount_text:
                sg.popup_error("El monto es obligatorio")
                continue
            if not category_name:
                sg.popup_error("Debe seleccionar una categoría.")
                continue
            try:
                movement_date = convert_movement_date(date_text) if date_text else None
            except ValueError as error:
                sg.popup_error(str(error))
                continue
            category = next((category
                            for category in finance_manager.get_active_categories()
                            if category.name == category_name), None)
            if category is None:
                sg.popup_error("La categoría seleccionada no es valida")
                continue
            movement_id = generate_movement_id(finance_manager.movements)
            try:
                movement = Movement(movement_id, movement_title, amount_text, movement_type, category, movement_date)
                finance_manager.add_movement(movement)
            except ValueError as error:
                sg.popup_error(translate_error(error))
                continue
            save_movements(finance_manager.movements)
            window.close()
            return True