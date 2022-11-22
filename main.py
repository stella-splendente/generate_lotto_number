#-*-coding:utf-8-*-
import tkinter
from tkinter import ttk
import random
from tkinter import messagebox

check_number_list = []

def gen_number():
    #1
    except_nums = []
    for i in range(0, 45):
        if check_number_list[i].get() == 1:
            except_nums.append(i+1)
    if len(except_nums) > 39:
        messagebox.showinfo(title="Error!",message="번호 6개는 필수입니다.")
        return

    numbers = []
    while(len(numbers)<6):
        num = random.randint(1,45)
        if num in except_nums or num in numbers:
            continue
        numbers.append(num)
    numbers.sort()
    svar_nums.set(numbers)
    
    #2
    except_nums = []
    for i in range(0, 45):
        if check_number_list[i].get() == 1:
            except_nums.append(i+1)
    if len(except_nums) > 39:
        messagebox.showinfo(title="Error!",message="번호 6개는 필수입니다.")
        return

    numbers = []
    while(len(numbers)<6):
        num = random.randint(1,45)
        if num in except_nums or num in numbers:
            continue
        numbers.append(num)
    numbers.sort()
    svar_nums2.set(numbers)
    
    #3
    except_nums = []
    for i in range(0, 45):
        if check_number_list[i].get() == 1:
            except_nums.append(i+1)
    if len(except_nums) > 39:
        messagebox.showinfo(title="Error!",message="번호 6개는 필수입니다.")
        return

    numbers = []
    while(len(numbers)<6):
        num = random.randint(1,45)
        if num in except_nums or num in numbers:
            continue
        numbers.append(num)
    numbers.sort()
    svar_nums3.set(numbers)

    #4
    except_nums = []
    for i in range(0, 45):
        if check_number_list[i].get() == 1:
            except_nums.append(i+1)
    if len(except_nums) > 39:
        messagebox.showinfo(title="Error!",message="번호 6개는 필수입니다.")
        return

    numbers = []
    while(len(numbers)<6):
        num = random.randint(1,45)
        if num in except_nums or num in numbers:
            continue
        numbers.append(num)
    numbers.sort()
    svar_nums4.set(numbers)

    #5
    except_nums = []
    for i in range(0, 45):
        if check_number_list[i].get() == 1:
            except_nums.append(i+1)
    if len(except_nums) > 39:
        messagebox.showinfo(title="Error!",message="번호 6개는 필수입니다.")
        return

    numbers = []
    while(len(numbers)<6):
        num = random.randint(1,45)
        if num in except_nums or num in numbers:
            continue
        numbers.append(num)
    numbers.sort()
    svar_nums5.set(numbers)
'''
def call():
    l_nums.grid(row=9, column=0, columnspan=10)
    l_nums2.grid(row=10, column=0, columnspan=10)
    l_nums3.grid(row=11, column=0, columnspan=10)
    l_nums4.grid(row=12, column=0, columnspan=10)
    l_nums5.grid(row=13, column=0, columnspan=10)
'''

root = tkinter.Tk()
root.title("커피집차리러 가즈아").encode('utf-8')
root.resizable(False, False)

svar_nums = tkinter.StringVar(root, )
svar_nums2 = tkinter.StringVar(root, )
svar_nums3 = tkinter.StringVar(root, )
svar_nums4 = tkinter.StringVar(root, )
svar_nums5 = tkinter.StringVar(root, )
l_nums = ttk.Label(root, textvariable=svar_nums)
l_nums2 = ttk.Label(root, textvariable=svar_nums2)
l_nums3 = ttk.Label(root, textvariable=svar_nums3)
l_nums4 = ttk.Label(root, textvariable=svar_nums4)
l_nums5 = ttk.Label(root, textvariable=svar_nums5)

b_gen = ttk.Button(root, text="커피집 가즈아", command=gen_number,width=40)

for i in range(0,45):
    x=i%5
    y=i//5
    temp_v = tkinter.IntVar(root)
    ttk.Label(root, text=i+1).grid(row=y, column=x*2)
    check_number_list.append(temp_v)
    ttk.Checkbutton(root, variable=temp_v, onvalue=1, offvalue=0).grid(row=y, column=x*2+1)



l_nums.grid(row=9, column=0, columnspan=10)
l_nums2.grid(row=10, column=0, columnspan=10)
l_nums3.grid(row=11, column=0, columnspan=10)
l_nums4.grid(row=12, column=0, columnspan=10)
l_nums5.grid(row=13, column=0, columnspan=10)
b_gen.grid(row=14, column=0, columnspan=10)

root.mainloop()
