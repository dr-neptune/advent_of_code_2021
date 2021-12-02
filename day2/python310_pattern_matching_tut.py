# https://www.python.org/dev/peps/pep-0636/
# Python 3.10 introduced structural pattern matching. Since day 2 is just pattern matching, this seemed like a good time to upgrade

# matching sequences
command = input("What are you doing next? ")

# matching multiple patterns
match command.split():
    case [action]:
        # interpret single verb action
        pass
    case [action, obj]:
        # interpresent action, obj
        pass

# matching specific values
match command.split():
    case ['quit']:
        print('Goodbye!')
        quit_game()
    case ['look']:
        current_room.describe()
    case ['get', obj]:
        character.get(obj, current_room)
    case['go', direction]:
        current_room = current_room.neighbor(direction)

# matching multiple values
match command.split():
    case ['drop', *objects]:
        # allows a character to drop a list of objects
        for obj in objects:
            character.drop(obj, current_room)

# adding a wildcard
match command.split():
    case['quit']:
        pass
    case['go', direction]:
        pass
    # other cases
    case _:
        print(f"Sorry, I couldn't understand {command!r}")

# or patterns
match command.split():
    # other cases
    case ['north'] | ['go', 'north']:
        current_room = current_room.neighbor('north')
    case ['get', obj] | ['pick', 'up', obj] | ['pick', obj, 'up']:
        # code for picking up the given object
        pass

# capturing matched sub-patterns
match command.split():
    case ['go', ('north' | 'south' | 'east' | 'west') as direction]:
        current_room = current_room.neighbor(direction)

# adding conditions to patterns
match command.split():
    case ['go', direction] if direction in current_room.exits:
        current_room = current_room.neighbor(direction)
    case ['go', _]:
        print("Sorry, you can't go that way")

# adding a UI: matching objects
match event.get():
    case Click(position=(x, y)):
        handle_click_at(x, y)
    case KeyPress(key_name='Q') | Quit():
        game.quit()
    case KeyPress(key_name="up arrow"):
        game.go_north()
    # others
    case KeyPress():
        # ignore other keystrokes
        pass
    case other_event:
        raise ValueError(f"Unrecognized event: {other_event}")

# matching positional arguments
from dataclasses import dataclass

@dataclass
class Click:
    position: tuple
    button: Button

match event.get():
    case Click((x, y)):
        handle_click_at(x, y)

# matching against constants and enums
match event.get():
    case Click((x, y), button=Button.LEFT):  # this is a left click
        handle_click_at(x, y)
    case Click():
        pass  # ignore other clicks

# going to the cloud: Mappings
for action in actions:
    match action:
        case {'text': message, 'color': c}:
            ui.set_text_color(c)
            ui.display(message)
        case {'sleep': duration}:
            ui.wait(duration)
        case {'sound': url, 'format': 'ogg'}:
            ui.play(url)
        case {'sound': _, 'format': _}:
            warning('Unsupported audio format')

# Quick Intro

# simplest form
def http_error(status):
    match status:
        case 400:
            return 'bad request'
        case 404:
            return 'not found'
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

# combining several literals
match status:
    case 401 | 403 | 404:
        return 'Not allowed'

# unpacking assignments
point = (0, 0)

match point:
    case (0, 0):
        print('origin')
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError('thats not the point')

@dataclass
class Point:
    x: int
    y: int

point = Point(0, 12)

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print('origin')
        case Point(x=0, y=y):
            print(f"y = {y}")
        case Point(x=x, y=0):
            print(f"x = {x}")
        case Point():
            print('somewhere else')
        case _:
            print('not a point')

where_is(point)

# nested patterns
point = [Point(0, 0), Point(0, 2)]
point = Point(2, 2)

match point:
    case []:
        print('no points')
    case [Point(0, 0)]:
        print('the origin')
    case [Point(x, y)]:
        print(f"Single point ({x}, {y})")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    # guard
    case Point(x, y) if x == y:
        print(f"Y=X at {x}")
    case _:
        print("Something else")
