import os
import requests

def send_message():
    token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    
    # Pesan Valentine Baru untuk Mattheo
    pesan = (
        "Halo Mattheo. \n\n"
        "Happy valentine ya, semenjak kamu hadir, aku ngerasa hari hariku lebih banyak warnanya karena kamu. "
        "Mungkin awalnya kamu emang ngerasa kayak iseng aja buat deketin aku (kayak yang pernah kamu bilang), "
        "awalnya juga aku mikir kamu cuma bercanda, tapi entah gimana caranya, aku bisa tertarik juga sama kamu.\n\n"
        "Kamu lucu, gemesin, meski kamu selalu nolak kalau dibilang kayak gitu, tapi percaya deh, "
        "kamu emang beneran selucu dan segemes itu wkwk.\n\n"
        "Kamu jangan pernah ngerasa sendiri ya mat, aku ada disini buat kamu, jadi temen sekaligus support system buat kamu, anjayy. "
        "Ya mungkin aku bukan orang yang romantis kayak yang pernah aku bilang ke kamu pas itu, "
        "aku bukan orang yang nunjukin kasih sayangnya secara terang-terangan, tapi kamu harus tau kalo aku sayang sama kamu. "
        "**I really really love you.** \n\n"
        "Mungkin aku masih butuh waktu yang sedikit lama buat lanjut ke hal yang sedikit lebih serius sama kamu, "
        "aku harap aku bisa ga buat kamu nunggu lebih lama. Aku ga pernah minta kamu selalu tinggal sama aku, "
        "karena aku ga mau kalau nantinya kita ga pernah bisa sama sama, aku bakal ngecewain kamu karena buat kamu terlalu berharap.\n\n"
        "Jangan sedih-sedih ya mat, kamu hidup didunia ini juga berhak dapat kebahagiaan. "
        "Mungkin kamu ngerasa selalu gagal dalam jalin hubungan, jangan selalu mikir buruk kayak gitu. "
        "Kamu bisa ngelakuin hal lain kalo emang kamu ngerasa 'gagal' di satu hal. Pastinya ada nantinya yang bakal nerima kamu mat.\n\n"
        "**Kamu berhak bahagia**, kamu berhak dapat perlakuan yang baik, kamu berhak punya seseorang yang sayang dan jaga kamu dengan baik, kamu berhak punya banyak temen.\n\n"
        "Ini valentine pertama yang aku rayain mat, gak banyak yang bisa aku kasih ke kamu, "
        "tapi aku udah berusaha buat sesuatu yang mungkin bisa kamu sukai? Wkwk ya aku berharap gitu deh, semoga kamu suka.\n\n"
        "Semuanya bisa kamu liat disini ya mat @ilouvei\n\n"
        "Sekali lagi happy valentine buat mamat lucu hehe, *i love you.* "
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
