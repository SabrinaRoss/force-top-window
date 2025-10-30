from pywinauto import Desktop
import win32gui
import win32con

class OpenWindows:
    def __init__(self):
        self.windows = self.get_current_windows()
        self.selected_window = None

    def get_current_windows(self):
        return Desktop(backend="uia").windows()

    def list_current_windows(self) -> int:
        i = 0
        for w in self.windows:
            print(f"{i}: {w.window_text()}")
            print()
            i+=1
        return i
    
    def choose_window(self):
        max_num: int = self.list_current_windows()
        num = None
        try:
            num: int = int(input("Choose the number representing the applicaiton you want to select: "))
        except ValueError:
            print("Dude, that is not a number, please do something value")
            
        if num is None:
            print("Invalid input: dude it's suppose to be a number...")
            return None
        elif num >= max_num or num < 0:
            print("Invalid number")
            return None
        self.selected_window = self.windows[num]
        print(f"You have selected window: {self.selected_window.window_text()}")
    
    def set_always_on_top(self):
        if self.selected_window is None:
            print("Dude select a window")
            return

        hwnd = self.selected_window.handle
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        print(f"{self.selected_window.window_text()} is now always on the top!!!!!")

    def unset_always_on_top(self):
        if self.selected_window is None:
            print("Dude select a window")
            return
        
        hwnd = self.selected_window.handle
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        print(f"{self.selected_window.window_text()} is now deselected from always on top!!!!!")