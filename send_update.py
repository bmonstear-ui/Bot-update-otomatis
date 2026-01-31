import os
import requests

def send_message():
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    
    # Pesan romantis kamu
    pesan = (
        "Halo Mattheo.\n\n"
        "Happy valentine ya, semenjak kamu hadir, aku ngerasa hari hariku lebih banyak warnanya karena kamu. "
        "Kamu udah cukup lama kenal aku, dan aku ngerasa juga udah cukup lama buat kenal kamu.\n\n"
        "Mungkin awalnya kamu emang ngerasa aku gak akan serius buat jalin hubungan sama kamu, karena kamu yang datang tiba-tiba ke aku. "
        "Tapi entah gimana caranya, aku bisa tertarik juga sama kamu.\n\n"
        "Kamu lucu, gemesin, meski kamu selalu nolak kalau dibilang kayak gitu, tapi percaya deh, kamu emang beneran selucu dan segemes itu wkwk.\n\n"
        "Hari ini hari valentine, aku ngerasa hari ini adalah hari yang cocok buat tanggal jadian kita gak sih? **Tolong setuju sama aku, hahaha.**\n\n"
        "Ya mungkin aku bukan orang yang romantis, aku bukan orang yang nunjukin kasih sayangnya secara terang-terangan, "
        "tapi kamu harus tau kalo aku sayang dan cinta sama kamu. **I really love you.**\n\n"
        "Jadi, *do you wanna be my valentine, love?* "
    )
    
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id, 
        "text": pesan,
        "parse_mode": "Markdown"
    }
    requests.post(url, json=payload)

if __name__ == "__main__":
    send_message()
