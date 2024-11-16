import argparse
import struct
import yaml

# Определение опкодов для команд
OPCODES = {
    11: 'LOAD_CONST',
    7: 'LOAD_MEM',
    21: 'STORE_MEM',
    59: 'MUL'
}

MEMORY_SIZE = 256  # Размер памяти УВМ

def interpreter(binary_file, memory_range_start, memory_range_end, result_file):
    with open(binary_file, 'rb') as f:
        bytecode = f.read()

    memory = [0] * MEMORY_SIZE
    stack = []
    pc = 0  # Счетчик команд

    while pc < len(bytecode):
        opcode = bytecode[pc]
        pc += 1

        instruction = OPCODES.get(opcode)
        if instruction is None:
            raise ValueError(f'Неизвестный опкод: {opcode}')

        if instruction == 'LOAD_CONST':
            # Читаем следующий 4-байтовый аргумент
            value = struct.unpack('>I', bytecode[pc:pc+4])[0]
            pc += 4
            stack.append(value)
        elif instruction == 'LOAD_MEM':
            if not stack:
                raise ValueError('Стек пуст при выполнении LOAD_MEM')
            address = stack.pop()
            if address < 0 or address >= MEMORY_SIZE:
                raise ValueError(f'Неверный адрес памяти: {address}')
            value = memory[address]
            stack.append(value)
        elif instruction == 'STORE_MEM':
            if len(stack) < 2:
                raise ValueError('Недостаточно элементов в стеке для STORE_MEM')
            value = stack.pop()
            address = stack.pop()
            if address < 0 or address >= MEMORY_SIZE:
                raise ValueError(f'Неверный адрес памяти: {address}')
            memory[address] = value
        elif instruction == 'MUL':
            # Читаем следующий 4-байтовый аргумент (смещение)
            offset = struct.unpack('>I', bytecode[pc:pc+4])[0]
            pc += 4
            if len(stack) < 3:
                raise ValueError('Недостаточно элементов в стеке для MUL')
            addr_result = stack.pop()
            operand2 = stack.pop()
            addr_operand1 = stack.pop() + offset
            if addr_operand1 < 0 or addr_operand1 >= MEMORY_SIZE:
                raise ValueError(f'Неверный адрес операнда 1: {addr_operand1}')
            operand1 = memory[addr_operand1]
            result = operand1 * operand2
            if addr_result < 0 or addr_result >= MEMORY_SIZE:
                raise ValueError(f'Неверный адрес для результата: {addr_result}')
            memory[addr_result] = result
        else:
            raise ValueError(f'Неизвестная инструкция: {instruction}')

    # Сохраняем указанный диапазон памяти в файл result.yaml
    memory_slice = memory[memory_range_start:memory_range_end+1]
    with open(result_file, 'w') as f:
        yaml.dump(memory_slice, f, allow_unicode=True)

def main():
    parser = argparse.ArgumentParser(description='Interpreter for UVM.')
    parser.add_argument('--binary', required=True, help='Входной бинарный файл.')
    parser.add_argument('--memory_range', type=int, nargs=2, required=True, help='Диапазон памяти для сохранения.')
    parser.add_argument('--result', required=True, help='Файл для сохранения результата в формате YAML.')
    args = parser.parse_args()

    interpreter(args.binary, args.memory_range[0], args.memory_range[1], args.result)

if __name__ == '__main__':
    main()
