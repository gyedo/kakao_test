def test1(arr1, arr2):
    return [ y.replace('1', '#').replace('0', ' ') for y in ["{0:b}".format(x) for x in map(lambda (a,b):a|b, zip(arr1, arr2))]]
