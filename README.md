# Домашнее задание к занятию "`Система мониторинга Zabbix. Часть 2`" - `Горбунов Владимир`



### Задание 1

`Кастомный шаблон:`<br>

![Название скриншота](https://github.com/Night-N/8-zabbix2/blob/main/zabbix-1.jpg)<br>

### Задание 2-3

`Два хоста с привязанными шаблонами:`<br>

![Название скриншота](https://github.com/Night-N/8-zabbix2/blob/main/zabbix-2.jpg)<br>
![Название скриншота](https://github.com/Night-N/8-zabbix2/blob/main/zabbix-3.jpg)<br>

### Задание 4

`Кастомный дэшборд:`<br>

![Название скриншота](https://github.com/Night-N/8-zabbix2/blob/main/zabbix-4.jpg)<br>

### Задание 5

`Карта со сработавшим триггером:`<br>

![Название скриншота](https://github.com/Night-N/8-zabbix2/blob/main/zabbix-5.jpg)<br>

### Задание 6

`Параметр со скриптом баш и latest data:`<br>
```
#!/bin/bash
case $1 in
    "1")
        echo "Gorbunov Vladimir"
    ;;
    "2")
        date -I
    ;;
    *)
        echo "unknown input"
    ;;
esac
```

![Название скриншота](https://github.com/Night-N/8-zabbix2/blob/main/zabbix-6.jpg)<br>

### Задание 7
`Параметр с кодом Python и latest data:`<br>
```
import sys
import os
import re
if (sys.argv[1] == '-ping'):
    result=os.popen("ping -c 1 " + sys.argv[2]).read() 
    result=re.findall(r"time=(.*) ms", result) 
    print(result[0]) 
elif (sys.argv[1] == '-simple_print'): 
    print(sys.argv[2]) 
elif (sys.argv[1] == '1'): 
    print("Gorbunov Vladimir") 
elif (sys.argv[1] == '2'): 
    result=os.popen("date -I").read()
    print(result)
else: 
    print(f"unknown input: {sys.argv[1]}") 
```

![Название скриншота](https://github.com/Night-N/8-zabbix2/blob/main/zabbix-7.jpg)<br>

### Задание 8

`Автообнаружение:`<br>

![Название скриншота](https://github.com/Night-N/8-zabbix2/blob/main/zabbix-8.jpg)<br>

### Задание 9

`доработанный скрипт:`<br>



