class school():
    les1 = 'Math'
class monday(school):
    les2 = 'geography'
class tuesday(monday):
    les3 = 'history'
class lessons(tuesday):
    pass
copy = lessons()
print('Сегодня у вас:', copy.les1,',', copy.les2, ',', copy.les3)