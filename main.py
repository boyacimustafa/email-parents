import pandas
import ezgmail
import os
import ezgmail
os.chdir('C:\\Users\\mustafa boyar\\documents\github\\email-parents')
ezgmail.init()

def load_filter_sort(xl_file):
    allgrades_xl = pandas.read_excel(xl_file)
    failing_semester2grades=allgrades_xl[(allgrades_xl["grading_termName"]=="Semester 2") & (allgrades_xl["grading_task"]=="End of Course Grade") & (allgrades_xl["grading_progressPercent"]<60)]
    failing_semester2grades.sort_values(by=['student_stateID'])
    return failing_semester2grades


failing_students=load_filter_sort("allgrades.xlsx")
print(failing_students)


emails = pandas.read_excel("emails.xlsx")
failing_students_with_parentemails=failing_students.merge(emails,left_on=['student_stateID'],right_on=['student_stateID'])
#failing_students_with_parentemails.to_excel("failing_students_with_parentemails.xlsx")

# Get the unique values of 'student_stateID' column
unique_student_id=failing_students_with_parentemails.student_stateID.unique()


for index in range(len(unique_student_id)):
    failing_student_data=failing_students_with_parentemails[failing_students_with_parentemails['student_stateID']==unique_student_id[index]]
    failed_classes = failing_student_data.loc[:,["grading_courseName","grading_progressPercent"]]
    failing_student_data=failing_student_data.reset_index(drop=True)
    first_name = failing_student_data.at[0,"student_firstName"]

    message= "Dear parent \n" + first_name +" is failing the following classes.\n"+failed_classes.to_string(header=False, index=False)


    ezgmail.send('firaca6967@sumwan.com', 'Subject line', message)
