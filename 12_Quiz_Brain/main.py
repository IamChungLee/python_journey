from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    #Grab question parts from data.py and stores them in variables
    question_text = question["question"]
    question_answer = question["correct_answer"]
    #uses variables to put in in questions structure obtained in  question_model.py
    new_question = Question(question_text, question_answer)
    #stores loop of created questions into question_bank creating a list
    question_bank.append(new_question)

#call the funcitonal quiz class from quiz_brain and pass in the argument which has to be a quiz
#in this case out quiz questions we created above
quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")