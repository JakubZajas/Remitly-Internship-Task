import json
import re

PATTERN = r"[\w+=,.@-]+"


class JsonChecker:

    def check_policy_resource(self, input_file):
        """ Method returns False when the Resource field in JSON file contains a single asterisk  """

        try:
            with open(input_file, "r") as file:
                data = json.load(file)

        except FileNotFoundError:
            raise FileNotFoundError(f"File path not found: {input_file}")
        except json.JSONDecodeError:
            raise ValueError(f"File contains invalid value format: {input_file}")

        if not isinstance(data, dict):
            raise ValueError(f"Invalid Policy format in: {input_file}")
        if "PolicyDocument" not in data or not isinstance(data["PolicyDocument"], dict):
            raise ValueError(f"Invalid 'PolicyDocument' format in: {input_file}")
        if "PolicyName" not in data or not isinstance(data["PolicyName"], str):
            raise ValueError(f"Invalid 'PolicyName' format in: {input_file}")
        if len(data["PolicyName"]) < 1 or len(data["PolicyName"]) > 128:
            raise ValueError(f"Invalid 'PolicyName' format in: {input_file}")
        if not bool(re.findall(PATTERN, data["PolicyName"])):
            raise ValueError(f"Invalid 'PolicyName' format in: {input_file}")
        if "Statement" not in data["PolicyDocument"]:
            raise ValueError(f"Missing 'Statement' in 'Policy Document' in: {input_file}")
        if "Resource" not in data["PolicyDocument"]["Statement"][0]:
            raise ValueError(f"Missing 'Resource' in 'Statement' in 'Policy Document' in: {input_file}")

        for field in data["PolicyDocument"]["Statement"]:
            if field["Resource"] == "*":
                return False
        return True
