import tkinter

root = tkinter.Tk()

# 异常处理类
class FError(Exception):
    pass

class MyCalculator():

    def __init__(self, width, height, title):
        # 设置窗体大小
        root.maxsize(height=height, width=width)
        root.minsize(height=height, width=width)
        root.title(title)
        self.color_index = 0
        # 设置初始透明度
        self.nums = 1
        # 显示面板
        self.top_frame = None
        # 键盘面板
        self.bootom_frame = None
        # 操作函数
        self.calList = []
        self.flag = False;
        # 储存结果的临时变量
        self.result = 0
        self.result_panel1 = None
        self.result_panel2 = None
        self.format = True

    def set_label(self):
        self.top_frame = tkinter.Frame(root,width=450,height=200)
        self.top_frame.place(x=0,y=0)

        self.result_panel1 = tkinter.StringVar()
        self.result_panel2 = tkinter.StringVar()
        self.result_panel1.set('')
        self.result_panel2.set(0)

        result_label1 = tkinter.Label(self.top_frame, font=('微软雅黑', 25), bg='#FFFEFF', bd='9', fg='#000000', anchor='se',
                              textvariable=self.result_panel1)
        result_label1.place(width=450, height=100)
        result_label2 = tkinter.Label(self.top_frame,font=('微软雅黑', 50), bg='#FFFEFF', bd='9', fg='#000000', anchor='se',
                               textvariable=self.result_panel2)
        result_label2.place(x=0,y=100, width=450, height=100)

    def set_span(self):
        self.bootom_frame = tkinter.Frame(root, width=450, height=400)
        self.bootom_frame.place(x=0, y=200)

        button_c = tkinter.Button(self.bootom_frame, text='C', bd='0', font=('微软雅黑', 20), bg='#69B3AD',
                                  fg='#FFFEFF', command=lambda: self.pressC())
        button_c.place(x=0, y=0, width=90, height=80)

        button_back = tkinter.Button(self.bootom_frame, text='<-', bd='0', font=('微软雅黑', 20), bg='#69B3AD',
                                     fg='#FFFEFF', command=lambda: self.pressBack())
        button_back.place(x=90, y=0, width=90, height=80)

        button_minus = tkinter.Button(self.bootom_frame, text='±', bd='0', font=('微软雅黑', 20), bg='#69B3AD',
                                      fg='#FFFEFF', command=lambda: self.pressMinus())
        button_minus.place(x=180, y=0, width=90, height=80)

        button_left = tkinter.Button(self.bootom_frame, text='(', bd='0', font=('微软雅黑', 20), bg='#69B3AD',
                                     fg='#FFFEFF', command=lambda: self.pressLeft())
        button_left.place(x=270, y=0, width=90, height=80)

        button_right = tkinter.Button(self.bootom_frame, text=')', bd='0', font=('微软雅黑', 20), bg='#69B3AD',
                                      fg='#FFFEFF', command=lambda: self.pressRight())
        button_right.place(x=360, y=0, width=90, height=80)

        button_1 = tkinter.Button(self.bootom_frame, text='1', bd='0', font=('微软雅黑', 20), bg='#429488',
                                  fg='#FFFEFF', command=lambda: self.pressNum('1'))
        button_1.place(x=0, y=80, width=90, height=80)

        button_2 = tkinter.Button(self.bootom_frame, text='2', bd='0', font=('微软雅黑', 20), bg='#429488',
                                  fg='#FFFEFF', command=lambda: self.pressNum('2'))
        button_2.place(x=90, y=80, width=90, height=80)

        button_3 = tkinter.Button(self.bootom_frame, text='3', bd='0', font=('微软雅黑', 20), bg='#429488',
                                  fg='#FFFEFF', command=lambda: self.pressNum('3'))
        button_3.place(x=180, y=80, width=90, height=80)

        button_power = tkinter.Button(self.bootom_frame, text='^', bd='0', font=('微软雅黑', 20), bg='#429488',
                                      fg='#FFFEFF', command=lambda: self.pressOperation('^'))
        button_power.place(x=270, y=80, width=90, height=80)

        button_remainder = tkinter.Button(self.bootom_frame, text='%', bd='0', font=('微软雅黑', 20), bg='#429488',
                                          fg='#FFFEFF', command=lambda: self.pressOperation('%'))
        button_remainder.place(x=360, y=80, width=90, height=80)

        button_4 = tkinter.Button(self.bootom_frame, text='4', bd='0', font=('微软雅黑', 20), bg='#429488',
                                  fg='#FFFEFF', command=lambda: self.pressNum('4'))
        button_4.place(x=0, y=160, width=90, height=80)

        button_5 = tkinter.Button(self.bootom_frame, text='5', bd='0', font=('微软雅黑', 20), bg='#429488',
                                  fg='#FFFEFF', command=lambda: self.pressNum('5'))
        button_5.place(x=90, y=160, width=90, height=80)

        button_6 = tkinter.Button(self.bootom_frame, text='6', bd='0', font=('微软雅黑', 20), bg='#429488',
                                  fg='#FFFEFF', command=lambda: self.pressNum('6'))
        button_6.place(x=180, y=160, width=90, height=80)

        button_plus = tkinter.Button(self.bootom_frame, text='+', bd='0', font=('微软雅黑', 20), bg='#429488',
                                     fg='#FFFEFF', command=lambda: self.pressOperation('+'))
        button_plus.place(x=270, y=160, width=90, height=80)

        button_sub = tkinter.Button(self.bootom_frame, text='-', bd='0', font=('微软雅黑', 20), bg='#429488',
                                    fg='#FFFEFF', command=lambda: self.pressOperation('-'))
        button_sub.place(x=360, y=160, width=90, height=80)

        button_7 = tkinter.Button(self.bootom_frame, text='7', bd='0', font=('微软雅黑', 20), bg='#429488',
                                  fg='#FFFEFF', command=lambda: self.pressNum('7'))
        button_7.place(x=0, y=240, width=90, height=80)

        button_8 = tkinter.Button(self.bootom_frame, text='8', bd='0', font=('微软雅黑', 20), bg='#429488',
                                  fg='#FFFEFF', command=lambda: self.pressNum('8'))
        button_8.place(x=90, y=240, width=90, height=80)

        button_9 = tkinter.Button(self.bootom_frame, text='9', bd='0', font=('微软雅黑', 20), bg='#429488',
                                  fg='#FFFEFF', command=lambda: self.pressNum('9'))
        button_9.place(x=180, y=240, width=90, height=80)

        button_mul = tkinter.Button(self.bootom_frame, text='*', bd='0', font=('微软雅黑', 20), bg='#429488',
                                    fg='#FFFEFF', command=lambda: self.pressOperation('*'))
        button_mul.place(x=270, y=240, width=90, height=80)

        button_div = tkinter.Button(self.bootom_frame, text='/', bd='0', font=('微软雅黑', 20), bg='#429488',
                                    fg='#FFFEFF', command=lambda: self.pressOperation('/'))
        button_div.place(x=360, y=240, width=90, height=80)

        button_0 = tkinter.Button(self.bootom_frame, text='0', bd='0', font=('微软雅黑', 20), bg='#429488',
                                  fg='#FFFEFF', command=lambda: self.pressNum('0'))
        button_0.place(x=0, y=320, width=180, height=80)

        button_point = tkinter.Button(self.bootom_frame, text='.', bd='0', font=('微软雅黑', 20), bg='#429488',
                                      fg='#FFFEFF', command=lambda: self.pressNum('.'))
        button_point.place(x=180, y=320, width=90, height=80)

        button_eq = tkinter.Button(self.bootom_frame, text='=', bd='0', font=('微软雅黑', 20), bg='#69B3AD',
                                   fg='#FFFEFF', command=lambda: self.pressEqual())
        button_eq.place(x=270, y=320, width=180, height=80)

    def pressC(self):
        self.calList.clear()
        self.result_panel1.set('')
        self.result_panel2.set(0)

    def pressBack(self):
        result = self.result_panel2.get()
        result = result[:-1]
        self.calList.clear()
        self.calList.append(result)
        if self.calList[0] == '':
            self.result_panel2.set(0)
        else:
            self.result_panel2.set(''.join(self.calList))

    def pressMinus(self):
        num = self.result_panel2.get()
        if num[0] == '(' and num[-1] == ')' or num[0] == '-':
            if num[1] == '-':
                num = str(num)[2:-1]
            if num[0] == '-':
                num = str(num)[1:]
        elif num[0] != '-':
            num = '(-' + num + ')'
        self.result_panel2.set(num)
        if len(self.calList) > 0:
            self.calList[-1] = num
        if len(self.calList) == 0:
            self.calList.append(num)

    def pressLeft(self):
        self.calList.append('(')
        self.result_panel2.set(''.join(self.calList))

    def pressRight(self):
        self.calList.append(')')
        self.result_panel2.set(''.join(self.calList))

    def pressNum(self, num):
        oldNum = self.result_panel2.get()
        if oldNum == '0' and self.flag == False:
            if num == '.':
                num = '0.'
            self.result_panel2.set(num)
        else:
            if self.flag == True and oldNum[0] != '(':
                if len(self.calList) == 1:
                    self.result_panel2.set(num)
                    self.calList.clear()
                    self.calList.append(num)
                else:
                    self.calList.append(num)
                    self.result_panel2.set(''.join(self.calList))
                self.flag = False
            else:
                newNum = oldNum + num
                self.result_panel2.set(newNum)
                self.calList.clear()
                self.calList.append(newNum)

    def pressOperation(self, operation):
        num = self.result_panel2.get()
        if num[-1] in '+-/*^%':
            self.format = False
        if len(num) > 0:
            if num[0] == '(' and len(num) != 1:
                self.calList.clear()
                self.calList.append('(' + num[1:])
            else:
                self.calList.clear()
                self.calList.append(num)

        self.isPressOperation = True
        self.calList.append(operation)
        self.result_panel2.set(''.join(self.calList))

    def pressEqual(self):
        if self.format == False:
            self.format = True
            try:
                raise FError("格式错误")
            except FError:
                self.result_panel2.set('操作符错误')
                self.calList.clear()
                self.result_panel1.set('')
                return
        try:
            if len(self.calList) != 0:
                self.result = round(eval(''.join(self.calList).replace('^','**')), 11)
                self.result_panel2.set(self.result)
                self.result_panel1.set(''.join(self.calList))
                self.calList.clear()
                self.calList.append(str(self.result))
                self.flag = True
            else:
                self.result_panel1.set(0)
        except SyntaxError:
            self.result_panel2.set('没有操作数')
            self.calList.clear()
            self.result_panel1.set('')
        except ZeroDivisionError:
            self.result_panel2.set('除数不能为0')
            self.calList.clear()
            self.result_panel1.set('')
        except:
            self.result_panel2.set('ERROR')
            self.calList.clear()
            self.result_panel1.set('')


    def Mouse_Press3(self, e):
        global color_list
        color_list = ['#6495ed', '#8b008b', '#00ced1']
        if self.color_index == len(color_list):
            self.color_index = 0
        e.widget['bg'] = color_list[self.color_index]
        self.color_index += 1

    # 鼠标滚轮事件
    def Mouse_on(self, e):
        if e.delta == -120 and self.nums > 0.11:
            self.nums -= 0.1
            root.attributes("-alpha", self.nums)  # 窗口透明度70 %
        elif e.delta == 120 and self.nums < 1:
            self.nums += 0.1
            root.attributes("-alpha", self.nums)

    def call_fun(self):
        self.bootom_frame.bind_class('Button', '<ButtonPress-3>', self.Mouse_Press3)
        root.bind('<MouseWheel>', self.Mouse_on)


if __name__ == '__main__':
    calculator = MyCalculator(450, 600, '森林')
    calculator.set_label()
    calculator.set_span()
    calculator.call_fun()
    root.mainloop()
