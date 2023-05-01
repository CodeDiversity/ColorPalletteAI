import json
from flask import Flask, render_template, request
import openai
from dotenv import dotenv_values

app = Flask(__name__,
            template_folder='templates',
            static_url_path='',
            static_folder='static')

config = dotenv_values('.env')

openai.api_key = config['OPENAI_API_KEY']


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    app.logger.info('Hit the post request route')
    query = request.form.get("query")
    colors = get_colors(query)

    return colors


def get_colors(msg):
    prompt = f"""
  You are a color palette generating assistant that responds to text prompts for color pallets.
  You should generate color pallets that fit the theme or mood or instructions given in the prompt.
  The pallets should be between 2 and 8 colors.add()
  
  Q: Convert the following verbal description of a color pallete into a list of colors: The Mediterranean Sea
  A: ["#006699", "#66CCCC","#F0E68C", "#008000", "#F08080"]
  
  Q: Convert the followign verbal description of a color pallete into a list of colors: sgae, nature, earth
  A: ["#EDF1D6", "#9DC08B", "#609966", "#40513B"]
  
  Q: Convert the following verbal description of a color pallete into a list of colors: {msg}
  A:
  
  """
    response = openai.Completion.create(
        prompt=prompt,
        model="text-davinci-003",
        max_tokens=200,
    )

    colors = json.loads(response["choices"][0]["text"])
    return {"colors": colors}


if (__name__ == "__main__"):
    app.run(debug=True)
