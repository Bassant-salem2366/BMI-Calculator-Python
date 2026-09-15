import os
import matplotlib.pyplot as plt
#PART 1: FUNCTIONS:Bassant
def validAges(age):
    return 2 <= age <= 150
def validgender(g):
    return g.lower().strip() in ["male", "female"]
def getBMIstate(bmi):
    if bmi < 15:
        return "severally underweight"
    elif 15 <= bmi < 20:
        return "underweight"
    elif 20 <= bmi < 25:
        return "fit"
    elif 25 <= bmi <30:
        return "overweight"
    elif 30 <= bmi <35:
        return "obese I"
    elif 35<= bmi < 40:
        return "obese II"
    else:
        return "obese III"
#rahma
bmi_colors = {
    "severally underweight": "\033[91m",
    "underweight": "\033[93m",
    "fit": "\033[92m",
    "overweight": "\033[93m",
    "obese I": "\033[91m",
    "obese II": "\033[91m",
    "obese III": "\033[91m"
}
reset_color = "\033[0m"
#bassant
def get_tips(gender, status):
    if gender == "female":
        if status == "underweight":
            return "Eat More Frequently,Don't Drink Before Meals\nSleep is Crucial,Manage Stress\nCheck with a Professional\nImportant Note: If you are experiencing sudden, unexplained weight loss or a complete lack of appetite,\n please consult a healthcare provider to ensure there isn't an underlying medical condition."
        elif status == "fit":
            return "Focus on Protein,Hydration is Non-Negotiable\nAim for 7–9 hours,Manage Cortisol\nPro-Tip: Every 12 weeks, consider a Deload Week where you reduce your exercise volume by 50%.\n This allows your central nervous system to recover and prevents burnout."
        elif status == "overweight":
            return "Aim for 20–30g of protein at every meal,Fiber for Fullness\nAim for 7–9 hours to keep your insulin sensitivity high,Avoid distracted eating\nA Note on Health: It is always a good idea to have a quick blood panel done by your doctor.\n Conditions like PCOS, hypothyroidism, or vitamin D deficiency can make weight loss significantly harder regardless of how hard you work."
        else:
            return "Check a doctor for a health check."
    else:  # Male
        if status == "underweight":
            return "Aim for 300–500 calories above your maintenance level for steady growth,Eat Every 3 Hours\nA 800-calorie shake is easier to consume than a 800-calorie meal of chicken and rice,Add Healthy Fats\nCheck Your Thyroid: If you are eating 3,000+ calories a day and still losing weight,\n see a doctor to rule out hyperthyroidism or digestive issues like Celiac disease."
        elif status == "fit":
            return "Aim for roughly 0.8g to 1g of protein per pound of body weight,Ensure you’re eating enough healthy fats\nEat clean 80% of the time, but allow for social meals 20% of the time,Sleep is Your Best Supplement\nThe Golden Rule: Maintenance is about being consistently good, rather than occasionally great."
        else:
            return "Aim for 5–6 smaller, nutrient-dense meals rather than 3 heavy ones,\nWalking 8,000–10,000 steps a day is one of the most effective ways to burn fat without spiking cortisol or making you ravenously hungry.\nA Note on Health: If you find it nearly impossible to lose weight despite a good diet,\n consider asking your doctor for a blood panel to check your Testosterone, Thyroid (TSH), and Fasting Insulin levels."
def calculate_bmr(weight_kg, height_cm, age, gender):
    if gender == "male":
        return (10 * weight_kg) + (6.25 * height_cm) - (5 * age) + 5
    else:  # female
        return (10 * weight_kg) + (6.25 * height_cm) - (5 * age) - 161
#rahma
def draw_bmi_diagram(bmi):
    ranges = [
        (0, 15, "severally underweight"),
        (15, 20, "underweight"),
        (20, 25, "fit"),
        (25, 30, "overweight"),
        (30, 35, "obese I"),
        (35, 40, "obese II"),
        (40, 50 , "obese III")
    ]
    plt.figure()
    for start, end, label in ranges:
        plt.axvspan(start, end, alpha=0.3)
        plt.text((start + end) / 2, 0.5, label, ha='center')
    plt.scatter(bmi, 0.5)
    plt.text(bmi, 0.6, f"BMI = {bmi}", ha='center')
    plt.yticks([])
    plt.xlabel("BMI Scale")
    plt.title("BMI Status Diagram")
    plt.xlim(10, 40)
    plt.show()
