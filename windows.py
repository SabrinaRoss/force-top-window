from pywinauto import Desktop

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
            return None
        elif int(num) >= max_num:
            return None
        self.selected_window = self.windows[num]
        print(f"You have selected window: {self.selected_window.window_text()}")