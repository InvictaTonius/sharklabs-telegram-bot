import os
import logging
from dotenv import load_dotenv
import requests
from telegram.ext import Updater, CommandHandler

# Load .env file
load_dotenv()
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

API_BASE = "https://public-api.sharkpool.org"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def fetch_json(path: str):
    url = f"{API_BASE}{path}"
    r = requests.get(url, timeout=10)
    r.raise_for_status()
    return r.json()


def start(update, context):
    update.message.reply_text(
        "🦈 SharkLabs Bot\n\n"
        "/metrics - show metrics\n"
        "/lst - show LST history\n"
        "/stake <voteaddr> - show validator stake"
    )


def metrics(update, context):
    try:
        data = fetch_json("/metrics")
        msg = (
            "📊 SharkLabs Metrics\n\n"
            f"Epoch: {data['epoch']} ({data['epochProgress']}%)\n"
            f"Remaining: {data['remainingTime']}s\n"
            f"APY: {data['sharkSolApy']}%\n"
            f"Pool: {data['poolAmount']} lamports\n"
            f"SOL Price: ${data['solanaPrice']}\n"
            f"TPS: {data['transactionsPerSecond']}"
        )
        update.message.reply_text(msg)
    except:
        update.message.reply_text("❌ Error fetching metrics.")


def lst(update, context):
    try:
        data = fetch_json("/lst/metrics")["metrics"][-5:]
        lines = ["📈 LST Metrics (last 5):"]
        for m in data:
            ts = m["time"].replace("T", " ").replace("Z", "")
            lines.append(f"{ts} — APY: {m['ratioApy']} | Lamports: {m['lastEpochTotalLamports']}")
        update.message.reply_text("\n".join(lines))
    except:
        update.message.reply_text("❌ Error fetching LST metrics.")


def stake(update, context):
    if len(context.args) == 0:
        update.message.reply_text("Usage: /stake <vote_address>")
        return

    vote = context.args[0]
    try:
        data = fetch_json(f"/validators/vote/{vote}/stake")
        msg = (
            f"🦈 Stake for {vote}\n"
            f"Current Stake: {data['currentStake']} lamports"
        )
        update.message.reply_text(msg)
    except:
        update.message.reply_text("❌ Invalid validator or API error.")


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("metrics", metrics))
    dp.add_handler(CommandHandler("lst", lst))
    dp.add_handler(CommandHandler("stake", stake))

    print("Bot is running...")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()


