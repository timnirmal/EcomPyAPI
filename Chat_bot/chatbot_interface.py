import json

import colorama
import numpy as np
from tensorflow import keras

colorama.init()

import pickle

with open("intents.json") as file:
    data = json.load(file)


def chat(input):
    inp: str = str(input)
    # time taken to load the model
    # start = time.time()

    # load trained model
    model = keras.models.load_model('chat_model')

    # load tokenizer object
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    # load label encoder object
    with open('label_encoder.pickle', 'rb') as enc:
        lbl_encoder = pickle.load(enc)

    # parameters
    max_len = 20

    while True:
        # print(Fore.LIGHTBLUE_EX + "User: " + Style.RESET_ALL, end="")
        if inp.lower() == "quit":
            break

        result = model.predict(keras.preprocessing.sequence.pad_sequences(tokenizer.texts_to_sequences([inp]),
                                                                          truncating='post', maxlen=max_len))
        tag = lbl_encoder.inverse_transform([np.argmax(result)])

        for i in data['intents']:
            if i['tag'] == tag:
                # print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL, np.random.choice(i['responses']))
                # time taken to finish the chat
                # end = time.time()
                # print("Time taken to load the model: ", end - start)
                return np.random.choice(i['responses'])

        # print(Fore.GREEN + "ChatBot:" + Style.RESET_ALL,random.choice(responses))

# print(Fore.YELLOW + "Start messaging with the bot (type quit to stop)!" + Style.RESET_ALL)
