# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
import uuid
import datetime as dt
import dateutil.parser
import time

def serialize_object(inst, cls, **kwargs):
    serialized = {}
    for name, value in kwargs.items():
        if repr(value)[0:7] == 'Decimal':
            serialized[name] = value
        else:
            try:
                serialized[name] = [x.serialized if x else None for x in value]
            except (AttributeError, TypeError) as e:
                # print(e, 'BAD ERROR')
                try:
                    serialized[name] = value
                except Exception as e:
                    print(e)

    for column in cls.__table__.columns:
        attribute = getattr(inst, column.name)
        if isinstance(attribute, dt.datetime):
            serialized[column.name] = attribute.isoformat()                
        elif isinstance(attribute, dt.date):
            serialized[column.name] = attribute.isoformat()
        elif repr(attribute)[0:7] == 'Decimal':
            serialized[column.name] = float(attribute)
        elif isinstance(attribute, (bytes, bytearray)):
            pass
        elif isinstance(attribute, uuid.UUID):
            serialized[column.name] = str(attribute)
        else:
            try:
                serialized[column.name] = attribute
            except:
                serialized[column.name] = str(repr(attribute))
    return serialized


def try_parsing_date(text, end_of_day=False, start_of_day=False, convert_from_utc=False):
    if not text or text == 'Invalid date':
        return None
    parsed_date = None
    for fmt in ('%Y-%m-%d %H:%M', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d', 
                '%-m/%-d/%Y', '%m/%d/%Y', '%m/%d/%Y %H:%M:%S', '%-m/%-d/%Y %H:%M:%S', '%m/%d/%Y, %I:%M %p', '%m/%d/%Y, %I:%M:%S %p', '%Y-%m-%dT%H:%M:%S', '%Y-%m-%dT%H:%M:%S.%f'):
        try:
            parsed_date = dt.datetime.strptime(text, fmt)
        except ValueError:
            pass
    if not parsed_date:
        parsed_date = dateutil.parser.parse(text) + dt.timedelta(seconds=time.localtime().tm_gmtoff)
    
    if convert_from_utc:
        parsed_date = parsed_date + dt.timedelta(seconds=time.localtime().tm_gmtoff)
    if end_of_day:
        return dt.datetime(parsed_date.year, parsed_date.month, parsed_date.day, 23, 59, 59, 999999)
    if start_of_day:
        return dt.datetime(parsed_date.year, parsed_date.month, parsed_date.day, 0, 0, 0, 0)
    
    return parsed_date

