from tkinter import*
from PIL import Image, ImageTk
from tkinter.messagebox import *
import json
root = Tk()
root.title("Steam")
root.geometry('1920x1080')
#Frame Menyu
frame_menu = Frame(root,width = 1920,height = 1080,bg ='#0f1948')
frame_menu.place(x=1,y=1)
#Frame Login
frame_login = Frame(root,width=1920,height=1080)
frame_login.config(background="#0f1948")
#Frame Registration
frame_registration = Frame(root,width = 1920,height = 1080,bg = '#0f1948')
frame_registration.config(background="#0f1948")
#Frame Account Info
frame_acc_info = Frame(root,width=1920,height=1080,bg="#0f1948")
frame_acc_info.config(background="#0f1948")
#Frame Library
frame_libriary = Frame(root,width=1920,height=1080,bg="#0f1948")
frame_libriary.config(background="#0f1948")

def main_menu():
    frame_menu.place_forget()
    root.geometry('1920x1080')
    frame_login.place(relx=0,rely=0.1)
    frame_menu.pack()

def Registration():
    frame_login.place_forget()
    frame_registration.place(relx=0,rely=0)

def open_library():
    for widget in frame_libriary.winfo_children():
        widget.destroy()
    Button(frame_libriary, text="Return", fg="#ffffff", background="#0f1948", border=0, font="Arial 15", command=open_menu).place(relx=0.02, rely=0.01)

    if Login_lbl["text"] != "":
        frame_menu.place_forget()
        frame_libriary.place(relx=0, rely=0)

        with open("Files/son.json", "r") as FileHandler:
            users = json.loads(FileHandler.readline())

        user = users[Login_lbl["text"]]
        check_list = [False, False, False, False]
        names_list = []

        coords = [[0.05, 0.1], [0.05, 0.6], [0.55, 0.1], [0.55, 0.6]]
        for i in range(len(user["games"])):
            image_1 = Image.open(user["games"][i][1])
            resized_image_1 = image_1.resize((350, 250))
            photo_image_1 = ImageTk.PhotoImage(resized_image_1)
            Label_img = Label(frame_libriary, image=photo_image_1, anchor=NW, highlightthickness=0, border=0)
            Label_img.image = photo_image_1
            Label_img.place(relx=coords[i][0], rely=coords[i][1])

            image_2 = Image.open(user["games"][i][2])
            resized_image_2 = image_2.resize((350, 500))
            photo_image_2 = ImageTk.PhotoImage(resized_image_2)
            Label_img = Label(frame_libriary, image=photo_image_2, anchor=NW, border=0)
            Label_img.image = photo_image_2
            Label_img.place(relx=coords[i][0]+0.2, rely=coords[i][1])
            check_list[i] = True
            names_list.append(user["games"][i][0])

        if check_list[0]:
            Button(frame_libriary, text=f"Удалить {names_list[0]}", command=lambda: delete_game(names_list[0]), border=0, background="red", fg="white", font="Arial 17", anchor=CENTER, width=24, height=2).place(relx=0.05 + 0.01, rely=0.1 + 0.3)
        if check_list[1]:
            Button(frame_libriary, text=f"Удалить {names_list[1]}", command=lambda: delete_game(names_list[1]), border=0, background="red", fg="white", font="Arial 17", anchor=CENTER, width=24, height=2).place(relx=0.05 + 0.01, rely=0.6 + 0.3)
        if check_list[2]:
            Button(frame_libriary, text=f"Удалить {names_list[2]}", command=lambda: delete_game(names_list[2]), border=0, background="red", fg="white", font="Arial 17", anchor=CENTER, width=24, height=2).place(relx=0.55 + 0.01, rely=0.1 + 0.3)
        if check_list[3]:
            Button(frame_libriary, text=f"Удалить {names_list[3]}", command=lambda: delete_game(names_list[3]), border=0, background="red", fg="white", font="Arial 17", anchor=CENTER, width=24, height=2).place(relx=0.55 + 0.01, rely=0.6 + 0.3)

    else:
        showerror("Error", "Вы не зашли в аккаунт")

def open_menu():
    frame_libriary.place_forget()
    frame_login.place_forget()
    frame_menu.place(relx=0, rely=0)

def open_login():
    frame_registration.place_forget()
    frame_login.place(relx=0, rely=0)

Button(frame_login, text="Return", fg="#ffffff", background="#0f1948", border=0, font="Arial 15", command=open_menu).place(relx=0.02, rely=0.01)
Button(frame_registration, text="Return", fg="#ffffff", background="#0f1948", border=0, font="Arial 15", command=open_login).place(relx=0.02, rely=0.01)


