from lib.diary import *
from lib.diary_entry import *

def test_diary_initialises_correctly_one():
    diary_one = Diary()

def test_display_diary_entries_correctly():
    diary_one = Diary()
    diary_entry = DiaryEntry("title one", "content one")
    diary_entry_two = DiaryEntry("title two", "content two") 

    result = diary_one.add(diary_entry)   
    diary_one.add(diary_entry_two) 
    assert result == "Entry added to diary"
    assert diary_one.all() == ["title one", "title two"] 

def test_count_words_counts_all_entries():
    diary_one = Diary()
    diary_entry = DiaryEntry("title one", "content one")
    diary_entry_two = DiaryEntry("title two", "content two")

    # Add entries to the diary
    diary_one.add(diary_entry)
    diary_one.add(diary_entry_two)


    # Calculate word count by calling count_words on each DiaryEntry
    result = diary_entry.count_words() + diary_entry_two.count_words()

    # Call count_words on the Diary instance
    total_count = diary_one.count_words()

    # Assert that the sum of count_words results from DiaryEntry instances is equal to count_words result from Diary instance
    assert result == total_count
    
    # result = diary_entry.count_words() + diary_entry_two.count_words()
    # assert result == 8

def test_diary_reading_time_returns_estimate_reading_time():
    diary_one = Diary()
    diary_entry = DiaryEntry("title one", "content one")
    diary_entry_two = DiaryEntry("title two", "content two")

    diary_one.add(diary_entry)
    diary_one.add(diary_entry_two)

    result = diary_entry.reading_time(2) + diary_entry_two.reading_time(2)

    total_wpm = diary_one.reading_time(2)

    assert result == total_wpm

def test_diary_find_best_reading_time_returns_estimate_reading_time():
    diary_one = Diary()
    diary_entry = DiaryEntry("Title one", "content one")
    diary_entry_two = DiaryEntry("Title two", "content two is longer to read")

    diary_one.add(diary_entry)
    diary_one.add(diary_entry_two)

    result = diary_one.find_best_entry_for_reading_time(2,4)

    assert result == "Title two is the best entry for reading time."