# 1  Создаем виртуальное окружение при помощи комадны python3 -m venv venv 

# 2 устанавливаем нужные библиотеки и джанго при помощ команды pip install 

# 3 создаем дирикторию проекта и файл manage.py при помощи команды django-admin startproject . 

# 4 создаем приложение для проекта где у нас будет вся логика создаем python3 manage.py startapp <name> , django-admin startapp <name>

#5 закинуть в настройках installed apps

# 6 работать с проектом 

# проведение миграций 
# 1 создает файлы миграции python3 makeemigrations 

#2 исполняются наши файлы миграции (измение базы данных)

# cоздание суперюзера - python3 manage.py createsuperuser