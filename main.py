import pandas
import os
os.chdir('C:\\Users\\mustafa boyar\\documents\github\\email-parents')

def load_filter_sort(xl_file):
    allgrades_xl = pandas.read_excel(xl_file)
    failing_semester2grades=allgrades_xl[(allgrades_xl["grading_termName"]=="Semester 2") & (allgrades_xl["grading_task"]=="End of Course Grade") & (allgrades_xl["grading_progressPercent"]<60)]
    failing_semester2grades.sort_values(by=['student_stateID'])
    return failing_semester2grades


failing_students=load_filter_sort("allgrades.xlsx")
print(failing_students)