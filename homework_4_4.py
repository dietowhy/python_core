with open("file1.bin", "rb") as f:
    data1 = f.read()

with open("file2.bin", "rb") as f:
    data2 = f.read()

with open("file1.bin", "wb") as f:
    f.write(data2)

with open("file2.bin", "wb") as f:
    f.write(data1)

with open("file1.bin", "rb") as f:
    print("file1:", f.read())

with open("file2.bin", "rb") as f:
    print("file2:", f.read())