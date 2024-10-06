import tkinter as tk
import tkinter.ttk as ttk
from Convert import *

def main() -> None:
    
    def process_inputs():
        inputs = {'Input Number': input_number_var.get(), 'Input Base': input_base_var.get(), 'Convert Base': conv_base_var.get()}
        for inp in inputs:
            try: 
                if inp != 'Input Number':
                    int(inputs[inp])
            except ValueError:
                output_label['foreground'] = 'red'
                output_var.set(f' Error : Invalid Input For {inp}!')
                break
        else:
            if inputs['Input Base'] == '10':
                output = Convert.decimal_conv(inputs['Input Number'], inputs['Convert Base'])
            else:
                if inputs['Convert Base'] == '10':
                    output = Convert.to_decimal_conv(inputs['Input Number'], inputs['Input Base'])
                else:
                    decimal_value = Convert.to_decimal_conv(inputs['Input Number'], inputs['Input Base'])
                    decimal_value = decimal_value.split(':')[1].strip()
                    output = Convert.decimal_conv(decimal_value, inputs['Convert Base'])
                    
            if 'Error!' in output:
                output_label['foreground'] = 'red'
            else:
                output_label['foreground'] = 'lightgreen'
                
            output_var.set(output)
                    
  
    input_number_var = tk.StringVar()
    input_base_var = tk.StringVar()
    conv_base_var = tk.StringVar()
    output_var = tk.StringVar()
    
    
    input_frame = ttk.Frame(master=ROOT_WINDOW, borderwidth=1, relief=tk.RIDGE, padding=10)
    input_frame.pack(fill='both', padx=10, pady=10)
    
    input_number_label = ttk.Label(master=input_frame, text='Enter the Number', font=LABEL_FONT, anchor='center', foreground='white', background='black', padding=5)
    input_number_label.pack(pady=(0, 5), fill='x')
    
    input_number_entry = ttk.Entry(master=input_frame, textvariable=input_number_var, width=ENTRY_WIDTH, justify='center')
    input_number_entry.pack(pady=5)
    
    input_base_label = ttk.Label(master=input_frame, text='Enter the Base', font=LABEL_FONT, anchor='center', foreground='white', background='black', padding=5)
    input_base_label.pack(pady=5, fill='x')
    
    input_base_entry = ttk.Entry(master=input_frame, textvariable=input_base_var, width=ENTRY_WIDTH, justify='center')
    input_base_entry.pack(pady=5)
    
    conv_base_label = ttk.Label(master=input_frame, text='Enter a Base for the Convertion', font=LABEL_FONT, anchor='center', foreground='white', background='black', padding=8)
    conv_base_label.pack(pady=5, fill='x')
    
    conv_base_entry = ttk.Entry(master=input_frame, textvariable=conv_base_var, width=ENTRY_WIDTH, justify='center')
    conv_base_entry.pack(pady=5)
    
    output_frame = ttk.Frame(master=ROOT_WINDOW, borderwidth=1, relief=tk.RIDGE, padding=10)
    output_frame.pack(fill='both', padx=10, pady=10, expand=True)
    
    output_frame.columnconfigure((0,1), weight=1, uniform='u')
    output_frame.rowconfigure((0,1), weight=1, uniform='u')
    
    submit_button = ttk.Button(master=output_frame, padding=BTN_MARGIN, text='Enter', command=process_inputs)
    submit_button.grid(column=0, row=0, sticky='we', padx=3)
    
    clear_button = ttk.Button(master=output_frame, padding=BTN_MARGIN, text='Clear', command=lambda: print("Clear"))
    clear_button.grid(column=1, row=0, sticky='we', padx=3)
    
    output_label = ttk.Label(master=output_frame, textvariable=output_var, font='Arial 11 bold', anchor='center', padding=10, borderwidth=1, relief=tk.RIDGE, background='black')
    output_label.grid(column=0, row=1, columnspan=2, sticky='news')
    
    
def runGUI():    
        global ROOT_WINDOW
        
        ROOT_WINDOW = tk.Tk()
        ROOT_WINDOW_WIDTH = 450
        ROOT_WINDOW_HEIGHT = 480
        ROOT_WINDOW_X_POSITION = ROOT_WINDOW.winfo_screenwidth() // 2 - ROOT_WINDOW_WIDTH // 2
        ROOT_WINDOW_Y_POSITION = ROOT_WINDOW.winfo_screenheight() // 2 - ROOT_WINDOW_HEIGHT // 2 - WINDOW_OFFSET
        ROOT_WINDOW.geometry(f"{ROOT_WINDOW_WIDTH}x{ROOT_WINDOW_HEIGHT}+{ROOT_WINDOW_X_POSITION}+{ROOT_WINDOW_Y_POSITION}")
        ROOT_WINDOW.title("Number Converter")
        ROOT_WINDOW.resizable(True, False)
        ROOT_WINDOW.attributes('-topmost', True)

        main()

        ROOT_WINDOW.mainloop()

WINDOW_OFFSET = 50
LABEL_FONT = 'Courier 12 bold'
ENTRY_WIDTH = 30 
BTN_MARGIN = 20

if __name__ == "__main__":
    runGUI()