def delete_game(game):
    with open("Files/son.json", "r") as FileHandler:
        users = json.loads(FileHandler.readline())

    user = users[Login_lbl["text"]]

    for i in user["games"]:
        if i[0] == game:
            users[Login_lbl["text"]]["games"].remove(i)

    try:
        with open("Files/son.json", "wb") as FileHandler:
            json.dump({}, FileHandler)
    except Exception as e:
        print("OK")

    with open("Files/son.json", "w") as FileHandler:
        json.dump(users, FileHandler)

    open_library()


def back_to_menyu():
    with open("Files/son.json", "r")as FileHandler:
        users = json.loads(FileHandler.readline())
    for i in users.values():
        if i ["login"] == entry1.get() and i["password"] == entry2.get():
            frame_login.place_forget()
            frame_menu.place(relx=0, rely=0)
            user={
                "login": i["login"],
                "password": i ["password"],
                "gmail": i ["gmail"]
            }
            acc_open(user)
def acc_open(user):
    global isLogined
    isLogined =True
    frame_menu.place_forget()
    frame_login.place_forget()
    frame_acc_info.place(relx=0,rely=0)
    Login_lbl["text"]= user["login"]
    Gmail_lbl["text"]= user["gmail"]

    login_label = Label(frame_acc_info, text=f"Добро пожаловать, {user['login']}!", font="Arial 18 bold", bg="#0f1948",fg="white")
    login_label.place(relx=0.5, rely=0.1, anchor="center")
    gmail_label = Label(frame_acc_info, text=f"Ваш email: {user['gmail']}", font="Arial 14 bold", bg="#0f1948",fg="white")
    gmail_label.place(relx=0.5, rely=0.150, anchor="center")
    logout_button = Button(frame_acc_info, text="Выйти", font="Arial 12 bold", bg="yellow", command=logout)
    logout_button.place(relx=0.4, rely=0.085, anchor="center")

Login_lbl = Label(frame_menu,text = "",font= "Arial 14 bold",bg="#0f1948",fg="White")
Login_lbl.place(relx=0.900,rely=0.050)
Gmail_lbl=Label(frame_menu,text= "",font="Arial 14 bold",bg="#0f1948",fg="White")
Gmail_lbl.place(relx=0.900,rely=0.030)

def logout():

    global isLogined
    isLogined = False
    frame_acc_info.place_forget()
    frame_menu.place(relx=0, rely=0)

def register():
    if "@gmail.com" in entry_G.get():
        print(entry_G.get())
    else:
        showerror("Error", "Пожалуйста добавьте маил")
    if len(entry_P.get()) > 8:
        print(entry_P.get())
    else:
        showerror("Error","Колличество символов должно быть больше 8")
    if entry_CP.get() == entry_P.get():
        print(entry_CP.get())
    else:
        showerror("Error", "Пароль не совпадают")

    user = {
        "gmail":entry_G.get(),
        "login":entry_L.get(),
        "password":entry_P.get(),
        "games":[]
    }

    with open("Files/son.json", "r")as FileHandler:
        users=json.loads(FileHandler.readline())

    users[entry_L.get()] = user

    with open("Files/son.json", "w")as FileHandler:
        json.dump(users,FileHandler)
    frame_registration.place_forget()
    frame_login.place(relx=0,rely=0)

#Registration Board

lbl_G = Label(frame_registration,text = "GMAIL",font= "Arial 14 bold",bg="#0f1948",fg="Yellow")
lbl_G.place(relx=0.440,rely=0.200)
entry_G = Entry(frame_registration,font="Arial 14 bold")
entry_G.place(relx=0.440,rely=0.225,height=30)
lbl_L = Label(frame_registration,text = "LOGIN",font= "Arial 14 bold",bg="#0f1948",fg="Yellow")
lbl_L.place(relx=0.440,rely=0.255)
entry_L = Entry(frame_registration,font="Arial 14 bold")
entry_L.place(relx=0.440,rely=0.280)
lbl_P = Label(frame_registration,text="PASSWORD",font= "Arial 14 bold",bg="#0f1948",fg="Yellow")
lbl_P.place(relx=0.440,rely=0.310)
entry_P = Entry(frame_registration,font="Arial 14 bold")
entry_P.place(relx=0.440,rely=0.335)
lbl_CP = Label(frame_registration,text="CONFIRM PASSWORD",font= "Arial 14 bold",bg="#0f1948",fg="Yellow")
lbl_CP.place(relx=0.440,rely=0.360)
entry_CP = Entry(frame_registration,font="Arial 14 bold")
entry_CP.place(relx=0.440,rely=0.385)
btn = Button(frame_registration,text="Press for Registration",width=15,height=2,command=register)
btn.place(relx=0.465,rely=0.415)

