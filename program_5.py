# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

##
# Program 5: Course Info
# Grant Dresser
# 10/24/2025
##

def main():
    courses = {}

    print ("Enter course ID and name course name pairs")
    print ("Type 'done' when you are done entering courses.")

    while True:
        course_id = input("Course ID (or done): ").strip()
        if course_id.lower() == "done":
            break
        course_name = input("Course Name: ").strip()
        courses[course_id] = course_name

    subject_name = input("Enter a subject ID (example: COS): ").strip()
    print(f"Courses for subject '{subject_name}':")
    found = False
 
    for course_id, course_name in courses.items():
        if course_id.lower().startswith(subject_name.lower()):
            print(f"{course_id}: {course_name}")
            found = True

    if not found:
        print(f"No courses found with that subject.")

main()