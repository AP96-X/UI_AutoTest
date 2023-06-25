#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：Platform2.0_API_Auto_Test
@File    ：mysql_tools.py
@IDE     ：PyCharm
@Author  ：Pan Junmeng
@Date    ：2023/3/10 15:22
"""

import pymysql
from Utils.read_yaml import read_data

"""
安装pymysql模块
获得数据库连接
查询数据
删除数据
"""
db_data = read_data.load_config('db.yaml')


class MYSQL:
    def __init__(self, database):
        self.user = db_data[f'{database}']['username']
        self.passwd = db_data[f'{database}']['password']
        self.host = db_data[f'{database}']['host']
        self.port = db_data[f'{database}']['port']
        self.db = db_data[f'{database}']['db']
        self.conn = pymysql.connect(
            user=self.user,
            passwd=self.passwd,
            host=self.host,
            port=int(self.port),
            db=self.db,
        )
        self.cursor = self.conn.cursor()

    def select_sql(self, sql_str):
        try:
            self.cursor.execute(sql_str)
            all_data = self.cursor.fetchall()
            return all_data
        except Exception as e:
            print(e)
            # finally:
            self.cursor.close()  # 关闭游标
            self.conn.close()  # 关闭数据库连接

    def delete_sql(self, sql_str):
        try:
            self.cursor.execute(sql_str)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(e)
            # finally:
            self.cursor.close()
            self.conn.close()


if __name__ == '__main__':
    print(MYSQL('cowin_standard').select_sql('SELECT STANDARD_ID FROM standard WHERE STANDARD_NAME = "国家标准";'))
    print(
        MYSQL('cowin_standard').select_sql('SELECT STANDARD_ID FROM standard WHERE STANDARD_NAME = "国家标准";')[0][0])
    print(
        MYSQL('cowin_dataservice').select_sql("SELECT COUNT(*) FROM service_info WHERE not SERVICE_STATUS = 'CREATE';"))
    print(
        MYSQL('cowin_dataservice').select_sql("SELECT COUNT(*) FROM service_info WHERE not SERVICE_STATUS = 'CREATE';")[
            0][0])
