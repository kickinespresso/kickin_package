import pytest
from autos.car import Car


def test_car_driving():
    car = Car(name = "camry", fuel = 5)
    assert type(car.current_fuel()) is int
    assert car.drive() is True


def test_car_low_fuel():
    car = Car(name = "camry", fuel = 2)
    assert type(car.current_fuel()) is int
    assert car.drive() is True
    assert car.drive() is True
    assert car.drive() is False


@pytest.fixture()
def resource():
    print("setup")
    yield Car(name = "camry", fuel = 2)
    print("teardown")


class TestResource(object):
    def test_that_depends_on_resource(self, resource):
        print("testing {}".format(resource))

    def test_fuel_consumption(self, resource):
        assert resource.current_fuel() is 2
        fuel_remaining = resource.current_fuel()
        resource.drive()
        assert resource.current_fuel() is fuel_remaining - 1
