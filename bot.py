from telegram.ext import Updater, CommandHandler
import requests

# =============================
# CONFIG
# =============================

BOT_TOKEN = "8383695498:AAG3iyK2Uldaene9NS7g4Anc3BRozTOZuDc"

PRODUCTS = [
    {
        "name": "Produk 1",
        "url": "https://hrtagold.id/api/v1/catalogs/product/43c9d78b-acf4-811d-c3e1-d126a53cc581"
    },
    {
        "name": "Produk 2",
        "url": "https://hrtagold.id/api/v1/catalogs/product/d9f6a8ed-cfba-a50a-32f0-9ac4907dbed3"
    },
    {
        "name": "Produk 3",
        "url": "https://hrtagold.id/api/v1/catalogs/product/95b9ef98-6404-9eed-bfda-007ce41fd77e"
    }
]

# =============================
# FUNCTION
# =============================

def get_product_data(api_url):
    r = requests.get(api_url, timeout=10)
    data = r.json()

    product_name = data["data"]["name"]
    stock = data["data"]["stock"]

    return product_name, stock


def start(update, context):
    msg = (
        "🤖 Bot Stock Monitor Aktif\n\n"
        "Gunakan perintah:\n"
        "/cek → cek stok semua produk"
    )
    update.message.reply_text(msg)


def cek(update, context):
    result_msg = "📦 *STOK PRODUK HRTAGOLD*\n\n"

    for product in PRODUCTS:
        try:
            name, stock = get_product_data(product["url"])

            result_msg += (
                f"🛒 *{name}*\n"
                f"Stock: {stock}\n\n"
            )

        except Exception as e:
            result_msg += (
                f"⚠️ {product['name']}\n"
                "Gagal mengambil data\n\n"
            )

    update.message.reply_text(result_msg, parse_mode="Markdown")


# =============================
# MAIN
# =============================

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("cek", cek))

    print("Bot berjalan...")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
