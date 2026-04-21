from groq import Groq
from app.config import settings

client = Groq(api_key=settings.GROQ_API_KEY)

SYSTEM_PROMPT = """You are PrepMate, an expert AI interviewer conducting a mock interview.
You have access to the candidate's resume. Your job is to:
1. Ask one question at a time — either technical or HR/behavioural
2. Listen to the candidate's answer
3. Give brief feedback on their answer (1-2 lines)
4. Then ask the next relevant question
5. Mix technical and HR questions naturally
6. Base technical questions on their actual resume skills and experience

Rules:
- Ask only ONE question per response
- Keep feedback short and constructive
- Be encouraging but honest
- Do not reveal you are an AI unless directly asked
- Start by greeting the candidate and asking the first question
"""

def build_messages(resume_text: str, conversation_history: list) -> list:
    messages = [
        {
            "role": "system",
            "content": f"{SYSTEM_PROMPT}\n\nCANDIDATE RESUME:\n{resume_text}"
        }
    ]
    messages.extend(conversation_history)
    return messages


def get_ai_response(resume_text: str, conversation_history: list) -> str:
    messages = build_messages(resume_text, conversation_history)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7,
        max_tokens=500
    )

    return response.choices[0].message.content