from tag_manipulator import TagManipulator


def test_split_empty_string_result_empty_array():
    # arrange
    stringToSplit = ""
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult


def test_split_comma_empty_string_result_empty_array():
    # arrange
    stringToSplit = ","
    expResult = []
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit)

    # assert
    assert result == expResult


def test_split_one_string_result_array_of_one():
    # arrange
    stringToSplit = "java"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult


def test_split_one_string_with_leading_comma_result_array_of_one_without_comma():
    # arrange
    stringToSplit = ",java"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult


def test_split_one_string_with_comma_separated_words_result_array_of_two_words():
    # arrange
    stringToSplit = "java,python"
    regex = ","
    expResult = ["java", "python"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult


def test_split_one_string_with_leading_space_result_array_of_one_word_without_space():
    # arrange
    stringToSplit = " java"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult


def test_split_one_string_with_trailing_comma_result_array_of_one_without_comma():
    # arrange
    stringToSplit = "java,"
    regex = ","
    expResult = ["java"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult


def test_split_one_string_comma_separated_words_or_sentences_with_whitespace_result_array_of_two_sentences_with_whitespace_seperating_it():
    # arrange
    stringToSplit = "java byte code, python"
    regex = ","
    expResult = ["java byte code", "python"]
    result = None
    cut = TagManipulator()

    # act
    result = cut.parse_string(stringToSplit, regex)

    # assert
    assert result == expResult