def enter_account():
    frame_menu.place_forget()
    frame_login.place(relx=0,rely=0)

def exit_login():
    frame_login.place_forget()
    frame_menu.place(relx= 0,rely = 0)

def exit_libriary():
    frame_libriary.place_forget()
    frame_menu.place(relx= 0,rely = 0)


def switch():
    if int_var.get() == 1:
         entry2 ['show'] = '*'
    else:
         entry2 ['show'] = ''

def clear():
    entry2.delete(0,'end')
    entry1. delete(0,'end')

def Photo0():
    ...

def Login():
    if entry1.get() == entry_L.get():
        print("OK")
    else:
        showerror("Error","Логин не верный, пожалуйста повторите попытку")
        return
    if entry2.get() == entry_P.get():
        print("OK")
    else:
        showerror("Error","Пороль введен не правельно, пожалуйста повторите попытку")
        return


# Вход в Магазин

lbl1 = Label(frame_login,text="Login",font="Arial 14 bold",bg="#0f1948",fg="Yellow")
lbl1.place(relx=0.480,rely=0.390)
entry1 = Entry(frame_login,font= "Arial 14")
entry1.place(relx=0.455,rely=0.415,height=20)
entry1.config(width=15)

lbl2 = Label(frame_login,text="Password",font="Arial 14 bold",bg="#0f1948",fg="Yellow")
lbl2.place(relx=0.470,rely=0.440)
entry2 = Entry(frame_login,font= "Arial 14")
entry2.place(relx=0.455,rely=0.465,height=20)
entry2.config(width=15)

btn1 = Button(frame_login,text="Registration",font="Arial 12 bold",bg="Yellow",command=Registration)
btn1.place(relx=0.455,rely=0.490)
btn2 = Button(frame_login,text = "Enter",font="Arial 12 bold",bg= "Yellow",command=back_to_menyu)
btn2.place(relx=0.515,rely=0.490)

int_var = IntVar()
check_btn = Checkbutton(frame_login, text='Switch states', variable=int_var, command=switch, font="Arial 10 bold", width=10,fg="Black")
check_btn.place(relx=0.470, rely=0.530)


# Список с играми
img1 = Image.open("Photo/steam-icon-2048x2048-rbyixh0f.png")
resized_image = img1.resize((150, 100))
photo = ImageTk.PhotoImage(resized_image)
label1 = Label(frame_menu, image=photo)
label1.image = photo
label1.place(relx=0, rely=0)

def move_to_library():
    label3.place_forget()
    label3.place(relx=0.184, rely=0.120)

def remove_from_library():
    label3.pack_forget()


library_games = []

# Функция для добавления игры в библиотеку
def add_to_library(game,img_1, img_2):
    with  open ("Files/son.json", "r") as FileHandler:
        users = json.loads(FileHandler.readline())
    if Login_lbl["text"] != "":
        user = users[Login_lbl["text"]]
        for i in user["games"]:
            if i[0] == game:
                showerror("Error", "Такая игра уже есть.")
                return

        users[Login_lbl["text"]]["games"].append([game, img_1, img_2])
        showinfo("Success", "Игра успешно добавлена.")
        print(users)
        try:
            with open("Files/son.json", "wb") as FileHandler:
                json.dump({}, FileHandler)
        except Exception as e:
            print("OK")


        with open("Files/son.json", "w") as FileHandler:
            json.dump(users, FileHandler)
    else:
        showerror("Error", "Вы не зашли в аккаунт.")
        return





# Функция для удаления игры из библиотеки
def remove_from_library():
    if library_games:
        library_games.pop()
        update_library()

# Функция для обновления содержимого frame_libriary на основе списка library_games
def update_library():
    for widget in frame_libriary.winfo_children():
        widget.destroy()
    row = 0
    col = 0
    for game_name, image_path in library_games:
        img3 = Image.open("Photo/Capture3.PNG")
        resized_image = img.resize((150, 100))
        photo = ImageTk.PhotoImage(resized_image)
        labe3 = Label(frame_libriary, image=photo3)
        labe3.image = photo3
        label3.pack(side=LEFT, padx=5, pady=5)
        col += 1
        if col > 3:
            col = 0
            row += 1

btn_exit_library = Button(frame_libriary, text="Exit Library", font="Arial 12 bold", borderwidth=4, command=exit_libriary)
btn_exit_library.place(relx=0.9, rely=0.030)
btn_exit_Login = Button(frame_login, text="Exit Library", font="Arial 12 bold", borderwidth=4, command= exit_login)
btn_exit_library.place(relx=0.9, rely=0.030)
# Photo of gane "Vrising"
img3 = Image.open("Photo/Capture3.PNG")
resized_image3 = img3.resize((420,200))
photo3 = ImageTk.PhotoImage(resized_image3)
label3=Label(frame_menu, image=photo3)
label3.image=photo3
label3.place(relx=0.184, rely=0.120)

