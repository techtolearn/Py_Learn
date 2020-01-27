# https://www.youtube.com/watch?v=Uh2ebFW8OYM&list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU&index=25
'''
Python Tutorial: File Objects - Reading and Writing to Files
'''
# f = open('Basic-Commands.txt', 'r')
# print(f.name)
# print(f.mode)
# f.close()

#with open('Basic-Commands.txt', 'r') as f: # it automatically close the file using this format
    # print(f.name)
    # print(f.mode)
    # print(f.closed) # it will tell us file closed so we no need to close separately

    # f_contents = f.read()
    # print(f_contents)
    # print("\n")
    # f_contentLine = f.readline()  # it will read first line of the file
    # print(f_contentLine,ends =' ')

# read all the line of test using for loop
# for line in f:
#     print(line,end='')


# print only specified character from file
#     f_char = f.read(100)
#     fileLen = len(f_char)
#     print('file length is : \t'+str(fileLen)+'\n'+ f_char)


# with open('Basic-Commands.txt', 'r') as f:
#
#     size_to_read =100
#     f_contents = f.read(size_to_read)
#     print(f.tell())  # it will tell us how many char system read which is 100
#     f.seek(0)    # when use this method in a loop it will start print again from begining (1th line)
#
#     while len(f_contents) > 0:
#         print(f_contents, end=' ')
#         f_contents = f.read(size_to_read) # 1end the infinite loop and 2. print next chunk of contents consecutively till end of the file


# writing file
# with open('test.txt', 'w') as f: # if the file text1.txt is not exist, it will create new file and write the contents
#     f.write('Testing')
#     f.seek(0)  ##it will overrite first and re-write from the begining
#     f.write('Testing')


# performing read and write
# with open('test.txt', 'r') as rf:  # read the test file
#     with open('test_copy.txt', 'w') as wf:  # create test_copy file and write the text file contents here
#         for line in rf:
#             wf.write(line)

# # performing read and write picture file  - read and write should be in binary mode as it is picture file
# with open('Tanvi.jpg', 'rb') as rf:  # read the test file
#     with open('Tanvi_copy.jpg', 'wb') as wf:  # create test_copy file and write the text file contents here
#         for line in rf:
#             wf.write(line)

# performing read and write chunk of picture file  - read and write should be in binary mode as it is picture file
with open('Tanvi.jpg', 'rb') as rf:  # read the test file
    with open('Tanvi_copy.jpg', 'wb') as wf:  # create test_copy file and write the text file contents here
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while(len(rf_chunk)) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
