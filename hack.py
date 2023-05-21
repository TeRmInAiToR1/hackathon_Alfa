from tkinter import *
from tkinter.ttk import Combobox
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

year_int = []
fio_arr = []


def search_year():
    id_exep = []
    count_fo_ex = 0
    for j in range(714):
        gg = fil.bithday[j]  # стрчка
        # print(gg)
        year = ""
        count = 0
        count_num = 0;
        for i in gg:  # элемент
            # print(i, " - ", count)
            if count == 2:
                year += i
                count_num += 1
            if i == ".":
                count += 1
            if i == '-':
                # print(count_fo_ex)
                id_exep.append(count_fo_ex)

            if count_num == 4:
                count_num = 0
                count = 0
                year_int.append(2023 - int(year))
                year = ""
                # print(year_int)
        count_fo_ex += 1

    count_fo_exep = 0
    cc = 0
    str_fio = ""
    for j in range(714):
        count_fo_exep += 1
        ff = fio.FIO[j]

        for i in ff:  # элемент

            # print(str_fio, " - ", i)
            if count_fo_exep > 1 and i == "Ф" and count_fo_exep != id_exep[cc]:
                # print(str_fio)
                fio_arr.append(str_fio)
                str_fio = ""
            elif count_fo_exep == id_exep[cc] and len(id_exep) - 1 > cc:
                # print(len(id_exep))
                # print(cc)
                cc += 1
                str_fio = ""

            str_fio += i

    # print(len(year_int))
    # for j in range(len(fio_arr)):
    #   print(fio_arr[j])

    # print(gg)
    # gg[4]


def clicked():
    if combo.get() == "Компетенции":
        y = 3
    if combo.get() == "Категория":
        y = 4
    if combo.get() == "Должность":
        y = 5
    if comboX.get() == "Компетенции":
        x = 3
    if comboX.get() == "Категория":
        x = 4
    if comboX.get() == "Должность":
        x = 5
    if combo.get() == "Возраст":
        y = 9
    if comboX.get() == "Возраст":
        x = 9
    if combo.get() == "Пол":
        y = 1
    if comboX.get() == "Пол":
        x = 1
    if combo.get() == "Образование":
        y = 11
    if comboX.get() == "Образование":
        x = 11
    if comboGR.get() == "Круговой(ox)":
        fig = px.pie(upd_df, names=x)
        fig.show()
    elif comboGR.get() == "Линия":
        fig = px.line(upd_df, x=x, y=y)
        fig.show()
    elif comboGR.get() == "Столбик":
        fig = px.histogram(upd_df, x=x, y=y)
        fig.show()
    elif comboGR.get() == "Скрипичный":
        fig = px.violin(upd_df, x=x, y=y)
        fig.show()


path = r'C:\Users\danil\Downloads\Telegram Desktop\utf.csv'
df = pd.read_csv(path, sep=';', header=None)

df.columns = ['FIO', 'pol', 'role', 'spisol', 'kat', 'dolzh', 'nach_trud_st', 'working_place', 'prof', 'bithday',
              'nach_tru_de', 'edu', 'edu_place', 'gr_year', 'spec', '1', '2', '3', '4', '5', '6', '7', '8']

with open(path, 'r', encoding='utf-8') as f:
    with open("upd_utf1.csv", 'w', encoding='utf-8') as f1:
        next(f)  # skip header line
        for line in f:
            f1.write(line)

upd_df = pd.read_csv("upd_utf1.csv", sep=';', header=None)

fil = df[['bithday']]
fio = df[['FIO']]

# path_new = r'C:\Users\danil\Downloads\Telegram Desktop\rad_control.csv'
# df_new = pd.read_csv(path_new, sep=';', header=None)

# with open(path_new,'r',encoding='utf-8') as f:
#    with open("upd_rad_control.csv",'w',encoding='utf-8') as f1:
#        next(f) # skip header line
#        for line in f:
#            f1.write(line)

# upd_df_new = pd.read_csv("upd_rad_control.csv", sep=';', header=None)
# results = upd_df_new[[0]]
# print(results)


##print(results)

# categories = ['Результат','Результат 2','Результат 3',
#              'Результат 4', 'Результат 5']

# fig = go.Figure()

# fig.add_trace(go.Scatterpolar(
#      r=[1, 5, 2, 2, 4],
#      theta=categories,
#      fill='toself',
#      name='Участник 1'
# ))
# fig.add_trace(go.Scatterpolar(
#      r=[4, 3, 2.5, 1, 3.3],
#      theta=categories,
#      fill='toself',
#      name='Участник 2'
# ))

# fig.update_layout(
#  polar=dict(
#    radialaxis=dict(
#      visible=True,
#      range=[0, 5]
#    )),
#  showlegend=False
# )

# fig.show()


window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('400x250')

combo = Combobox(window)
combo['values'] = ("Компетенции", "Категория", "Пол", "Должность", "Возраст", "Образование")
combo.current(0)  # установите вариант по умолчанию
combo.grid(column=0, row=40)
comboX = Combobox(window)
comboX['values'] = ("Компетенции", "Категория", "Пол", "Должность", "Возраст", "Образование")
comboX.current(0)  # установите вариант по умолчанию
comboX.grid(column=0, row=10)
comboGR = Combobox(window)
comboGR['values'] = ("Круговой(ox)", "Линия", "Столбик(ox)", "Скрипичный")
comboGR.grid(column=0, row=60)
comboGR.current(0)
lbl = Label(window, text="Укажите ось OX")
lbl.grid(column=0, row=0)
lbl2 = Label(window, text="Укажите ось OY")
lbl2.grid(column=0, row=30)
lbl3 = Label(window, text="Тип Графика")
lbl3.grid(column=0, row=50)
btn = Button(window, text="Подтвердить", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()