#20 Solve using regex
# import re
#
# def get_filename(file_path):
#     return re.search(r'^[A-Za-z]{1,8}\.[A-Za-z]{1,3}$', filepath).group()
#
# get_filename()




#30 ) Read an entire text file. (
# def file_read(file_path):
#        with open(file_path, "r") as reader:
#            result = reader.read()
#            print(result)
#
# result = file_read('text.txt')
# print(result)

#30  Read a file line by line and store it into a list
# def file_read(file_path):
#     with open(file_path) as f:
#         result = [line for line in f]
#     return result
#
# result = file_read('text.txt')
# print(result)


#40 ) Write a text in fullname_list line by line into fullname.txt file.
# def file_write(fullname_list):
#
#     with open('fullname.txt', 'w') as f:
#         f.write("\n".join(fullname_list))
#
#
# fullname_list = [
# 'Andre Montgomery Jr.',
# 'Natasha Rubio',
# 'Emily Serrano',
# 'Amber Nixon',
# 'Leslie Gomez'
# ]
#
# result = file_write(fullname_list)
# print(result)

#100 Read file using python generator
# import re
#
# def get_text(file_example):
#     return re.search(r'SIS(.*?)Best', file_example).group(1)
#
# result = get_text("example.txt")
# print(result)



