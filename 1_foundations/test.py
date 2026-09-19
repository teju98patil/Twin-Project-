print("start")
import ssl
ssl.create_default_context()
print("ssl ok")
import httpx
httpx.Client()
print("httpx ok")
from openai import OpenAI
print("openai imported")
client = OpenAI(api_key="dummy")
print("client created")