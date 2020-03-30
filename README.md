## API REST com o framework falcon do Python

### libs
```shell
$ pip install -r requirements.txt
```

### run (port 3000)
```shell
$ ./app.sh
```

### curl GET
```shell
$ curl http://0.0.0.0:3000/{namespace}/category-sub-code/{category_sub_code}
$ curl http://0.0.0.0:3000/{namespace}/category-sub-code/{category_sub_code}/due-code/{due_code}
$ curl http://0.0.0.0:3000/{namespace}/due-code/{due_code}
```