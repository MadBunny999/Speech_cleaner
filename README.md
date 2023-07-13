# Speech_cleaner
<b> В данном репозитории представлен веб-сервис, позволяющий чистить записанное аудио от постороннего шума. Чтобы запустить сервис: </b>
Склонируйте репрзиторий еа свой ПК следующей командой:
<code> git clone https://github.com/alexmackfi/speech_denoise.git </code>
Перейдите в папку с проектом:
<code> cd Speech_cleaner </code>
Создайте виртуальное окружение:
<code> source venv/bin/activate </code>
Если у вас Windows эта команда будет выглядеть так:
<code> source venv/Scripts/activate </code>
После установите необходимые для работы библиотеки:
<code> pip install -r requirements.txt </code>
Запустите файл wsgi.py и радостно пользуйтесь сервером:
<code> python wsgi.py </code>

Чтобы запустить докер выполните следующие команды:
<code> git clone https://github.com/alexmackfi/speech_denoise.git </code>
<code> cd Speech_denoise </code>
<code> docker build -t tort . </code>
<code> docker run -d -p 8000:8000 tort </code>
Перейдите по ссылке http://localhost:8000 

<code> docker run -d -p 5000:5000 tort </code> 
http://localhost:5000 для Windows) Описание проведенных экспериментов находится в папке trainig.
