# Speech_cleaner
<b> В данном репозитории представлен веб-сервис, позволяющий чистить записанное аудио от постороннего шума. Чтобы запустить сервис: </b> <br>
Склонируйте репрзиторий еа свой ПК следующей командой: <br>
<code> git clone https://github.com/alexmackfi/speech_denoise.git </code> <br>
Перейдите в папку с проектом:<br>
<code> cd Speech_cleaner </code><br>
Создайте виртуальное окружение:<br>
<code> source venv/bin/activate </code><br>
Если у вас Windows эта команда будет выглядеть так:<br>
<code> source venv/Scripts/activate </code><br>
После установите необходимые для работы библиотеки:<br>
<code> pip install -r requirements.txt </code><br>
Запустите файл wsgi.py и радостно пользуйтесь сервером:<br>
<code> python wsgi.py </code><br><br>

<b>Также запустить сервис можно при помощи технологии Docker:</b><br><br>
Склонируйте репрзиторий еа свой ПК следующей командой: <br>
<code> git clone https://github.com/alexmackfi/speech_denoise.git </code> <br>
Перейдите в папку с проектом:<br>
<code> cd Speech_cleaner </code><br>
Выполните следующую послеловотельность команд: <br>
<code> docker build -t tort . </code><br>
<code> docker run -d -p 8000:8000 tort </code> <br>
Перейдите по ссылке http://localhost:8000 <br>
Если у вас операционная система Windows, то необходимо изменить содержание Dockerfile, раскомментировать строки содержащие в себе значение <b>5000</b> и заомментировать строки содержащие <b>8000</b>:<br>
Тогда команды изменятся соответственно:<br>
<code> docker run -d -p 5000:5000 tort </code> <br>
Перейдите по ссылке http://localhost:5000 
