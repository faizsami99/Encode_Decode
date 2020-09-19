import tkinter
import tkinter.filedialog as dil
import base64
import os
# variables
message = ""

# Functions


def Encode():
    global message
    message = TextArea.get("1.0", "end")
    message = bytes(message, 'utf-8')
    message = base64.b64encode(message)
    TextArea.delete("1.0", "end")
    TextArea.insert("1.0", message)
    print("i am Encode")


def Decode():
    global message
    message = TextArea.get("1.0", "end")
    message = bytes(message, 'utf-8')
    message = base64.b64decode(message)
    TextArea.delete("1.0", "end")
    TextArea.insert("1.0", message)


def Change_Encode():
    MyBtn.config(text="Encode", command=Encode)


def Change_Decode():
    MyBtn.config(text="Decode", command=Decode)


def openfile():
    global file
    file = dil.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                                   ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0, "end")
        with open(file, "r") as f:
            TextArea.insert(1.0, f.read())


def save():
    global file
    if file == None:
        file = dil.asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[
                                     ("All Files", "*.*"), ("Text Documents", "*.txt")])

        if file == "":
            file = None

        else:
            f = open(file, "w")
            f.write(TextArea.get(1.0, "end"))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")
    else:
        f = open(file, "w")
        f.write(TextArea.get(1.0, "end"))
        f.close()



root = tkinter.Tk()
root.geometry("700x530")
root.resizable(False, False)
root.title("Encoder Decoder")


# Button
MyBtn = tkinter.Button(root, text="Encode", font="times 13 bold",  width="90",
                       activeforeground="white", activebackground="red", bg="grey", fg="black", command=Encode)
MyBtn.pack(side="bottom")


# Menu bar
main_menu = tkinter.Menu(root)

option_menu = tkinter.Menu(main_menu, tearoff=0)
option_menu.add_command(label="Encode", command=Change_Encode)
option_menu.add_command(label="Decode", command=Change_Decode)
option_menu.add_command(label="Save", command=save)
option_menu.add_command(label="Open", command=openfile)
option_menu.add_command(label="Exit", command=quit)
main_menu.add_cascade(label="File", menu=option_menu)

root.config(menu=main_menu)


# Text Area
# text = tkinter.StringVar()
scrollbar = tkinter.Scrollbar(root)
scrollbar.pack(side="right", fill="y")
TextArea = tkinter.Text(root, font="lucida 13", yscrollcommand=scrollbar.set)
file = None
TextArea.pack(fill="both")
scrollbar.config(command=TextArea.yview)


root.mainloop()
