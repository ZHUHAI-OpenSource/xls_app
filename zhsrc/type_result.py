#!/usr/bin/python3
# --------------------------------------------------
# -*- coding:utf-8 -*-
#
#   @time      :    2019/2/22 2:43
#   @author    :    ZHUHAI.EE
#   @email     :    zhlhwmy_gzh@163.com
#   @file      :    type_result.py
#   @software  :    
#   @version   :      
#  -----------------------------------------------
import pandas as pds


def deal_data(_new_df, _df, _df_2, _result_by_people):
    _list = list(_df)
    c = []
    for i in pds.Series(_list).unique():
        new_df_0 = _new_df[_df == i]
        b = list(new_df_0['money'].groupby(_df_2).sum())
        b = (i, b)
        b = list(b)
        _result_by_people.append(b)