
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

    def output(self) -> tuple[int, str] :
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

class DataStream:

    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []
        self._totals: dict[str, int] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)
        self._totals[proc.__class__.__name__] = 0

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            handled = False
            for proc in self._processors:
                if proc.validate(element):
                    proc.ingest(element)
                    name = proc.__class__.__name__
                    if isinstance(element, list):
                        self._totals[name] += len(element)
                    else:
                        self._totals[name] += 1
                    handled = True
                    break
            if not handled:
                print(f"DataStream error - Can't process element in stream: {element}")

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            name = proc.__class__.__name__
            total = self._totals[name]
            remaining = len(proc._data)
            print(f"{name}: total {total} items processed, remaining {remaining} on processor")


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")
    print("")
    stream = DataStream()
    stream.print_processors_stats()
    print("")
    numeric = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [{"log_level": "WARNING", "log_message": "Telnet access! Use ssh instead"},
         {"log_level": "INFO", "log_message": "User wil is connected"}],
        42,
        ["Hi", "five"]
    ]

    print("Registering Numeric Processor")
    stream.register_processor(numeric)
    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()
    print("")
    print("Registering other data processors")
    stream.register_processor(text)
    stream.register_processor(log)
    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()
    print("")
    print("Consume some elements from the data processors: Numeric 3, Text 2, Log 1")
    for _ in range(3):
        numeric.output()
    for _ in range(2):
        text.output()
    for _ in range(1):
        log.output()
    stream.print_processors_stats()

