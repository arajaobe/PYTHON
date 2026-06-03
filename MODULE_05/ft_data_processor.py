
import typing
import abc

class DataProcessor(abc.ABC):
    def __init__(self):
        self.data: list[str] = []
        self.index: int = 0

    @abc.abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str] :
        index = self.index
        value = self.data.pop(0)
        self.index += 1
        return (index, value)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if not isinstance(data, int | float | list):
            return False
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
        return True

    def ingest(self, data: int | float | list) -> None:
        if not self.validate(data):
            raise Exception("Improper numeric data")
        else:
            if isinstance(data, list):
                for word in data:
                    self.data.append(str(word))
            else:
                self.data.append(str(data))


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if not isinstance(data, str | list):
            return False
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
        return True

    def ingest(self, data: str| list) -> None:
        if not self.validate(data):
            raise ("Improper text data")
        else:
            if isinstance(data, list):
                for word in data:
                    self.data.append(str(word))
            else:
                self.data.append(str(data))


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            for k, v in data.items():
                if not isinstance(k,str) or not isinstance(v, str):
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


    def ingest(self, data: dict | list) -> None:
        if not self.validate(data):
            raise ("Improper log data")
        else:
            if isinstance(data, list):
                for d in data:
                    self.data.append(f"{d['log_level']}: {d['log_message']}")
            else:
                self.data.append((f"{data['log_level']}: {data['log_message']}"))


def main():
    print("=== Code Nexus - Data Processor ===\n")

    print("Testing Numeric Processor...")
    data_num = NumericProcessor()
    print("Trying to validate input '42':", data_num.validate(42))
    print("Trying to validate input 'Hello':", data_num.validate('Hello'))
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        data_num.ingest("foo")
    except Exception as e:
        print("Got exception:", e)
    valid_data_num= [1, 2, 3, 4, 5]
    try:
        data_num.ingest(valid_data_num)
    except Exception as e:
        print("Got exception:", e)
    print("Processing data:", valid_data_num)
    print("Extracting 3 values...")
    for _ in range(3):
        i, value = data_num.output()
        print(f"Numeric value {i} {value}")

    print("\n")
    print("Testing Text Processor...")
    data_text = TextProcessor()
    print("Trying to validate input '42':", data_text.validate(42))
    valid_data_text = ['Hello', 'Nexus', 'World']
    try:
        data_text.ingest(valid_data_text)
    except Exception as e:
        print("Got exception:", e)
    print("Processing data:", valid_data_text)
    print("Extracting 1 value...")
    for _ in range(1):
        i, value = data_text.output()
        print(f"Text value {i} {value}")

    print("\n")
    print("Testing Log Processor...")
    data_log = LogProcessor()
    print("Trying to validate input 'Hello':", data_log.validate("bbb"))
    valid_data_log =  [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                    {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    try:
        data_log.ingest(valid_data_log)
    except Exception as e:
        print("Got exception:", e)
    print("Processing data:", valid_data_log)
    print("Extracting 2 values...")
    for _ in range(2):
        i, value = data_log.output()
        print(f"Log entry {i} : {value}")


if __name__ == "__main__":
    main()