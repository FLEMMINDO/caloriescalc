import tkinter as tk
from tkinter import ttk
import datetime
from PIL import ImageTk, Image

def solve(whateat, to60, to90, window):

    # ВЫЧИСЛЕНИЯ
    whateat = [str(i) for i in whateat.split()]
    for a in whateat:
        to60 -= int(food[a])
        to90 -= int(food[a])

    window.destroy()
    if to60 <= 0:
        left60lbl.config(text = 'NICE', bg = 'green')
    else:
        left60lbl.config(text=to60, bg = 'red')
        almostfail = Image.open('almostfailure.jpg')
        almostfailure = ImageTk.PhotoImage(almostfail.resize((150, 150)))
        to60imglbl.configure(image=almostfailure)
        to60imglbl.image = almostfailure

    if to90 <= 0:
        left90lbl.config(text = 'NICE', bg ='green')
    else:
        left90lbl.config(text=to90, bg='red')
        fail = Image.open('failure.png')
        failure = ImageTk.PhotoImage(fail.resize((150, 150)))
        to60imglbl.configure(image=failure)
        to60imglbl.image = failure

    if to60 <= 0 and to90 <= 0:
        succ = Image.open('success.jpeg')
        success = ImageTk.PhotoImage(succ.resize((150, 150)))
        to60imglbl.configure(image=success)
        to60imglbl.image = success

def addtodict(key, value, calcwin, window):

    # ДОБАВЛЕНИЕ ПРОДУКТОВ В СЛОВАРЬ
    food[f'{key}'] = f'{value}'
    tk.Label(calcwin, text = key + ' - ' + value + ' cal', bg = 'Yellow').pack(anchor='w', padx = 10, pady = 10)
    window.destroy()

def addproduct(calcwin):

    # ОКНО ДОБАВЛЕНИЯ ПРОДУКТА
    # ------------------
    addproductwin = tk.Tk()
    addproductwin.title('Добавление продукта')
    addproductwin.geometry('600x400+150+150')

    productnamelbl = tk.Label(addproductwin, text = 'Название продукта')
    productnamelbl.pack(anchor='center', expand = 1)
    productnameentry = ttk.Entry(addproductwin)
    productnameentry.pack(anchor='center', expand = 1)

    productcallbl = tk.Label(addproductwin, text='Калорийность продукта')
    productcallbl.pack(anchor='center', expand = 1)
    productcalentry = ttk.Entry(addproductwin)
    productcalentry.pack(anchor='center', expand = 1)

    addtodictbut = tk.Button(addproductwin, text="Добавить", bg='Yellow')
    addtodictbut.pack(side ='bottom', padx = 40, pady = 40)
    addtodictbut.bind('<ButtonPress>', func = lambda event: addtodict(productnameentry.get().replace(' ', ''),productcalentry.get().replace(' ',''), calcwin, addproductwin))
    # ------------------

def calculation(event):

    # ОКНО КАЛЬКУЛЯЦИИ
    # ------------------
    to60imglbl.configure(image = to60img)
    to60imglbl.image = to60img

    left90lbl.config(text= str(to60by90days) + ' cal', bg='#F0F0F0')

    left60lbl.config(text = str(to60by60days) + ' cal', bg = '#F0F0F0')

    calcwin = tk.Tk()
    calcwin.title('Рассчёт')
    calcwin.geometry(f'{h}x{w}+400+400')

    addcalcbut = tk.Button(calcwin, text = 'Выполнить вычисления', bg = 'Yellow')
    addcalcbut.pack(side='bottom', padx= 30, pady= 30)
    addcalcbut.bind('<ButtonPress>', func = lambda event: solve(whateatedfield.get(), to60by60days, to60by90days, calcwin))

    whateatedfield = ttk.Entry(calcwin)
    whateatedfield.pack(side='bottom')

    addproductbut = tk.Button(calcwin, text="Добавить продукт", bg='Yellow')
    addproductbut.pack(side = 'top', pady= 30)
    addproductbut.bind('<ButtonPress>',func = lambda event: addproduct(calcwin))

    for i in food:
        tk.Label(calcwin, text = i + ' - ' + str(food.get(i)) + ' cal', bg = 'Yellow').pack(anchor='w', padx = 10, pady = 10)
    # ------------------

def update():

    # ОБНОВЛЕНИЕ ТАЙМЕРА
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    delta = datetime.datetime(tomorrow.year,tomorrow.month,tomorrow.day) - datetime.datetime.now()
    timeleft = str(delta).split(".")[0]
    clock.config(text=timeleft)
    clock.after(1000,update)


