import pytest
from src.calculator import add

def test_add():
    assert add(2, 3) == 5

# 失敗するテスト（Copilot に修正を依頼したい対象）
def test_multiply():
    from src.calculator import multiply
    assert multiply(2, 4) == 8
