from google import genai

client = genai.Client(api_key="AIzaSyAVqTr5dasvbhO38VZJEH-eGDRF--HUfys")

prompt = input("Ingresa un prompt: ")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt,
)

print(response.text)