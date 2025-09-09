def calculate_salary(hours, rate):
    base = hours * rate
    tax = base * 0.1
    return base - tax

def process_data(data):
    cleaned = [d.upper() for d in data if d]
    return sorted(cleaned)

def generate_report(name, score):
    if score >= 85:
        grade = "Distinction"
    else:
        grade = "Pass"
    return {"name": name, "grade": grade}

def display_summary(data):
    print("=== REPORT ===")
    for idx, item in enumerate(data, start=1):
        print(f"{idx}. {item}")
