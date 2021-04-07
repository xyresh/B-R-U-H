#
#   File: bruh.pyw
#
#   Author: mrayo
#
#


#extra meme spice here
import sys

from tkinter import messagebox 

from playsound import playsound

def bruh ():
    playsound('bruh.mp3')

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import bruh_support
#stuff button does
def aboot():
    messagebox.showinfo("About","this niggerish program \nWas written By Mrayo")


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    bruh_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    bruh_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  
        _fgcolor = '#000000'  
        _compcolor = '#d9d9d9'
        _ana1color = '#d9d9d9' 
        _ana2color = '#ececec' 
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("250x100+662+359")
        top.minsize(120, 1)
        top.maxsize(1924, 1041)
        top.resizable(False,  False)
        top.title("B R U H")
        top.configure(background="#ffffff")
	
	#lelz stuffs
        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                label="About")
        self.sub_menu.add_command(
                command = aboot,
                label="About")
        self.sub_menu.add_command(
                command = quit,
                label="Quit")

        self.TButton1 = ttk.Button(top)
        self.TButton1.place(relx=0.04, rely=0.1, height=85, width=226)
        self.TButton1.configure(command=bruh)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''B R U H''')
        self.tooltip_font = "TkDefaultFont"
        self.TButton1_tooltip = \
        ToolTip(self.TButton1, self.tooltip_font, '''click it you Moron''')



from time import time, localtime, strftime
#some random comment here lol
class ToolTip(tk.Toplevel):
    """
    Provides a ToolTip widget for Tkinter.
    To apply a ToolTip to any Tkinter widget, simply pass the widget to the
    ToolTip constructor
    """
    def __init__(self, wdgt, tooltip_font, msg=None, msgFunc=None,
                 delay=0.5, follow=True):

        self.wdgt = wdgt
        # The parent of the ToolTip is the parent of the ToolTips widget
        self.parent = self.wdgt.master
        # Initalise the Toplevel
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        # Hide initially
        self.withdraw()
        # The ToolTip Toplevel should have no frame or title bar
        self.overrideredirect(True)

        # The msgVar will contain the text displayed by the ToolTip
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        # The text of the ToolTip is displayed in a Message widget
        tk.Message(self, textvariable=self.msgVar, bg='#FFFFDD',
                font=tooltip_font,
                aspect=1000).grid()

        # Add bindings to the widget.  This will NOT override
        # bindings that the widget already has
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')

    def spawn(self, event=None):
        """
        Spawn the ToolTip.  This simply makes the ToolTip eligible for display.
        Usually this is caused by entering the widget

        Arguments:
          event: The event that called this funciton
        """
        self.visible = 1
        # The after function takes a time argument in milliseconds
        self.after(int(self.delay * 1000), self.show)

    def show(self):
        """
        Displays the ToolTip if the time delay has been long enough
        """
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()

    def move(self, event):
        """
        Processes motion within the widget.
        Arguments:
          event: The event that called this function
        """
        self.lastMotion = time()
        # If the follow flag is not set, motion within the
        # widget will make the ToolTip disappear
        #
        if self.follow is False:
            self.withdraw()
            self.visible = 1

        # Offset the ToolTip 10x10 pixes southwest of the pointer
        self.geometry('+%i+%i' % (event.x_root+20, event.y_root-10))
        try:
            # Try to call the message function.  Will not change
            # the message if the message function is None or
            # the message function fails
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)

    def hide(self, event=None):
        """
        Hides the ToolTip.  Usually this is caused by leaving the widget
        Arguments:
          event: The event that called this function
        """
        self.visible = 0
        self.withdraw()

    def update(self, msg):
        """
        Updates the Tooltip with a new message. Added by Rozen
        """
        self.msgVar.set(msg)


if __name__ == '__main__':
    vp_start_gui()





