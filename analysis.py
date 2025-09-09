def calculate_salary(hours, rate):
    total = hours * rate
    bonus = 500
    return total + bonus

def process_data(data):
    cleaned = [d.strip().lower() for d in data]
    unique = list(set(cleaned))
    return unique

def generate_report(name, score):
    if score > 90:
        grade = "A"
    else:
        grade = "B"
    return f"Student: {name}, Grade: {grade}"

def display_summary(data):
    print("Summary Report:")
    for item in data:
        print(f"- {item}")
