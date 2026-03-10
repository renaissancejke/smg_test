from app.shortener import generate_short_id, SHORT_ID_LENGTH


def test_generate_short_id_length():
    short_id = generate_short_id()
    assert len(short_id) == SHORT_ID_LENGTH


def test_generate_short_id_is_alphanumeric():
    for _ in range(20):
        short_id = generate_short_id()
        assert short_id.isalnum(), f"Non-alphanumeric short_id generated: {short_id}"


def test_generate_short_id_uniqueness():
    ids = {generate_short_id() for _ in range(50)}
    assert len(ids) == 50
