class Airplane:
    def __init__(self, model, engines=2):
        self.model = model
        self.engines = engines

    @classmethod
    def get_redy(cls, model):
        sample_plane = cls(model, 3)
        sample_plane.engine_on(0)
        sample_plane.engine_on(1)
        sample_plane.engine_on(2)

        return sample_plane


airplane = Airplane.get_redy('ABC')

# or without static constructor
airplane = Airplane('ABC', 3)
airplane.engine_on(0)
airplane.engine_on(1)
airplane.engine_on(2)

airplane = Airplane.get_ready('ABC')
