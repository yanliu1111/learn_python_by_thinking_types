class Life:
    hero_life = 0
    villain_life = 0

    @staticmethod # static method is a method that does not use the instance, we can call static method from the class itself
    # other example, if have common functionality such as datetime.now() or datetime.today(), we dont need to create new instance
    # static method is does not take a self argument because it works directly with the class and not on the instance
    def inc_hero_life(life: int) -> None:
        Life.hero_life += life
    @staticmethod
    def dec_hero_life(life: int) -> None:
        Life.hero_life -= life
    @staticmethod
    def inc_villain_life(life: int) -> None:
        Life.villain_life += life

    @staticmethod
    def dec_villain_life(life: int) -> None:
        Life.villain_life -= life