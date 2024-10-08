**Измерение температуры, влажности, TDS и EC**

![Stars](https://img.shields.io/github/stars/ivan-rudakov/telegram_tds_notificator?style=flat-square)
![Forks](https://img.shields.io/github/forks/ivan-rudakov/telegram_tds_notificator?style=flat-square)
![Watchers](https://img.shields.io/github/watchers/ivan-rudakov/telegram_tds_notificator?style=flat-square)

Описание проекта:

Этот проект предназначен для измерения температуры, влажности, уровня TDS (общего содержания растворенных твердых веществ) и электрической проводимости (EC) с использованием датчиков DHT11 и TDS. Программа собирает данные с помощью этих датчиков, сохраняет их в очередях фиксированного размера и выводит усредненные значения измерений.

Основные компоненты:

DHT11: Датчик температуры и влажности
TDS-сенсор: Датчик для измерения TDS и EC (подключен через I2C)
Данные сохраняются в очередях с фиксированной длиной для сглаживания измерений. Средние значения рассчитываются и возвращаются через функцию get_values().

Компоненты
DHT11: Датчик температуры и влажности.
TDS-сенсор: Датчик для измерения уровня TDS и электрической проводимости (EC).
pyiArduinoI2Ctds: Библиотека для взаимодействия с TDS-сенсором по протоколу I2C.
Adafruit DHT: Библиотека для работы с датчиком DHT11.
Зависимости
Для работы проекта необходимо установить следующие зависимости:

Adafruit CircuitPython DHT:
```bash
pip install -r requirements.txt
```

Основные файлы
main.py: Основной файл, содержащий логику сбора данных с датчиков.
telegram_bot.py: Файл, предназначенный для работы с телеграм ботом.
README.md: Описание проекта и инструкций по запуску.

Логика работы
Инициализация датчиков:

DHT11 подключен к GPIO на Raspberry Pi (используется пин D4).
TDS-сенсор подключен через I2C-интерфейс.

Сбор данных:

Температура и влажность считываются с датчика DHT11.
TDS и EC считываются с TDS-сенсора с учетом текущей температуры.

Очереди данных:

Используются очереди фиксированного размера для хранения последних 10 измерений температуры, влажности, TDS и EC.
Очереди обновляются каждую секунду.
Вывод данных:

Программа выводит последние значения измерений в реальном времени.
Функция get_values() возвращает усредненные значения температуры, влажности, TDS и EC.
Запуск проекта
Подключите датчики к вашей системе (например, Raspberry Pi).

Убедитесь, что все зависимости установлены.

Запустите основной файл:

```bash
python main.py
```
Программа будет собирать данные и выводить их в консоль.

Примечания
Если датчики не подключены или возникают ошибки при измерении, возвращаемые значения будут по умолчанию установлены в -1.
При отсутствии температурных данных температура устанавливается в 20°C по умолчанию, чтобы обеспечить корректную работу TDS-сенсора.
