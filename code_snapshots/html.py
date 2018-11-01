import os
from flask import Flask, render_template, g, request
import requests
import random

app = Flask(__name__)

	@app.route('/')
	def home():
		return 'home'

		@app.route('/categories')
		def category():
			categories = requests.get('http://jservice.io/api/categories', {'count': 10})
			category_json = categories.json()
			return categories.text	

			@app.route('/category/<category_id>')
			def category_question(category_id=None):
				questions = requests.get('http://jservice.io/api/category/', {'id': category_id}).json()['clues']
				question_obj = random.choice(questions)
				question, answer= question_obj['question'], question_obj['answer']
				return question + ' ' + answer

				@app.route('/question')
				def question():
					question_obj = requests.get('http://jservice.io/api/random').json()[0]
					question, answer = question_obj['question'], question_obj['answer']
					return question + ' ' + answer

					@app.route('/answer')
					def check_answer():
						real_answer = 'Yes'
						input_answer = 'Yes'
						if real_answer.lower() == input_answer.lower():
							return 'Correct'
							else:
							return 'Incorrect'


							if __name__ == '__main__':
							port = int(os.environ.get('PORT', 5000))
# app.run(host='0.0.0.0', port=port, debug=True)
app.run(debug=True)
