import typing
import abc


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self.index: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise Exception("Empty data")
        index = self.index
        value = self._data.pop(0)
        self.index += 1
        return (index, value)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if not isinstance(data, (int, float, list)):
            return False
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
        return True

    def ingest(self, data: int | float | list[int | float]) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        if isinstance(data, list):
            for word in data:
                self._data.append(str(word))
        else:
            self._data.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if not isinstance(data, (str, list)):
            return False
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
        return True

    def ingest(self, data: str | list[str]) -> None:
        if not self.validate(data):
            raise Exception("Improper text data")
        if isinstance(data, list):
            for word in data:
                self._data.append(word)
        else:
            self._data.append(data)


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            for k, v in data.items():
                if not isinstance(k, str) or not isinstance(v, str):
                    return False
            return True
        if isinstance(data, list):
            for d in data:
                if not isinstance(d, dict):
                    return False
                for k, v in d.items():
                    if not isinstance(k, str) or not isinstance(v, str):
                        return False
            return True
        return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if not self.validate(data):
            raise Exception("Improper log data")
        if isinstance(data, list):
            for d in data:
                self._data.append(f"{d['log_level']}: {d['log_message']}")
        else:
            self._data.append(f"{data['log_level']}: {data['log_message']}")


def main() -> None:
    print("=== Code Nexus - Data Processor ===")

    print("Testing Numeric Processor...")
    data_num = NumericProcessor()
    print("Trying to validate input '42':", data_num.validate(42))
    print("Trying to validate input 'Hello':", data_num.validate('Hello'))
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        data_num.ingest("foo")
    except Exception as e:
        print("Got exception:", e)
    valid_data_num = [1, 2, 3, 4, 5]
    data_num.ingest(valid_data_num)
    print("Processing data:", valid_data_num)
    print("Extracting 3 values...")
    for _ in range(3):
        i, value = data_num.output()
        print(f"Numeric value {i}: {value}")

    print("")
    print("Testing Text Processor...")
    data_text = TextProcessor()
    print("Trying to validate input '42':", data_text.validate(42))
    valid_data_text = ['Hello', 'Nexus', 'World']
    data_text.ingest(valid_data_text)
    print("Processing data:", valid_data_text)
    print("Extracting 1 value...")
    i, value = data_text.output()
    print(f"Text value {i}: {value}")

    print("")
    print("Testing Log Processor...")
    data_log = LogProcessor()
    print("Trying to validate input 'Hello':", data_log.validate("Hello"))
    valid_data_log = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    data_log.ingest(valid_data_log)
    print("Processing data:", valid_data_log)
    print("Extracting 2 values...")
    for _ in range(2):
        i, value = data_log.output()
        print(f"Log entry {i}: {value}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)