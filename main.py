import os
import random
import uuid
from file_operations import render_template
from faker import Faker


def generate_context():
    fake = Faker("ru_RU")
    letters_mapping = {}
    with open('letters_mapping.txt') as f:
        letters_mapping = eval(f.read())

    skills = []
    with open('skills.txt') as f:
        skills = [line.strip() for line in f]

    runic_skills = []
    for skill in skills:
        for letter, replacement in letters_mapping.items():
            skill = skill.replace(letter, replacement)
        runic_skills.append(skill)

    selected_skills = random.sample(runic_skills, 3)

    strength = random.randint(3, 18)
    agility = random.randint(3, 18)
    endurance = random.randint(3, 18)
    intelligence = random.randint(3, 18)
    luck = random.randint(3, 18)

    context = {
        "first_name": fake.name_male().split()[0],
        "last_name": fake.last_name_male(),
        "job": fake.job(),
        "town": fake.city(),
        "strength": strength,
        "agility": agility,
        "endurance": endurance,
        "intelligence": intelligence,
        "luck": luck,
        "skill_1": selected_skills[0],
        "skill_2": selected_skills[1],
        "skill_3": selected_skills[2]
    }

    name = f"{context['first_name']} {context['last_name']}"
    context["name"] = name
    context["id"] = str(uuid.uuid4())

    return context


def main():
    output_folder = "cards"
    os.makedirs(output_folder, exist_ok=True)
    for i in range(1, 11):
        context = generate_context()
        filename = f"user{i}.svg"
        output_path = os.path.join(output_folder, filename)
        render_template("template.svg", output_path, context)


if __name__ == '__main__':
    main()
