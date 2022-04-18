import pytest
from linked_list.linked_list import linked_list, Node



# Test empty linked list
def test_is_empty_ll():
    ll = linked_list()
    expected = None
    actual = ll.head
    assert expected == actual

# Test insert value into linked list
def test_insert_in_ll():
    ll = linked_list()
    ll.insert(Node("Python"))
    expected = f"Python -->{None}"
    actual = ll.__str__()
    assert expected == actual

#Test if the head has the first node value in the linked list 
def test_head_is_first_node(ll):
    expected = "Python"
    actual = ll.head.value
    assert expected == actual


# Test inserting 2 values
def test_inserted_2_values():
    ll = linked_list()
    ll.insert(Node(1))
    ll.insert(Node(2))
    expected = f"2 -->1 -->{None}"
    actual = ll.__str__()
    assert expected == actual

# Test add to an existing linked list
def test_add_to_existing_ll(ll):
    expected = f"Python -->1.33 -->5 -->True -->{None}"
    ll.append(Node(True))
    actual = ll.__str__()
    assert expected == actual

# Test does a value exist in the linked list or not
def test_value_existed_in_ll(ll):
    expected = True
    actual = ll.includes(1.33)
    assert expected == actual

def test_value_is_not_existed_in_ll(ll):
    expected = False
    actual = ll.includes(5.1)
    assert expected == actual

# Test inserting 3 values
def test_return_all_inserted_values(ll):
    expected = f"Python -->1.33 -->5 -->{None}"
    actual = ll.__str__()
    assert expected == actual


@pytest.fixture
def ll():
    ll = linked_list()
    ll.insert(Node(5))
    ll.insert(Node(1.33))
    ll.insert(Node("Python"))
    return ll