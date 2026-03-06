from pathlib import Path
path = Path()
print(path.absolute())


for file in path.glob('*.py'):
    print(file)