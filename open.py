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
