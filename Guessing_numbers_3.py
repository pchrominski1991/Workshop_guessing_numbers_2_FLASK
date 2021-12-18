from flask import Flask, request

app = Flask(__name__)


FORM_get_1 = """<!DOCTYPE html>                              # Welcome form   
<html lang="en">
<form action="/" method="POST">
<head>
</head>
<H2>Choose and remember a number from 1 to 1000. <br>
<form>
<input type="hidden" name="min" value="{}"></input>
<input type="hidden" name="max" value="{}"></input>
<input type="submit" value="OK">
</form>
</html>"""

FORM_get_2 = """                                            
<!DOCTYPE html>
<html lang="en">
<form action="/" method="POST">
<head>
</head>
<h1>"Your number is: {guess} "</h1>
<form>
<input type="submit" name="answer" value="too big">
<input type="submit" name="answer" value="too small">
<input type="submit" name="answer" value="you won">
<input type="hidden" name="min" value="{min}">
<input type="hidden" name="max" value="{max}">
<input type="hidden" name="guess" value="{guess}">
</form>
</html>
"""

FORM_get_3 = """<!DOCTYPE html>                               
<html lang="en">
<form action="/" method="POST">
<head>
</head>
<h1>I guess! Your number is {guess} </h1>
</html>"""


@app.route('/', methods=["POST", "GET"])
def check():
    if request.method == "GET":
        return FORM_get_1.format(0, 1000)
    else:
        min_num = int(request.form.get("min"))
        max_num = int(request.form.get("max"))
        answer = request.form.get("answer")
        guess = int(request.form.get("guess", 500))
        if answer == "too big":
            max_num = guess
        elif answer == "too small":
            min_num = guess
        elif answer == "you won":
            return FORM_get_3.format(guess=guess)

        guess = (max_num - min_num) // 2 + min_num

        return FORM_get_2.format(guess=guess, min=min_num, max=max_num)


if __name__ == "__main__":
    app.run(debug=True, port=5002)