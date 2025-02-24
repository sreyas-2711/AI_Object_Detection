from groq import Groq
import base64
import os


# Function to encode the local image into a base64 string
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Specify the path to your local image file
def get_groq_response(imagepath):
    base64_image = encode_image(imagepath)

    # Initialize the Groq client (ensure your GROQ_API_KEY is set in your environment)

    os.environ["GROQ_API_KEY"] = "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"
    client = Groq()

    # Create a chat completion request using a Llama Vision preview model.
    # The prompt instructs the model to list the objects detected in the image.
    chat_completion = client.chat.completions.create(
        model="llama-3.2-11b-vision-preview",  # or "llama-3.2-90b-vision-preview"
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "list the objects and 5 project ideas along with a brief idea on what we can do with it."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
    )
    return chat_completion.choices[0].message.content


def get_groq_quiz(imagepath):
    base64_image = encode_image(imagepath)

    # Initialize the Groq client (ensure your GROQ_API_KEY is set in your environment)

    os.environ["GROQ_API_KEY"] = "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"
    client = Groq()

    # Create a chat completion request using a Llama Vision preview model.
    # The prompt instructs the model to list the objects detected in the image.
    chat_completion = client.chat.completions.create(
        model="llama-3.2-11b-vision-preview",  # or "llama-3.2-90b-vision-preview"
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "list the objects and 5 kahoot type quiz questions on that object(s)"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
    )
    return chat_completion.choices[0].message.content