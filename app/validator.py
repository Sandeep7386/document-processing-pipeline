import re
from datetime import datetime

def validate_name(name):
    return bool(name and re.match(r"^[A-Za-z ]{2,50}$", name))

def validate_amount(amount):
    return amount is not None and amount > 0

def validate_date(date):
    try:
        d = datetime.strptime(date, "%d/%m/%Y")
        return d <= datetime.now()
    except:
        return False

def validate_id(id):
    return bool(id and re.match(r"^[A-Z0-9]{6,12}$", id))

def validate_all(data):
    return {
        "name": validate_name(data["name"]),
        "amount": validate_amount(data["amount"]),
        "date": validate_date(data["date"]),
        "id": validate_id(data["id"])
    }