# Button for Game "Vrising"
btn_capture3 = Button(frame_menu,text="Buy\n 'Vrising' ",font="Arial 12 bold",borderwidth=4,width=10,height=5,fg="red",command = lambda:add_to_library("Vrising","Photo/Capture3.PNG", "Photo/capture 5.jpg")).place(relx =0.650,rely = 0.170)
btn_remove_from_library = Button(frame_libriary, text="Remove from Library", font="Arial 12 bold", borderwidth=4, width=20, height=2, fg="red", command=remove_from_library)
btn_remove_from_library.place(relx=0.5, rely=0.9)

# Photo for game "It takes two"
img2 = Image.open("Photo/Capture.PNG")
resized_image2 = img2.resize((420,200))
photo1 = ImageTk.PhotoImage(resized_image2)
label2 = Label(frame_menu, image=photo1)
label2.image=photo1
label2.place(relx=0.184, rely=0.310)

# Button for Game "It takes two"
btn_capture = Button(frame_menu,text="Buy \n'It takes Two' ",font="Arial 12 bold",borderwidth=4,width=10,height=5,fg="red", command=lambda:add_to_library("It Takes Two","Photo/Capture.PNG", "Photo/capture 6.png")).place(relx =0.650,rely = 0.350)

# Photo for game "Assasian Creed"
img4 = Image.open("Photo/capture 4.png")
resized_image4 = img4.resize((420,200))
photo4 = ImageTk.PhotoImage(resized_image4)
label4=Label(frame_menu, image=photo4)
label4.image=photo4
label4.place(relx=0.184, rely=0.500)

# Button of Game "Assasian Creed"
btn_capture4 = Button(frame_menu,text="Buy\n 'Assasian Creed' ",font="Arial 12 bold",borderwidth=4,width=12,height=5,fg="red", command=lambda:add_to_library("Assassin's Creed","Photo/capture 4.png", "Photo/capture 5x5.png")).place(relx =0.650,rely = 0.550)

# Photo for game "Batman"
img = Image.open("Photo/cature 8.png")
resized_image0 = img.resize((420,200))
photo0 = ImageTk.PhotoImage(resized_image0)
label0 = Label(frame_menu, image=photo0)
label0.image = photo0
label0.place(relx=0.184, rely=0.690)

# Button for game "Batman"
btn_capture8 = Button(frame_menu,text= "Buy\n'Batman\nArham Night'",font="Arial 12 bold",borderwidth=4,width=12,height=5,fg="red", command=lambda:add_to_library("Batman","Photo/cature 8.png", "Photo/cature 8x8.png")).place(relx =0.650,rely = 0.750)

img5 = Image.open("Photo/capture 5.jpg")
resized_image5 = img5.resize((400,200))
photo5 = ImageTk.PhotoImage(resized_image5)
label5=Label(frame_menu, image=photo5)
label5.image=photo5
label5.place(relx=0.405, rely=0.120)

img6 = Image.open("Photo/capture 6.png")
resized_image6 = img6.resize((400,200))
photo6 = ImageTk.PhotoImage(resized_image6)
label6=Label(frame_menu, image=photo6)
label6.image=photo6
label6.place(relx=0.405, rely=0.310)


img7 = Image.open("Photo/capture 5x5.png")
resized_image7 = img7.resize((400,200))
photo7 = ImageTk.PhotoImage(resized_image7)
label7=Label(frame_menu, image=photo7)
label7.image=photo7
label7.place(relx=0.405, rely=0.500)

img = Image.open("Photo/cature 8x8.png")
resized_image0 = img.resize((400,200))
photo0 = ImageTk.PhotoImage(resized_image0)
label0 = Label(frame_menu, image=photo0)
label0.image = photo0
label0.place(relx=0.405, rely=0.690)

# Виджеты для переходов страниц
Bt_Shop= Button(frame_menu,text = "Shop",font="Arial 12 bold",borderwidth=4).place(relx=0.35,rely =0.030)
Btn_Library = Button(frame_menu,text="Library",font="Arial 12 bold",borderwidth=4,command = open_library).place(relx=0.45,rely=0.030)
Btn_Account = Button(frame_menu,text="Account",font="Arial 12 bold",borderwidth=4,command= enter_account).place(relx=0.55,rely=0.030)
Btn_Exit = Button(frame_menu,text="Exit",font="Arial 12 bold",borderwidth=4,).place(relx=0.65,rely=0.030)

isLogined = False
root.mainloop()



