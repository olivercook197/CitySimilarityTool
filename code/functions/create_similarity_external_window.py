from tkinter import *


def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=window.winfo_width(), height=280)


def data(similarities):
    for i in range(0, len(similarities)):
        Label(frame, text=f"{similarities[i][0]}, {similarities[i][1]}", font=("Helvetica", 15)).grid(row=i, column=0)
        Label(frame, text=f"{round(similarities[i][2], 3)}", font=("Helvetica", 15)).grid(row=i, column=1)



def create_window(similarities, similarity_chosen, main_city):
    global canvas
    global window
    global frame
    max_line_length = 0
    for i in range(0, len(similarities)):
        if len(similarities[i][0] + similarities[i][1]) > max_line_length:
            max_line_length = len(similarities[i][0] + similarities[i][1])

    geometry = f"{max_line_length * 15 + 50}x{len(main_city['city_localisation'] + main_city['country_localisation']) * 2 + 400}"

    window = Tk()
    window.geometry(geometry)
    window.update_idletasks()

    myframe = Frame(window, relief=GROOVE, height=280, bd=1)
    myframe.pack()
    canvas = Canvas(myframe)
    frame = Frame(canvas, width=window.winfo_width())
    myscrollbar = Scrollbar(myframe, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=myscrollbar.set)

    similarity_label = Label(myframe,
                             text=f"Cities with at least a {similarity_chosen} similarity to {main_city['city_localisation']}, {main_city['country_localisation']}",
                             font=("Helvetica", 18), wraplengt=window.winfo_width() - 10).pack(side=TOP, pady=5)

    myscrollbar.pack(side="right", fill="y")
    canvas.pack(side="left")
    canvas.create_window((0, 0), window=frame, anchor='nw')
    frame.bind("<Configure>", myfunction)

    total_number_of_cities_label = Label(window, text=f"Total number of cities: {len(similarities)}",
                                         font=("Helvetica", 16)).pack(pady=5)
    close_button = Button(window, text="Close", command=window.destroy).pack()

    data(similarities)