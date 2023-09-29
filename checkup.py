import streamlit as st
import google.generativeai as palm
import base64
import json
import pprint

# Configure the client library by providing your API key.
palm.configure(api_key="AIzaSyB-6Ljt2vEA7uHjXyXrQF_8GgYZFQzMCQ4")

# Set default values
defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.25,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}

# Define the conversation context
context = "Goal: To provide a series of questions and guidelines to help women perform pre-screening for gynecological issues, guided by a seasoned gynecological doctor specialist, using simple layman terms and clear instructions, with visuals whenever possible, and referring to the latest research and highly credible and trustworthy websites for more information.\nAudience: Women of all ages.\n\nPurpose: To help women identify potential gynecological problems early on, so that they can seek appropriate medical care.\n\nContext: The user is interested in performing a pre-screening for gynecological issues, and is being guided by a seasoned gynecological doctor specialist.\n\nQuestions:\n- Please share your demographics (age, race and ethnicity, family history of any disease if applicable, and any lifestyle factors such as smoking, etc) with me, so that I can provide personalized suggestions.\n- Can you describe your symptoms? For example, \"I feel like I have a rock in my breast.\"\n- If you are feeling vague, please let me know, and I will ask further clarifying questions to help you.\n\nPrompts:\n- I am a seasoned gynecological doctor specialist, and I am here to help you keep track of your health and avoid future complications.\n- I will guide you through a series of questions and instructions, using simple layman terms and clear visuals.\n- If I encounter a use case that I don't understand, I will refer you to visit a doctor or provide resources you can read.\n- I will also provide simple, easy-to-follow suggestions to keep a healthy lifestyle for women of all ages.\n\nGuidelines:\n- Use simple layman terms and clear instructions, with visuals whenever possible.\n- Refer to the latest research and highly credible and trustworthy websites for more information.\n- Raise flags whenever you read alarming symptoms from the user.\n- Encourage the user to seek medical care if necessary.\n- Ask follow-up questions to clarify the user's symptoms and understanding of their health.\n- Process further information provided by the user in subsequent queries to provide more tailored guidance.\n\nProceed to ask the user more questions and provide guidance whenever more information is needed.\n\nProvide women with personalized, informative, and helpful pre-screening guidance, even if the user is vague or provides limited information in their initial query.\n\nAt the end of the conversation, summarize the key points and provide the user with resources to learn more from trustworthy and approved institutions.\n\nKeep conversations short and consistent.\nOnly provide further instructions or advice if requested."

# Define the example conversations
examples = [
  [
    "Hello, I'm interested in doing a pre-screening for gynecological issues.",
    "Great! I can help you with that. Please share your demographics (age, race and ethnicity, family history of any disease if applicable, and any lifestyle factors such as smoking, etc) with me, so that I can provide personalized suggestions."
  ],
  [
    "I'm 35 years old, and I identify as female.",
    "Okay. Can you describe your symptoms? Like, what are you feeling? Where? Are any unusual stuff in your body?"
  ],
  [
    "I've been having some abnormal vaginal discharge, and it's been making me feel really uncomfortable.",
    "I see. Can you tell me more about the color, consistency, and odor of the discharge?"
  ],
  [
    "It's a thick, white discharge, and it has a fishy odor.",
    "Okay. Have you had any other symptoms, such as pain, itching, or burning?"
  ],
  [
    "No, just the discharge.",
    "I see. I'm glad you're being proactive about your health. I'm going to ask you a few more questions to get a better understanding of your situation."
  ]
]

messages = [
  "What are some common gynecological symptoms that women should be aware of?",
  "Here are some common gynecological symptoms that women should be aware of:\n\n* Abnormal vaginal discharge: This can be any change in the color, consistency, or odor of your vaginal discharge. It can be a sign of infection, sexually transmitted disease, or other health problems.\n* Painful intercourse: This can be caused by a number of things, including infection, dryness, or inflammation.\n* Irregular menstrual bleeding: This can be a sign of a number of things, including pregnancy, hormonal imbalance, or fibroids.\n* Pelvic pain: This can be caused by a number of things, including infection, endometriosis, or ovarian cysts.\n* Vaginal itching: This can be caused by a number of things, including infection, dryness, or allergies.\n* Vaginal burning: This can be caused by a number of things, including infection, dryness, or allergies.\n* Vaginal odor: This can be caused by a number of things, including infection, poor hygiene, or certain medications.\n\nIf you are experiencing any of these symptoms, it is important to see a doctor to get a diagnosis and treatment."
]

print(messages)

# Start the Streamlit app
st.title("Gynecological Pre-screening Assistant")

# Request text input from the user
new_req = st.text_input("Please enter your request or query:")

# Define the next request handler
def next_request(new_req):
  """Handles the next request from the user."""

  # Get the user's response
  messages.append(new_req)
  print(messages)

  # Generate a response from the AI model
  ai_response = palm.chat(
    **defaults,
    context=context,
    examples=examples,
    messages=messages
  )

  # Update the Streamlit app with the AI response
  st.write(ai_response.last)

# Start the conversation
next_request(new_req)

# Run the Streamlit app
st.stop()

