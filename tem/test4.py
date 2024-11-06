from datetime import date, timedelta
import random

# Generate random date within the past 10 years
def random_date():
    start_date = date.today() - timedelta(days=365 * 10)
    end_date = date.today()
    return start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

# Gender choices
genders = ["m", "f", "o"]

# Sample data lists
names = [
    "John Doe", "Jane Smith", "Alice Johnson", "Bob Brown", "Chris Green",
    "Michael Adams", "Emma Wilson", "Olivia Thomas", "Liam Martinez",
    "Sophia Anderson", "Ava Jackson", "Mason White", "Isabella Harris",
    "James Martin", "Amelia Lewis", "Benjamin Young", "Lucas King",
    "Mia Wright", "Charlotte Scott", "Elijah Turner", "David Lee", "Sara Collins",
    "William Baker", "Ella Perez", "Jack Murphy", "Zoe Clark", "Jacob Rivera",
    "Henry Brooks", "Evelyn Wood", "Samuel Sanders", "Madison Edwards", "Daniel Lopez",
    "Aria Reed", "Logan Powell", "Lily Howard", "Alexander Stewart", "Grace Ramirez",
    "Ella Peterson", "Owen Foster", "Emily Ward", "Sofia Fisher", "Joseph Morris",
    "Jackson Long", "Victoria Ross", "Sebastian Morgan", "Hannah Bell", "Ethan Nelson"
]
problems = [
    "Hypertension", "Diabetes", "Chronic back pain", "Migraine", "Arthritis",
    "Heart disease", "Asthma", "Skin allergies", "Thyroid issues", "Kidney stones",
    "Fatigue", "Depression", "Anxiety", "High cholesterol", "Cancer",
    "Pneumonia", "Bronchitis", "Insomnia", "Gastroesophageal reflux", "Chronic headache",
    "High blood pressure", "Osteoporosis", "Rheumatoid arthritis", "Stroke",
    "Parkinson's disease", "Chronic liver disease", "Bipolar disorder", "PTSD", 
    "Anemia", "Urinary infection", "Ulcers", "Sciatica", "Hepatitis"
]
medical_histories = [
    "History of hypertension", "Diabetes Type II for 5 years", "Chronic back pain",
    "Migraines since teenage years", "Arthritis in knees", "Heart attack two years ago",
    "Diagnosed with asthma in childhood", "Allergic to dust", "Hypothyroidism",
    "Had kidney stones removed", "Low energy levels", "History of depression",
    "Anxiety and stress issues", "Family history of high cholesterol", "Cancer survivor",
    "Had pneumonia last year", "Occasional bronchitis", "Diagnosed with insomnia",
    "Gastro issues since 20s", "Chronic migraines", "Eczema in childhood", 
    "Seasonal allergies", "Suffered head trauma in 2010", "Rare blood type", 
    "Nerve pain since 5 years", "Recovering from stroke", "Pre-diabetic", 
    "Experienced fainting episodes"
]
operation_histories = [
    "Appendectomy", "Gallbladder removal", "Heart bypass surgery", "Knee surgery",
    "None", "Thyroid surgery", "Kidney stone removal", "C-section",
    "Hernia surgery", "Tonsillectomy", "None", "Spinal surgery", "Sinus surgery",
    "Hysterectomy", "Liver transplant", "Hand surgery", "ACL reconstruction",
    "Eye surgery", "Dental surgery", "Stent placement", "Hip replacement",
    "Back surgery", "Skin grafting", "Bariatric surgery", "Breast surgery",
    "Amputation", "Gallstone removal"
]
other_details = [
    "Non-smoker", "Vegetarian", "Exercises regularly", "Avoids caffeine", "Low-salt diet",
    "Non-drinker", "Meditates regularly", "Frequent traveler", "Single parent",
    "Recently retired", "Health-conscious", "Prefers organic food", "Works in office",
    "Prefers home-cooked meals", "Practices yoga", "Allergic to penicillin",
    "Gluten-free diet", "Likes outdoor sports", "Married", "Parent of two", 
    "Cyclist", "Pet owner", "Volunteer worker", "Vegan", "Running enthusiast",
    "Keto diet follower", "College student", "Divorced", "Widowed", "Avid reader"
]
contact_prefix = "98765432"  # Starting 8 digits for a generic contact number
address_lines = [
    "123 Elm Street, Springfield", "456 Maple Avenue, Shelbyville", "789 Oak Road, Capital City",
    "321 Pine Street, North Haverbrook", "654 Cedar Lane, Ogdenville", "789 Willow Blvd, Springfield",
    "1010 Birch Lane, Capital City", "2020 Chestnut Dr, Shelbyville", "3030 Redwood Ave, Ogdenville",
    "4040 Walnut St, Springfield", "5050 Aspen Rd, Capital City", "6060 Beech Pl, Shelbyville",
    "7070 Cedar Pkwy, Ogdenville", "8080 Fir Dr, Springfield", "9090 Hickory Ln, Capital City",
    "1111 Juniper Ave, Shelbyville", "1212 Laurel St, Ogdenville", "1313 Magnolia Blvd, Springfield",
    "1414 Oakmont Dr, Capital City", "1515 Poplar St, Shelbyville"
]

# Create 200 dummy Patient entries
id = 1000100
for i in range(0, 40):
    
    name= names[i]
    img = ''
    gender=random.choice(genders),
    age=random.randint(1, 100),
    problem=random.choice(problems),
    medical_history=random.choice(medical_histories),
    operation_history=random.choice(operation_histories),
    other_details=random.choice(other_details),
    contact_no=contact_prefix + f"{random.randint(1000, 9999)}",
    profile_created_on_or_first_diagnos=random_date(),
    address=random.choice(address_lines)

    
    
    print(f'''INSERT INTO  public."Data_manager_patient" (id, name, img, gender, problem, 
                medical_history, operation_history, other_details, contact_no, age, 
                profile_created_on_or_first_diagnos, address) VALUES ({id}, '{name}', '{img}',
              '{gender[0]}', '{problem[0].replace("'", "-")}', '{medical_history[0].replace("'", "-")}', 
              '{operation_history[0].replace("'", "-")}', '{other_details[0].replace("'", "-")}', '{contact_no[0]}', 
              '{age[0]}', '{profile_created_on_or_first_diagnos[0]}', 
              '{address}');''')

    id = id + int(random.randint(100, 1000))  + int(random.randint(2000, 3000))  + int(random.randint(5000, 7000)) + int(random.randint(8000, 9000))
    
