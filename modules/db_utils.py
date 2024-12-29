import sqlite3
import json

# Database setup
DB_NAME = "business_calculator.db"

def init_db():
    """Initialize the database and create tables if they do not exist."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create the main data table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        key TEXT NOT NULL,
        value TEXT NOT NULL
    )
    """)

    # Create the risk data table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS risk_data (
        risk TEXT NOT NULL,
        likelihood REAL NOT NULL,
        adjusted_impact REAL NOT NULL,
        mitigation_cost REAL NOT NULL,
        risk_score REAL NOT NULL
    )
    """)

    # Create the financial metrics table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS financial_metrics (
        total_revenue REAL,
        total_costs REAL,
        profit_loss REAL
    )
    """)

    # Create the workforce metrics table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS workforce_metrics (
        total_staffing_costs REAL,
        revenue_per_employee REAL,
        cost_categories TEXT,
        cost_values TEXT
    )
    """)

    # Create the growth metrics table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS growth_metrics (
        average_roi REAL,
        payback_period REAL,
        roi_distribution TEXT
    )
    """)

    # Create the risk metrics table if it doesn't exist
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS risk_metrics (
        overall_risk_score REAL,
        mitigated_risks INTEGER,
        unmitigated_risks INTEGER,
        risk_categories TEXT,
        risk_values TEXT
    )
    """)

    # Create other necessary tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS overall_risk_score (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        score REAL NOT NULL
    )
    """)

    conn.commit()
    conn.close()

def save_to_database(key, value):
    """Save data to the database, replacing existing entries with the same key."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Serialize the value to a JSON string before saving
    value_serialized = json.dumps(value, default=str)  # Ensure that complex objects are converted to strings

    # Delete any existing data with the same key
    cursor.execute("DELETE FROM data WHERE key = ?", (key,))

    # Insert the new serialized data
    cursor.execute("INSERT INTO data (key, value) VALUES (?, ?)", (key, value_serialized))

    conn.commit()
    conn.close()

def load_from_database(key, default=None):
    """Load data from the database by key."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT value FROM data WHERE key = ?", (key,))
    row = cursor.fetchone()
    conn.close()
    
    # If data exists, deserialize it back to original format
    if row:
        return json.loads(row[0])  # Deserialize JSON string back into Python object
    return default

def clear_data(key=None):
    """Clear data from the database. If a key is provided, only clear that key."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    if key:
        cursor.execute("DELETE FROM data WHERE key = ?", (key,))
        cursor.execute(f"DELETE FROM {key}")  # Deleting from specific table if the key matches
    else:
        # Clear all relevant tables
        cursor.execute("DELETE FROM data")  # Clear general data table
        cursor.execute("DELETE FROM risk_data")  # Clear risk data
        cursor.execute("DELETE FROM financial_metrics")  # Clear financial metrics
        cursor.execute("DELETE FROM workforce_metrics")  # Clear workforce metrics
        cursor.execute("DELETE FROM growth_metrics")  # Clear growth metrics
        cursor.execute("DELETE FROM overall_risk_score")  # Clear overall risk score table

    conn.commit()
    conn.close()

def save_risk_data(risk_data):
    """Save risk data to the risk_data table."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Insert each row into the risk_data table
    for risk, likelihood, adjusted_impact, mitigation_cost, risk_score in risk_data:
        cursor.execute("""
        INSERT INTO risk_data (risk, likelihood, adjusted_impact, mitigation_cost, risk_score) 
        VALUES (?, ?, ?, ?, ?)
        """, (risk, likelihood, adjusted_impact, mitigation_cost, risk_score))

    conn.commit()
    conn.close()

def load_risk_data():
    """Load all risk data from the risk_data table."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Fetch all the risk data
    cursor.execute("SELECT * FROM risk_data")
    risk_data = cursor.fetchall()

    conn.close()
    return risk_data

# Initialize the database when the module is loaded
init_db()
