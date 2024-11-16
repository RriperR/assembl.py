import argparse
import yaml
import struct

# Определение опкодов для команд
OPCODES = {
    'LOAD_CONST': 11,
    'LOAD_MEM': 7,
    'STORE_MEM': 21,
    'MUL': 59
}

def parse_instruction(line):
    parts = line.strip().split()
    if not parts:
        return None, None
    instruction = parts[0]
    args = parts[1:] if len(parts) > 1 else []
    return instruction, args

def assemble(input_file, output_file, log_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    binary_code = bytearray()
    log = []

    for line in lines:
        instruction, args = parse_instruction(line)
        if instruction is None:
            continue  # Пустая строка или комментарий
        opcode = OPCODES.get(instruction)
        if opcode is None:
            raise ValueError(f'Неизвестная инструкция: {instruction}')

        # Добавляем опкод в бинарный код
        binary_code.append(opcode)

        # Обрабатываем аргументы
        for arg in args:
            # Преобразуем аргумент в число и записываем как 4 байта (32 бита)
            value = int(arg)
            binary_code.extend(struct.pack('>I', value))

        # Добавляем инструкцию в лог
        log.append({'instruction': instruction, 'args': [int(arg) for arg in args]})

    # Сохраняем бинарный файл
    with open(output_file, 'wb') as f:
        f.write(binary_code)

    # Сохраняем лог в YAML формате
    with open(log_file, 'w') as f:
        yaml.dump(log, f, allow_unicode=True)

def main():
    parser = argparse.ArgumentParser(description='Assembler for UVM.')
    parser.add_argument('--input', required=True, help='Входной ASM файл.')
    parser.add_argument('--output', required=True, help='Выходной бинарный файл.')
    parser.add_argument('--log', required=True, help='Лог-файл в формате YAML.')
    args = parser.parse_args()

    assemble(args.input, args.output, args.log)

if __name__ == '__main__':
    main()
