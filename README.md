# Документация API для управления пользователями

## Введение
Это API предоставляет возможность управления пользователями. С помощью этого API можно получать информацию о пользователях, создавать новых пользователей, обновлять их данные и удалять существующих.

## Модель пользователя
```python
class User(BaseModel):
    id: int
    username: str
    wallet: float
    birthdate: date
```

## Модель пользователя
Модель User представляет пользователя приложения и содержит следующие поля:

- `id`: уникальный идентификатор пользователя (int).
- `username`: имя пользователя (str).
- `wallet`: баланс пользователя (float).
- `birthdate`: дата рождения пользователя (date).

## Эндпоинты

### Получение списка всех пользователей
- **Метод:** GET
- **Путь:** `/users/`
- **Возвращаемый тип данных:** список пользователей `List[User]`
- **Описание:** Этот эндпоинт возвращает список всех пользователей приложения.

### Получение пользователя по его ID
- **Метод:** GET
- **Путь:** `/users/{user_id}`
- **Входные параметры:** `user_id` (int) — идентификатор пользователя.
- **Возвращаемый тип данных:** пользователь (`User`)
- **Описание:** Этот эндпоинт возвращает информацию о пользователе по его уникальному идентификатору.

### Создание нового пользователя
- **Метод:** POST
- **Путь:** `/users/`
- **Тело запроса:** данные нового пользователя (`User`)
- **Возвращаемый тип данных:** пользователь (`User`)
- **Описание:** Этот эндпоинт создает нового пользователя на основе предоставленных данных.

### Обновление данных пользователя
- **Метод:** PUT
- **Путь:** `/users/{user_id}`
- **Входные параметры:** `user_id` (int) – идентификатор пользователя.
- **Тело запроса:** обновленные данные пользователя (`User`)
- **Возвращаемый тип данных:** пользователь (`User`)
- **Описание:** Этот эндпоинт обновляет данные пользователя на основе предоставленных данных.

### Удаление пользователя по его ID
- **Метод:** DELETE
- **Путь:** `/users/{user_id}`
- **Входные параметры:** `user_id` (int) — идентификатор пользователя.
- **Возвращаемый тип данных:** сообщение
- **Описание:** Этот эндпоинт удаляет пользователя из приложения по его уникальному идентификатору.

### Примеры запросов и ответов

#### Получение списка всех пользователей

**Запрос:**
GET /users/


**Ответ:**
```json
[
    {"id": 1, "username": "user1", "wallet": 100.0, "birthdate": "1990-1-1"},
    {"id": 2, "username": "user2", "wallet": 200.0, "birthdate": "1995-5-15"}
]
```
### Получение пользователя по его ID
**Запрос:**
GET /users/1

**Ответ:**
```json
{
    "id": 1,
    "username": "user1",
    "wallet": 100.0,
    "birthdate": "1990-1-1"
}
```
### Создание нового пользователя
**Запрос:**
POST /users/

**Тело запроса:**
```json
{
    "id": 3,
    "username": "user3",
    "wallet": 150.0,
    "birthdate": "1988-10-10"
}

```


**Ответ:**
```json
{
    "id": 3,
    "username": "user3",
    "wallet": 150.0,
    "birthdate": "1988-10-10"
}

```

### Обновление данных пользователя

**Запрос:**
PUT /users/3

**Тело запроса:**
```json
{
    "id": 3,
    "username": "updated_user3",
    "wallet": 200.0,
    "birthdate": "1988-10-10"
}

```
**Ответ:**

```json
{
    "id": 3,
    "username": "updated_user3",
    "wallet": 200.0,
    "birthdate": "1988-10-10"
}

```
### Удаление пользователя по его ID

**Запрос:**
DELETE /users/3

**Ответ:**
```json
{"message": "Пользователь удален!"}

```

## Ошибки

При возникновении ошибок сервер возвращает соответствующий HTTP статус-код и сообщение об ошибке в формате JSON.

### Статус код 404: Пользователь не найден

**Пример ответа:**
```json
{
    "detail": "Пользователь не найден"
}
```
### Статус код 400: Неверный запрос

**Пример ответа:**
```json
{
    "detail": "Неверный запрос"
}

```
### Статус код 500: Внутренняя ошибка сервера

**Пример ответа:**

```json
{
    "detail": "Внутренняя ошибка сервера"
}

```


