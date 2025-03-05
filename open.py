from openai import OpenAI
import streamlit as st  

# pip install openai streamlit
# for run: streamlit run open.py

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
