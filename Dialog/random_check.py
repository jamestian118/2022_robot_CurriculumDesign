import random
from turtle import st
from unicodedata import name
from unittest import result
import pandas as pd
import global_value


def random_check():
    dict_from_csv = pd.read_csv('students_data.csv').to_dict()
    list_id = list(dict_from_csv['id'].values())
    list_random = list(range(0, len(list_id)))
    for n in range(len(list_id)):
        if dict_from_csv['absenteeism'][n] != 0:
           list_random.append(n + len(list_id)) 
    num = list_random[random.randint(0, len(list_random))]
    
    if num>= len(list_id):
        num = num - len(list_id)
    student_id = list_id[num]
    name = dict_from_csv['name'][num]

    print(list_random)
    


def success_answer(name, student_id):
    global_value.student_comment.append('{}.{}{} answer_success'.format(
        global_value.number_of_courses, student_id, name))


def fail_answer(name, student_id):
    global_value.student_comment.append('{}.{}{} answer_fail'.format(
        global_value.number_of_courses, student_id, name))


def absenteeism(name, student_id):
    global_value.student_comment.append('{}.{}{} dont attend'.format(
        global_value.number_of_courses, student_id, name))
    student_id = int(student_id)
    dict_from_csv = pd.read_csv('students_data.csv').to_dict()
    result_number = list(dict_from_csv['id'].values()).index(student_id)
    dict_from_csv['absenteeism'][result_number] = dict_from_csv['absenteeism'][result_number] + 1
    dict_from_csv['attendance_rate'][result_number] = 1 - dict_from_csv['absenteeism'][result_number] / \
                                                        global_value.number_of_courses
    pd.DataFrame(dict_from_csv).to_csv('students_data_convert.csv')

