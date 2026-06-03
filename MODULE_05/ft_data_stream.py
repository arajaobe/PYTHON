
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

class DataStream(DataProcessor):
        def register_processor(self, proc: DataProcessor) -> None:
            pass
