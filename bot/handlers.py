from telegram import Update
from telegram.ext import ContextTypes

from bot.questions import QUESTIONS
from bot.results import RESULTS
from bot.keyboards import get_start_keyboard, get_question_keyboard, get_result_keyboard


def reset_user_data(context):
    context.user_data["question_index"] = 0
    context.user_data["scores"] = {
        "survivor": 0,
        "between": 0,
        "builder": 0,
        "adapted": 0,
    }


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reset_user_data(context)

    text = (
        "Привет.\n\n"
        "Это честный тест:\n"
        "Ты адаптировался(ась) — или просто выживаешь?\n\n"
        "Нажми кнопку ниже."
    )

    await update.message.reply_text(
        text,
        reply_markup=get_start_keyboard()
    )


async def show_question(query, context):
    question_index = context.user_data["question_index"]
    question_text = QUESTIONS[question_index]["text"]

    await query.edit_message_text(
        question_text,
        reply_markup=get_question_keyboard(question_index)
    )


async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data in ("start_test", "restart"):
        reset_user_data(context)
        await show_question(query, context)
        return

    if data.startswith("answer_"):
        answer_index = int(data.split("_")[1])
        question_index = context.user_data["question_index"]

        selected_answer = QUESTIONS[question_index]["answers"][answer_index]
        result_type = selected_answer["type"]

        context.user_data["scores"][result_type] += 1
        context.user_data["question_index"] += 1

        if context.user_data["question_index"] >= len(QUESTIONS):
            scores = context.user_data["scores"]
            final_result = max(scores, key=scores.get)

            result = RESULTS[final_result]
            text = f"{result['title']}\n\n{result['description']}"

            await query.edit_message_text(
                text,
                reply_markup=get_result_keyboard()
            )
        else:
            await show_question(query, context)