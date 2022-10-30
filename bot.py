# Задача 2. Прикрутить бота к задачам с предыдущего семинара:
#   2. Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.

from new_person import writing_down as wd
import view

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

t_book = wd()
view.export_book(t_book)


# эта функция позволяет выгрузить новый телефоннный справочник 'newfile.txt' в телеграм-бот 
# после внесения изменений в файл "file.txt" в папке (до запуска бота)
async def new_book_telephone(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file = open('newfile.txt', 'rb')
    await update.message.reply_document(file)

# функция приветствия
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

# эта функция позволяет загрузить изменения телефоннного справочника в телеграм-бот (в виде файла 
# "file.txt", хранящегося в отдельной папке ./import to bot/) с получением нового телефонного справочника 
# 'newfile.txt' в корневой папке
async def getfile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await (await context.bot.get_file(update.message.document)).download(
        f'{update.message.document["file_name"]}')
    await update.message.reply_text(f"file saved as {update.message.document['file_name']}")
    print("ok")
    t_book = wd()
    view.export_book(t_book)

app = ApplicationBuilder().token(
    "5408193276:AAH29vRgDIHfCbTSj5bJJw0Bq_zwdjRFNzU").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(MessageHandler(filters.Document.ALL, getfile))
app.add_handler(CommandHandler("new_book", new_book_telephone))

app.run_polling()
