from windows import OpenWindows

def main():
    cur_win = OpenWindows()
    cur_win.choose_window()
    if cur_win.selected_window is None:
        print("Select a Window Bozo")
        return
    cur_win.set_always_on_top()

    try:
        input("Window is now pinned to the top! Press a button to stop the pinning:  ")
    finally:
        cur_win.unset_always_on_top()

if __name__== "__main__":
    main()