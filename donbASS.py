from tkinter import *
from unittest import result
root = Tk()
root.title("Enigma")

def encrypt():
    # if r_var == 0:
    #     alphabet =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    #     bias = e1.get()    
    #     message = e2.get().upper()    
    #     result1 = ''
    #     for i in message:
    #         mesto = alphabet.find(i)
    #         new_place = mesto + bias
    #         if i in alphabet:
    #             result1 += alphabet[new_place] 
    #         else:
    #             result1 += i
    #     testResult = 'fff'
    #     l1.config(text = testResult)
    alphabet =  'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    bias = int(e1.get())   
    message = e2.get().upper()    
    result1 = ''
    for i in message:
            place = alphabet.find(i)
            new_place = place + bias
            if i in alphabet:
                result1 += alphabet[new_place] 
            else:
                result1 += i
                testResult = 'fff'
                l1.config(text = testResult)
    
        
    if r_var == 1:
        def form_dict():
            d = {}
            iter = 0
            for i in range(0,127):
                d[iter] = chr(i)
                iter = iter +1
                return d   
        def encode_val(word):
            list_code = []
            lent = len(word)
            d = form_dict() 

            for w in range(lent):
                for value in d:
                    if word[w] == d[value]:
                       list_code.append(value) 
            return list_code
        def comparator(value, key):
            len_key = len(key)
            dic = {}
            iter = 0
            full = 0

            for i in value:
               dic[full] = [i,key[iter]]
               full = full + 1
               iter = iter +1
               if (iter >= len_key):
                   iter = 0 
            return dic 

        def full_encode(value, key):
            dic = comparator(value, key)
            lis = []
            d = form_dict()

            for v in dic:
                go = (dic[v][0]+dic[v][1]) % len(d)
                lis.append(go) 
            return lis
        def decode_val(list_in):
            list_code = []
            lent = len(list_in)
            d = form_dict() 


            for i in range(lent):
                for value in d:
                   if list_in[i] == value:
                    list_code.append(d[value]) 
            return list_code    


e1 = Entry()
e1.pack()
e2 = Entry()
e2.pack()

l1 = Label(text = "") 
l1.pack()
l2 = Label(width=50, text = "Шифрование") 
l2.pack()
l3 = Label(width=50, text = "Шифрование") 
l3.pack()
l4 = Label(width=50, text = "Шифрование") 
l4.pack()
l5 = Label(width=50, text = "Шифрование") 
l5.pack()

b1 = Button(width=5, height=5, text = "Зашифровать", command  = encrypt)
b1.pack()

r_var = BooleanVar()
r_var.set(0)
r1 = Radiobutton(text='Шифр Цезаря', variable=r_var, value=0)
r1.pack()
r2 = Radiobutton(text='Шифр Виженера', variable=r_var, value=1)
r2.pack()
r3 = Radiobutton(text='Азбука Морзе', variable=r_var, value=2)
r3.pack()
r4 = Radiobutton(text='Шифр Гронсфельда', variable=r_var, value=3)
r4.pack()
r5 = Radiobutton(text='Шифр Энигмы', variable=r_var, value=4)
r5.pack()


    
root.mainloop()