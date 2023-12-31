# Backend Test Task ✅

## Tools

1. Python
2. FastAPI
3. Selenium
4. Docker

## Задача

Необходимо написать API, в котором будет следующий endpoint:

1. **/getPhotos (username: str, max_count: int)** - возвращает ссылки на фотографии из instagram аккаунтов
    1. Данный endpoint должен обрабатывать N запросов параллельно
    2. Возвращает ответ в следующем формате:
    
    ```json
    {
    	"urls": [] // ссылки на фотографии
    }
    ```
    

## Требования

1. Решение должно запускаться одной командой
    
    ```bash
    docker compose up
    ```
    
2. Решение должно поддерживать параллельную работу
3. Структура репозитория:
    
    ```json
    .
    - main.py // скрипт, который запускает RestAPI 0.0.0.0:8080
    - build.sh // билдит докер образ
    - requirements.txt
    - docker
    	- docker-compose.yaml
    	- Dockerfile
    - routers
    	- __init__.py
    	- instagram.py // тут должен быть роутер для /getPhotos
    - dependencies.py // тут вы можете хранить нужные для вас функции
    ```
    

### **Требования**

- Самое главное это - рабочий код, залитый на github
- Также важно умение объяснить то, как работает этот код
- Можно использовать все, что угодно: любые открытые репозитории, материалы (⚠️но обязательно использование selenium / playwright)

## Лицензия

MIT
