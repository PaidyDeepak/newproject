from config import model


def get_response(user_input, profile):

    prompt = f"""
    You are a career guidance expert.

    User Profile:
    Education: {profile.get("education")}
    Qualification: {profile.get("qualification")}
    Technologies: {profile.get("technologies")}
    Experience: {profile.get("experience")}

    User Question:
    {user_input}

    Provide clear career guidance.
    """

    response = model.generate_content(prompt)

    return response.text
