from aes import generate_key, encrypt, decrypt
import tkinter
import customtkinter

class EncrypApp(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.geometry("300x200")
        self.title("Password manager")

        self.btn_key = customtkinter.CTkButton(self, text="Create Key", command=self.verify_key_page)
        self.btn_key.place(relx=0.5, rely=.1, anchor=tkinter.N)

        self.btn_encry = customtkinter.CTkButton(self, text="Encrypt Record", command=self.encry_page)
        self.btn_encry.place(relx=.5, rely=.5, anchor=tkinter.CENTER)

        self.btn_decry = customtkinter.CTkButton(self, text="Decrypt Record", command=self.decry_page)
        self.btn_decry.place(relx=.5, rely=.9, anchor=tkinter.S)

    def verify_key_page(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("300x200")
        window.title("Verify Key")

        self.lbl_verify = customtkinter.CTkLabel(window, width=120, height=25, text="Are you sure you want to create a new key?")
        self.lbl_verify.place(relx=.5, rely=.1, anchor=tkinter.N)

        self.btn_ok = customtkinter.CTkButton(window, width=120, height=32, text="Create Key", command=self.key_page)
        self.btn_ok.place(relx=.05, rely=.8, anchor=tkinter.SW)

        self.btn_cancel = customtkinter.CTkButton(window, width=120, height=32, text="Cancel", command=exit)
        self.btn_cancel.place(relx=.94, rely=.8, anchor=tkinter.SE)


    def key_page(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("300x200")
        window.title("Confirm Key Generation")

        generate_key()

        self.lbl_confirm_key = customtkinter.CTkLabel(window, width=120, height=25, text="Key as been successfully generated")
        self.lbl_confirm_key.place(relx=.5, rely=.1, anchor=tkinter.N)

        self.btn_exit = customtkinter.CTkButton(window, width=120, height=32, text="Exit", command=exit)
        self.btn_exit.place(relx=.5, rely=.8, anchor=tkinter.S)

    def encry_page(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("300x200")
        window.title("Encrypt Record")


        self.lbl_web_info = customtkinter.CTkLabel(window, width=120, height=25, text="Enter website information")
        self.lbl_web_info.place(relx=.5, rely=.05, anchor=tkinter.N)

        self.txtbox_website_encry = customtkinter.CTkEntry(window, width=120, height=25, placeholder_text="Website")
        self.txtbox_website_encry.place(relx=.5, rely=.25, anchor=tkinter.CENTER)

        self.txtbox_username_encry = customtkinter.CTkEntry(window, width=120, height=25, placeholder_text="Username")
        self.txtbox_username_encry.place(relx=.5, rely=.45, anchor=tkinter.CENTER)

        self.txtbox_password = customtkinter.CTkEntry(window, width=120, height=25, placeholder_text="Password", show="*")
        self.txtbox_password.place(relx=.5, rely=.65, anchor=tkinter.CENTER)

        self.btn_add_record = customtkinter.CTkButton(window, width=120, height=32, text="Enter Record", command=self.exec_encry)
        self.btn_add_record.place(relx=.5, rely=.95, anchor=tkinter.S)

    def exec_encry(self):

        flag = encrypt(self.txtbox_website_encry.get(), self.txtbox_username_encry.get(),self.txtbox_password.get()) 
        if(flag == False):
            window = customtkinter.CTkToplevel(self)
            window.geometry("300x200")
            window.title("Error: Similar Record Exist")

            self.lbl_error_dup_web = customtkinter.CTkLabel(window, width=120, height=25, text="Error: A record with a similar website exist!")
            self.lbl_error_dup_web.place(relx=.5, rely=.1, anchor=tkinter.N)
            


    def decry_page(self):
        window = customtkinter.CTkToplevel(self)
        window.geometry("300x200")
        window.title("Decrypt Record")

        self.lbl_decry_web = customtkinter.CTkLabel(window, width=120, height=25, text="Enter website to decrypt")
        self.lbl_decry_web.place(relx=.5, rely=.025, anchor=tkinter.N)

        self.txtbox_website_decry = customtkinter.CTkEntry(window, width=120, height=25, placeholder_text="Website")
        self.txtbox_website_decry.place(relx=.5, rely=.25, anchor=tkinter.CENTER)

        self.btn_fetch_record = customtkinter.CTkButton(window, width=120, height=32, text="Enter Website", command=self.exec_decry)
        self.btn_fetch_record.place(relx=.5, rely=.51, anchor=tkinter.S)

        self.txtbox_final_user = customtkinter.CTkTextbox(window, width=200, height=10)
        self.txtbox_final_user.place(relx=.5, rely = .65, anchor=tkinter.CENTER)

        self.txtbox_final_pass = customtkinter.CTkTextbox(window, width=200, height=10)
        self.txtbox_final_pass.place(relx=.5, rely = .87, anchor=tkinter.CENTER)

    def exec_decry(self):
        username, password = decrypt(self.txtbox_website_decry.get())

        if(username == None):       
            window = customtkinter.CTkToplevel(self)
            window.geometry("300x200")
            window.title("Error: Website DNE")

            self.lbl_error_dne_web = customtkinter.CTkLabel(window, width=120, height=25, text="Error: Website was not found in records!")
            self.lbl_error_dne_web.place(relx=.5, rely=.1, anchor=tkinter.N)
        else:    
            self.txtbox_final_user.insert("0.0", username)
            self.txtbox_final_pass.insert("0.0", password) 

if __name__ == "__main__":
    app = EncrypApp()
    app.mainloop()
