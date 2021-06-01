# rectangle_geo_test.py

def rectangle_area(x1, x2):
    return x1 * x2

def rectangle_perimeter(x1, x2):
    return 2 * (x1 + x2)

def test_rectangle_area():
    x1 = 3 # Arrange
    x2 = 4 # Arrange
    expected_area = 12 # Arrange
    calculated_area = rectangle_area(x1, x2) # Act
    assert expected_area == calculated_area # Assert

def test_rectangle_perimeter():
    assert rectangle_perimeter(2, 4) == 12