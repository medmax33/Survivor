class History:

    def __init__(self):
        self.current_state: int = 0
        self.history_array: list = ['']
        self.undo_flag: bool = False

    def remove_history(self):
        if self.undo_flag:
            self.history_array = [self.history_array[self.current_state]]
            self.current_state = 0
            self.undo_flag = False

    def add(self, new_history: str) -> str:
        self.remove_history()
        self.history_array.append(self.history_array[self.current_state] + new_history)
        self.current_state += 1
        return self.history_array[self.current_state]

    def delete(self, n: int) -> str:
        self.remove_history()
        if n > len(self.history_array[self.current_state]):
            self.history_array.append('')
        else:
            self.history_array.append(self.history_array[self.current_state][:-n])
        self.current_state += 1
        return self.history_array[self.current_state]

    def give_value(self, i: int) -> str:
        if i > len(self.history_array[self.current_state]) - 1 or i < 0:
            return ''
        else:
            return self.history_array[self.current_state][i]

    def undo(self) -> str:
        if self.current_state <= 0:
            self.current_state = 0
        else:
            self.current_state -= 1
        self.undo_flag = True
        return self.history_array[self.current_state]

    def redo(self) -> str:
        if self.current_state < len(self.history_array) - 1:
            self.current_state += 1
        return self.history_array[self.current_state]

    def current(self) -> str:
        return self.history_array[self.current_state]


def BastShoe(command: str) -> str:

    try:
        if len(command) > 1:
            c, val = command.split(' ', maxsplit=1)
        else:
            c = command
            val = ''

        if c == '1':
            return new_line.add(val)
        elif c == '2':
            return new_line.delete(int(val))
        elif c == '3':
            return new_line.give_value(int(val))
        elif c == '4':
            return new_line.undo()
        elif c == '5':
            return new_line.redo()
        else:
            return new_line.current()
    except IndexError:
        return new_line.current()
    except ValueError:
        return new_line.current()


new_line = History()
