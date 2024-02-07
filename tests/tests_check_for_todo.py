from lib.check_for_todo import *
import pytest

def test_check_for_todo():
    result = check_for_todo('This contains #TODO')
    assert result is True

def test_check_for_todo_no_todo():
    result = check_for_todo('Not here')
    assert result is False