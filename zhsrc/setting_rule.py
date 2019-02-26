#!/usr/bin/python3
# --------------------------------------------------
# -*- coding:utf-8 -*-
#
#   @time      :    2019/2/22 04:35
#   @author    :    ZHUHAI.EE
#   @email     :    zhlhwmy_gzh@163.com
#   @file      :    setting_rule.py
#   @software  :    
#   @version   :      
#  -----------------------------------------------


def read_rule_file(_org_sheet, _rule_dict, chk):
    t2_rows = _org_sheet.nrows
    key = []
    value = []
    for i in range(2, t2_rows):
        key.append((_org_sheet.cell(i, 0), _org_sheet.cell(i, 1)))
        value.append((_org_sheet.cell(i, 2), _org_sheet.cell(i, 3)))

    rule_dict = list(zip(key, value))

    for k in range(len(rule_dict)):
        rule_dict[k] = list(rule_dict[k])
        _rule_dict.append(rule_dict[k])
        if chk == 1:
            print('chk table-->', k, _rule_dict[k])