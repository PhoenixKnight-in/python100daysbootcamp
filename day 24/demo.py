# # file = open("my_file.txt")
# # contents = file.read()
# # print(contents)
# # file.close()
# with open("my_file.txt") as F:
#     contents = F.read()
#     print(contents)
#
# with open(r"C:\Users\asus\Desktop\my_file.txt","r",newline="") as F:
#     reader = F.readlines()
#     for line in reader:
#         print(line)
with open("../../../Desktop/my_file.txt","r",newline='') as F:
    reader = F.readlines()
    for line in reader:
        print(line)