import tkinter as tk

# Sample data structure to store student details
student_details = {
    "4242": {
        "Name": "Rajuyamala",
        "Age": 20,
        "Branch": "Computer Science",
        "Gmail": 'rajuya5566@gmail.com',
        "Phn num":'9390739983',
        "Birthday":'08/08/2002',
        "Addres":'turumella,West pallanadu district,1-36'
    },
    "4454": {
        "Name": "amar",
        "Age": 19,
        "Branch": "Electrical Engineering",
        "Gmail": 'amar143@gmail.com',
        "Phn num":'9392301433',
        "Birthday":'02/12/2003',
        "Addres":'pinnalli,guntur district,2-96'
    },
    "4243": {
        "Name": "siva",
        "Age": 20,
        "Branch": "Mechanical Science",
        "Gmail": 'siva221okokm@gmail.com',
        "Phn num":'8985989921',
        "Birthday":'15/08/2000',
        "Addres":'narasaraopet,pallanadu district,9-74'
    },
     "4244": {
        "Name": "naresh",
        "Age": 18,
        "Branch": "Civil",
        "Gmail": 'naresh666@gmail.com',
        "Phn num":'9493787794',
        "Birthday":'16/06/2004',
        "Addres":'vijayawada,krishna district,6-98'
     },
    "4245": {
        "Name": "sai krishna",
        "Age": 20,
        "Branch": "Mechine learning",
        "Gmail":'krish123@gmail.com',
        "Phn num":'9652994999',
        "Birthday":'09/02/2000',
        "Addres":'ongole,prakkasam district,25-85'
     },
}


def display_student_details():
    student_id = entry_id.get()
    if student_id in student_details:
        details = student_details[student_id]
        output_label.config(text=f"Name: {details['Name']}\nAge: {details['Age']}\nBranch: {details['Branch']}\nGmail: {details['Gmail']}\nPhn num:{details['Phn num']}\nBirthday: {details['Birthday']}\nAddres: {details['Addres']}")
    else:
        output_label.config(text="Student not found.")

# Create the main application window
root = tk.Tk()
root.title("Student Details")

# Create input widgets
label_id = tk.Label(root, text="Enter Student ID:",width=100)
label_id.pack()

entry_id = tk.Entry(root)
entry_id.pack()

submit_button = tk.Button(root, text="Submit", command=display_student_details,width=25)
submit_button.pack()

# Create the output label
output_label = tk.Label(root, text="", justify=tk.LEFT)
output_label.pack()

# Start the application event loop
root.mainloop()