def write_user_to_file(user):
    with open("users_data.txt", "a") as file:
        file.write(
            f"{user['id']}|{user['name']}|{user['age']}|{user['history']}\n"
        )
def read_users_from_file():
    users = []
    if os.path.exists("users_data.txt"):
        with open("users_data.txt", "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) == 5:
                    uid, name, gender, age, history = parts
                    users.append({
                        "id": int(uid),
                        "name": name,
                        "gender": gender,
                        "age": int(age),
                        "history": eval(history)
                    })
    return users
#PART 2: DATA STORAGE :rahma
user_database = read_users_from_file()

if user_database:
    next_id = max(user["id"] for user in user_database) + 1
else:
    next_id = 101
# --- PART 3: MAIN PROGRAM LOOP ---
while True:
    print("\n" + "_" * 40)
    print("      BMI MANAGEMENT SYSTEM")
    print("_" * 40)
    print("1. New User Registration")
    print("2. Returning User (Login with ID)")
    print("3. Exit System")
    choice = input("\nSelect an option (1-3): ")
    if choice == '3':
        break
    target_user = None
# user choices bassant
    if choice == '1':
        name = input("Enter your name: ").strip()
        while True:
            gender = input("Enter gender (male/female): ").lower().strip()
            if validgender(gender): break
            print("Invalid gender.")
        while True:
            ages = input("Enter age: ")
            if ages.isdigit() and validAges(int(ages)):
                age = int(ages)
                break
            print("Invalid age (Must be 2-150).")
        #profile bassant and rahma
        target_user = {
            'id': next_id,
            'name': name,
            'gender': gender,
            'age': age,
            'history': []
        }
        user_database.append(target_user)
        write_user_to_file(target_user)
        print(f"\nWelcome {name}! Your unique ID is: {next_id}")
        next_id += 1
    elif choice == '2':
        search_input = input("Enter your ID: ")
        if not search_input.isdigit():
            print("Please enter a valid numeric ID.")
            continue
        search_id = int(search_input)
        target_user = None
        for user in user_database:
            if user['id'] == search_id:
                target_user = user
                break
        if not target_user:
            print("ID not found. Try again or register as a new user.")
            continue
        print(f"Welcome back, {target_user['name']}!")
    #CALCULATION bassant
    if target_user:
        unit_choice = input("Use (1) US Units or (2) Metric? ")
        if unit_choice == '1':
            w_pound = float(input("Weight in lbs: "))
            h_foot = float(input("Height in feet: "))
            weight_kg = w_pound * 0.453592
            height_m = h_foot * 0.3048
        else:
            weight_kg = float(input("Weight in kg: "))
            height_cm = float(input("Height in cm: "))
            height_m = height_cm / 100
        bmi = round(weight_kg / (height_m ** 2), 2)
        status = getBMIstate(bmi)
        tips = get_tips(target_user['gender'], status)
        # Update History rahma
        target_user['history'].append(bmi)
        write_user_to_file(target_user)
        color = bmi_colors.get(status, reset_color)
        print(f"\n--- Result for {target_user['name']} ---")
        print(f"Current BMI: {bmi} ({color}{status}{reset_color})")
        print(f"Tips: {tips}")#bassant
        print('your daily calory needs',calculate_bmr(weight_kg, height_cm, age, gender)) #bassant
        print(f"Your full history: {target_user['history']}")
        draw_bmi_diagram(bmi)
#final output rahma
print("\n" + "*" * 40)
print("       FINAL DATABASE SUMMARY")
print("*" * 40)
for u in user_database:
    print(f"ID: {u['id']} | Name: {u['name']} | Attempts: {len(u['history'])}")
    if u['history']:
        print(f"   Latest BMI: {u['history'][-1]}")
    print("-" * 20)
