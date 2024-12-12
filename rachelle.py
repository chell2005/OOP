from tkinter import *
import sqlite3

root = Tk()
root.title('Business_info')
root.geometry("600x600")
root.config(bg='sky blue')

conn = sqlite3.connect('D:/paylz_ni_maryana/business_info.db')
c = conn.cursor()

def submit():
    conn = sqlite3.connect('D:/paylz_ni_maryana/business_info.db')
    c = conn.cursor()
    c.execute("INSERT INTO business_info VALUES (:fname, :lname, :age, :b_name, :address, :p_number)",
              {
                  'fname': fname.get(),
                  'lname': lname.get(),
                  'age': age.get(),
                  'b_name': b_name.get(),
                  'address': address.get(),
                  'p_number': p_number.get(),
              })
    conn.commit()
    conn.close()

    fname.delete(0, END)
    lname.delete(0, END)
    age.delete(0, END)
    b_name.delete(0, END)
    address.delete(0, END)
    p_number.delete(0, END)

def query():
    conn = sqlite3.connect('D:/paylz_ni_maryana/business_info.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM business_info")
    records = c.fetchall()

    print_records = ""
    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + str(record[2]) + " " + str(record[3]) + " " + str(record[4]) + " " + str(record[5]) + "\n"
    query_label = Label(root, text=print_records)
    query_label.grid(row=15, column=0, columnspan=2)

    conn.commit()
    conn.close()

def delete():
    conn = sqlite3.connect('D:/paylz_ni_maryana/business_info.db')
    c = conn.cursor()
    c.execute("DELETE from business_info WHERE oid=" + delete_box.get())

    delete_box.delete(0, END)

    conn.commit()
    conn.close()

def update():
    conn = sqlite3.connect('D:/paylz_ni_maryana/business_info.db')
    c = conn.cursor()
    record_id = delete_box.get()

    c.execute("""UPDATE business_info SET
        fname = :first,
        lname = :last,
        age = :age,
        b_name = :business,
        address = :address,
        p_number = :phone,
        WHERE oid = :oid""",
              {
                  'first': fname_editor.get(),
                  'last': lname_editor.get(),
                  'age': age_editor.get(),
                  'business': b_name_editor.get(),
                  'address': address_editor.get(),
                  'phone': p_number_editor.get(),
                  'oid': record_id
              })
    conn.commit()
    conn.close()

def edit():
    editor = Tk()
    editor.title('Update Record from database')
    editor.geometry("500x500")

    conn = sqlite3.connect('D:/paylz_ni_maryana/business_info.db')
    c = conn.cursor()

    record_id = delete_box.get()
    c.execute("SELECT * FROM business_info WHERE oid=" + record_id)
    records = c.fetchall()

    global fname_editor
    global lname_editor
    global age_editor
    global b_name_editor
    global address_editor
    global p_number_editor

    fname_editor = Entry(editor, width=30)
    fname_editor.grid(row=1, column=1, padx=20, pady=(10, 0))
    lname_editor = Entry(editor, width=30)
    lname_editor.grid(row=2, column=1, padx=20)
    age_editor = Entry(editor, width=30)
    age_editor.grid(row=3, column=1, padx=20)
    b_name_editor = Entry(editor, width=30)
    b_name_editor.grid(row=4, column=1, padx=20)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=5, column=1, padx=20)
    p_number_editor = Entry(editor, width=30)
    p_number_editor.grid(row=6, column=1, padx=20)

    fname_label = Label(editor, text="First Name", bg='pink')
    fname_label.grid(row=1, column=0, pady=(10, 0))
    lname_label = Label(editor, text="Last Name", bg='pink')
    lname_label.grid(row=2, column=0)
    age_label = Label(editor, text="Age", bg='pink')
    age_label.grid(row=3, column=0)
    b_name_label = Label(editor, text="Business Name", bg='pink')
    b_name_label.grid(row=4, column=0)
    address_label = Label(editor, text="Address", bg='pink')
    address_label.grid(row=5, column=0)
    p_number_label = Label(editor, text="Phone Number", bg='pink')
    p_number_label.grid(row=6, column=0)

    for record in records:
        fname_editor.insert(0, record[0])
        lname_editor.insert(0, record[1])
        age_editor.insert(0, record[2])
        b_name_editor.insert(0, record[3])
        address_editor.insert(0, record[4])
        p_number_editor.insert(0, record[5])

    update_btn = Button(editor, text="Save Records", command=update)
    update_btn.grid(row=14, column=0, columnspan=2, pady=10, padx=10, ipadx=138)

    conn.commit()
    conn.close()

fname = Entry(root, width=30, bg='violet')
fname.grid(row=0, column=1, padx=20)
lname = Entry(root, width=30, bg='violet')
lname.grid(row=1, column=1, padx=20)
age = Entry(root, width=30, bg='violet')
age.grid(row=2, column=1, padx=20)
b_name = Entry(root, width=30, bg='violet')
b_name.grid(row=3, column=1, padx=20)
address = Entry(root, width=30, bg='violet')
address.grid(row=4, column=1, padx=20)
p_number = Entry(root, width=30, bg='violet')
p_number.grid(row=5, column=1, padx=20)

fname_label = Label(root, text="First Name")
fname_label.grid(row=0, column=0)
lname_label = Label(root, text="Last Name")
lname_label.grid(row=1, column=0)
age_label = Label(root, text="Age")
age_label.grid(row=2, column=0)
b_name_label = Label(root, text="Business Name")
b_name_label.grid(row=3, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=4, column=0)
p_number_label = Label(root, text="Phone Number")
p_number_label.grid(row=5, column=0)

submit_btn = Button(root, text="New Business Records", command=submit, bg='white')
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

query_btn = Button(root, text="View Business Records", command=query, bg='white')
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=137)

delete_btn = Button(root, text="Delete Records", command=delete, bg='white')
delete_btn.grid(row=12, column=0, columnspan=2, pady=10, padx=10, ipadx=136)

edit_btn = Button(root, text="Edit Records", command=edit, bg='white')
edit_btn.grid(row=14, column=0, columnspan=2, pady=10, padx=10, ipadx=138)

delete_box = Entry(root, width=30, bg='white')
delete_box.grid(row=10, column=1, padx=30)

delete_box_label = Label(root, text="Select ID.No", bg='white')
delete_box_label.grid(row=10, column=0)

root.mainloop()
