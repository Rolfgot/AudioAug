# AudioAug

Консольное приложения для аугментации аудиофайла формата wav

## Установка

Для инициализации виртуальной среды необходимо ввести команды:

```commandline
python -m venv venv
venv\Scripts\activate
```

И необходимо поставить следующие библиотеки:

```commandline
pip install numpy, scipy, pyyaml, soundfile
```

## Запуск

Для запуска необходимо запустить команду в консоли в папке проекта:

```commandline
python main.py --config_path=config.yml --file_path=test.wav
```

## Конфигурация

В файле config.yml есть значения параметров аугментации