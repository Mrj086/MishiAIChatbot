# Mishi AI Chatbot using Google Gemini API
#MD. Miraj-Ul-Islam
!pip -q install -U google-genai

from google import genai

# Enter your API key
api_key = input("Enter your Gemini API key: ").strip()

# Create client
client = genai.Client(api_key=api_key)

print("\n🤖 Mishi AI Chatbot")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Mishi: Goodbye!")
        break

    if not user_input:
        continue

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_input
        )

        print("\nMishi:", response.text)
        print()

    except Exception as e:
        print("\n❌ Error:", e)
        print()