file = open('youtube.yext', 'w')

try:
    file.write('Hello, world!')
finally:
    file.close()

with open('youtube.yext', 'w') as file:
    file.write('Hello Anas')