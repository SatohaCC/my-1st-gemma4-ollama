import ollama

MODEL = "gemma4:e4b"

system_prompt = """
あなたは優秀な薬剤師です。
患者さん質問に対して、平易な言葉で答えてください。
"""

stream = ollama.chat(
    model=MODEL,
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "ヒルドイドソフトという薬をもらったが、どの程度塗ればいいの？"},
    ],
    stream=True,
    options={
        "temperature": 0.1,
        "top_p": 0.9,
        "top_k": 40,
    }
)


for chunk in stream:
  print(chunk['message']['content'], end='', flush=True)

# Bad response: 薄く塗るように答えてしまう。
