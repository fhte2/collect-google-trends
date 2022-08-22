
def trim_month(month):
    """
    removes leading zeroes from month numbers
    """
    if list(month)[0] == '0':
        return month[1]
    else:
        return month

def check_date(start_year, end_year, start_month, end_month):
    """
    checks if the input dates makes sense
    """
    if end_year < start_year:
        print('End year cannot be smaller than start year. Update the dates and try again.')
        return False
    elif (end_year == start_year ) and (end_month < start_month):
        print('End month cannot be smaller than start month if start and end year are the same. Update the dates and try again.')
        return False
    else: 
        return True