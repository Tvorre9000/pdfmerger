import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import simpledialog
import PyPDF2

def select_files():
    # Open file dialog to select multiple PDF files
    file_paths = filedialog.askopenfilenames(
        title="Select PDF files",
        filetypes=(("PDF files", "*.pdf"), ("All files", "*.*"))
    )
    return list(file_paths)  # Convert tuple to list

def arrange_files(file_paths):
    # Create a new window for file arrangement
    arrange_window = tk.Tk()
    arrange_window.title("Arrange PDF Files")

    # Create a Listbox to display and allow rearrangement of files
    listbox = tk.Listbox(arrange_window, selectmode=tk.SINGLE, height=10, width=50)
    listbox.pack(pady=10)

    # Populate the listbox with selected files
    for file in file_paths:
        listbox.insert(tk.END, file)

    # Add buttons for rearranging
    def move_up():
        selected = listbox.curselection()
        if selected:
            index = selected[0]
            if index > 0:
                # Swap items in the list
                file_paths[index], file_paths[index - 1] = file_paths[index - 1], file_paths[index]
                # Update listbox to reflect the new order
                listbox.delete(index)
                listbox.insert(index - 1, file_paths[index])
                listbox.selection_set(index - 1)

    def move_down():
        selected = listbox.curselection()
        if selected:
            index = selected[0]
            if index < len(file_paths) - 1:
                # Swap items in the list
                file_paths[index], file_paths[index + 1] = file_paths[index + 1], file_paths[index]
                # Update listbox to reflect the new order
                listbox.delete(index)
                listbox.insert(index + 1, file_paths[index])
                listbox.selection_set(index + 1)

    def confirm():
        arrange_window.destroy()

    # Add buttons to move files up or down
    move_up_button = tk.Button(arrange_window, text="Move Up", command=move_up)
    move_up_button.pack(side=tk.LEFT, padx=5)

    move_down_button = tk.Button(arrange_window, text="Move Down", command=move_down)
    move_down_button.pack(side=tk.LEFT, padx=5)

    confirm_button = tk.Button(arrange_window, text="Confirm", command=confirm)
    confirm_button.pack(pady=20)

    arrange_window.mainloop()

def merge_pdfs(file_paths, output_name):
    try:
        # Create a PDF merger object
        pdf_merger = PyPDF2.PdfMerger()

        # Add the files to the merger object in the specified order
        for pdf in file_paths:
            pdf_merger.append(pdf)

        # Write the merged PDF to an output file
        pdf_merger.write(output_name)
        messagebox.showinfo("Success", f"PDFs merged successfully into {output_name}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def main():
    # Step 1: Select PDF files
    file_paths = select_files()

    if not file_paths:
        messagebox.showwarning("No Files", "No PDF files selected. Exiting program.")
        return

    # Step 2: Arrange the order of selected files
    arrange_files(file_paths)

    # Step 3: Ask for the output file name
    output_name = simpledialog.askstring("Output Name", "Enter the name for the merged PDF (with .pdf extension):")

    if not output_name:
        messagebox.showwarning("No Output Name", "No output name entered. Exiting program.")
        return

    # Step 4: Merge PDFs and save to the specified file
    merge_pdfs(file_paths, output_name)

if __name__ == "__main__":
    main()