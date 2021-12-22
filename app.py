from tkinter import *
from tkinter import messagebox
import bidi.algorithm as bidi
def Collect():
    try:
        carrort_num = int(Entry_carrot.get())
        corn_num = int(Entry_corn.get())
        garlic_num  =  int(Entry_garlic.get())
        #prices
        carrot_price = 0.200 * carrort_num
        corn_price = 0.400 * corn_num
        garlic_price = 0.500 * garlic_num
        price = corn_price + carrot_price + garlic_price
        print("corn price : {} , carrot price {}, garlic price {}".format(corn_price, carrot_price, garlic_price))
        print("Total price: {}".format(price))
        #messagebox.showinfo("Collected","{} Omani rial.".format(price))
        collect_lbl.config(text="Collected, {} Omani rial.".format(price), fg= "green")
    except:
        print("Error")
        collect_lbl.config(text="Price Error", fg= "red")
        #messagebox.showerror("Error","Price Error")
        


#window
window  = Tk()
window.title("super market")
window.geometry("1280x800")
#-----------------------
#lbl_names
lbl_carrot = Label(text=bidi.get_display("Carrot-جزر"),font="arial")
lbl_carrot.grid(row=0,column=0)

lbl_corn = Label(text=bidi.get_display("Corn-ذرة"),font="arial")
lbl_corn.grid(row=0,column=1)

lbl_corn = Label(text=bidi.get_display("Garlic-ثوم"),font="arial")
lbl_corn.grid(row=0,column=2)


#--------------------------
#entrys
Entry_carrot = Entry(font="arial", justify="center")
Entry_carrot.grid(row=1,column=0,padx=10)
Entry_carrot.insert("end","0")

Entry_corn = Entry(font="arial", justify="center")
Entry_corn.grid(row=1,column=1,padx=10)
Entry_corn.insert("end","0")

Entry_garlic = Entry(font="arial", justify="center")
Entry_garlic.grid(row=1,column=2,padx=10)
Entry_garlic.insert("end","0")


#Collect button
Collect_btn = Button(text=bidi.get_display("Collect-جمع"),command=Collect)
Collect_btn.place(x=640,y=720)
#collect show
collect_lbl = Label(text="",font="arial")
collect_lbl.place(x = 600, y= 760)



if __name__ == "__main__":
    window.mainloop()