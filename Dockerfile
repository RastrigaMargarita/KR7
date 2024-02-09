# Используем базовый образ Python
FROM python:3

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем зависимости в контейнер
COPY ./requirements.txt .

# Устанавливаем зависимости
RUN pip install --use-pep517 --no-cache-dir -r requirements.txt

# Копируем код приложения в контейнер
COPY . .

