import ctypes
import ctypes.wintypes
from time import sleep
import pyautogui

# Definição das teclas
F1 = 0x70
F2 = 0x71
F3 = 0x72
F4 = 0x73
F5 = 0x74
F6 = 0x75
F7 = 0x76
F8 = 0x77
F9 = 0x78
F10 = 0x79
F11 = 0x7A
F12 = 0x7B

DELETE = 0X2E
LEFT = 0x25
UP = 0x26
RIGHT = 0x27
DOWN = 0x28
CONTROL = 0x11
RETURN = 0x0D

class Handler:
    def __init__(self):
        self.user32 = ctypes.windll.user32
        self.EnumWindows = self.user32.EnumWindows
        self.EnumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.wintypes.HWND, ctypes.wintypes.LPARAM)
        self.GetWindowText = self.user32.GetWindowTextW
        self.GetWindowTextLength = self.user32.GetWindowTextLengthW
        self.otp_hwnd = None

    def foreach_window(self, hwnd, lParam):
        length = self.GetWindowTextLength(hwnd)
        if length > 0:
            buffer = ctypes.create_unicode_buffer(length + 1)
            self.GetWindowText(hwnd, buffer, length + 1)
            window_title = buffer.value
            if self.target_window_title.lower() in window_title.lower():
                self.otp_hwnd = hwnd
                return False
        return True
    
    def get(self, window_title):
        self.target_window_title = window_title
        self.EnumWindows(self.EnumWindowsProc(self.foreach_window), 0)
        return self.otp_hwnd

class Window:
    def __init__(self, target_window_title):
        self.WM_KEYDOWN = 0x0100
        self.WM_KEYUP = 0x0101
        self.WM_MOUSEMOVE = 0x0200
        self.MK_LBUTTON = 0x0001

        self.WM_LBUTTONDOWN = 0x0201
        self.WM_LBUTTONUP = 0x0202
        self.WM_RBUTTONDOWN = 0x0204
        self.WM_RBUTTONUP = 0x0205

        self.gdi32 = ctypes.windll.gdi32
        self.user32 = ctypes.windll.user32
        self.kernel32 = ctypes.windll.kernel32

        self.hwnd = self.get_window_handle(target_window_title)

        if not self.hwnd:
            raise RuntimeError(f"Janela '{self.target_window_title}' não encontrada.")
        
    def get_window_handle(self, target_window_title):
        handler = Handler()
        return handler.get(target_window_title)

    def get_window_rect(self):
        rect = ctypes.wintypes.RECT()
        ctypes.windll.user32.GetWindowRect(self.hwnd, ctypes.byref(rect))
        return rect

    def get_relative_x_y(self, x, y):
        window_rect = self.get_window_rect()
        relative_x = x - window_rect.left
        relative_y = y - window_rect.top
        return relative_x, relative_y

    def move_to(self, old_x, old_y):
        x, y = self.get_relative_x_y(old_x, old_y)
        lParam = (y << 16) | x
        self.user32.PostMessageW(self.hwnd, self.WM_MOUSEMOVE, self.MK_LBUTTON, lParam)
    
    def click(self, delay=0.1):
        self.user32.SendMessageW(self.hwnd, self.WM_LBUTTONDOWN, 1)
        sleep(delay)
        self.user32.SendMessageW(self.hwnd, self.WM_LBUTTONUP, 0)
            
    def right_click(self, delay=0.1):
        self.user32.SendMessageW(self.hwnd, self.WM_RBUTTONDOWN, 1)
        sleep(delay)
        self.user32.SendMessageW(self.hwnd, self.WM_RBUTTONUP, 0)

    def key(self, keycode, delay=0.2):
        self.keyDown(keycode)
        sleep(delay)
        self.keyUp(keycode)

    def keyDown(self, keycode):
        self.user32.PostMessageW(self.hwnd, self.WM_KEYDOWN, keycode, 1)

    def keyUp(self, keycode):
        self.user32.PostMessageW(self.hwnd, self.WM_KEYUP, keycode, 0)

    def image_on_screen(self, image):
        try:
            location = pyautogui.locateOnScreen(image, confidence=0.8)
            if location:
                return location
            return False
        except pyautogui.ImageNotFoundException:
            return False
            
    def get_foreground_window(self):
        """Obtém o handle (HWND) da janela atualmente em foco."""
        return self.user32.GetForegroundWindow()
    
    def set_foreground_window(self, hwnd):
        self.user32.ShowWindow(hwnd, 11)
        sleep(0.2)
        return self.user32.ShowWindow(hwnd, 1)
    
    
