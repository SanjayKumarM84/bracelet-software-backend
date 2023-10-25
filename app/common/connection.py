
import traceback

from sqlalchemy import text

from config import *


def add_item(obj):
    try:
        db.session.add(obj)
        db.session.commit()
        return obj
    except:
        print(traceback.print_exc())
        return None


def add_all(obj):
    try:
        db.session.add_all(obj)
        db.session.commit()
        return obj
    except Exception as ex:
        print(traceback.print_exc())
        return None


def get_item(*args):
    try:
        result = db.session.query(*args)
        return result
    except Exception as err:
        print(traceback.print_exc())
        return None


def update_item(obj):
    try:
        db.session.commit()
        return obj
    except Exception as err:
        print(traceback.print_exc())
        return None


def delete_item(obj):
    try:
        db.session.delete(obj)
        db.session.commit()
        return obj
    except Exception as err:
        print(traceback.print_exc())
        return None


def raw_select(sql):
    try:
        result_proxy = raw_execution(sql)
        result = []
        for row in result_proxy:
            row_as_dict = dict(row)
            result.append(row_as_dict)
        result_proxy.close()
        return result
    except Exception as err:
        print(traceback.print_exc())
        return []


def raw_execution(sql):
    try:
        result = db.engine.execute(text(sql).execution_options(autocommit=True))
        return result
    except Exception as err:
        print(traceback.print_exc())
        return []


def get_count(sql):
    try:
        result = db.engine.execute(sql)
        if result:
            one_row = result.fetchone()
            return one_row[0]
        return None
    except Exception as err:
        print(traceback.print_exc())
        return None


def query_list_to_dict(obj):
    result = {}
    for key in obj.__mapper__.c.keys():
        result[key] = getattr(obj, key)
    return result