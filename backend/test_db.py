import sys
from sqlalchemy import text

try:
    from app.db.database import engine
except Exception as e:
    print("Failed to import engine from app.db.database.")
    print("Error:", e)
    sys.exit(1)

def test_connection():
    print(f"Attempting to connect to: {engine.url.render_as_string(hide_password=True)}")
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("🎉 Database connection successful!")
            print("Query 'SELECT 1' returned:", result.scalar())
    except Exception as e:
        print("❌ Database connection failed!")
        print("Error details:", e)

if __name__ == "__main__":
    test_connection()
