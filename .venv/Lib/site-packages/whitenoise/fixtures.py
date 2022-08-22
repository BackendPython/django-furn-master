
class Fixture:
    '''
    Fixture takes the name of a model to act on,
    a list of dependancies, a number of items,
    and a dict of fields and generators
    '''

    def __init__(self, dependencies, model, quantity, fields):
        self.dependencies = dependencies
        self.model = model
        self.quantity = quantity
        self.fields = fields

class CircularDependancyException(Exception):
    pass

class DependencyResolver:
    '''
    Resolves dependencies, obviously
    '''
    def __init__(self, fixtures):
        self.fixtures = fixtures

    def recurse_resolve(self, node, resolved, unresolved):
        if node not in resolved:
            unresolved.append(node)
            for edge in node.dependencies:
                if edge in unresolved:
                    raise CircularDependancyException("Circular dependancy detected %s" % edge)
                self.recurse_resolve(edge, resolved, unresolved)
            unresolved.remove(node)
            resolved.append(node)

    def get_ordered_set(self):
        resolved = []
        unresolved = []
        for fixture in self.fixtures:
            self.recurse_resolve(fixture, resolved, unresolved)
        return resolved


class FixtureRunner:
    '''
    Takes a list of Fixtures and runs them on the specified connection
    '''

    def __init__(self, fixtures):

        self.fixtures = DependencyResolver(fixtures).get_ordered_set()
        if type(self) == FixtureRunner:
            # Disallow creation of the base class
            raise NotImplementedError("FixtureRunner MUST be subclassed")

    def run(self):
        for fixture in self.fixtures:
            self.apply_fixture(fixture)

    def apply_fixture(self, fixture):
        raise NotImplementedError()

class SQLAlchemyFixtureRunner(FixtureRunner):

    def __init__(self, session, fixtures):
        super().__init__(fixtures)
        self.session = session

    def apply_fixture(self, fixture):
        for _ in range(fixture.quantity):
            model_instance = fixture.model()
            for field, generator in fixture.fields.items():
                generator.session = self.session
                setattr(model_instance, field, generator.generate())
            self.session.add(model_instance)
            self.session.commit()

class DjangoFixtureRunner(FixtureRunner):
    def apply_fixture(self, fixture):
        for _ in range(fixture.quantity):
            model_instance = fixture.model()
            for field, (generator, options) in fixture.fields.items():
                setattr(model_instance, field, generator.generate())
            model_instance.save()
