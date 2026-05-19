# ── Grading config ─────────────────────────────────────
GRADE_SCALE = [
    (90, "A+", 4.0),
    (80, "A",  3.7),
    (70, "B+", 3.3),
    (60, "C+", 2.3),
    (50, "D",  1.0),
    (40, "C-", 1.7),
    (0,  "F",  0.0),
]
PASS_MARK = 40
students = [
    {"name": "Aarav",   "marks": {"Maths": 88, "Science": 76, "English": 91, "Hindi": 65, "CS": 95}},
    {"name": "Sneha",   "marks": {"Maths": 55, "Science": 60, "English": 72, "Hindi": 80, "CS": 38}},
    {"name": "Rohan",   "marks": {"Maths": 35, "Science": 42, "English": 50, "Hindi": 38, "CS": 60}},
    {"name": "Priya",   "marks": {"Maths": 92, "Science": 89, "English": 95, "Hindi": 88, "CS": 97}},
    {"name": "Karan",   "marks": {"Maths": 70, "Science": 65, "English": 58, "Hindi": 72, "CS": 80}},
    {"name": "Meera",   "marks": {"Maths": 45, "Science": 38, "English": 62, "Hindi": 55, "CS": 50}},
    {"name": "Arjun",   "marks": {"Maths": 78, "Science": 82, "English": 74, "Hindi": 69, "CS": 88}},
]

def get_letter_grade(average):
    for marks, grade, gpa in GRADE_SCALE:
        if average >= marks:
            return grade, gpa
    print('Grade: F, GPA: 0.0')
    return "F"
    pass

def get_average(marks_dict):
    total_marks = sum(marks_dict.values())
    average = total_marks / len(marks_dict)
    print('Average Marks:', average)
    return average
    pass

def get_failed_subjects(marks_dict):
    sub_f=[]
    for subject, marks in marks_dict.items():
        if marks < PASS_MARK:
            sub_f.append(subject)
    print('Failed Subjects:', sub_f)
    return sub_f
    pass

def build_results(students):
    
    results = []

    for stud in students:

        marks_dict = stud['marks']

        # average
        sample_avg = get_average(marks_dict)

        # grade + gpa
        grade, gpa = get_letter_grade(sample_avg)

        # failed subjects
        failed_subjects = get_failed_subjects(marks_dict)

        # total marks
        total = sum(marks_dict.values())

        # create result dictionary
        result = {
            "name": stud["name"],
            "marks": marks_dict,
            "average": sample_avg,
            "grade": grade,
            "gpa": gpa,
            "failed_subjects": failed_subjects,
            "total": total
        }

        results.append(result)

    # sort by average descending
    sorted_students = sorted(
        results,
        key=lambda x: x['average'],
        reverse=True
    )

    # assign ranks
    for rank, stud in enumerate(sorted_students, start=1):
        stud["rank"] = rank

    return sorted_students
    pass

def print_report_table(results):
    print(f"{'Rank':<5} {'Name':<10} {'Marks':<10} {'Average':<10} {'Grade':<10} {'GPA':<10}")

    print("-" * 60) # prints the line

    for student in results:
        print(
    f"{student['rank']:<5} "
    f"{student['name']:<10} "
    f"{student['total']:<10} "
    f"{student['average']:<10.2f} "
    f"{student['grade']:<10} "
    f"{student['gpa']:<10.2f}"
)

    for student in results:
        if student['failed_subjects']:
            print(f"{student['name']} failed in: {', '.join(student['failed_subjects'])}")
            # prints the failed subjects for each student if any
    pass

def get_subject_stats(students):
    subjects = list(students[0]['marks'].keys())
    stats = {}

def get_subject_stats(students):
    subjects = list(students[0]["marks"].keys())
    stats    = {}                     

    for subject in subjects:        
        scores = [s["marks"][subject] for s in students]
        # Maths → [88, 55, 35, 92, 70, 45, 78]

        highest = max(students, key=lambda s: s["marks"][subject])
        lowest  = min(students, key=lambda s: s["marks"][subject])


        stats[subject] = {
            "avg":     round(sum(scores) / len(scores), 1),
            "highest": (highest["name"], highest["marks"][subject]),
            "lowest":  (lowest["name"],  lowest["marks"][subject]),
        }

    return stats
pass

def print_subject_summary(stats, results):
    print(f"{'Subject':<10} {'Average':<10} {'Highest':<20} {'Lowest':<20}")
    print("-" * 60)

    for subject, data in stats.items():
        print(f"{subject:<10} {data['avg']:<10.1f} {data['highest'][0]} ({data['highest'][1]}) {data['lowest'][0]} ({data['lowest'][1]})")
        
    pass

def main():
    results = build_results(students)
    print_report_table(results)
    stats = get_subject_stats(students)
    print_subject_summary(stats, results)
    pass

if __name__ == "__main__":
    main()
