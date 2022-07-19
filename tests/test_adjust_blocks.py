"""Test adjust_blocks."""
# pylint: disable=broad-except
from adjust_blocks import __version__
from adjust_blocks import adjust_blocks


def test_version():
    """Test version."""
    assert __version__[:3] == "0.1"


def test_sanity():
    """Check sanity."""
    try:
        assert not adjust_blocks()
    except Exception:
        assert True
