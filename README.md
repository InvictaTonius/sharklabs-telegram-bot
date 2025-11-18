# SharkLabs Telegram Bot

This Telegram bot interacts with the official **SharkLabs / SharkPool Public API** and provides Solana staking metrics, LST data, and validator stake information.  
This project was built as part of the **SharkLabs coding task**.

---

## 🚀 Features & Commands

### **/start**
Displays the bot menu and list of available commands.

### **/metrics**
Shows core SharkPool metrics:
- Epoch  
- Epoch progress (%)  
- Remaining time  
- SharkSOL APY  
- Pool amount (lamports)  
- SOL price  
- Transactions per second (TPS)

### **/lst**
Shows the **last 5** LST (Liquid Staking Token) metrics including:
- Timestamp  
- APY  
- Last epoch total lamports  

### **/stake `<vote_address>`**
Provides the current stake amount for a specific validator.

Example:
```
/stake 7dHbWXg7SU9V…
```

---

## 🛠 Technologies Used

- **Python 3.11**
- **python-telegram-bot 13.15** (synchronous, stable version)
- **requests** (HTTP API requests)
- **python-dotenv** (for loading environment variables)
- **SharkLabs Public API**  
  https://public-api.sharkpool.org

---

## ▶️ How to Run Locally

### **1. Clone or download the project**

### **2. Create a `.env` file in the project folder**
Add this line (replace with your actual token from BotFather):

```
TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN_HERE
```

### **3. Install dependencies**

```
pip install -r requirements.txt
```

### **4. Run the bot**

```
python3.11 bot.py
```

When the bot is running, open Telegram and message your bot:
```
/start
/metrics
/lst
/stake <vote_address>
```

---

## 📦 Requirements File

Your `requirements.txt` should contain:

```
python-telegram-bot==13.15
requests
python-dotenv
```

---

## 📝 Submission Notes

This repository was created for the **SharkLabs Telegram Bot coding task**.  
If the repository is private, access has been granted to the SharkLabs team at:

```
sharksolnode@gmail.com
```

---

## 📄 License

This project is provided for evaluation and educational purposes.
