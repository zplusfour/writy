import flask
import openai

app = flask.Flask(__name__)
openai.api_key_path = '.env'

@app.route('/')
def index():
  return flask.render_template('index.html', text="", autoq="")

@app.route('/public/<path:path>')
def public(path):
  return flask.send_from_directory('public', path)


@app.route('/', methods=['POST'])
def index_post():
  text = flask.request.form['text']
  response = openai.Completion.create(
    engine="davinci",
    prompt=f"{text}",
    temperature=0,
    max_tokens=64,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["."]
  )
  autoq = response.choices[0].text
  return flask.render_template('index.html', text=text, autoq=autoq)

if __name__ == '__main__':
  app.run(debug=True)