# Ассемблер и Интерпретатор для Учебной Виртуальной Машины (УВМ)

## Общее описание

Данный проект реализует ассемблер и интерпретатор для учебной виртуальной машины (УВМ) на языке Python. УВМ работает с фиксированным размером памяти и поддерживает базовый набор команд для выполнения простых операций.

**Основные возможности:**

- **Ассемблер**: Преобразует текстовые ассемблерные команды в бинарный файл.
- **Интерпретатор**: Выполняет бинарный код, изменяет состояние памяти УВМ и сохраняет результат выполнения.

## Описание функций и настроек

### Ассемблер (`assembler.py`)

**Функции:**

- `assemble(input_file, output_file, log_file)`: Читает ассемблерный код из `input_file`, преобразует его в бинарный код и сохраняет в `output_file`. Также генерирует лог-файл `log_file` в формате YAML.

**Настройки:**

- `--input`: Путь к входному ASM файлу.
- `--output`: Путь к выходному бинарному файлу.
- `--log`: Путь к лог-файлу в формате YAML.

### Интерпретатор (`interpreter.py`)

**Функции:**

- `interpreter(binary_file, memory_range_start, memory_range_end, result_file)`: Выполняет бинарный код из `binary_file`, изменяет состояние памяти, и сохраняет указанный диапазон памяти в `result_file`.

**Настройки:**

- `--binary`: Путь к входному бинарному файлу.
- `--memory_range`: Диапазон памяти для сохранения (начало и конец).
- `--result`: Путь к файлу для сохранения результата в формате YAML.

### Команды УВМ

- `LOAD_CONST <значение>`: Загружает константу на стек.
- `LOAD_MEM`: Загружает значение из памяти по адресу с вершины стека.
- `STORE_MEM`: Сохраняет значение из стека в память по указанному адресу.
- `MUL <смещение>`: Умножает два значения и сохраняет результат в памяти.

## Команды для сборки проекта

1. **Сборка ассемблерного кода:**

   ```bash
   python assembler.py --input source.asm --output program.bin --log log.yaml
   ```
   ```bash
   python interpreter.py --binary program.bin --memory_range 0 11 --result result.yaml
   ```

## Примеры использования
### Пример ассемблерного кода (source.asm)
```commandline
LOAD_CONST 0
LOAD_CONST 1
STORE_MEM
LOAD_CONST 1
LOAD_CONST 2
STORE_MEM
LOAD_CONST 2
LOAD_CONST 3
STORE_MEM
LOAD_CONST 3
LOAD_CONST 4
STORE_MEM
LOAD_CONST 4
LOAD_CONST 5
STORE_MEM
LOAD_CONST 5
LOAD_CONST 6
STORE_MEM
LOAD_CONST 6
LOAD_CONST 6
STORE_MEM
LOAD_CONST 7
LOAD_CONST 5
STORE_MEM
LOAD_CONST 8
LOAD_CONST 4
STORE_MEM
LOAD_CONST 9
LOAD_CONST 3
STORE_MEM
LOAD_CONST 10
LOAD_CONST 2
STORE_MEM
LOAD_CONST 11
LOAD_CONST 1
STORE_MEM
LOAD_CONST 0
LOAD_CONST 6
LOAD_MEM
LOAD_CONST 0
MUL 0
LOAD_CONST 1
LOAD_CONST 7
LOAD_MEM
LOAD_CONST 1
MUL 0
LOAD_CONST 2
LOAD_CONST 8
LOAD_MEM
LOAD_CONST 2
MUL 0
LOAD_CONST 3
LOAD_CONST 9
LOAD_MEM
LOAD_CONST 3
MUL 0
LOAD_CONST 4
LOAD_CONST 10
LOAD_MEM
LOAD_CONST 4
MUL 0
LOAD_CONST 5
LOAD_CONST 11
LOAD_MEM
LOAD_CONST 5
MUL 0
```

## Результаты выполнения
### После выполнения интерпретатора содержимое result.yaml будет следующим:
```yaml
- 6
- 10
- 12
- 12
- 10
- 6
- 6
- 5
- 4
- 3
- 2
```


## Результаты прогона тестов
### Тест 1: Проверка корректности умножения элементов векторов.

#### Ожидаемый результат:

Значения по адресам 0-5 должны быть равны результатам поэлементного умножения соответствующих элементов векторов A и B.
Фактический результат:

Значения соответствуют ожидаемым.
### Тест 2: Проверка сохранения исходных значений векторов.

#### Ожидаемый результат:

Значения по адресам 6-11 должны соответствовать исходному вектору B.
Фактический результат:

Значения соответствуют ожидаемым.