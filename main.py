"""
Written by Andrew Bond

Python Developer | Network Designer | Superyacht Builder (M/Y Eris)

# Copyright (c) 2023, ANDREW BOND. All rights reserved.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

LinkedIn: https://www.linkedin.com/in/ahbond/
SJSU: https://www.sjsu.edu/people/andrew.bond/
Email: abptlm@gmail.com
"""

from flask import Flask, render_template
import dash_2

app = Flask(__name__)

# Define your Flask routes
@app.route('/')
def index():
    return render_template('index.html', gauge1=dash-2.gauge1, gauge2=dash-2.gauge2)

if __name__ == '__main__':
    app.run(debug=True)
