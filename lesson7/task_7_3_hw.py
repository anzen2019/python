"""3. Создать структуру файлов и папок, как написано в задании 2
(при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает
все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание,
что html-файлы расположены в родительских папках (они играют роль пространств имён);
предусмотреть возможные исключительные ситуации; это реальная задача,
которая решена, например, во фреймворке django."""
import os
import shutil

main_dir = 'my_project'
if os.path.exists(main_dir): #перешли в папку my_project
    os.chdir(main_dir)

tmp_dir = 'templates'
if not os.path.exists(tmp_dir):
    os.mkdir(tmp_dir) #создали папку tamplates

#создание файлов base, index в my_project
file_base = 'base.html'
if not os.path.exists(file_base):
    file = open(file_base, 'w')
    file.close()
file_index = 'index.html'
if not os.path.exists(file_index):
    file = open(file_index, 'w')
    file.close()
#скопировалиайлы в папку authapp
shutil.copy2('index.html', 'authapp/index.html')
shutil.copy2('base.html', 'authapp/base.html')

#переместили файлы в папку mainapp, чтобы их потом не удалять
os.replace("index.html", "mainapp/index.html")
os.replace("base.html", "mainapp/base.html")

#переместили папки с файлами в templates
os.replace("authapp", "templates/authapp")
os.replace("mainapp", "templates/mainapp")







