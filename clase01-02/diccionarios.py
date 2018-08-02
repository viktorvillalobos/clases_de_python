# Lista de personas
personas = [
    {
        "name": "Eli",
        "age": 26
    },
    {
        "name": "Victor",
        "age": 26
    }
]

for persona in personas:
    if persona.get('name') == 'Victor':
        persona['age'] = 30


print(personas)



