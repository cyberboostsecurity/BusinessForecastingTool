import sqlite3
import streamlit as st

# Function to set up the database
def setup_database():
    conn = sqlite3.connect("business_app.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resource_allocation (
            id INTEGER PRIMARY KEY,
            sales_estimate REAL,
            employees INTEGER,
            equipment_needed TEXT
        )
    """)
    conn.commit()
    return conn

# Resource Allocation Module
def resource_allocation():
    st.header("Resource Allocation")
    st.write("Plan and allocate resources based on expected sales and availability.")

    # User inputs
    sales_estimate = st.number_input("Expected Monthly Sales (\u00A3)", min_value=0.0, step=100.0)
    employees = st.number_input("Number of Employees", min_value=0, step=1)
    equipment_needed = st.text_area("Equipment Needed", placeholder="List equipment here...")

    # Set up the database
    conn = setup_database()
    cursor = conn.cursor()

    # Save data
    if st.button("Save Data"):
        cursor.execute(
            "INSERT INTO resource_allocation (sales_estimate, employees, equipment_needed) VALUES (?, ?, ?)",
            (sales_estimate, employees, equipment_needed)
        )
        conn.commit()
        st.success("Data saved successfully!")

    # View data
    if st.button("View Saved Data"):
        cursor.execute("SELECT * FROM resource_allocation")
        rows = cursor.fetchall()
        if rows:
            st.write("### Saved Data")
            for row in rows:
                st.write(f"ID: {row[0]}, Sales: \u00A3{row[1]}, Employees: {row[2]}, Equipment: {row[3]}")
        else:
            st.info("No data found.")

    # Clear data
    if st.button("Clear Data"):
        cursor.execute("DELETE FROM resource_allocation")
        conn.commit()
        st.warning("All data cleared.")

    # Close the database connection
    conn.close()

