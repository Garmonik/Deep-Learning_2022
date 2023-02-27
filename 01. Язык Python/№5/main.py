def process(strings):
    result = []
    for string in strings:
        s = string.split()
        result.append(' '.join([x for x in s if x.isalpha()]))
    return result
