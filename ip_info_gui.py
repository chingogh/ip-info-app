import customtkinter as ctk
from tkinter import scrolledtext, messagebox
from ip_info_cli import fetch_ip_info

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class IPInfoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("IPv4/IPv6 Information App")
        self.geometry("600x400")

        # Button
        self.fetch_btn = ctk.CTkButton(self, text="Get IP Info", command=self.show_info)
        self.fetch_btn.pack(pady=20)

        # Output box
        self.output_box = scrolledtext.ScrolledText(
            self, wrap="word", bg="#1e1e1e", fg="white", font=("Consolas", 11)
        )
        self.output_box.pack(fill="both", expand=True, padx=20, pady=10)

    def show_info(self):
        self.output_box.delete(1.0, "end")
        info = fetch_ip_info()
        if "error" in info:
            messagebox.showerror("Error", f"Failed to fetch IP info: {info['error']}")
        else:
            for key, value in info.items():
                self.output_box.insert("end", f"{key}: {value}\n")

if __name__ == "__main__":
    app = IPInfoApp()
    app.mainloop()
