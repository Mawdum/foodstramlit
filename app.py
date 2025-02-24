import streamlit as st
import pandas as pd
import random

# โหลดข้อมูล
file_path = "Lineman_Shops_Final_Clean.csv"
df = pd.read_csv(file_path)

# ตั้งค่าหัวข้อแอป
st.title("แนะนำเมนูอาหารเย็น")

# ตัวเลือกการกรอง
price_levels = df["price_level"].dropna().unique()
categories = df["category"].dropna().unique()

filter_type = st.radio("เลือกประเภทการกรอง", ["price_level", "category"])

if filter_type == "price_level":
    choice = st.selectbox("เลือกระดับราคา", price_levels)
    filtered_df = df[df["price_level"] == choice]
else:
    choice = st.selectbox("เลือกหมวดหมู่อาหาร", categories)
    filtered_df = df[df["category"] == choice]

# ปุ่มกดเพื่อแสดงผล
if st.button("แสดงเมนู"):
    # หากมีข้อมูลที่ตรงตามเงื่อนไข
    if not filtered_df.empty:
        # สุ่มผลลัพธ์ไม่เกิน 5 รายการ
        sampled_df = filtered_df.sample(n=min(5, len(filtered_df)))

        # แสดงผลลัพธ์
        for index, row in sampled_df.iterrows():
            st.subheader(row["name"])
            st.write(f"**หมวดหมู่:** {row['category']}")
            st.write(f"**ระดับราคา:** {row['price_level']}")
            st.write(f"[ดูเพิ่มเติม]({row['url']})")
    else:
        st.write("ไม่พบเมนูที่ตรงกับเงื่อนไขของคุณ")
