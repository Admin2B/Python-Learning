from collections import namedtuple


User=namedtuple('User',['name','age','height'])
user=User(name='bobby',age=29,height=175)
print(user.name,user.age,user.height)