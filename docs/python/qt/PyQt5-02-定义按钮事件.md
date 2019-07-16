
# PyQt5-02-定义按钮事件

### 1、在生成的窗体类里边添加成员函数：

```
    def firtPyQt5_button_click(self):
        QtWidgets.QMessageBox.information(self.pushButton, "标题", "这是第一个PyQt5 GUI程序")
        
```


### 2、关联事件：
在 def setupUi(self,):里 的 self.retranslateUi(*)前添加：
```
        self.pushButton.clicked.connect(self.firtPyQt5_button_click)

```
