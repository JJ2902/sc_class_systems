class Diary:
    def __init__(self):
        self.entries = []

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self.entries.append(entry)
        return "Entry added to diary"

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return [entry.title for entry in self.entries]

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        total_words = 0

        for entry in self.entries:
            total_words += entry.count_words()
        
        return total_words

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        total_wpm = 0

        for entry in self.entries:
            total_wpm += entry.reading_time(wpm)

        return total_wpm

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        closest_reading_time = None
        closest_time_difference = float('inf')

        for entry in self.entries:
            words = len(entry.contents.split())
            reading_time = words / wpm  

            if reading_time > minutes:
                continue

            time_difference = abs(reading_time - minutes)
            if time_difference < closest_time_difference:
                closest_entry = entry
                closest_time_difference = time_difference

        return f"{closest_entry.title} is the best entry for reading time."
                
                
                
        # return f"{entry.title} is the best entry for reading time."
