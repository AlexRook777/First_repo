from datetime import datetime

def calculate_person_age(date_of_birth_str: str) -> int:
    date_of_birth = datetime.strptime(date_of_birth_str, "%Y-%m-%d")  # str parse time
    today = datetime.today()

    age = today.year - date_of_birth.year

    if (date_of_birth.month, date_of_birth.day) > (today.month, today.day):
        age -= 1

    return age

print(calculate_person_age("1974-08-19"))  # 25
print(calculate_person_age("1974-02-19"))  # 1