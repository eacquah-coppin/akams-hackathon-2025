import pandas as pd
from faker import Faker

# Initialize the Faker instance to generate dummy data
fake = Faker()

# Generate dummy data for the Students Table
students_data = []
for _ in range(100):  # Creating 100 student records
    students_data.append([
        fake.unique.random_number(digits=6),  # StudentID (Primary Key)
        fake.first_name(),                    # FirstName
        fake.last_name(),                     # LastName
        fake.date_of_birth(minimum_age=18, maximum_age=25),  # DateOfBirth
        fake.random_element(elements=("Male", "Female")),  # Gender
        fake.email(),                         # Email
        fake.phone_number(),                  # PhoneNumber
        fake.date_this_century(),             # EnrollmentDate
        fake.random_element(elements=("Computer Science", "Engineering", "Business", "Biology")),  # Program
        fake.random_element(elements=("Freshman", "Sophomore", "Junior", "Senior")),  # Year
        round(fake.random_number(digits=2) / 10, 2)  # GPA
    ])

students_df = pd.DataFrame(students_data, columns=[
    "StudentID", "FirstName", "LastName", "DateOfBirth", "Gender", "Email", "PhoneNumber", "EnrollmentDate", "Program", "Year", "GPA"])

# Generate dummy data for the Faculty Table
faculty_data = []
for _ in range(100):  # Creating 100 faculty records
    faculty_data.append([
        fake.unique.random_number(digits=6),  # FacultyID (Primary Key)
        fake.first_name(),                    # FirstName
        fake.last_name(),                     # LastName
        fake.date_of_birth(minimum_age=30, maximum_age=65),  # DateOfBirth
        fake.random_element(elements=("Male", "Female")),  # Gender
        fake.email(),                         # Email
        fake.phone_number(),                  # PhoneNumber
        fake.date_this_century(),             # HireDate
        fake.random_element(elements=("Computer Science", "Engineering", "Business", "Biology")),  # Department
        fake.random_element(elements=("Assistant Professor", "Associate Professor", "Professor", "Lecturer")),  # Title
        fake.sentence(nb_words=5),             # ResearchInterest
        fake.image_url()                       # Image
    ])

faculty_df = pd.DataFrame(faculty_data, columns=[
    "FacultyID", "FirstName", "LastName", "DateOfBirth", "Gender", "Email", "PhoneNumber", "HireDate", "Department", "Title", "ResearchInterest", "Image"])

# Generate dummy data for the Staff Table
staff_data = []
for _ in range(100):  # Creating 100 staff records
    staff_data.append([
        fake.unique.random_number(digits=6),  # StaffID (Primary Key)
        fake.first_name(),                    # FirstName
        fake.last_name(),                     # LastName
        fake.date_of_birth(minimum_age=25, maximum_age=60),  # DateOfBirth
        fake.random_element(elements=("Male", "Female")),  # Gender
        fake.email(),                         # Email
        fake.phone_number(),                  # PhoneNumber
        fake.date_this_century(),             # HireDate
        fake.random_element(elements=("Administration", "HR", "Finance", "IT")),  # Department
        fake.random_element(elements=("Manager", "Coordinator", "Director", "Assistant")),  # Position
        fake.image_url()                       # Image
    ])

staff_df = pd.DataFrame(staff_data, columns=[
    "StaffID", "FirstName", "LastName", "DateOfBirth", "Gender", "Email", "PhoneNumber", "HireDate", "Department", "Position", "Image"])

# Save each table to a separate CSV file
students_df.to_csv('Students.csv', index=False)
faculty_df.to_csv('Faculty.csv', index=False)
staff_df.to_csv('Staff.csv', index=False)

print("CSV files have been generated successfully!")
