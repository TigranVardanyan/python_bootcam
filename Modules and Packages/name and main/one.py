#one.py

def func():
    print('Func() in one.py')

print('TOP LEVEL IN ONE.PY')

if __name__ == '__main__':
    print('One.py run directly')
else:
    print("One.py has been imported")