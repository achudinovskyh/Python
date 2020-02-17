shopping_list_file = open('./text.txt', 'r')
shopping_list = shopping_list_file.readlines()
count = 1
print('Shopping list:')
for item in shopping_list:
    print('  {}) {}'.format(count, item.strip()))
    count += 1

shopping_list_file.close()
