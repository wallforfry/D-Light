"""
Project : D-Light
File : main
Author : DELEVACQ Wallerand
Date : 19/06/17
"""

from flask import Flask, request, render_template_string

flaskPort = 5000

app = Flask(__name__)


@app.route("/d-light", methods=['GET'])
def led():
    if request.method == "GET":
        red = str(request.args.get('red'))
        green = str(request.args.get('green'))
        blue = str(request.args.get('blue'))
        white = str(request.args.get('white'))

        allumerLed(red, blue, green, white)

        return render_template_string(red+" "+green+" "+" "+blue+" "+white)


def allumerLed(red, blue, green, white):
    """
    Ecrivez ici le code pour allumer vos leds
    :param red: String red
    :param blue: String blue
    :param green: String green
    :param white: String white
    :return: None
    """

    #ÉCRIRE ICI ET RETIRER APRÈS LE MOT " pass " en dessous de cette ligne
    pass


if __name__ == "__main__":
    print("helloworld")
    app.run(host="0.0.0.0", port=flaskPort)
