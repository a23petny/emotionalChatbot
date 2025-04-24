import os
import json
import time
from flask import Flask, request, Response
from twilio_func import send_whatsapp_message 
from const import MSG_DIR, API_KEY, SYSTEM_MESSAGE
from openai import OpenAI
from pathlib import Path


client = OpenAI(api_key=API_KEY)

app = Flask(__name__)

def append_msg(phone, body, role):
    
    file_path = Path(MSG_DIR) / f"{phone}.json"

    if file_path.exists():
        with file_path.open("r", encoding="utf-8") as f:
            history = json.load(f)
    else:
        history = []

    history.append({
        "time": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "role": role,
        "body": body
    })

    with file_path.open("w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
    
    return history



@app.post("/receive")
def receive_whatsapp_message():
    to_number = request.form["From"]
    body = request.form["Body"]

    save_name = to_number.replace("whatsapp:", "").replace("+", "")
    history = append_msg(save_name, body, "user")

    chat_messages = [{"role": "system", "content": SYSTEM_MESSAGE}]
    for message in history:
        chat_messages.append({"role": message["role"], "content": message["body"]})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_messages
    )

    reply = response.choices[0].message.content.strip()

    append_msg(to_number, reply, "assistant")
    send_whatsapp_message(reply, to_number)
    return Response(status=200)


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port, debug=True)
