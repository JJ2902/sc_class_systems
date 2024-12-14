import math

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        if title == "" or contents == "":
            raise Exception("Diary entries must have a title or contents")
        self.title = title
        self.contents = contents
        #   Sets the title and contents properties
        self.title = title
        self.contents = contents

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        combineStr = f"{self.title} {self.contents}"
        word_list = combineStr.split()
        
        return len(word_list)

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        if wpm == 0:
            raise Exception("Cannot calculate")
        countedTotal = self.count_words()

        reading_time = countedTotal/wpm
        return math.ceil(reading_time)

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        words_user_can_read = wpm * minutes
        words = self.contents.split()
        chunk_words = words[:words_user_can_read]
        return " ".join(chunk_words)