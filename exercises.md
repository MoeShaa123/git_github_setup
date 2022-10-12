## Dictionary task

```python
# Example story
story1 = {
    "start" : "A Lion lay asleep in the forest, his great head resting on his paws.",
    "middle" : "A timid little Mouse came upon him unexpectedly, and in her fright and haste to get away, ran across the Lion's nose.",
    "end" : "Roused from his nap, the Lion laid his huge paw angrily on the tiny creature to kill her."
}

print(story1) # print entire story

print(type(story1)) # print type

print(story1.keys()) # print only keys

print(story1.values()) # print only values

# print each individual value
print(story1["start"])
print(story1["middle"])
print(story1["end"])

story1["Hero"] = "yourSuperHero"  # add item to dict
print(story1)

```

## Input task

```python
print("What is your name")
name = input()

print("What is your height")
height = input()

print("What is your favourite colour?")
favourite_colour = input()

print(f"Your name is {name}, I am {height} and my favourite colour is {favourite_colour} ")

secret_spirit_animal = "panda"

print("Guess my secret spirit animal")
animal = input()

if animal == secret_spirit_animal:
    print("OMG how did you know?")
else: print("Wrong, try again")

```
