def BastShoe(command: str) -> str:

    try:
        if len(command) > 1:
            c, val = command.split(' ', maxsplit=1)
        else:
            c = command
            val = ''

        if c == '1':
            return add(val, current_state)
        # elif c == '2':
        #     return new_line.delete(int(val))
        # elif c == '3':
        #     return new_line.give_value(int(val))
        # elif c == '4':
        #     return new_line.undo()
        # elif c == '5':
        #     return new_line.redo()
        # else:
        #     return new_line.current()
    except IndexError:
        return current_string
    except ValueError:
        return current_string


def add(new_history: str, current_state: int) -> str:
    # remove_history()
    history.append(history[current_state] + new_history)
    current_state += 1
    return history[current_state]


# def delete(self, n: int) -> str:
#     self.remove_history()
#     if n > len(self.history_array[self.current_state]):
#         self.history_array.append('')
#     else:
#         self.history_array.append(self.history_array[self.current_state][:-n])
#     self.current_state += 1
#     return self.history_array[self.current_state]


# def remove_history():
#     if undo_flag:
#         history = [history[current_state]]
#         current_state = 0
#         undo_flag = False


# def give_value(self, i: int) -> str:
#     if i > len(self.history_array[self.current_state]) - 1 or i < 0:
#         return ''
#     else:
#         return self.history_array[self.current_state][i]
#
#
# def undo(self) -> str:
#     if self.current_state <= 0:
#         self.current_state = 0
#     else:
#         self.current_state -= 1
#     self.undo_flag = True
#     return self.history_array[self.current_state]
#
#
# def redo(self) -> str:
#     if self.current_state < len(self.history_array) - 1:
#         self.current_state += 1
#     return self.history_array[self.current_state]
#
#
# def current(self) -> str:
#     return self.history_array[self.current_state]

history: list = []
current_state: int = 0
current_string: str = ''
undo_flag: bool = False

print(BastShoe('1 lkasjdlak'))