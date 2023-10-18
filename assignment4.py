#grading system
def get_grade(score):
    if 0 <= score <= 30:
        return 'D'
    elif 31 <= score <= 50:
        return 'C'
    elif 51 <= score <= 70:
        return 'B'
    elif 71 <= score <= 100:
        return 'A'
    else:
        return 'Unrecognized marks'

# Input 
maths = int(input("Enter the maths score (0-100): "))
physics = int(input("Enter the physics score (0-100): "))
geo = int(input("Enter the geo score (0-100): "))
chem = int(input("Enter the chem score (0-100): "))

# Calculate average score
average_score = (maths + physics + geo + chem) / 4

# grades calc
maths_grade = get_grade(maths)
physics_grade = get_grade(physics)
geo_grade = get_grade(geo)
chem_grade = get_grade(chem)

# Print grades and average 
print(f"Maths: {maths} - Grade: {maths_grade}")
print(f"Physics: {physics} - Grade: {physics_grade}")
print(f"Geo: {geo} - Grade: {geo_grade}")
print(f"Chem: {chem} - Grade: {chem_grade}")
print(f"Average Score: {average_score:.2f}")
