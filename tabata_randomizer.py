from exercises import EXERCISES
from random import shuffle

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
        for index, exercise in enumerate(exercises):
            if exercise['name'] == 'Side plank x2':
                if index <= 6:
                    return exercises[:self.number_of_sets - 1]
                elif index == 7:
                    return exercises[:self.number_of_sets - 1:1]
        return exercises[:self.number_of_sets]

    def get_exercises(self):
        return self.exercises

    def get_training_plan(self):
        training_plan = []
        for exercise in self.randomize():
            training_plan.append(exercise['name'])
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