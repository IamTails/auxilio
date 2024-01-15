import os
import json
import random


def load_files_to_dict(directory):
    current_file_directory = os.path.dirname(os.path.realpath(__file__))
    full_directory = os.path.join(current_file_directory, directory)
    file_contents = {}
    files = os.listdir(full_directory)

    for filename in files:
        filepath = os.path.join(full_directory, filename)
        with open(filepath) as f:
            data = json.load(f)
        base_filename = os.path.splitext(filename)[0]
        file_contents[base_filename] = data
    return file_contents


contents = load_files_to_dict('../assets/arrays')
adv_failure_strings = contents['adv_failure_strings']
adv_scenarios = contents['adv_scenarios']
adv_success_strings = contents['adv_success_strings']
fake_robbery_scenarios = contents['fake_robbery_scenarios']
funny_crime_scenarios = contents['funny_crime_scenarios']
job_descriptions = contents['job_descriptions']
math_equations = contents['math_equations']
riddles = contents['riddles']
trivia_questions = contents['trivia_questions']


def get_random_adv_scenario():
    random.shuffle(adv_scenarios)
    return random.choice(adv_scenarios)


def get_random_adv_failure_string():
    random.shuffle(adv_failure_strings)
    return random.choice(adv_failure_strings)


def get_random_adv_success_string():
    random.shuffle(adv_success_strings)
    return random.choice(adv_success_strings)


def get_random_fake_robbery_scenario():
    random.shuffle(fake_robbery_scenarios)
    return random.choice(fake_robbery_scenarios)


def get_random_funny_crime_scenario():
    random.shuffle(funny_crime_scenarios)
    return random.choice(funny_crime_scenarios)


def get_random_job_description():
    random.shuffle(job_descriptions)
    return random.choice(job_descriptions)


def get_random_math_equation():
    random.shuffle(math_equations)
    return random.choice(math_equations)


def get_random_riddle():
    random.shuffle(riddles)
    return random.choice(riddles)


def get_random_trivia_question():
    random.shuffle(trivia_questions)
    return random.choice(trivia_questions)


