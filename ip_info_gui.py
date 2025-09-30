import customtkinter as ctk
from tkinter import messagebox
from ip_info_cli import fetch_ip_info

# 🎨 Theme setup
ctk.set_appearance_mode("dark")   # Options: "light", "dark", "system"
ctk.set_default_color_theme("green")  # Options: "blue", "green", "dark-blue"

class IPInfoApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 🌟 Window config
        self.title("🌐 IPv4 / IPv6 Info App")
        self.geometry("650x450")
        self.resizable(False, False)

        # === Header ===
        header = ctk.CTkLabel(
            self,
            text="✨ IP Information Lookup ✨",
            font=("Arial Rounded MT Bold", 22),
            text_color="#FFD700",
        )
        header.pack(pady=15)

        # === Main Frame ===
        main_frame = ctk.CTkFrame(self, corner_radius=20)
        main_frame.pack(fill="both", expand=True, padx=20, pady=10)

        # Button
        self.fetch_btn = ctk.CTkButton(
            main_frame,
            text="🔎 Get My IP Info",
            font=("Arial", 16, "bold"),
            height=40,
            corner_radius=15,
            command=self.show_info,
        )
        self.fetch_btn.pack(pady=20)

        # Output box
        self.output_box = ctk.CTkTextbox(
            main_frame,
            wrap="word",
            width=560,
            height=250,
            font=("Consolas", 12),
            corner_radius=15,
            fg_color="#1E1E1E",
            text_color="#FFFFFF",
        )
        self.output_box.pack(pady=10, padx=10)

        # Footer
        footer = ctk.CTkLabel(
            self,
            text="💡 Tip: Check your ISP, location & more instantly!",
            font=("Arial", 12),
            text_color="lightgray",
        )
        footer.pack(pady=5)

    def show_info(self):
        """Fetch and display IP details."""
        self.output_box.delete("1.0", "end")
        info = fetch_ip_info()
        if "error" in info:
            messagebox.showerror("Error", f"❌ Failed to fetch IP info: {info['error']}")
        else:
            pretty = "\n".join([f"🌸 {key}: {value}" for key, value in info.items()])
            self.output_box.insert("end", pretty)

if __name__ == "__main__":
    app = IPInfoApp()
    app.mainloop()
