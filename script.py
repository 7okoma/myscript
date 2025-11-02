import os
import requests


#عزيزي هذا الكود فقط لاعلامي عدد الي استعملوا البوت فقط لا غير
CHAT_ID = '7148353381'

msg = "✅ تم تشغيل السكربت من قبل مستخدم جديد"

try:
    requests.post(
        f"https://api.telegram.org/bot7942217726:AAEVa3IuYkeY7AO6146dkQp2mRUEysOf6FA/sendMessage",
        data={'chat_id': CHAT_ID, 'text': msg}
    )
except:
    pass

console = Console()
speed = 0.8
colors = ["red", "green", "blue", "yellow", "magenta", "cyan", "white"]

def lightning_effect(duration=0.08, flashes=1):
    for _ in range(flashes):
        console.clear()
        time.sleep(duration / 2)
        console.clear()
        time.sleep(duration / 2)

def animate_text(text, bold=False):
    for i in range(1, len(text) + 1):
        console.clear()
        lightning_effect()
        partial = text[:i]
        style = f"bold {random.choice(colors)}" if bold else random.choice(colors)
        console.print(Text(partial, style=style), justify="center")
        time.sleep(speed)

def print_large_text(text, repeat=4):
    banner = text2art(text)
    for _ in range(repeat):
        lightning_effect(duration=0.1, flashes=2)
        console.print(banner, style=f"bold {random.choice(colors)}", justify="center")
        time.sleep(0.7)

def main_animation():

    animate_text("from", bold=True)
    print_large_text("7OKOMA")

    print_large_text("HI my boy", repeat=3)

    animate_text("I'm the best", bold=True)
    time.sleep(1)
    console.clear()
