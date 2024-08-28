my_dict = {'artem': 2001, 'anton': 2010, 'vova': 1999}
print(my_dict)
print(my_dict.get('anton') )
print(my_dict.get('vana') )
my_dict.update({'lana': 1993, 'alan': 1998})
print(my_dict)
del my_dict['vova']
print(my_dict)