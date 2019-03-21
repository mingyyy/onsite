
path = "raw/ubud.txt"
with open(path, "r") as f:
    file = f.readlines()

# first line is the title
counter = 0
for line in file:
    print(line)
    if counter == 0:
        title = line.strip()
    while line == "\n":
        para = "".join(line)
        break
    counter += 1

page = f'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <>
    <title>{title}</title>
</head>
<body>
    <h1></h1>

</body>
</html>
'''