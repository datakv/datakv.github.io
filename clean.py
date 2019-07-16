import os


exist=["docs","mkdocs.yml","clean.py",".git"]

list = os.listdir("./") #列出目录下的所有文件和目录
for line in list:
    if line in exist :
        pass

    else :
        os.system("rm -rf " + line)

# exit(0)

os.system("mkdocs build")
os.system("mv site/* ./")


