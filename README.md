# Learn Python from Thinking Types

This repository is designed to provide a quick review of Python basics. The accompanying YouTube channel introduces a new teaching structure that follows a data type-centric approach.

Learning resources [Basic Python learning](https://www.youtube.com/watch?v=jH85McHenvw).

PS: After python 3.6, the type hints are not required. They are just a way to make the code more readable. The type hints are not enforced by the python interpreter. So, if you are using python 3.6 or above, you can skip the type hints. -- I know, I know, I am a bit late to the party.¯\_(ツ)\_/¯

# Projects in part-09 and part-10

I built two projects and overthought they look simple, they are densely packed with all above concepts.

1. Cash Register
2. SuperHero Game

# Project2 - Packages - Thinking In Layers

The whole idea behind creating packages is to divide our application into logical sub-components.
These sub-components can be grouped by their type of functionality.

## Layers for our game application

| Sr No | Layer Name     | Particular                   | Visibility | Role      |
| ----- | -------------- | ---------------------------- | ---------- | --------- |
| 1     | Data Layer     | Package `models` & `schemas` | Private    | Internal  |
| 2     | Business Logic | `impl.py`                    | Private    | Internal  |
| 3     | API            | Package `game`               | Public     | Interface |
| 4     | Client         | `main.py`                    |            | Consumer  |

This repo includes all what I want to practice and repeat. Some details check this excellent [tutorial repo](https://github.com/octallium/modern-python-101).👍
