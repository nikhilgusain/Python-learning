with open("temp.txt", "r+") as f:
    f.write("Line a+")
    f.flush()
    f.seek(0)
    print(f.read())
    
