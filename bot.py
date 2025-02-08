import telebot
import time

TOKEN = "7963748720:AAEFuQBmanO3rp3W3TehiIAwTuk6EJ1yoCA"  
bot = telebot.TeleBot(TOKEN)

CHANNELS = {
    "A": "@BEK_AIR_N1",
    "J": "@Yoqubovblog",
    "AJ": ["@BEK_AIR_N1", "@Yoqubovblog"]
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Xush kelibsiz!")

@bot.message_handler(commands=['A', 'J', 'AJ'])
def make_admin(message):
    command = message.text[1:]  # "/" belgisini olib tashlash
    user_id = message.from_user.id

    if command in CHANNELS:
        channels = CHANNELS[command]
        if isinstance(channels, str):  # Agar bitta kanal bo‘lsa
            channels = [channels]

        for channel in channels:
            try:
                bot.promote_chat_member(
                    chat_id=channel,
                    user_id=user_id,
                    can_change_info=True,
                    can_post_messages=True,
                    can_edit_messages=True,
                    can_delete_messages=True,
                    can_invite_users=True,
                    can_pin_messages=True
                )
                bot.send_message(user_id, f"✅ {channel} kanalida admin bo‘ldingiz!")
            except Exception as e:
                bot.send_message(user_id, f"❌ {channel} kanalida admin bo‘lish imkoni yo‘q: {e}")
    else:
        bot.send_message(message.chat.id, "❌ Noto‘g‘ri buyruq!")

# Botni uzluksiz ishlashini ta'minlash
while True:
    try:
        print("Bot ishlayapti...")
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Xatolik: {e}")
        time.sleep(5)  # Xatolik bo‘lsa, 5 soniyadan keyin qayta ishga tushadi
