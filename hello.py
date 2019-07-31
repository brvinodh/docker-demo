from flask import Flask
import numpy as np

app = Flask(__name__)


@app.route("/quote")
def quote():
    num = np.random.random_integers(0,16)
    return quotes[num]

@app.route("/")
def hello():
    return "Hello World -- from Docker!"

quotes=["I finally realized that people are prisoners of their phones... that's why it's called a ''cell'' phone.",
"What is the best thing to do when you have a hole in a boat and water is leaking inside? Make another hole to drain the water.",
"I had an extremely busy day, converting oxygen into carbon dioxide. ",
"I had an extremely busy day, converting oxygen into carbon dioxide. ",
"There are a 100 billions nerves in the human body, and there are people who have the ability to irritate all of them. ",
"Did you just fall? No, I was checking if gravity still works. ",
"It takes real skills to choke on air, fall up the stairs and trip over nothing. I have those skills. ",
"There are so many times I made you angry, upset, irritated and tired. Today I just wanted to say that I'm thinking of continuing. ",
"Sometimes I just want someone to hug me and say ''I know it's hard, but you'll be okay. Here's a coffee and a million dollars.'' ",
"I don't understand people who say ''I don't know how to thank you.'' Like they never heard of money. ",
"It may look like I'm doing nothing, but in my head I'm quite busy. ",
"Why is Monday so far from Friday, and Friday so close to Monday? ",
"Singing in the shower is all fun and games until you get shampoo in your mouth. Then it becomes a soap opera. ",
"It's true that we don't know what we've got until we lose it, but it's also true that we don't know what we've been missing until it arrives. ",
"Laughing is one of the best exercises, it's like running inside your mind. You can do it almost anywhere and it's even better with a friend. ",
"Insanity: doing the same thing over and over again and expecting different results. ",
"Your secrets are safe with me... I wasn't even listening. "]

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
