# display.py

from status import cek_status

def tampilkan_inventory(inventory):
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
