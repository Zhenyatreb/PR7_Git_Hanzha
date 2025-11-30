
print ('hello python')

# 1.(Bubble Sort)
def bubble_sort(array):
    n = len(array)
    # n - 1 проходів
    for pass_num in range(n - 1, 0, -1):
        # Внутрішній цикл проходить до вже відсортованої частини
        for i in range(pass_num):
            # Якщо наступний елемент менший за попередній, міняємо місцями
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]  # Обмін елементів
    
    return array  # Повертаємо відсортований масив (згідно з вимогою завдання)


# 2.(Selection Sort)
def selection_sort(array):
    n = len(array)
    # Зовнішній цикл (кількість проходів)
    for i in range(n - 1, 0, -1):
        # Реалізуємо пошук найбільшого елементу в підсписку [0...i]
        maxpos = 0
        for j in range(1, i + 1):
            if array[maxpos] < array[j]:
                maxpos = j
        
        # Міняємо місцями поточний (найбільший) елемент з елементом на позиції i
        array[i], array[maxpos] = array[maxpos], array[i]
        
    return array  # Повертаємо відсортований масив (згідно з вимогою завдання)


# 3.(Insertion Sort)
def insertion_sort(array):
    for index in range(1, len(array)):
        currentValue = array[index]
        position = index

        # Зсуваємо елементи, що більші за currentValue, вправо
        while position > 0 and array[position - 1] > currentValue:
            array[position] = array[position - 1]
            position -= 1

        # Вставляємо поточний елемент у знайдену позицію
        array[position] = currentValue
        
    return array  # Повертаємо відсортований масив (згідно з вимогою завдання)


# Код для перевірки (не обов'язково включати у фінальний файл)
if __name__ == '__main__':
    test_list = [64, 34, 25, 12, 22, 11, 90]
    
    print(f"Original: {test_list}")
    print(f"Bubble Sort: {bubble_sort(test_list.copy())}")
    print(f"Selection Sort: {selection_sort(test_list.copy())}")
    print(f"Insertion Sort: {insertion_sort(test_list.copy())}")
