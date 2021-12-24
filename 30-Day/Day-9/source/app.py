from flask import Flask, request, render_template_string
import subprocess
app = Flask(__name__)
app.secret_key = "ccsCTF{CMD_1S_h16h_vulnerability}"


@app.route("/")
def index():
    search = request.args.get('search') or None
    template = '''

		<h1> ?search= </h1>
		{}
	'''.format(search)

    return render_template_string(template)
