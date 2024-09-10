from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("__name__")
#define the entrance functionality
@app.route("/")
def load_detector():
    #load the index
    return render_template("index.html")

#define the response to the button press
@app.route("/emotionDetector", methods=["GET","POST"])
def emo_detector():
    #get the input and pass it to the emotion detector
    inputText = request.args.get('textToAnalyze')
    emotions = emotion_detector(inputText)

    #format the response
    response = "For the given statement, the system response is "
    #add in the emotions
    response = response + f"'anger': {emotions['anger']}, "  
    response = response + f"'disgust': {emotions['disgust']}, "  
    response = response + f"'fear': {emotions['fear']}, "  
    response = response + f"'joy': {emotions['joy']}, "  
    response = response + f"and 'sadness': {emotions['sadness']}. "    
    response = response + f"The dominant emotion is <b>{emotions['dominant_emotion']}</b>"  
    return response

if __name__ == "__main__":
    app.run(debug=True)