from pyls import format_size

def testformat_size():
    # Assert and validate
    assert format_size(0) == "0.0 B"                    # Edge case: zero size
    assert format_size(1023) == "1023.0 B"              # Edge case: just below 1 KB
    assert format_size(1024) == "1.0 KB"                # Edge case: exactly 1 KB
    assert format_size(1025) == "1.0 KB"                # Just above 1 KB
    assert format_size(2048) == "2.0 KB"                # Exactly 2 KB
    assert format_size(2048 * 1024) == "2.0 MB"         # Exactly 2 MB
    assert format_size(2048 * 1024 * 1024) == "2.0 GB"  # Exactly 2 GB


def testformat_size_two():
    # Test with negative size (should raise ValueError)
    try:
        format_size(-1024)
    except ValueError:
        pass            # Expected behavior
    else:
        assert False, "Expected ValueError for negative size"


def testformat_size_three():
        # Test with large size
    assert format_size(2 ** 60) == "1024.0 TB"  # 1 TB