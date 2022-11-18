from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    user = os.getenv('DB_USER')
    host = os.getenv('HOST')
    database = os.getenv('DB_NAME')

    print("Connecting to postgresql")

    engine = create_engine('postgresql://user:postgres!host/database')

    connection = engine.connect()

    result = engine.execute(
        text(
            "SELECT * FROM account LIMIT 5"
        )
    )
    print(f"Selected {result.rowcount} rows.")

    for row in result.fetchall():
        print(row)

if __name__ == "__main__":
    main()
