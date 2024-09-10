import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        #test joy
        self.asserEqual(emotion_detector("I am really glad this happened")['dominant_emotion'],'joy')

        #test anger
        self.asserEqual(emotion_detector("I am really mad about this")['dominant_emotion'],'anger')

        #test disgust
        self.asserEqual(emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'],'disgust')

        #test sadness
        self.asserEqual(emotion_detector("I am so sad about this")['dominant_emotion'],'sadness')

        #test fear
        self.asserEqual(emotion_detector("I am really afraid this will happen")['dominant_emotion'],'fear')

if __name__ == "__main__":
    unittest.main()