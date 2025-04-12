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
