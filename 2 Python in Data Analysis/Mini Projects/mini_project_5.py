print("__________PDF Merger__________")

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from pypdf import PdfWriter, PdfReader
import os

class PDFMergerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger")
        self.root.geometry("600x500")
        self.root.configure(bg='#f0f0f0')
        
        self.pdf_files = []
        
        # Title
        title_label = tk.Label(root, text="🔗 PDF Merger", font=("Arial", 18, "bold"), bg='#f0f0f0')
        title_label.pack(pady=10)
        
        # File selection frame
        file_frame = tk.Frame(root, bg='#f0f0f0')
        file_frame.pack(pady=10, padx=10, fill="x")
        
        add_btn = tk.Button(file_frame, text="➕ Add PDF Files", command=self.add_files, 
                           bg='#4CAF50', fg='white', font=("Arial", 10), padx=10, pady=5)
        add_btn.pack(side=tk.LEFT, padx=5)
        
        clear_btn = tk.Button(file_frame, text="🗑️ Clear List", command=self.clear_files,
                             bg='#f44336', fg='white', font=("Arial", 10), padx=10, pady=5)
        clear_btn.pack(side=tk.LEFT, padx=5)
        
        # File list display
        list_label = tk.Label(root, text="Selected Files:", font=("Arial", 10, "bold"), bg='#f0f0f0')
        list_label.pack(anchor="w", padx=20, pady=(10, 5))
        
        self.file_listbox = scrolledtext.ScrolledText(root, height=8, width=70, font=("Courier", 9))
        self.file_listbox.pack(padx=20, pady=5, fill="both", expand=True)
        self.file_listbox.config(state=tk.DISABLED)
        
        # Output path
        output_frame = tk.Frame(root, bg='#f0f0f0')
        output_frame.pack(pady=10, padx=20, fill="x")
        
        tk.Label(output_frame, text="Output Folder:", font=("Arial", 9), bg='#f0f0f0').pack(anchor="w")
        
        output_button_frame = tk.Frame(root, bg='#f0f0f0')
        output_button_frame.pack(padx=20, pady=5, fill="x")
        
        self.output_path = tk.StringVar(value=r"C:\Users\amand\Desktop\Data Analysis\Python in Data Analysis\Mini Projects")
        self.output_entry = tk.Entry(output_button_frame, textvariable=self.output_path, width=60, font=("Courier", 8))
        self.output_entry.pack(side=tk.LEFT, padx=5, fill="x", expand=True)
        
        browse_btn = tk.Button(output_button_frame, text="📁 Browse", command=self.select_output_folder,
                              bg='#2196F3', fg='white', font=("Arial", 9), padx=5)
        browse_btn.pack(side=tk.LEFT, padx=5)
        
        # Merge button
        merge_btn = tk.Button(root, text="🔗 Merge PDFs", command=self.merge_pdfs,
                             bg='#FF9800', fg='white', font=("Arial", 12, "bold"), padx=20, pady=8)
        merge_btn.pack(pady=10)
        
        # Status message
        status_label = tk.Label(root, text="Status:", font=("Arial", 10, "bold"), bg='#f0f0f0')
        status_label.pack(anchor="w", padx=20, pady=(10, 5))
        
        self.status_text = scrolledtext.ScrolledText(root, height=5, width=70, font=("Courier", 8))
        self.status_text.pack(padx=20, pady=5, fill="both", expand=True)
        self.status_text.config(state=tk.DISABLED)
    
    def add_files(self):
        files = filedialog.askopenfilenames(title="Select PDF files", filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")])
        if files:
            self.pdf_files.extend(files)
            self.update_file_list()
    
    def clear_files(self):
        self.pdf_files = []
        self.update_file_list()
        self.log_status("File list cleared", "info")
    
    def update_file_list(self):
        self.file_listbox.config(state=tk.NORMAL)
        self.file_listbox.delete(1.0, tk.END)
        for i, file in enumerate(self.pdf_files, 1):
            self.file_listbox.insert(tk.END, f"{i}. {file}\n")
        self.file_listbox.config(state=tk.DISABLED)
    
    def select_output_folder(self):
        folder = filedialog.askdirectory(title="Select output folder")
        if folder:
            self.output_path.set(folder)
    
    def log_status(self, message, msg_type="info"):
        self.status_text.config(state=tk.NORMAL)
        if msg_type == "info":
            prefix = "ℹ️ "
        elif msg_type == "success":
            prefix = "✅ "
        else:
            prefix = "❌ "
        self.status_text.insert(tk.END, f"{prefix}{message}\n")
        self.status_text.see(tk.END)
        self.status_text.config(state=tk.DISABLED)
    
    def merge_pdfs(self):
        if not self.pdf_files:
            messagebox.showwarning("Warning", "Please select at least 1 PDF file!")
            return
        
        self.status_text.config(state=tk.NORMAL)
        self.status_text.delete(1.0, tk.END)
        self.status_text.config(state=tk.DISABLED)
        
        try:
            merger = PdfWriter()
            
            for pdf in self.pdf_files:
                if os.path.exists(pdf):
                    reader = PdfReader(pdf)
                    for page in reader.pages:
                        merger.add_page(page)
                    self.log_status(f"Added {os.path.basename(pdf)}", "info")
                else:
                    self.log_status(f"Warning: {pdf} not found", "warning")
            
            output_folder = self.output_path.get()
            output_file = os.path.join(output_folder, "merged.pdf")
            
            with open(output_file, "wb") as f:
                merger.write(f)
            
            self.log_status(f"PDF merge complete!", "success")
            self.log_status(f"File saved at: {output_file}", "success")
            
            if os.path.exists(output_file):
                self.log_status("File successfully created!", "success")
                messagebox.showinfo("Success", f"PDFs merged successfully!\n\nSaved at:\n{output_file}")
                os.startfile(output_file)
            else:
                self.log_status("File not found!", "error")
        
        except Exception as e:
            self.log_status(f"Error: {str(e)}", "error")
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    gui = PDFMergerGUI(root)
    root.mainloop()
