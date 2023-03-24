#dos metodos aparentemente diferentes pero la estructura es la misma
def customers_with_name_startswith(letter):
    "Selecciono clientes con nombres que empieza con la letra @letter"
    selected_customers = []
    for customer in customers:
        if customer.name.startswith(letter):
            selected_customers.append(customer)
    return selected_customers
        
    
def overdraw_accounts():
    "Selecciono las cuentas que tiene giro en descubierto"
    selected_accounts = []
    for account in accounts:
        if account.is_overdraw():
            selected_accounts.append(account)
    return selected_accounts

#un solo método que sirve para los dos
def select(objects, condition):
    selected= []
    for an_object in objects:
        if condition(an_object):
            selected.append(an_object)
    return selected
