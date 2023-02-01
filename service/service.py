#!/usr/bin/python3
# coding: utf-8

from repository.postgres_repository import Database

DB = 'virtual_soccer'
TABLE = 'matches'

db = Database(DB)


def get_matches(cup=None, match_date=None):
    sql = f"""SELECT * FROM {TABLE}"""
    if cup or match_date:
        sql = sql + """ WHERE"""
        if cup and not match_date:
            sql = sql + f""" cup = '{cup}'"""
        elif match_date and not cup:
            sql = sql + f""" match_datetime >= '{match_date} 00:00:00' AND match_datetime <= '{match_date} 23:59:59'"""
        else:
            sql = sql + f""" cup = '{cup}'"""
            sql = sql + f""" AND"""
            sql = sql + f""" match_datetime >= '{match_date} 00:00:00' AND match_datetime <= '{match_date} 23:59:59'"""
    sql = sql + ' ORDER BY match_datetime DESC'
    return db.query(sql)
