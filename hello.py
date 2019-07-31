from flask import Flask
  2 import numpy as np
  3
  4 app = Flask(__name__)
  5
  6
  7 @app.route("/quote")
  8 def quote():
  9     num = np.random.random_integers(0,16)
 10     return quotes[num]
 11
 12 @app.route("/")
 13 def hello():
 14     return "Hello World -- from Docker!"
 15
 16 quotes=["I finally realized that people are prisoners of their phones... that's why it's called a ''cell'' phone.",
 17 "What is the best thing to do when you have a hole in a boat and water is leaking inside? Make another hole to drain the water.",
 18 "I had an extremely busy day, converting oxygen into carbon dioxide. ",
 19 "I had an extremely busy day, converting oxygen into carbon dioxide. ",
 20 "There are a 100 billions nerves in the human body, and there are people who have the ability to irritate all of them. ",
 21 "Did you just fall? No, I was checking if gravity still works. ",
 22 "It takes real skills to choke on air, fall up the stairs and trip over nothing. I have those skills. ",
 23 "There are so many times I made you angry, upset, irritated and tired. Today I just wanted to say that I'm thinking of continuing. ",
 24 "Sometimes I just want someone to hug me and say ''I know it's hard, but you'll be okay. Here's a coffee and a million dollars.'' ",
 25 "I don't understand people who say ''I don't know how to thank you.'' Like they never heard of money. ",
 26 "It may look like I'm doing nothing, but in my head I'm quite busy. ",
 27 "Why is Monday so far from Friday, and Friday so close to Monday? ",
 28 "Singing in the shower is all fun and games until you get shampoo in your mouth. Then it becomes a soap opera. ",
 29 "It's true that we don't know what we've got until we lose it, but it's also true that we don't know what we've been missing until it arrives. ",
 30 "Laughing is one of the best exercises, it's like running inside your mind. You can do it almost anywhere and it's even better with a friend. ",
 31 "Insanity: doing the same thing over and over again and expecting different results. ",
 32 "Your secrets are safe with me... I wasn't even listening. "]

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
