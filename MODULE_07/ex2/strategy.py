
import abc
from ex0.creature import Creature
from ex1.capability import TransformCapability
from ex1.capability import HealCapability


class BattleStrategy(abc.ABC):

    @abc.abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    @abc.abstractmethod
    def act(self, creature: Creature) -> None:
        pass


class InvalidStrategyError(Exception):
    def __init__(self, creature_name: str, strategy_name: str) -> None:
        super().__init__(
            f"Invalid Creature '{creature_name}' "
            f"for this {strategy_name} strategy"
        )


class NormalStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return True

    def act(self, creature: Creature) -> None:
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(creature.name, "agressive")
        assert isinstance(creature, TransformCapability)
        print(creature.transform())
        print(creature.attack())
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(creature.name, "defensive")
        print(creature.attack())
        assert isinstance(creature, HealCapability)
        print(creature.heal())

