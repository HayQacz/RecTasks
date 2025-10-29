import datetime

# https://www.gov.pl/web/gov/czym-jest-numer-pesel

def get_pesel_info(pesel: str) -> dict:
    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    if 81 <= month <= 92:
        year += 1800
        month -= 80
    elif 1 <= month <= 12:
        year += 1900
    elif 21 <= month <= 32:
        year += 2000
        month -= 20
    elif 41 <= month <= 52:
        year += 2100
        month -= 40
    elif 61 <= month <= 72:
        year += 2200
        month -= 60
    else:
        pass

    try:
        day_of_birth = datetime.date(year, month, day)
    except ValueError:
        day_of_birth = None

    gender_number = int(pesel[9])
    gender = "Male" if gender_number % 2 == 1 else "Female"

    return {
        'date_of_birth': day_of_birth,
        'gender': gender,
    }