from scripts.chp2.video2.mapmaker_start import Point

def test_make_one_point():
    p1 = Point("Dakar", 14.7167, 17.4677)
    assert p1.get_lat_long == (14.7167, 17.4677)

def test_invalid_point_gen():
    with pytest.raises(ValueError) as exp:
        Point("Buenos Aires", 12.11386, -555.08268)
    assert str(exp.value) == "Invalid latitude, longitude"