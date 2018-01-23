from sopel import module
from emo.wdemotions import EmotionDetector

emo = EmotionDetector()
emoArray = []

@module.rule('')
def hi(bot, trigger):
    # emoArray.append(emo)
    emo(trigger)
    # bot.say('Hi, ' + trigger.nick)
    # print emo.detect_emotion_in_raw(bot, trigger)
