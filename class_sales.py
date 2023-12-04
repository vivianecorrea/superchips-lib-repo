import streamlit as st
import sqlite3
import pandas as pd


class Sales():

    def create_sales_table():
        conn = sqlite3.connect('sales.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sales (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product TEXT,
                amount INTEGER,
                date DATE
            )
        ''')
        conn.commit()
        conn.close()

    def show_sales_summary():
        conn = sqlite3.connect('sales.db')
        df = pd.read_sql_query("SELECT * FROM sales", conn)
        conn.close()
        return df

    def add_sale(product, amount, date):
        conn = sqlite3.connect('sales.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO sales (product, amount, date) VALUES (?, ?, ?)", (product, amount, date))
        conn.commit()
        conn.close()

    def edit_sale(id, product, amount, date):
        conn = sqlite3.connect('sales.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE sales SET product=?, amount=?, date=? WHERE id=?", (product, amount, date, id))
        conn.commit()
        conn.close()

    def delete_sale(id):
        conn = sqlite3.connect('sales.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM sales WHERE id=?", (id,))
        conn.commit()
        conn.close()