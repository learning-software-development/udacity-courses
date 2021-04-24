import os

W_DIR = r"C:/learn-unity-dev"


def rename_file():
    file_list = os.listdir(W_DIR)
    os.chdir(W_DIR)
    for file_name in file_list:
        # os.rename(file_name.translate(None, '0123456789'))
        print(file_name)

    print(file_list)


rename_file()
