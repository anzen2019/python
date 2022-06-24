"""
1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой
папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp
"""
import os
main_dir = 'my_project'
if not os.path.exists(main_dir):
    os.mkdir(main_dir)

os.chdir(main_dir) #перешли в папку my_project
other_paths = ['settings', 'mainapp', 'adminapp', 'authapp']
for i in range(len(other_paths)):
    if not os.path.exists(other_paths[i]):
        os.mkdir(other_paths[i])





