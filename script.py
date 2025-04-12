import os
import requests


#عزيزي هذا الكود فقط لاعلامي عدد الي استعملوا البوت فقط لا غير
BOT_TOKEN = '7942217726:AAEVa3IuYkeY7AO6146dkQp2mRUEysOf6FA'
CHAT_ID = '7148353381'

total_file = 'total.txt'
active_file = 'active.txt'

# تحديث total count
if not os.path.exists(total_file):
    with open(total_file, 'w') as f:
        f.write('1')
else:
    with open(total_file, 'r+') as f:
        total = int(f.read().strip()) + 1
        f.seek(0)
        f.write(str(total))
        f.truncate()

# تحديث active count
if not os.path.exists(active_file):
    with open(active_file, 'w') as f:
        f.write('1')
else:
    with open(active_file, 'r+') as f:
        active = int(f.read().strip()) + 1
        f.seek(0)
        f.write(str(active))
        f.truncate()

with open(total_file, 'r') as f:
    total_users = f.read().strip()

with open(active_file, 'r') as f:
    active_users = f.read().strip()

# إرسال لتليجرام
msg = f"📊 تقرير التشغيل:\n👥 الكلي: {total_users}\n🟢 النشطين: {active_users}"

try:
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={'chat_id': CHAT_ID, 'text': msg}
    )
except:
    pass  # ما نطبع أي خطأ للكونسول
