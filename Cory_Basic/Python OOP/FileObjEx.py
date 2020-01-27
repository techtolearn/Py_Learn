#Ref : https://www.youtube.com/watch?v=Uh2ebFW8OYM

# Example 1
# f = open('Creditcard.txt', 'r')
# print(f.name)
# print(f.mode)
# print(f.encoding)
# print(f.closed)

# Example 2
# with open('C:\Learning\Creditcard.txt','r') as f:
#     print("read all lines ones")
#     print("===================")
#     f_contents = f.read()
#     print(f_contents)
#     print("\n")
# with open('C:\Learning\Creditcard.txt','r') as f:
#     print("read sinle lines ones")
#     print("=====================")
#     f_contents = f.readline()
#     print(f_contents)
#      print("\n")

# Example 3
# with open('C:\Learning\Creditcard.txt','r') as f:
#     for line in f:
#        print(line,end='')  #end='' remove the empty lines


# Example 4 -print limited number of character
# with open('C:\Learning\Creditcard.txt','r') as f:
#     print("read all lines ones")
#     print("===================")
#    # f_contents = f.read(100)
#     size_to_read =100
#     print(f.tell())
#     f_contents = f.read(size_to_read)
#     print(f_contents)
#
#     print(f.tell())

#Example 4  file write
# with open('C:\Learning\Creditcard.txt','r') as f:
#     f.write("Hello world")



# Example 5  file write  - copy from one file to another
# with open('C:\Learning\Creditcard.txt','r') as rf:
#     with open('C:\Learning\Creditcard1.txt','w') as wf:
#         for line in rf:
#             wf.write(line)

# Example 5  file write  - copy from image file to another - image file copy should be in Binary mode (b)
# with open('C:\Learning\Tanvi.jpg','rb') as rf:
#     with open('C:\Learning\Tanv1i.jpg','wb') as wf:
#         for line in rf:
#             wf.write(line)

# Example 5  file write  - copy from image file to another - image file copy should be in Binary mode (b)
with open('C:\Learning\Tanvi.jpg','rb') as rf:
    with open('C:\Learning\Tanvi1.jpg','wb') as wf:
        chuck_size = 652412211
        rf_chunk = rf.read(chuck_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)

