--cоздание контейнера из докерфайла
docker build -t tort .
--посмотреть отработавшие контейнеры
docker ps --filter "status=exited"
--запустить контейнер докера (в дебаг режиме)
docker run -d -p 5000:5000 tort
--остановить контейнер
docker stop <id>
--посмотреть список активных контейнеров
docker container ls
--удалить контейнер
docker rm <id>