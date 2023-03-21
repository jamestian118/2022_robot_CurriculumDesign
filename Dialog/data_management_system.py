# 利用将csv文件转换为字典来实现信息存储

import pandas as pd
import numpy as np
import global_value

def data_management(choice_number):
    dict_from_csv = pd.read_csv('students_data.csv').to_dict()
    print(dict_from_csv)

    # 假设GUI是使用数值来选择
    if choice_number == 1:  # 添加学生信息
        # 创建一个空字典
        new_student_info = {}
        # 输入学生信息
        new_student_info['name'] = input('请输入学生姓名：')
        new_student_info['id'] = input('请输入学生学号：')
        new_student_info['absenteeism'] = 0
        new_student_info['attendance_rate'] = 0.0
        # 将学生信息添加到字典中
        dict_from_csv['name'][len(dict_from_csv['name'])] = (new_student_info['name'])
        dict_from_csv['id'][len(dict_from_csv['id'])] = (new_student_info['id'])
        dict_from_csv['absenteeism'][len(dict_from_csv['absenteeism'])] = (new_student_info['absenteeism'])
        dict_from_csv['attendance_rate'][len(dict_from_csv['attendance_rate'])] = (new_student_info['attendance_rate'])
        # 将字典转换为csv文件
        pd.DataFrame(dict_from_csv).to_csv('students_data_convert.csv')
        print('添加学生信息成功！')
    elif choice_number == 2:  # 删除学生信息
        name = input('请输入要删除的学生姓名：')
        # student_id = int(input('请输入要删除的学生学号：'))
        # result_number = list(dict_from_csv['id'].values()).index(student_id)
        del dict_from_csv['name'][list(dict_from_csv['name'].values()).index(name)]
        print('删除学生信息成功！')
    elif choice_number == 3:  # 修改学生信息
        # 输入要修改的学生姓名
        name = input('请输入要修改的学生姓名：')
        # 输入要修改的学生信息
        new_student_info = {}
        new_student_info['name'] = input('请输入学生姓名：')
        new_student_info['id'] = input('请输入学生学号：')
        new_student_info['absenteeism'] = input('请输入学生缺勤次数：')
        new_student_info['attendance_rate'] = (1 - (new_student_info['absenteeism']) / global_value.number_of_courses)
        # 将学生信息添加到字典中
        dict_from_csv['name'][len(dict_from_csv['name'])] = (new_student_info['name'])
        dict_from_csv['id'][len(dict_from_csv['id'])] = (new_student_info['id'])
        dict_from_csv['absenteeism'][len(dict_from_csv['absenteeism'])] = (new_student_info['absenteeism'])
        dict_from_csv['attendance_rate'][len(dict_from_csv['attendance_rate'])] = (new_student_info['attendance_rate'])
        # 将字典转换为csv文件
        pd.DataFrame(dict_from_csv).to_csv('students_data_convert.csv')
        print('修改学生信息成功！')
    elif choice_number == 4:  # 查询学生信息
        # 输入要查询的学生学号
        student_id = input('请输入要查询的学生学号：')
        # 查询学生信息
        dict_from_csv = pd.read_csv('students_data.csv').to_dict()
        result_number = list(dict_from_csv['id'].values()).index(int(student_id))
        print('学生姓名：{}, 学号：{}, 出勤率：{}'.format(dict_from_csv['name'][result_number], dict_from_csv['id'][result_number], dict_from_csv['attendance_rate'][result_number]))


# # 测试代码
# import pandas as pd
# import numpy as np
# from sklearn.decomposition import dict_learning


# # dict_from_csv = pd.read_csv(
# #     'students_data.csv', header=None, index_col=0, squeeze=True).to_dict()
# dict_from_csv = {'name': ['fan', 'li', 'liu'], 'id': [3, 2201350211, 4], 'absenteeism': [0, 0, 0], 'attendance_rate': [0.0, 0.0, 0.0]}
# pd.DataFrame(dict_from_csv).to_csv('students_data_convert.csv')
# dict_from_csv = pd.read_csv('students_data_convert.csv').to_dict()
# # dict_from_csv['name'].append(input('wu'))
# list_dict_from_csv = list(dict_from_csv['id'].values())
# print(list_dict_from_csv.index(2201350211))

# # pd.DataFrame(dict_from_csv).to_csv('students_data_convert.csv')
