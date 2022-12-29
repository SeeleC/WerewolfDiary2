from functions import read_file


class Location:
    def __init__(self, value):
        self.value = value
        location_data = read_file(f'resources\\places\\{value}.json')
        self.help = location_data['help']

    def get_help(self):
        result = {}
        for entry in self.help:
            args = '['
            for i in entry['args']:
                entry_string += i + '/'
            entry_string = entry_string[:-1] + ']'
            result.append(entry_string)
        return result
