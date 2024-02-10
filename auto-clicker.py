import win32api
import win32con
import time

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def main():
    interval = 4.5  # Set the interval in seconds
    while True:
        a, b = win32api.GetCursorPos()
        click(a, b)
        print(f"Click at ({a}, {b})")
        time.sleep(interval)

if __name__ == "__main__":
    main()
