from game.schemas.villain import Villain

class VillainModel:
    def __init__(self) -> None:
        self.all: list[Villain] = self._get_all_villains()

    # add a method to display/print all the villains
    def __str__(self) -> str:
        name: list[str] = []
        for villain in self.all:
            name.append(villain.name)
        return f"Villains: {name}"
    
    def _get_all_villains(self) -> list[Villain]:
        thanos = Villain(name="Thanos", attack_power=400, life=1500)
        redskull = Villain(name="Redskull", attack_power=300, life=800)
        proxima = Villain(name="Proxima", attack_power=320, life=800)

        villains: list[Villain] = [thanos, redskull, proxima]
        return villains

    def get_villain(self, index: int) -> Villain | None:
        """Returns a villain based on the index"""
        if index < len(self.all):
            return self.all[index]
        else:            
            return None
