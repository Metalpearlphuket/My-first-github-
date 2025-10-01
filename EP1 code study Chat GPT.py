import tkinter as tk
from tkinter import messagebox
import csv
import os

# ---------- ฟังก์ชันบันทึก ----------
def save_data():
    material = entry_material.get()
    type_ = entry_type.get()
    weld = entry_weld.get()

    if not material or not type_ or not weld:
        messagebox.showwarning("Warning", "กรุณากรอกข้อมูลให้ครบ")
        return

    # สร้างไฟล์ CSV ถ้าไม่มี
    file_exists = os.path.isfile("materials.csv")
    with open("materials.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["วัสดุ", "ชนิด", "เชื่อม"])  # header
        writer.writerow([material, type_, weld])

    messagebox.showinfo("Success", "บันทึกข้อมูลสำเร็จแล้ว")
    entry_material.delete(0, tk.END)
    entry_type.delete(0, tk.END)
    entry_weld.delete(0, tk.END)

# ---------- UI ----------
root = tk.Tk()
root.title("Metal Pearl - เก็บข้อมูลวัสดุ")
root.geometry("350x200")

label_company = tk.Label(root, text="Company: Metal Pearl", font=("Arial", 12, "bold"))
label_company.pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=10)

# ฟอร์ม
tk.Label(frame, text="วัสดุ:").grid(row=0, column=0, sticky="e")
entry_material = tk.Entry(frame, width=25)
entry_material.grid(row=0, column=1)

tk.Label(frame, text="ชนิด:").grid(row=1, column=0, sticky="e")
entry_type = tk.Entry(frame, width=25)
entry_type.grid(row=1, column=1)

tk.Label(frame, text="เชื่อม:").grid(row=2, column=0, sticky="e")
entry_weld = tk.Entry(frame, width=25)
entry_weld.grid(row=2, column=1)

# ปุ่ม Save
btn_save = tk.Button(root, text="Save", command=save_data, bg="lightblue")
btn_save.pack(pady=10)

root.mainloop()
