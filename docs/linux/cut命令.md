

### 用途
Linux cut命令用于显示每行从开头算起 num1 到 num2 的文字。

```
$ cat r2.txt
COMMAND    PID     U
loginwind  109 wench
loginwind  109 wench
loginwind  109 wench
loginwind  109 wench
loginwind  109 wench
loginwind  109 wench
loginwind  109 wench
loginwind  109 wench
loginwind  109 wench
```

```
$ cut -b 1-9 r2.txt
COMMAND
loginwind
loginwind
loginwind
loginwind
loginwind
loginwind
loginwind
loginwind
loginwind
```

### 参数

- -b ：以字节为单位进行分割。这些字节位置将忽略多字节字符边界，除非也指定了 -n 标志。
- -c ：以字符为单位进行分割。
- -d ：自定义分隔符，默认为制表符。
- -f ：与-d一起使用，指定显示哪个区域。
- -n ：取消分割多字节字符。仅和 -b 标志一起使用。如果字符的最后一个字节落在由 -b 标志的 List 参数指示的范围之内，该字符将被写出；否则，该字符将被排除

```
$ who
wenchong console  Jul 14 07:22
wenchong ttys000  Jul 14 15:09
```
```
$ who | cut -b 26-
07:22
15:09
```

