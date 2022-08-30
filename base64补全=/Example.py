wf = open("base64_str补全=后.txt", "w")

with open("base64_str.txt", "r") as f:
    data = f.read()
    data = data.splitlines()

for line in data:
    missing_padding = len(line) % 4
    if missing_padding != 0:
        line += "=" * (4 - missing_padding)
    wf.write(line + "\n")