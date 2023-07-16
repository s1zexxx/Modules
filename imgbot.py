import openai
import telebot

openai_api_key = "YOUR_API_KEY"
openai.api_key = openai_api_key
bot = telebot.TeleBot("YOUR_TOKEN")

@bot.message_handler(commands=['img'])
def handle_img(message):
    prompt = message.text.replace('/img', '')
    if prompt.strip() == "":
        bot.reply_to(message, "Отправьте текст на основе которой искуственный интелект сделает фотографию.")
        return
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    bot.send_photo(message.chat.id, image_url)

bot.polling()
