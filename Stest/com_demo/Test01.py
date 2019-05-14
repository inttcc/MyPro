#!/usr/bin/env python 
# -*- coding:utf-8 -*-
employee = {}


def show_menu():
    print('*' * 20 + '欢迎登录员工管理系统' + '*' * 20)
    print('1.新增员工信息')
    print('2.删除员工信息')
    print('3.修改员工信息')
    print('4.查看员工信息')
    print('5.退出管理系统')
    print('*' * 56)


def employee_add():
    employee_id = input('请输入员工编号：')
    all_employee_id = list(employee.keys())
    if employee_id in all_employee_id:
        print('员工编号重复，添加失败')
        return
    employee_name = input('请输入员工姓名：')
    employee_sex = input('请输入员工性别：')
    employee_salary = input('请输入员工薪资：')
    employee_info = {'name': employee_name, 'sex': employee_sex, 'salary': employee_salary}
    employee[employee_id] = employee_info
    print('员工编号为%s的员工添加成功' % employee_id)


def employee_remove():
    employee_id = input('请输入要删除的员工编号：')
    all_employee_id = list(employee.keys())
    if employee_id not in all_employee_id:
        print('员工编号不存在，删除失败')
        return
    del employee[employee_id]
    print('员工编号为%s的员工删除成功' % employee_id)

def employee_edit():
    employee_id = input('请输入要修改的员工编号：')
    all_employee_id = list(employee.keys())
    if employee_id not in all_employee_id:
        print('员工编号不存在，修改失败')
        return
    new_employee_name = input('姓名是s%，您要修改为：'%employee[employee_id]['name'])
    new_employee_name = input('姓名是s%，您要修改为：'%employee[employee_id]['name'])
    new_employee_name = input('姓名是s%，您要修改为：'%employee[employee_id]['name'])
    employee_info = {'name': employee_name, 'sex': employee_sex, 'salary': employee_salary}
    employee[employee_id] = employee_info
    print('员工编号为%s的员工删除成功' % employee_id)



while True:
    show_menu()
    choice = input('请输入你的选择：')
    if choice == '1':
        employee_add()
        print(employee)
    elif choice == '2':
        employee_remove()
        print(employee)
    elif choice == '3':
        employee_edit()
        print('修改员工信息')
    elif choice == '4':
        print('查看员工信息')
    elif choice == '5':
        print('退出员工系统')
        break
    else:
        print('您的输入有误！')
