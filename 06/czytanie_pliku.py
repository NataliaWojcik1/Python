# try:
#   with open(filename, 'r') as f:
#     content = f.read()
#
#   print(content)
#
# except FileNotFoundError:
#     print('Error - no such file')

with open('tekst.txt', 'w') as f:
  f.write('Line 1\n')
  f.write('Line 2\n')
  f.write('Line 3\n')
  f.write('Line 4\n')
  f.write('The end!')

with open('Cytaty.txt')