def formatMoney(value):
    value = float(value.replace(',', '.')) if isinstance(value, str) else float(value)
    value = str(round(value, 2))
    split = value.split('.')
    intValue = value.split('.')[0]
    aux = ''
    if len(intValue) > 3:
        intValue = intValue[::-1]
        for i in range(0, len(intValue), 3):
            aux += intValue[i:i + 3] + '.' if i + 3 < len(intValue) else intValue[i:i + 3]
        aux = aux[::-1]
        intValue = aux
    if len(split) == 2:
        floatValue = value.split('.')[1]
        if len(floatValue) == 1:
            floatValue += '0'
        return '{},{}'.format(intValue, floatValue)
    else:
        return '{},00'.format(intValue)

def getNumber(entities):
    if entities:
        numbers = list(filter(lambda entity: entity['entity'] == 'number', entities))
        if numbers:
            return numbers[0]['value']
        else:
            return 0
    else:
        return 0

def getFlavor(entities):
    if entities:
        flavors = list(filter(lambda entity: entity['entity'] == 'sabor', entities))
        if flavors:
            return flavors[0]['value']
        else:
            return None
    else:
        return None