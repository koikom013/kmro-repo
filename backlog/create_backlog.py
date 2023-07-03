import tkinter as tk
from tkinter import ttk , messagebox
from tkcalendar import DateEntry
from PIL import ImageTk, Image

import customtkinter

root = tk.Tk()
root.geometry('800x600+600+200')
root.title('Backlog Management System')
root.resizable(False, False)

icon_path = r"kmro-repo\backlog\assets\icon.ico"
root.iconbitmap(icon_path)

bg_color = '#140A9A' #Gloria Blue
bg_color2 = '#E1E1E1' #Light Gray

image = Image.open(r"kmro-repo\backlog\assets\logo.png")
image = image.resize((149, 30))

photo = ImageTk.PhotoImage(image)


    

#--- Functions ---
       
def create_backlog_window():

    def on_closing():
        window.destroy()
        root.deiconify()

    def add_to_parts():
        pnumber_value = en_pnumber.get()
        pname_value = en_pname.get()
        quantity_value = en_quantity.get()

        if not pnumber_value or not pname_value or not quantity_value:
            messagebox.showinfo("Error", "All values must be provided.")
            return

        table.insert("", "end", values=(pnumber_value,pname_value, quantity_value))

        en_pnumber.delete(0, "end")
        en_pname.delete(0, "end")
        en_quantity.delete(0, "end")

    def remove_parts():
        selected_rows = table.selection()

        if not selected_rows:
            messagebox.showinfo("Error", "No row selected.")
        else:
            # Confirm deletion
            confirmation = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete the selected row(s)?")

            if confirmation:
                # Delete selected row(s) from the table and CSV file
                for row in selected_rows:
                    table.delete(row)

    root.withdraw()  # Hide the old window
    window = tk.Toplevel()
    window.geometry('800x600+600+200')
    window.iconbitmap(icon_path)
    

    frame1 = tk.Frame(window,height=60,width=800,bg=bg_color)
    frame1.pack()
    frame1.grid_propagate(False)

    frame2 = tk.Frame(window,height=400,width=800,bg=bg_color2)
    frame2.pack()
    frame2.grid_propagate(False)

    frame3 = tk.Frame(window,height=600,width=800,bg=bg_color2)
    frame3.pack()
    frame3.pack_propagate(False)


    lb_title = tk.Label(frame1,text='Backlog Management System',font=('Arial', 20, 'bold'),bg=bg_color,fg='white')
    lb_title.grid(row=0,column=0,padx=10,pady=(0,10))

    lb_logo = tk.Label(frame1, image=photo,bg=bg_color,width=191,height=50)
    lb_logo.grid(row=0,column=4, sticky='e',padx=(200,0),pady=(0,15))

    #--- Machine Details ---

    lb_subtitle = tk.Label(frame2,text='Machine Details',font=('Arial', 16, 'bold'),bg=bg_color2)
    lb_subtitle.grid(row=0,column=0, columnspan=3,sticky='w',pady=(20,0),padx=10)

    lb_unit = tk.Label(frame2,text='Unit ID',bg=bg_color2,width=12)
    lb_unit.grid(row=1,column=0,sticky='e')

    en_unit = ttk.Entry(frame2)
    en_unit.grid(row=1,column=1)

    lb_smr = tk.Label(frame2,text='SMR',bg=bg_color2,width=12)
    lb_smr.grid(row=1,column=2,sticky='e')

    en_smr = ttk.Entry(frame2)
    en_smr.grid(row=1,column=3)

    lb_inspdate = tk.Label(frame2,text='Inspection Date',bg=bg_color2,width=12)
    lb_inspdate.grid(row=1,column=4,sticky='e')

    en_inspdate = DateEntry(frame2, width=30)
    en_inspdate.grid(row=1,column=5, columnspan=2)

    #--- Parts List ---
            
    lb_subtitle2 = tk.Label(frame2,text='Parts List',font=('Arial', 16, 'bold'),bg=bg_color2)
    lb_subtitle2.grid(row=2,column=0,sticky='w',columnspan=3,pady=(20,0),padx=10)

    lb_pnumber = tk.Label(frame2,text='Part Number',bg=bg_color2,width=12)
    lb_pnumber.grid(row=3,column=0,sticky='e')

    en_pnumber = ttk.Entry(frame2)
    en_pnumber.grid(row=3,column=1)

    lb_pname = tk.Label(frame2,text='Part Name',bg=bg_color2,width=12)
    lb_pname.grid(row=3,column=2,sticky='e')

    en_pname = ttk.Entry(frame2)
    en_pname.grid(row=3,column=3)

    lb_quantity = tk.Label(frame2,text='Quantity',bg=bg_color2,width=12)
    lb_quantity.grid(row=3,column=4,sticky='e')

    en_quantity = ttk.Entry(frame2)
    en_quantity.grid(row=3,column=5)

    bt_parts = customtkinter.CTkButton(frame2,text='Add',command=add_to_parts,width=65,fg_color=bg_color)
    bt_parts.grid(row=3,column=6,padx=(5,0))

    bt_remove = customtkinter.CTkButton(frame2,text='Remove',command=remove_parts,width=65,fg_color=bg_color)
    bt_remove.grid(row=3,column=7,padx=(5,0))


    table = ttk.Treeview(frame2, columns=("Part_Number",'Part_Name', "Quantity"), show="headings")
    table.heading("Part_Number", text="Part Number")
    table.heading("Part_Name", text="Part Name")
    table.heading("Quantity", text="Quantity") 

    table.column('Part_Number',width=300)
    table.column('Part_Name',width=300)
    table.column('Quantity',width=175)
    table.grid(row=4,column=0,pady=(20,10),padx=10,columnspan=8)

    bt_submit = customtkinter.CTkButton(frame3,text='Create Backlog',fg_color=bg_color)
    bt_submit.pack(pady=(20,0))

    window.protocol("WM_DELETE_WINDOW", on_closing)

def homepage():
    bt_create = tk.Button(root,text='Create Backlog',command=create_backlog_window)
    bt_create.pack()


if __name__=='__main__':
    homepage()
    root.mainloop()