# for i in range(10):
#     value = i/100
#     my_string = 'The value {} was in my loop'.format(value)
#     print(my_string)


def make_average(x, y):
    arithm_avg = (x+y)/2
    geom_avg = (x*y)**.5
    return arithm_avg

avg = make_average(3, 4)
print(avg)
print(geom_avg)