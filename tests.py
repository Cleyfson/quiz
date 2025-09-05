import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct

def test_question_starts_with_no_choices():
    question = Question(title="q1")
    assert question.choices == []


def test_add_multiple_choices_increases_length():
    question = Question(title="q1")
    question.add_choice("a", False)
    question.add_choice("b", True)
    assert len(question.choices) == 2


def test_choice_text_is_preserved():
    question = Question(title="q1")
    question.add_choice("answer", True)
    assert question.choices[0].text == "answer"


def test_choice_can_be_correct():
    question = Question(title="q1")
    question.add_choice("correct", True)
    assert question.choices[0].is_correct


def test_choice_can_be_incorrect():
    question = Question(title="q1")
    question.add_choice("wrong", False)
    assert not question.choices[0].is_correct


def test_each_question_has_unique_id():
    q1 = Question(title="q1")
    q2 = Question(title="q2")
    assert q1.id != q2.id


def test_question_accepts_custom_points():
    q = Question(title="q1", points=5)
    assert q.points == 5


def test_question_default_points_is_one():
    q = Question(title="q1")
    assert q.points == 1


def test_add_choice_multiple_times():
    q = Question(title="q1")
    q.add_choice("a", False)
    q.add_choice("b", False)
    q.add_choice("c", True)
    texts = [c.text for c in q.choices]
    assert texts == ["a", "b", "c"]


def test_only_one_correct_choice_among_many():
    q = Question(title="q1")
    q.add_choice("a", False)
    q.add_choice("b", False)
    q.add_choice("c", True)
    corrects = [c for c in q.choices if c.is_correct]
    assert len(corrects) == 1
    assert corrects[0].text == "c"

@pytest.fixture
def question_with_choices():
    q = Question(title="Capital of France?", points=2)
    q.add_choice("Paris", True)
    q.add_choice("London", False)
    q.add_choice("Berlin", False)
    return q

def test_fixture_question_has_three_choices(question_with_choices):
    assert len(question_with_choices.choices) == 3


def test_fixture_question_correct_choice_is_paris(question_with_choices):
    corrects = [c for c in question_with_choices.choices if c.is_correct]
    assert len(corrects) == 1
    assert corrects[0].text == "Paris"