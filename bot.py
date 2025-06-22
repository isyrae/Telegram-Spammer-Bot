import asyncio
import time
from telegram import Bot
from telegram.error import RetryAfter, TimedOut, NetworkError
from config import BOT_TOKEN, GROUP_CHAT_ID, MESSAGE_TEXT, PHOTO_PATH, MAX_MESSAGES_PER_MINUTE

SAFE_INTERVAL = 60 / MAX_MESSAGES_PER_MINUTE
bot = Bot(token=BOT_TOKEN)

async def spam_messages():
    print("🚀 [@isyrae] Spammer started. Sending images safely...")
    sent_count = 0

    while True:
        try:
            with open(PHOTO_PATH, 'rb') as photo:
                await bot.send_photo(chat_id=GROUP_CHAT_ID, photo=photo, caption=MESSAGE_TEXT)
            sent_count += 1
            print(f"✅ Sent {sent_count} image(s).")
            await asyncio.sleep(SAFE_INTERVAL)

        except RetryAfter as e:
            print(f"⏳ Rate limit! Sleeping {e.retry_after}s...")
            await asyncio.sleep(int(e.retry_after) + 1)

        except (TimedOut, NetworkError) as e:
            print(f"⚠️ Network error: {e}. Retrying in 5s...")
            await asyncio.sleep(5)

        except FileNotFoundError:
            print(f"❌ Image file not found at {PHOTO_PATH}. Check the path.")
            break

        except Exception as e:
            print(f"❌ Unknown error: {e}")
            break

if __name__ == "__main__":
    asyncio.run(spam_messages())
