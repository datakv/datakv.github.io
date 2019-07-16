
# PyQt5-01-环境搭建
2019-6-7 18:44:30
---

### 1、当前使用的 python版本 
确认是python3

### 2、安装 QT5：
```
python -m pip install PyQt5
```
或者
```
python -m pip install PyQt5 -i https://pypi.douban.com/simple 
```

> 在后面加上“-i https://pypi.douban.com/simple”表示使用豆瓣所提供的镜像

### 3、安装qt5图形设计工具：

```
python -m pip install PyQt5-tools
```
或者
```
python -m pip install PyQt5-tools -i https://pypi.douban.com/simple
```
> 在后面加上“-i https://pypi.douban.com/simple” 同上

### 4、验证qt5是否安装成功：
```
from PyQt5 import QtWidgets, QtGui
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget();
window.show()
sys.exit(app.exec_())
```
> 此时正常弹出窗体，没有报错

### 5、为PyCharm 添加 QtDesigner 
 1. 打开settings->Tools->External Tools点击“+”
 2. 弹出对话框
```
name:QtDesigner 
Program:[选择designer.exe,一般都是在....\Lib\site-packages\pyqt5_tools\designer.exe]
Working directory: $FileDir$[通过后边的Insert Macros,选择‘FileDir - File directory’]
```

### 6、为PyCharm 添加 PyUIC 
 1. 打开settings->Tools->External Tools点击“+”
 2. 弹出对话框
```
name:PyUIC 
Program:[选择python.exe]
Parameters: -m PyQt5.uic.pyuic  $FileName$ -o $FileNameWithoutExtension$.py
Working directory: $FileDir$[通过后边的Insert Macros,选择‘FileDir - File directory’]
```

### 7、新建项目 t_qt
 1. 右键t_qt->External Tools->QtDesigner，设计界面，保存hello.ui；
 2. 右键hello.ui->External Tools->PyUIC，生成py文件；
 3. 定义类和main函数；
```


from t_qt import hello
from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class query_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = hello.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.query_formula)
        # 给button 的 点击动作绑定一个事件处理函数

    def query_formula(self):
        pass
        # 此处编写具体的业务逻辑


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = query_window()
    window.show()
    sys.exit(app.exec_())

```
 4. 执行。