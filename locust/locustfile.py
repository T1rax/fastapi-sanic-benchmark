import random

from locust import FastHttpUser, task


class DataGenerator:
    """Generates data for stress tests."""

    @staticmethod
    def generate_row() -> float:
        """Generates latitude."""
        return random.randint(0, 9)

    @staticmethod
    def generate_column() -> float:
        """Generates latitude."""
        return random.randint(0, 9)

    @staticmethod
    def generate_multiplier() -> float:
        """Generates latitude."""
        return random.uniform(2, 500)


class MyUser(FastHttpUser):
    """Class for API testing.

    launch with `locust` in bash.
    """

    host = "http://0.0.0.0:8000"

    @task
    def get_value(self) -> None:
        """Tests lightning history."""
        row_n = DataGenerator.generate_row()
        column_n = DataGenerator.generate_column()

        resp = self.client.get(
            "/items/{0}/{1}/".format(row_n, column_n),
            name="get item",
        )
        try:
            assert resp.status_code == 200
        except AssertionError:
            print(resp.status_code)

    @task
    def post_value(self) -> None:
        """Tests lightning history."""
        json_body = {
            "row": DataGenerator.generate_row(),
            "column": DataGenerator.generate_column(),
            "multiplier": DataGenerator.generate_multiplier(),
        }

        resp = self.client.post(
            "/items",
            json=json_body,
            name="post item",
        )
        try:
            assert resp.status_code == 200
        except AssertionError:
            print(resp.status_code)
