import google.generativeai as genai

MODEL_NAME = "gemini-2.5-flash"

def build_prompt(profile, messages):

    conversation = ""

    for msg in messages:
        conversation += f"{msg['role']}: {msg['content']}\n"

    prompt = f"""
    User Profile:
    Interests: {profile['interests']}
    Skills: {profile['skills']}
    Education: {profile['education']}
    Experience: {profile['experience']}

    Conversation History:
    {conversation}

    Provide career guidance.
    """

    return prompt


def generate_response(prompt):

    try:

        model = genai.GenerativeModel(MODEL_NAME)

        response = model.generate_content(prompt)

        return response.text

    except Exception as e:

        return f"Error: {e}"
