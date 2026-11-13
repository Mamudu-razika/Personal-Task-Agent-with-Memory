import os

import groq
import pydantic
import sqlmodel
from dotenv import load_dotenv

def main() -> None:
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

    status = f"yes ({len(api_key)} chars)" if api_key else "no"
    print(f"GROQ_API_KEY loaded: {status}")

    print(f"groq {groq.__version__}")
    print(f"sqlmodel {sqlmodel.__version__}")
    print(f"pydantic {pydantic.__version__}")


if __name__ == "__main__":
    main()