#!/usr/bin/python3
# --------------------------------------------------
# -*- coding:utf-8 -*-
#
#   @time      :    2019/2/18 12:56
#   @author    :    ZHUHAI.EE
#   @email     :    zhlhwmy_gzh@163.com
#   @file      :    get_data.py
#   @software  :    
#   @version   :      
#  -----------------------------------------------
import xlrd as xl
orignal_data = xl.open_workbook('data/table00.xls')
t1 = orignal_data.sheet_by_index(0)
t3 = orignal_data.sheet_by_index(2)
t2 = orignal_data.sheet_by_index(1)


# data transform
# function point: trans. check


def trans_table(_original_t, _new_t, chk):
    key = ()
    key2 = []
    mo = []
    value = []
    t1_rows = _original_t.nrows
    t1_cols = _original_t.ncols
    name = [t1_rows]
    id = [t1_rows]
    area = [t1_rows]
    type = [t1_rows]
    new_data = []
    for i in range(1, t1_rows):
        name.append(t1.cell(i, 0))
        id.append(t1.cell(i, 1))
        area.append(t1.cell(i, 2))
        type.append(t1.cell(i, 4))
        key = (name[i], id[i], area[i], type[i])
        for j in range(0, 10):
            key2.append(key)

        for j in range(0, 10):
            value.append((t1.cell(0, j + 5), t1.cell(i, j + 5)))
        len_key = len(key2)
        len_value = len(value)

    for n in range(len_key):

        key2[n] = list((key2[n] + value[n]))
        x = key2[n]
        x[4] = (x[3], x[4])
        del x[3]
        _new_t.append(key2[n])
        if chk == 1:
            print('check t', i, n, _new_t[n])