#!/usr/bin/python
# -*- coding: utf-8 -*-

import CVSReader
# import openpyxl
from os import path

class WageReader:

    wage_file = ""
    reader = None

    def __init__(self, filename):
        if not path.exists(filename) :
            raise Exception(u"错误, 工资文件不存在!\n")
        self.wage_file = filename

    def read_csv(self):
        rows = []
        key = None
        with open(self.wage_file, 'r') as fid:
            f = CVSReader.UnicodeReader(fid)
            for row in f:
                if key is None:
                    key = row
                else:
                    rows.append(dict(zip(key, row)))
        return rows

    def read_xls(self):
        # wb = openpyxl.load_workbook(self.wage_file)
        # print wb.get_sheet_names()
        pass

    def read_rows(self):
        filename, fileext = path.splitext(self.wage_file)
        if fileext.lower() == ".csv":
            return self.read_csv()
        elif fileext.lower() == ".xlsx" or fileext.lower() == ".xls":
            # return self.read_xls()
            print (u"错误, 暂时只支持.csv格式的工资, 请在excel中另存为.csv格式\n")
            return None
        else:
            print (u"错误, 暂时只支持.csv格式的工资, 请在excel中另存为.csv格式\n")
            return None
            # raise Exception(u"错误, 工资文件应该是.csv / .xls / .xlsx中的一种!\n")