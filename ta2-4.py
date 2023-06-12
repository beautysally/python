import sys
a=sys.stdin.read()
for i ,a in enumerate(a.splitlines()):
    print(f'{a}{i+1}')
  