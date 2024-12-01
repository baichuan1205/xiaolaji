# 写入文件
with open('example.txt', 'w') as file:
    file.write("Hello, World!Hello, World!Hello, World!Hello, World!")

# 读取文件
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)