if __name__ == '__main__':

    food = {
        'пельмени': 275,
        'дошик': 440,
        'макпоф': 196,
        'пицца': 2000,
    }

    to60by60days = 3550
    to60by90days = 3150

    #ГЛАВНОЕ ОКНО
    win = tk.Tk()
    h = 600
    w = 600
    winicon = tk.PhotoImage(file = 'icon.png')
    win.iconphoto(False, winicon)
    win.title('Калькулятор калорий')
    authorlbl = tk.Label(win, text='© made by DimaSICK Talybov', font=('tahoma', 10))
    authorlbl.pack(side='bottom')
    # win.iconphoto(False, winicon)
    # win.config(bg = '#59B4DB')
    # win.title('Калькулятор калорий')
    # win.geometry(f'{h}x{w}+200+100')
    # win.minsize(600,600)
    # win.maxsize(1000,800)

    #ВКЛАДКИ
    tab_control = ttk.Notebook(win)
    tab1 = ttk.Frame(tab_control)
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab1, text = 'FAQ')
    tab_control.add(tab2, text = 'Калькулятор')
    tab_control.pack(expand=1, fill="both")

    #ВКЛАДКА FAQ
    # ------------------
    #ГЛАВНАЯ НАДПИСЬ
    mainlbl = tk.Label(tab1, text = 'Welcome ту my приложение, humankind!', font=('device', 20, 'bold'), fg = 'blue')
    mainlbl.pack(side='top', pady = 15)

    #FRAME С FAQ
    faqfr = ttk.Frame(tab1, borderwidth=1, relief='solid', padding=[10, 10])
    faqfr.pack(side='top',fill='both',padx = 15, pady = 15, expand=1)

    mainlbl = tk.Label(faqfr, text='Как использовать приложение:', font=('device', 16, 'bold'))
    mainlbl.pack(side='top')

    with open('rules.txt', encoding='utf-8') as f:
        rules = f.read()
    ruleslbl = tk.Label(faqfr, text = rules, font=('device', 14))
    ruleslbl.pack(side='left')

    # ------------------



    #ВКЛАДКА КАЛЬКУЛЯТОР
    # ------------------
    #ОСТАВШИЕСЯ КАЛОРИИ(60ДНЕЙ)
    left60fr = ttk.Frame(tab2, borderwidth=1, relief='solid', padding=[8, 10])
    left60fr.pack(side='left', padx = 40)

    to60lbl = tk.Label(left60fr,text ='60кг за 60 дней', font=('device', 20, 'bold'))
    to60lbl.pack(side='top')

    left60lbl = tk.Label(left60fr,text =str(to60by60days) + ' cal', font=('device', 40, 'bold'), fg='blue')
    left60lbl.pack(side='left')

    # ОСТАВШИЕСЯ КАЛОРИИ(90ДНЕЙ)
    left90fr = ttk.Frame(tab2, borderwidth=1, relief='solid', padding=[8, 10])
    left90fr.pack(side='right', padx = 40)

    to90lbl = tk.Label(left90fr, text='60кг за 90 дней', font=('device', 20, 'bold'))
    to90lbl.pack(side='top')

    left90lbl = tk.Label(left90fr, text=str(to60by90days) + ' cal', font=('device', 40, 'bold'), fg = 'blue')
    left90lbl.pack(side='right')


    #ОСТАВШЕЕСЯ ВРЕМЯ
    timefr = ttk.Frame(tab2, relief='solid')
    timefr.pack(side='top', pady = 15)

    timelbl = tk.Label(timefr, text = 'До конца дня осталоось:',font=('device', 10, 'bold'))
    timelbl.pack(side='top',fill ='x')

    clock = tk.Label(timefr, font=('device', 40, 'bold'))
    clock.pack(side='top',fill ='x')
    update()

    #КНОПКА "НАЧАТЬ"
    mainbtn = tk.Button(tab2, text="Начать высчитывание калорий", bg='Yellow', height= 5, width= 25)
    mainbtn.pack(anchor='center', expand = 1)
    mainbtn.bind('<ButtonPress>', calculation)

    #КАРТИНКА
    photo60 = Image.open('by60.png')
    to60img = ImageTk.PhotoImage(photo60.resize((150,150)))
    to60imglbl = tk.Label(tab2, image = to60img)
    to60imglbl.pack(side = 'bottom', pady = 15)

    # ------------------

    win.mainloop()