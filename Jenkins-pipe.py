def pipe():
    my_file = open("C:\\Users\moshiko.gabay\\Desktop\\Jenkins-homework.txt",'w')
    content = my_file.write("moshiko gabay")

    my_file = open("C:\\Users\moshiko.gabay\\Desktop\\Jenkins-homework.txt", 'r')
    content = my_file.read()
    print(content)

    import shutil

    total, used, free = shutil.disk_usage("/")

    print("Total: %d GiB" % (total // (2 ** 30)))
    print("Used: %d GiB" % (used // (2 ** 30)))
    print("Free: %d GiB" % (free // (2 ** 30)))

    shutil.copy("C:\\Users\\moshiko.gabay\\Desktop\\Jenkins-homework.txt", "C:\\Users\\moshiko.gabay\\Desktop\\DevOps")

pipe()
