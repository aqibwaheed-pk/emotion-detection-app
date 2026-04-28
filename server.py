'''
Executing this function initiates the application of sentiment
analysis to be executed over the Flask channel and deployed on
localhost:5000.
'''
# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

# Initiate the flask app
app = Flask(__name__)

@app.route("/emotionDetector")
def sent_analyzer():
    '''
    This code receives the text from the HTML interface and
    runs sentiment analysis over it using emotion_detector()
    function. The output returns the emotion scores and dominant emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    output = f"For the given statement, the system response is "
    output += f"'anger': {response['anger']}, "
    output += f"'disgust': {response['disgust']}, "
    output += f"'fear': {response['fear']}, "
    output += f"'joy': {response['joy']}, "
    output += f"'sadness': {response['sadness']}. "
    output += f"The dominant emotion is {response['dominant_emotion']}."

    return output

@app.route("/")
def render_index_page():
    '''
    This function initiates the rendering of the main application
    page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    '''
    This function executes the flask app and deploys it on localhost:5000
    '''
    app.run(host='localhost', port=5000, debug=True)