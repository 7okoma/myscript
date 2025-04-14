import os
import requests


#عزيزي هذا الكود فقط لاعلامي عدد الي استعملوا البوت فقط لا غير
BOT_TOKEN = '7942217726:AAEVa3IuYkeY7AO6146dkQp2mRUEysOf6FA'
CHAT_ID = '7148353381'

msg = "✅ تم تشغيل السكربت من قبل مستخدم جديد"

try:
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={'chat_id': CHAT_ID, 'text': msg}
    )
except:
    pass

console = Console()
speed = 0.3  
colors = ["red", "green", "blue", "yellow", "magenta", "cyan", "white"]

def lightning_effect():
    console.clear()
    time.sleep(0.09)  

def animate_text(text, bold=False):
    for i in range(1, len(text) + 1):
        console.clear()
        lightning_effect()
        partial = text[:i]
        style = f"bold {random.choice(colors)}" if bold else random.choice(colors)
        console.print(Text(partial, style=style), justify="center")
        time.sleep(speed)

def print_large_text(text):
    banner = text2art(text)  
    for _ in range(4):  
        lightning_effect()
        console.print(banner, style=f"bold {random.choice(colors)}", justify="center")
        time.sleep(0.8)

animate_text("only in", bold=False)
print_large_text("black elgenral")

animate_text("from", bold=False)
print_large_text("7OKOMA")

print_large_text("TELEGRAM BOT")

animate_text("TELEGRAM BOT", bold=False)
