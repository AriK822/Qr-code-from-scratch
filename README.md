# Qr-code-from-scratch
A simple Qr-code generator in python from scratch.

#Example
```Python
my_qrcode = Qrcode(3, 'byte', "M", 0)
my_qrcode.set_up()
my_qrcode.process_massage("www.youtube.com")
listt = my_qrcode.data_list
```

Or you can easily change the following line 9 in viewer.py, with your own link, and view the resault using pygame:
- my_qrcode.process_massage("www.youtube.com")

Source: https://www.thonky.com/qr-code-tutorial/
