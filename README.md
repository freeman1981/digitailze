## Что бы как-то проще было делать уроки

### поднимаем окружение
```sh
docker-compose up --build
```

### подключаемся к контейнеру
```sh
docker exec -it learn_bash bash
```

### Дальше переходим в директорию нужного урока и экспериментируем
```sh
root@4bbaec98fda0:/usr/src/app# cd lesson<...>
```

### lesson4.29.3

```bash
cd lesson4/
ls -lR
su - sterx
cd /usr/src/app/lesson4
ls -lR # Ага!
```
