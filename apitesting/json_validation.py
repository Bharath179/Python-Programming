import re


class JSONValidator:
    @staticmethod
    def check_required_fields(item, required_fields):
        assert all(field in item for field in required_fields), f"Missing one of the required fields: {required_fields}"

    @staticmethod
    def check_field_types(item, expected_types):
        for key, expected_type in expected_types.items():
            assert isinstance(item.get(key), expected_type), f"{key} should be of type {expected_type.__name__}"

    @staticmethod
    def check_non_empty_strings(item, keys):
        for key in keys:
            value = item.get(key, "").strip()
            assert value != "", f"{key} should not be an empty string"

    @staticmethod
    def check_value_range(value, min_value=None, max_value=None):
        if min_value is not None:
            assert value >= min_value, f"Value {value} is less than minimum {min_value}"
        if max_value is not None:
            assert value <= max_value, f"Value {value} is more than maximum {max_value}"

    @staticmethod
    def check_unique_ids(items, id_field="id"):
        ids = [item[id_field] for item in items]
        assert len(ids) == len(set(ids)), f"Duplicate {id_field} values found"

    @staticmethod
    def check_total_sum(items, field):
        total = sum(item.get(field, 0.0) for item in items)
        assert total > 0, f"Total sum of '{field}' should be greater than 0"
        return total
