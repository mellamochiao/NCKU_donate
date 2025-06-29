import pandas as pd
from datetime import datetime
import os
import questionary

def load_data(year):
    path = f"data/{year}donations.csv"
    if not os.path.exists(path):
        print(f"❌ 檔案 {path} 不存在！請先執行爬蟲。")
        return None
    return pd.read_csv(path)  # ❗️ 不預先處理 amount，避免炸掉

# 共用金額清理函數
def clean_amount(df):
    df = df.copy()
    df["amount"] = df["amount"].astype(str).str.replace("元", "", regex=True).str.replace(",", "", regex=True)
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df = df.dropna(subset=["amount"])
    return df

def show_unit_total(df):
    unit = questionary.text("請輸入你想查詢的單位名稱").ask()
    target = df[df["purpose"].str.contains(unit, na=False)]
    target = clean_amount(target)
    total = target["amount"].sum()
    print(f"\n{unit} 今年收到的總捐款金額為：{total:,.0f} 元\n")

def show_donor_total(df):
    name = questionary.text("請輸入你想查詢的捐款人").ask()
    target = df[df["donor"].str.contains(name, na=False)]
    target = clean_amount(target)
    total = target["amount"].sum()
    print(f"\n{name} 今年總共捐款：{total:,.0f} 元\n")

def show_donors_to_unit(df):
    unit = questionary.text("請輸入單位名稱").ask()
    target = df[df["purpose"].str.contains(unit, na=False)]
    target = clean_amount(target)
    group = target.groupby("donor")["amount"].sum()
    print(f"\n{unit} 今年收到的捐款來源與金額：")
    print(group.sort_values(ascending=False).to_string())
    print()


def main():
    year = questionary.text("請輸入要查詢的年份（例如 2025）").ask()
    df = load_data(year)
    if df is None:
        return

    while True:
        choice = questionary.select(
            "請選擇你想查詢的功能：",
            choices=[
                "🔎 查詢某單位受捐款總額",
                "🙋 查詢捐款人捐款總額",
                "🧾 查詢某單位受捐款細項",
                "🚪 離開"
            ]).ask()

        if choice.startswith("🔎"):
            show_unit_total(df)
        elif choice.startswith("🙋"):
            show_donor_total(df)
        elif choice.startswith("🧾"):
            show_donors_to_unit(df)
        else:
            print("👋 Bye!")
            break

if __name__ == "__main__":
    main()
