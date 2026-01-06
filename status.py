# status.py

from datetime import datetime

def cek_status(expired_date):
    today = datetime.today().date()
    exp = datetime.strptime(expired_date, "%Y-%m-%d").date()

    if exp < today:
        return "❌ Expired"
    elif (exp - today).days <= 30:
        return "⚠️ Hampir Expired"
    else:
        return "✅ Aman"
