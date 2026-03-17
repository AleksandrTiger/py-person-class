class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        result.append(new_person)

    for i in range(len(people)):
        person = people[i]
        person_obj = result[i]

        if "wife" in person and person["wife"] is not None:
            wife_name = person["wife"]
            person_obj.wife = Person.people[wife_name]

        if "husband" in person and person["husband"] is not None:
            husband_name = person["husband"]
            person_obj.husband = Person.people[husband_name]

    return result
