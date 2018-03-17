from sopel import module
from emo.wdemotions import EmotionDetector

emo = EmotionDetector()


@module.rule('')
def hi(bot, trigger):

    # Print the text to default output.
    print('\n' + trigger.nick + ': "' + trigger + '"')
    print (emo.detect_emotion_in_raw(trigger))
