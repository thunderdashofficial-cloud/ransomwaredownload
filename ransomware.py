import tkinter as tk
from tkinter import messagebox
import time
import threading

# Fake countdown starting time (1 hour)
time_left = 3600  
correct_key = "abc22abc"  # The magic key

def update_timer():
    global time_left
    while time_left > 0:
        mins, secs = divmod(time_left, 60)
        timer_label.config(text=f"Time Left: {mins:02d}:{secs:02d}")
        time_left -= 1
        time.sleep(1)
    timer_label.config(text="Time Left: 00:00")
    messagebox.showwarning("Time Up", "Your files are now permanently encrypted! (Not really 😜)")

def check_key():
    entered_key = key_entry.get().strip()
    if entered_key == "":
        messagebox.showerror("Error", "Please enter a key!")
    elif entered_key == correct_key:
        messagebox.showinfo("Access Restored", "ACCESS RESTORED! YOUR FILES ARE SAFE 😎")
        root.after(3000, root.destroy)  # Close after 3 seconds
    else:
        messagebox.showerror("Decryption Failed", "INCORRECT KEY! Please try again.")

def disable_close():
    # Disable closing the window manually
    messagebox.showerror("Error", "You cannot close this window! Enter the correct key to unlock.")

# GUI setup
root = tk.Tk()
root.title("RANSOMWARE.EXE")
root.geometry("600x400")
root.config(bg="black")
root.resizable(False, False)

# Disable the window close button (X)
root.protocol("WM_DELETE_WINDOW", disable_close)

# Fake scary message
info_label = tk.Label(
    root,
    text=("All your files have been encrypted.\n"
          "Send $300 in Bitcoin to the wallet below to restore access.\n\n"
          "What Happens if I don't Pay:\n"
          "Your files will NEVER BE RECOVERED!\n"
          "We have access to your entire computer, including photos,\n"
          "files, and bank details. Once you have paid, you will receive\n"
          "an encryption key. Paste the key below to decrypt your files."),
    font=("Arial", 12),
    fg="white",
    bg="black",
    justify="center"
)
info_label.pack(pady=10)

# Fake countdown timer
timer_label = tk.Label(root, text="Time Left: 60:00", font=("Arial", 14, "bold"), fg="red", bg="black")
timer_label.pack(pady=10)

# Fake Bitcoin Wallet
wallet_label = tk.Label(root, text="BTC Wallet: 74239043753954344546", font=("Arial", 12), fg="red", bg="black")
wallet_label.pack(pady=5)

# Entry field for fake encryption key
key_entry = tk.Entry(root, font=("Arial", 12), width=40, justify="center")
key_entry.pack(pady=10)

# Fake decrypt button
decrypt_button = tk.Button(root, text="DECRYPT FILES", font=("Arial", 12, "bold"), bg="red", fg="white", command=check_key)
decrypt_button.pack(pady=10)

# Start countdown timer in background
threading.Thread(target=update_timer, daemon=True).start()

# Run GUI
root.mainloop()
