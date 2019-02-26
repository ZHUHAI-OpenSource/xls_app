#!/usr/bin/python3
# --------------------------------------------------
# -*- coding:utf-8 -*-
#
#   @time      :    2019/2/18 16:56
#   @author    :    ZHUHAI.EE
#   @email     :    zhlhwmy_gzh@163.com
#   @file      :    analysis.py
#   @software  :    
#   @version   :      
#   
#  -----------------------------------------------

import xlrd as xl
import pandas as pds
import xlwt as xw
import setting_rule
import read_database
import type_result

# open file


df1 = pds.read_excel('data/table00.xls', sheet_name=0)
df2 = pds.read_excel('data/table00.xls', sheet_name=1)
df3 = pds.read_excel('data/table00.xls', sheet_name=2)

# ------------------------------------------------
#
# main function
# ------------------------------------------------


new_table = []
read_database.trans_table(read_database.t1, new_table, 0)
print(len(new_table))
# 规则词典
rule_file1 = []
setting_rule.read_rule_file(read_database.t2, rule_file1, 0)
tr_table = []
for i in new_table:
    a = list(i[3])
    a = [str(j) for j in a]
    a = ''.join(a)
    for m in rule_file1:
        rule_cell = list(m[0])
        obj_cell = m[1]
        rule_cell = [str(i) for i in rule_cell]
        rule_cell = ''.join(rule_cell)
        if rule_cell == a:
            del i[3]
            t = list(obj_cell)
            i.insert(3, t[0])
            i.insert(4, t[1])

    i = [str(j) for j in i]
    i[0] = i[0].strip(' text:')
    i[3] = i[3].strip('text:')
    i[4] = i[4].strip('text:')
    i[5] = float(i[5].strip('number:'))
    tr_table.append(i)

new_df = pds.DataFrame(tr_table, columns=['name', 'id', 'region', 'type', 'subtype', 'money'])

result_by_people = []
result_by_subtype = []

type_result.deal_data(new_df, new_df['name'], new_df['type'], result_by_people)
type_result.deal_data(new_df, new_df['subtype'], new_df['region'], result_by_subtype)
