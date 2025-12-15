
from groq import Groq

# Initialize client
client = Groq(
    api_key="api_key"
)

def generate_caption(image_description):
    prompt = f"""
    You are an AI that creates short, creative image captions.
    Generate a caption for an image that shows:
    {image_description}
    """

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=1,
        max_tokens=60
    )

    # Correct way to extract text
    return completion.choices[0].message.content.strip()


if __name__ == "__main__":
    description = input("Describe the image: ")
    caption = generate_caption(description)
    print("\nGenerated Caption:")
    print(caption)
