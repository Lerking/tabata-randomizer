from exercises import EXERCISES
from random import shuffle
from gtts import gTTS
import playsound
import os.path

class TabataRandomizer():
    def __init__(self, number_of_sets: int = 8, number_of_reps: int = 4,
                rest_time: int = 15, work_time: int = 30):
        self.number_of_sets = number_of_sets
        self.number_of_reps = number_of_reps
        self.rest_time = rest_time
        self.work_time = work_time
        self.interval_time = self.rest_time + self.work_time
        self.exercises = EXERCISES

    def randomize(self):
        exercises = self.exercises
        shuffle(exercises)
        ex = []
        slots = 0
        for index, exercise in enumerate(exercises):
            tmp = {}
            slots += exercise['slots']
            if slots > self.number_of_sets:
                slots -= exercise['slots']
                continue
            tmp['name'] = exercise['name']
            tmp['speak'] = exercise['speak']
            ex.append(tmp)
            if not os.path.exists('audio/'+exercise['speak']):
                self.gen_audio(exercise['name'], exercise['speak'])
        return ex

    def gen_audio(self, text: str, speak: str):
        if 'x2' in text:
            text = text.replace('x2', 'times 2')
        tts = gTTS(text='Next up, '+text, lang='en', slow=False)
        tts.save('audio/'+speak)
        
    def get_exercises(self):
        return self.exercises

    def get_training_plan(self):
        training_plan = []
        for exercise in self.randomize():
            training_plan.append(exercise)
        return training_plan

    def get_training_time(self):
        return self.interval_time * self.number_of_sets * self.number_of_reps

if __name__ == '__main__':
    TE = TabataRandomizer()
    print(TE.get_training_plan())
    print(f'Combined training time: {TE.get_training_time() / 60:0.0f} minutes')
    print(TE.get_training_plan())
    print(f'Combined training time: {TE.get_training_time() / 60:0.0f} minutes')
    print(TE.get_training_plan())
    print(f'Combined training time: {TE.get_training_time() / 60:0.0f} minutes')
    print(TE.get_training_plan())
    print(f'Combined training time: {TE.get_training_time() / 60:0.0f} minutes')
    print(TE.get_training_plan())
    print(f'Combined training time: {TE.get_training_time() / 60:0.0f} minutes')
    print(TE.get_training_plan())
    print(f'Combined training time: {TE.get_training_time() / 60:0.0f} minutes')
    print(TE.get_training_plan())
    print(f'Combined training time: {TE.get_training_time() / 60:0.0f} minutes')
    print(TE.get_training_plan())
    print(f'Combined training time: {TE.get_training_time() / 60:0.0f} minutes')
    print(TE.get_training_plan())
    print(f'Combined training time: {TE.get_training_time() / 60:0.0f} minutes')
    print(TE.get_training_plan())
    print(f'Combined training time: {TE.get_training_time() / 60:0.0f} minutes')
    print(TE.get_training_plan())
    print(f'Combined training time: {TE.get_training_time() / 60:0.0f} minutes')
    pass
