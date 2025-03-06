# 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
from openai import OpenAI
import streamlit as st  

# pip install openai streamlit
# for run: streamlit run open.py

# openRouter

st.title("Chat with Palak") 
text = st.text_input("Enter your name")
ans = st.button("Check Answer")

def output(que):
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key="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"  
    )

    completion = client.chat.completions.create(
  extra_headers={
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  extra_body={},
  model="deepseek/deepseek-r1-distill-llama-8b",
  messages=[
    {
      "role": "user",
      "content": que
    }
  ]
)
    
    return completion.choices[0].message.content

if ans:
    if text.strip():  
        st.write(output(text))
    else:
        st.warning("Please enter some text before checking the answer!")