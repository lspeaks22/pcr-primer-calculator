import tkinter as tk
from tkinter import messagebox

def calculate_tm(seq):
    seq = seq.upper()
    a = seq.count("A")
    t = seq.count("T")
    g = seq.count("G")
    c = seq.count("C")
    return 2 * (a + t) + 4 * (g + c)

def gc_content(seq):
    seq = seq.upper()
    g = seq.count("G")
    c = seq.count("C")
    return round((g + c) / len(seq) * 100, 2)

def analyze_primers():
    forward = forward_entry.get().strip()
    reverse = reverse_entry.get().strip()

    if not forward or not reverse:
        messagebox.showwarning("Missing Input", "Please enter both primer sequences.")
        return

    try:
        f_tm = calculate_tm(forward)
        r_tm = calculate_tm(reverse)
        f_gc = gc_content(forward)
        r_gc = gc_content(reverse)
        f_len = len(forward)
        r_len = len(reverse)
        tm_diff = abs(f_tm - r_tm)
        is_valid = "Yes" if tm_diff <= 2 else "No"

        result_text = (
            f"Forward Primer:\n"
            f"  Sequence: {forward}\n"
            f"  Length: {f_len} | GC%: {f_gc}% | Tm: {f_tm}°C\n\n"
            f"Reverse Primer:\n"
            f"  Sequence: {reverse}\n"
            f"  Length: {r_len} | GC%: {r_gc}% | Tm: {r_tm}°C\n\n"
            f"Tm Difference: {tm_diff}°C\n"
            f"Valid Primer Pair: {is_valid}"
        )

        result_label.config(text=result_text)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Setup
root = tk.Tk()
root.title("PCR Primer Calculator")
root.geometry("500x400")
root.resizable(False, False)

tk.Label(root, text="Forward Primer Sequence:").pack(pady=(20, 0))
forward_entry = tk.Entry(root, width=50)
forward_entry.pack(pady=5)

tk.Label(root, text="Reverse Primer Sequence:").pack(pady=(10, 0))
reverse_entry = tk.Entry(root, width=50)
reverse_entry.pack(pady=5)

tk.Button(root, text="Analyze Primers", command=analyze_primers).pack(pady=20)

result_label = tk.Label(root, text="", justify="left", font=("Courier", 10), bg="white", anchor="nw", width=60, height=10, wraplength=450, relief="solid", bd=1)
result_label.pack(pady=10)

root.mainloop()
