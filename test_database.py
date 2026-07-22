from src.app.core.database import engine
from sqlalchemy import text


try:

    with engine.connect() as connection:

        result = connection.execute(
            text("SELECT 1")
        )

        print(result.fetchone())


except Exception as e:

    print(e)