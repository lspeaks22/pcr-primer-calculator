#imports
import tkinter as tk #GUI
from tkinter import ttk, messagebox #widgets and popup messages
from PIL import Image, ImageTk #image background

#calculating the melting tempature (Tm) of a DNA sequence
def calculate_tm(seq):
    seq = seq.upper()
    return 2 * (seq.count("A") + seq.count("T")) + 4 * (seq.count("G") + seq.count("C"))

#calculating the GC content %
def gc_content(seq):
    seq = seq.upper()
    gc_count = seq.count("G") + seq.count("C")
    return round((gc_count / len(seq)) * 100, 2) if seq else 0

#analyzing forward and reverse primers
def analyze_primers():
    forward = forward_entry.get().strip()
    reverse = reverse_entry.get().strip()

    if not forward or not reverse:
        messagebox.showwarning("Missing Input", "Please enter both primer sequences.")
        return

    try:
        f_len = len(forward)
        r_len = len(reverse)
        f_gc = gc_content(forward)
        r_gc = gc_content(reverse)
        f_tm = calculate_tm(forward)
        r_tm = calculate_tm(reverse)
        tm_diff = abs(f_tm - r_tm)
        anneal_temp = min(f_tm, r_tm) - 5
        pair_status = "Compatible!" if tm_diff <= 2 else "Not Compatible."

        result_text = (
            f"FORWARD PRIMER\n"
            f" • Sequence: {forward}\n"
            f" • Length: {f_len} bases\n"
            f" • GC Content: {f_gc}%\n"
            f" • Melting Temp (Tm): {f_tm}°C\n\n"
            f"REVERSE PRIMER\n"
            f" • Sequence: {reverse}\n"
            f" • Length: {r_len} bases\n"
            f" • GC Content: {r_gc}%\n"
            f" • Melting Temp (Tm): {r_tm}°C\n\n"
            f"Tm Difference: {tm_diff}°C\n"
            f"Suggested Annealing Temp: {anneal_temp}°C\n"
            f"Primer Pair Status: {pair_status}"
        )
        #showing results in output box
        result_box.config(text=result_text)
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

#GUI
#creating the main application
root = tk.Tk()
root.title("PCR Primer Compatibility Calculator") #title
root.geometry("880x500") #size of the window
root.configure(bg="#77abf0") #background
root.resizable(False, False) #fixed window size

#Background
try:
    bg_image = Image.open("dna.jpg").resize((880, 500))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
except:
    root.configure(bg="#449cbe") #backup background color if the image fails

#Layout
#left panel input
input_frame = tk.Frame(root, bg="white", bd=2, relief="ridge")
input_frame.place(x=30, y=30, width=380, height=440)

#right panel output
output_frame = tk.Frame(root, bg="white", bd=2, relief="ridge")
output_frame.place(x=440, y=30, width=410, height=440)

#Inputs
#Section title
tk.Label(input_frame, text="PCR Primer Input", font=("Courier", 14, "bold"), bg="white").pack(pady=15)

#primer concentration
tk.Label(input_frame, text="Primer Concentration (nM):", font=("Courier", 10), bg="white").pack(anchor="w", padx=20)
primer_conc = tk.Entry(input_frame, font=("Courier", 10))
primer_conc.insert(0, "500")
primer_conc.pack(padx=20, pady=5, fill="x")

#forward primer input
tk.Label(input_frame, text="Forward Primer Sequence:", font=("Courier", 10), bg="white").pack(anchor="w", padx=20)
forward_entry = tk.Entry(input_frame, font=("Courier", 10))
forward_entry.pack(padx=20, pady=5, fill="x")

#reverse primer input
tk.Label(input_frame, text="Reverse Primer Sequence:", font=("Courier", 10), bg="white").pack(anchor="w", padx=20)
reverse_entry = tk.Entry(input_frame, font=("Courier", 10))
reverse_entry.pack(padx=20, pady=5, fill="x")

#analyze both primers
analyze_btn = tk.Button(
    input_frame, text="Analyze Primers", command=analyze_primers,
    font=("Courier", 10, "bold"), bg="#006699", fg="white",
    relief="flat", padx=10, pady=5
)
analyze_btn.pack(pady=25)

#Output
#section title
tk.Label(output_frame, text="Primer Analysis Summary", font=("Courier", 14, "bold"), bg="white").pack(pady=15)

#results
result_box = tk.Label(
    output_frame, text="", font=("Consolas", 10), bg="#fefefe",
    justify="left", anchor="nw", wraplength=380, relief="solid", bd=1,
    width=50, height=20
)
result_box.pack(padx=10, pady=10, fill="both", expand=True)

#launch GUI application
root.mainloop()

