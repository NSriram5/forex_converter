from forex_python.converter import CurrencyRates, CurrencyCodes
import forex_python.converter
currency_symbols = CurrencyCodes()
currency_rates = CurrencyRates()

def convert(cur_from,cur_to,amount):
    '''
    Converts a currency from one unit to another or retuns a list of errors in string format
    >>> convert('USD','USD',5)
    '5.00 $'
    '''
    errors = []
    try:
        rates_dict = currency_rates.get_rates(cur_from)
    except forex_python.converter.RatesNotAvailableError:
        errors.append(f'{cur_from} is not a valid currency code')
    end_unit = currency_symbols.get_symbol(cur_to)
    if end_unit == None:
        errors.append(f'{cur_to} is not a valid currency code')
    try:
        amount = float(amount)
    except:
        errors.append(f'{amount} is not a valid currency amount')
    if len(errors)>0:
        return errors
    try:
        result = round(amount * rates_dict[cur_to],2)
    except:
        return ['Currency conversion failed']
    return f'{result} {end_unit}'