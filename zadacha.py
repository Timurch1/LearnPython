def to_often(nums: str):
    max_value = 0
    symbol = ''
    for i in nums:
        counter = 0
        for b in nums:
            if i == b:
                counter += 1
        if counter > max_value:
            max_value = counter
            symbol = i
    print("Чаще всего встречается символ {0}, он встречался в строке {1} {2} раз".format(symbol, nums,
    max_value))

strochka = input("Введите слово: ")
to_often(strochka)



# Удаление повторяющихся элементов и нахождения числа неповторящихся элементов)
def to_set(nums: list):
   nums = set(nums)
   for i in range(len(nums)):
       i += 1
   print("Результат: ", i, end=', ')
   return nums

it_list = [1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 10, 10, 15, 18, 18, 20]
print(to_set(it_list))

def good_price(nums: list[int]):
    min_num = nums[0]
    max_price = 0
    for x in nums:
        if x < min_num:
            min_num = x
            index_num = nums.index(min_num)
        elif x - min_num > max_price:
            day = x
            index_num2 = nums.index(x)
            max_price = x - min_num
    print("Покупайте в", index_num + 1, 'день за',min_num, 'и продавайте в', index_num2 + 1, 'за', day)
    return f'Выгода: {max_price}'

price = [5, 1, 3, 2]
print(good_price(price))


def binary_search(lst, item) -> int:
    low = 0
    higt = len(lst) - 1
    while low <= higt:
        mid = (low + higt) // 2
        guess = lst[mid]
        if guess == item:
            return mid
        elif guess > item:
            higt = mid - 1
        else:
            low = mid + 1

    for x in lst:
        is_index = lst.index(x)
        if x == lst[-1]:
            return is_index + 1
        if lst[is_index] < item and item < lst[is_index + 1]:
                return is_index + 1
res = binary_search([1, 2, 3, 5, 7, 10, 11, 12, 14, 16], 17)
print(res)


def to_often(nums: str):
    max_value = 0
    symbol = ''
    for i in nums:
        counter = 0
        for b in nums:
            if i == b:
                counter += 1
                if counter > max_value:
                    max_value = counter
                    symbol = i
    return symbol, max_value
def to_dict(stroka: str) -> dict:
    dict1 = {}
    count = 0
    while count != 5:
        count += 1
        symbol, max_value = to_often(stroka)
        dict1[symbol] = max_value
        stroka = stroka.replace(symbol, '')
    return dict1
home = to_dict("000112334566667888889")
print(home)

# Задача на поиск количества цифр в строке
def to_int_stroka(nums: str) -> int:
    res = 0
    for i in nums:
        if '0' <= i <= '9':
            res += 1
    return res


# Нахождение количества символа в строке
def search_symwal(stroka: str):
    res = 0
    for i in stroka:
        if i == symwal:
            res += 1
    print("Количество",symwal,':', res)
    return stroka

stroka= str(input("Введите слово: "))
symwal = str(input("Введите символ: "))
count = search_symwal(stroka)
print(count)

# Задача: существуют ли пассажиры с возрастом 60 или больше...

quest = ['1231234624M513', '1231264524Ж613', '1231234524M613']
count = 0
for i in quest:
    result = i.rfind('6')
    if result != -1 and result == 11:
        count += 1
if count:
    print(count)
else:
    print("Пассажиров с возрастом 60 или больше нету!")

# Передайте подушку
def time(it_time, n) -> int:
    person = 1
    c = 0
    while it_time > 0:
        if c == 0:
            person += 1
            if person == n:
                c -= 1
        elif c == -1:
            person -= 1
            if person == 1:
                c = 0
        it_time -= 1
    return person
result = time(2, 3)
print(result)
