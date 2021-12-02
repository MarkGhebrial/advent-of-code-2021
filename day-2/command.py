import re

class Command:
    def __init__ (self, textFromInput: str):
        pattern = re.compile(r"((forward)|(down)|(up)) ([0-9]+)")
        match = pattern.findall(textFromInput)[0]

        direction = match[0]
        distance = int(match[4])

        self.forwardDistance = 0
        self.verticalDistance = 0
        if direction == "forward":
            self.forwardDistance = distance
        else:
            if direction == "down":
                self.verticalDistance = distance
            elif direction == "up":
                self.verticalDistance = -distance

    def __str__ (self):
        return("Vertical distance: " + str(self.verticalDistance) + "; Forward distance: " + str(self.forwardDistance))