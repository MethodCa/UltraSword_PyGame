class FileManager:
    filename: str

    def __init__(self, filename):
        self.filename = filename

    def read_file_hiscore(self):  # reads text files and returns an array with the text file content (high score table)
        try:
            lines = []
            with open(self.filename, 'r') as file:
                for line in file:
                    words_in_line = line.split()
                    lines.append(words_in_line)
            return lines
        except FileNotFoundError:
            return None

    def read_file(self):
        result = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    result.append(line.strip())  # Strip removes trailing newline characters
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
        except Exception as e:
            print(f"Error reading file: {e}")
        return result

    def write_file(self, score_list):  # writes the high score in the text file
        try:
            with open(self.filename, 'w') as file:
                for item in score_list:
                    file.write(f"{item}\n")
            print(f"Sorted array saved to {self.filename}")
        except Exception as e:
            print(f"Error saving to file: {e}")

    def add_new_score(self, new_score):
        score_list = self.read_file()  # add text file content to the list
        score_list.append(new_score)  # Add the new string to the array

        def get_points(item):  # Define a custom sorting function based on the points
            return int(item.split()[-1])

        sorted_arr = sorted(score_list, key=get_points, reverse=True)[:5]
        self.write_file(sorted_arr)  # Use the custom sorting function to sort the updated array
