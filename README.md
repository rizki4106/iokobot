# iokobot
iokobot is a python library for help you to create a bot easly. We use machine learning algorithm to develop this bot

# Installation
```bash
pip3 install iokobot
```
or
```bash
git clone https://github.com/rizki4106/iokobot.git
```
```bash
cd iokobot && pip3 install -r requrements.txt
```

# How to use
This bot need training data for learn what should answer returned. you can use your own training data but make sure your data saved as csv file and on csv file there are two columns, first columns is the questions and second column is the answer, look at example below.

| questions | answers |
| --------- | ------- |
| what is computer ? | A computer is a machine that can be instructed to carry out sequences of arithmetic or logical operations automatically via computer programming |
| what is programming language ? |  programming language is a formal language comprising a set of instructions that produce various kinds of output. Programming languages are used in computer programming to implement algorithms |

```python
from iokobot import BotBody

bot = BotBody()
bot.fit("training.csv")
pred = bot.predict(""What is programming language ?")

score = bot.score()

print(pred)
print(score)
```
|No | Name | Description |
|---| ---- | ----------- |
|1| predict | get the answer from the bot |
|2| score | similarity score between your question and training data. this score from range -1 and 1. -1 is perfect different and 1 is perfect same|

#### notice
this bot will answer the questions based on similarity questions on training data, if you have more training data that would be better