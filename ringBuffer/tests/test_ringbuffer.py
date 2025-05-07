from ringbuffer import RingBuffer

def test_initialization():
    buffer = RingBuffer(3)
    assert buffer.size == 3
    assert buffer.buffer == [None, None, None]

def test_add_element():
    buffer = RingBuffer(3)
    buffer.add(17)
    assert buffer.buffer == [17, None, None]

def test_add_two_elements():
    buffer = RingBuffer(5)
    buffer.add(17)
    buffer.add(15)
    assert buffer.buffer == [17, 15, None, None, None]

def test_overwrite_elements():
    buffer = RingBuffer(3)
    buffer.add(1)
    buffer.add(2)
    buffer.add(3)
    buffer.add(4)
    assert buffer.buffer == [4, 2, 3]

def test_get_elements():
    buffer = RingBuffer(3)
    buffer.add(2)
    buffer.add(3)
    buffer.add(4)
    assert buffer.get() == [2, 3, 4]

def test_empty_slots():
    buffer = RingBuffer(3)
    buffer.add(2)
    buffer.add(3)
    assert buffer.get() == [2, 3, None]
