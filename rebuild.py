import os
import sys


exist=["docs","mkdocs.yml",".git"]

exist.append(sys.argv[0])

print(exist)


list = os.listdir("./") #列出目录下的所有文件和目录
for line in list:
    if line in exist :
        pass
    else :
        os.system("rm -rf " + line)

# exit(0)

os.system("mkdocs build")
os.system("mv site/* ./")

os.system("git add *")
os.system("git rm $(git ls-files --deleted)")
os.system("git commit -m \"feat:update\"")
os.system("git push origin master")


