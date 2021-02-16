import click
import os

basehtml = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="{{url_for('static', filename='style.css')}}" type='text/css'>
    <title>Flask App</title>
</head>
<body>
    {% block content %}
        
    {% endblock content %}
</body>
</html>"""
w3csshtml = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link href="{{url_for('static', filename='style.css')}}" type='text/css'>
    <title>Flask App</title>
</head>
<body>
    {% block content %}
        
    {% endblock content %}
</body>
</html>"""
boothtml = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
    <link href="{{url_for('static', filename='style.css')}}" type='text/css'>
    <title>Flask App</title>
  </head>
  <body>
    {% block content %}
        
    {% endblock content %}
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
  </body>
</html>"""

@click.command("")
@click.option("--template", help="Specify whether to use bootstrap, w3.css or plain html")
def create_app(template):
    """
    Create a flask app template with either bootstrap, w3.css, or no external stylecheets
    """
    os.mkdir('templates')
    os.mkdir('static')
    open('static/style.css', 'x')
    if template == 'bootstrap':
        with open('templates/base.html', 'a') as f:
            f.write(boothtml)
    elif template == 'w3css':
        with open('templates/base.html', 'a') as f:
            f.write(w3csshtml)
    else:
        with open('templates/base.html', 'a') as f:
            f.write(basehtml)
if __name__ == '__main__':
    create_app()