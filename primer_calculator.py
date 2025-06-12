import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

#Setting up the (Tm) of DNA sequence
def calculate_tm(seq):
    seq = seq.upper()
    a = seq.count("A")
    t = seq.count("T")
    g = seq.count("G")
    c = seq.count("C")
    return 2 * (a + t) + 4 * (g + c)

#Setting up Primers
def gc_content(seq):
    seq = seq.upper()
    g = seq.count("G")
    c = seq.count("C")
    return round((g + c) / len(seq) * 100, 2)

#analyze the primer pairs
def analyze_primers():
    forward = forward_entry.get().strip()
    reverse = reverse_entry.get().strip()

    if not forward or not reverse:
        messagebox.showwarning("Error.", "Please enter both primer sequences.")
        return

    try:
        f_tm = calculate_tm(forward)
        r_tm = calculate_tm(reverse)
        f_gc = gc_content(forward)
        r_gc = gc_content(reverse)
        tm_diff = abs(f_tm - r_tm)
        is_valid = "Compatible!" if tm_diff <= 2 else "Not ideal."

        result = (
            f"📌 Forward Primer\n"
            f"   • Sequence: {forward}\n"
            f"   • Length: {len(forward)} bases\n"
            f"   • GC Content: {f_gc}%\n"
            f"   • Tm: {f_tm}°C\n\n"
            f"📌 Reverse Primer\n"
            f"   • Sequence: {reverse}\n"
            f"   • Length: {len(reverse)} bases\n"
            f"   • GC Content: {r_gc}%\n"
            f"   • Tm: {r_tm}°C\n\n"
            f"🔎 Tm Difference: {tm_diff}°C\n"
            f"🧬 Primer Pair Compatibility: {is_valid}"
        )
        result_label.config(text=result)

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

#GUI
root = tk.Tk()
root.title("PCR Primer Calculator")
root.geometry("600x600")
root.resizable(False, False)

#DNA background jpg
try:
    bg_image = Image.open("dna.jpg")
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    messagebox.showerror("Image Error", f"Background image couldn't be loaded:\n{e}")

#Into text
intro_text = (
    "What is a PCR Primer?\n"
    "\n"
    "Primers are short DNA sequences that guide DNA replication in PCR. "
    "They're like bookmarks that tell the enzyme where to start copying.\n\n"
    "What does this calculator do?\n"
    "\n"
    "It checks if your forward and reverse primers are good to go by calculating GC content, "
    "melting temperature (Tm), and pair compatibility."
)
tk.Label(root, text=intro_text, wraplength=540, justify="left", bg=root["bg"], font=("Microsoft Sans Serif", 10)).pack(pady=(20, 10))

#Forward Primer Input
tk.Label(root, text="Forward Primer Sequence:", bg=root["bg"], font=("Courier", 10, "bold")).pack()
forward_entry = tk.Entry(root, width=60)
forward_entry.pack(pady=5)

#Reverse Primer Input
tk.Label(root, text="Reverse Primer Sequence:", bg=root["bg"], font=("Courier", 10, "bold")).pack()
reverse_entry = tk.Entry(root, width=60)
reverse_entry.pack(pady=5)

#Analyze
tk.Button(root, text="Analyze Primers", command=analyze_primers, font=("Courier", 10, "bold")).pack(pady=15)

#Results Box
result_label = tk.Label(
    root,
    text="",
    bg="#FFFFFF",  
    fg="black",    
    justify="left",
    anchor="nw",
    font=("Courier", 10, "bold"),
    relief="solid",
    bd=1,
    width=70,
    height=12,
    wraplength=520
)
result_label.pack(pady=10)

root.mainloop()
