import os
from langfuse import Langfuse

langfuse = Langfuse(
    os.environ["LANGFUSE_PUBLIC_KEY"],
    os.environ["LANGFUSE_SECRET_KEY"],
    host=os.environ.get("LANGFUSE_HOST", "https://us.cloud.langfuse.com"),
)
