import ollama
from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/summarize/")
def summarize(text: str = Form(...)):
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {"role": "user", "content": f"Summarize this:\n\n{text}"}
        ]
    )
    return {"summary": response['message']['content']}
