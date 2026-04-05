from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from bot.questions import QUESTIONS


# =========================
# КНОПКА СТАРТА
# =========================
def get_start_keyboard():
    keyboard = [
        [InlineKeyboardButton("🚀 Пройти честный тест", callback_data="start_test")]
    ]
    return InlineKeyboardMarkup(keyboard)


# =========================
# КНОПКИ ОТВЕТОВ
# =========================
def get_question_keyboard(question_index):
    keyboard = []
    answers = QUESTIONS[question_index]["answers"]

    for i, answer in enumerate(answers):
        button = InlineKeyboardButton(
            answer["text"],
            callback_data=f"answer_{i}"
        )
        keyboard.append([button])

    return InlineKeyboardMarkup(keyboard)


# =========================
# КНОПКИ ПОСЛЕ РЕЗУЛЬТАТА
# =========================
def get_result_keyboard():
    keyboard = [
        [InlineKeyboardButton("📸 Instagram", url="https://www.instagram.com/tochka_perezapuska")],
        [InlineKeyboardButton("🎵 TikTok", url="https://www.tiktok.com/@tochka_perezapuska")],
        [InlineKeyboardButton("▶ YouTube", url="https://youtube.com/@tochka_perezapuska")],
        [InlineKeyboardButton("🔁 Пройти ещё раз", callback_data="restart")]
    ]
    return InlineKeyboardMarkup(keyboard)