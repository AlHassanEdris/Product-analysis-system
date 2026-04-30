import pandas as pd

# قراءة الداتا
df = pd.read_csv("products.csv")

print("Before cleaning:", len(df))

# 1. حذف أي صفوف فاضية
df = df.dropna()

# 2. حذف التكرار
df = df.drop_duplicates()

# 3. تنظيف النصوص
df["name"] = df["name"].str.strip()
df["price"] = df["price"].str.strip()

# 4. تحويل السعر لرقم (اختياري مهم)
df["price"] = df["price"].str.replace("EGP", "", regex=False)
df["price"] = df["price"].str.replace(",", "", regex=False)

# 5. فلترة منتجات بدون اسم أو سعر
df = df[df["name"].str.len() > 0]
df = df[df["price"].str.len() > 0]

# 6. حفظ نسخة نظيفة
df.to_csv("products_clean.csv", index=False, encoding="utf-8")

print("After cleaning:", len(df))
print("Saved: products_clean.csv")