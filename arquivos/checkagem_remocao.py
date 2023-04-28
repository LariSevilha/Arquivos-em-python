import os
if os.path.exists('diciplinas.txt'):
    os.remove('diciplinas.txt')
else:
    print('O arquivo não existe')