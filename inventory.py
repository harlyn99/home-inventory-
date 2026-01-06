from datetime import datetime

# =========================
# 1. DATABASE SEMENTARA
# =========================

inventory = {
    "Makanan": {
        "Mi Instan Ayam Bawang": [
            {"jumlah": 2, "expired": "2026-03-20"},
            {"jumlah": 1, "expired": "2026-01-02"},
            {"jumlah": 2, "expired": "2026-04-06"}
        ]
    }
}

# =========================
# 2. FUNGSI CEK EXPIRED
# =========================

def cek_status(expired_date):
    today = datetime.today().date()
    exp = datetime.strptime(expired_date, "%Y-%m-%d").date()

    if exp < today:
        return "❌ Expired"
    elif (exp - today).days <= 30:
        return "⚠️ Hampir Expired"
    else:
        return "✅ Aman"

# =========================
# 3. TAMPILKAN INVENTORY
# =========================

def tampilkan_inventory():
    print("📦 INVENTORY RUMAH\n")

    for kategori, items in inventory.items():
        print(f"== {kategori} ==")

        for nama, batches in items.items():
            total_stok = sum(batch["jumlah"] for batch in batches)

            status_terburuk = min(
                (cek_status(batch["expired"]) for batch in batches),
                key=lambda s: ["❌ Expired", "⚠️ Hampir Expired", "✅ Aman"].index(s)
            )

            print(f"\n🍜 {nama}")
            print(f"Total stok: {total_stok}")
            print(f"Status: {status_terburuk}")

            for i, batch in enumerate(batches, start=1):
                print(
                    f"  Batch {i}: {batch['jumlah']} pcs | "
                    f"Exp: {batch['expired']} | "
                    f"{cek_status(batch['expired'])}"
                )

    print("\n=========================")

# =========================
# 4. JALANKAN PROGRAM
# =========================

tampilkan_inventory()
