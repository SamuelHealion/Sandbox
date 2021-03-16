
in_file = open("subjects.txt")
subjects = in_file.readlines()
in_file.close()

subjects = [subject.strip() for subject in subjects]
print(subjects)

# for subject in subjects:
#     if subject[2] == '1':
#         print(subject)

first_year_subjects = [s for s in subjects if s[2] == '1']
print(first_year_subjects)

