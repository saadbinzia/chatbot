from flask import Flask, request, jsonify

from main import chatWithBot

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def chatBot():
    chatInput = request.form['chatInput']
    return jsonify(chatBotReply=chatWithBot(chatInput))


if __name__ == '__main__':
    app.run(host='https://mobi-zilla-chatbot.vercel.app/', debug=True)