# from fetchData.loadData import getChampionsImage, getItemsImage, getChampions, getItems
# from config import CONSTANTS_MANAGER
# from helper import helper
# import os

# import cv2
# import numpy as np


# # def getAllInfo():
# #     os.chdir("..")
# #     os.chdir("web")
# #     print(os.path.realpath(os.getcwd()))
# #     # getChampions()
# #     # getItems()
# #     # getItemsImage()
# #     # getChampionsImage()


# if __name__ == "__main__":
#     # Change to parent directory
#     getAllInfo()
#     print(os.path.realpath(os.getcwd()))

"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai

# genai.configure(api_key="AIzaSyDCQ9pFO-O-n7Q5fAUp0C56ncJklOPiHZk")

# Create the model
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    # safety_settings = Adjust safety settings
    # See https://ai.google.dev/gemini-api/docs/safety-settings
    tools="code_execution",
)

chat_session = model.start_chat(history=[])

response = chat_session.send_message(
    (
        "What is the sum of the first 50 prime numbers? "
        "Generate and run code for the calculation, and make sure you get all 50."
    )
)

print(response.text)
