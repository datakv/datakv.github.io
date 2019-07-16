
# simiki的使用

2019-03-29

---


### Install 

	pip install simiki

### Update

	pip install -U simiki

### Init Site

	mkdir mywiki && cd mywiki
	simiki init

### Create a new wiki

	simiki new -t "Hello Simiki" -c first-catetory

### Generate

	simiki g

### Preview

	simiki p -w
	    默认地址：127.0.0.1:8000
	simiki p --host 0.0.0.0 --port 8888
	