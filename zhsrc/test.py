#!/usr/bin/python3
# --------------------------------------------------
# -*- coding:utf-8 -*-
#
#   @time      :    2019/2/20 8:17
#   @author    :    ZHUHAI.EE
#   @email     :    zhlhwmy_gzh@163.com
#   @file      :    test.py
#   @software  :    
#   @version   :      
#  -----------------------------------------------
import pandas as pds

import analysis
import xlwt as xw
result_by_people = analysis.result_by_people
result_by_subtype = analysis.result_by_subtype


def check_result(_sheet):
    ff = xw.Workbook()
    a = ff.add_sheet(_sheet)
    for i in range(len(result_by_people)):
        a.write(i, 1, str(result_by_people[i][0]))
        for j in range(len(result_by_people[i][1])):
            a.write(i, j + 2, float(str(result_by_people[i][1][j])))

    for i in range(len(result_by_subtype)):
        a.write(i + 1+ len(result_by_people), 1, str(result_by_subtype[i][0]))
        for j in range(len(result_by_subtype[i][1])):
            a.write(i + 1+ len(result_by_people),
                    j + 2, float(str(result_by_subtype[i][1][j])))

    print(len(result_by_people))
    print(len(result_by_subtype))
    ff.save('data/分类结果.xls')

check_result('口径1')