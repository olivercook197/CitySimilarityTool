from tkinter import *
import unidecode


class AutofillScreen:
    def __init__(self, root, df):
        self.type = type
        self.root = root
        self.df = df
        self.city = []


        start_typing_label = Label(root, text="Start typing...", font=("Helvetica", 14), fg="grey")
        start_typing_label.pack(pady=20)

        # create entry box
        global user_city_entry
        user_city_entry = Entry(root, font=("Helvetica", 20))
        user_city_entry.pack()

        # create listbox
        global city_name_listbox
        city_name_listbox = Listbox(root, width=50)
        city_name_listbox.pack(pady=40)

        # create OK button
        global ok_button_autofill
        c = []
        ok_button_autofill = Button(root, text="OK", command=lambda: c == AutofillScreen.ok_button_autofill_pressed(self))
        ok_button_autofill.pack()

        # create a list of city names
        global id_city_country_names
        id_city_country_names = []

        line_count = 0
        for city in df.iterrows():
            id_city_country_names.append([city[1][0], city[1][3], city[1][4]])
            line_count += 1

        update(id_city_country_names)

        # create a binding on the listbox on click
        city_name_listbox.bind("<<ListboxSelect>>", fillout)

        # create binding on the entry box
        user_city_entry.bind("<KeyRelease>", check)

    @staticmethod
    def ok_button_autofill_pressed(self):
        global selection
        global data
        data = []
        try:
            for item in id_city_country_names:
                if selection[0].lower() in item[1].lower() or selection[0].lower() in unidecode.unidecode(
                        item[1].lower()):
                    if selection[1].lower() in item[2].lower() or selection[1].lower() in unidecode.unidecode(
                            item[2].lower()):
                        data.append(item)
            print(data)
            if len(data) == 1:
                for widget in self.root.winfo_children():
                    widget.destroy()
                self.city = data



        except:
            error_window = Tk()
            error_window_text = Label(error_window, text="Invalid selection, please click on the city you would like.")
            error_window_text.pack()
            ok_error_window_button = Button(error_window, text="OK", command=error_window.destroy)
            ok_error_window_button.pack()
            selection = None


# update the listbox
def update(data):
    # clear listbox
    city_name_listbox.delete(0, END)
    # add cities to listbox
    for item in data:
        city_name_listbox.insert(END, item[1] + " (" + item[2] + ")")


# update entry box with listbox clicked
def fillout(event):
    # delete whatever is in the entry box
    user_city_entry.delete(0, END)
    # add clicked item to entry box
    user_city_entry.insert(0, city_name_listbox.get(ANCHOR))
    global selection
    selection = user_city_entry.get()
    selection = selection.split('(')
    selection[0] = selection[0][:-1]
    selection[1] = selection[1][:-1]


# create function to check entry vs listbox
def check(event):
    # grab what was typed
    typed = user_city_entry.get()

    if typed == "":
        data = id_city_country_names
    else:
        data = []
        for item in id_city_country_names:
            if typed.lower() in item[1].lower() or typed.lower() in unidecode.unidecode(item[1].lower()) or \
                    typed.lower() in item[2].lower() or typed.lower() in unidecode.unidecode(item[2].lower()):
                data.append(item)

    # update listbox with selected items
    update(data)

