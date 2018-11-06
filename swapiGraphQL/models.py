from sqlalchemy import Column, Table, Integer, String, ForeignKey
from sqlalchemy.orm import backref, relationship

from swapiGraphQL.database import Base


character_map = Table('character_map',
    Base.metadata,
    Column('film_id', Integer, ForeignKey('film.url_id')),
    Column('people_id', Integer, ForeignKey('people.url_id'))
)

planet_map = Table('planet_map',
    Base.metadata,
    Column('film_id', Integer, ForeignKey('film.url_id')),
    Column('planet_id', Integer, ForeignKey('planet.url_id'))
)

vehicle_map = Table('vehicle_map',
    Base.metadata,
    Column('film_id', Integer, ForeignKey('film.url_id')),
    Column('vehicle_id', Integer, ForeignKey('vehicle.url_id'))
)

starship_map = Table('starship_map',
    Base.metadata,
    Column('film_id', Integer, ForeignKey('film.url_id')),
    Column('starship_id', Integer, ForeignKey('starship.url_id'))
)

species_map = Table('species_map',
    Base.metadata,
    Column('film_id', Integer, ForeignKey('film.url_id')),
    Column('species_id', Integer, ForeignKey('species.url_id'))
)

peep_species_map = Table('peep_species_map',
    Base.metadata,
    Column('people_id', Integer, ForeignKey('people.url_id')),
    Column('species_id', Integer, ForeignKey('species.url_id'))
)

peep_vehicle_map = Table('peep_vehicle_map',
    Base.metadata,
    Column('people_id', Integer, ForeignKey('people.url_id')),
    Column('vehicle_id', Integer, ForeignKey('vehicle.url_id'))
)

peep_starship_map = Table('peep_starship_map',
    Base.metadata,
    Column('people_id', Integer, ForeignKey('people.url_id')),
    Column('starship_id', Integer, ForeignKey('starship.url_id'))
)


class ModelFilm(Base):
    """Film Model"""

    __tablename__ = 'film'

    film_id = Column('film_id', Integer, primary_key=True)
    url_id = Column('url_id', Integer, unique=True)
    title = Column('title', String)
    episode_id = Column('episode_id', Integer)
    opening_crawl = Column('opening_crawl', String)
    director = Column('director', String)
    producer = Column('producer', String)
    release_date = Column('release_date', String)
    created = Column('created', String)
    edited = Column('edited', String)

    character_list = relationship('ModelPeople', secondary=character_map,
                                  backref=backref('film_list', lazy='dynamic'))
    planet_list = relationship('ModelPlanet', secondary=planet_map,
                               backref=backref('film_list', lazy='dynamic'))
    vehicle_list = relationship('ModelVehicle', secondary=vehicle_map,
                                backref=backref('film_list', lazy='dynamic'))
    starship_list = relationship('ModelStarship', secondary=starship_map,
                                 backref=backref('film_list', lazy='dynamic'))
    species_list = relationship('ModelSpecies', secondary=species_map,
                                backref=backref('film_list', lazy='dynamic'))


class ModelPeople(Base):
    """People Model"""

    __tablename__ = 'people'

    people_id = Column('people_id', Integer, primary_key=True)
    url_id = Column('url_id', Integer, unique=True)
    name = Column('name', String)
    height = Column('height', String)
    mass = Column('mass', String)
    hair_color = Column('hair_color', String)
    skin_color = Column('skin_color', String)
    eye_color = Column('eye_color', String)
    birth_year = Column('birth_year', String)
    gender = Column('gender', String)
    homeworld = Column('homeworld', Integer, ForeignKey('planet.url_id'))
    created = Column('created', String)
    edited = Column('edited', String)

    species_list = relationship('ModelSpecies', secondary=peep_species_map,
                                backref=backref('people_list', lazy='dynamic'))
    vehicle_list = relationship('ModelVehicle', secondary=peep_vehicle_map,
                                backref=backref('pilot_list', lazy='dynamic'))
    starship_list = relationship('ModelStarship', secondary=peep_starship_map,
                                 backref=backref('pilot_list', lazy='dynamic'))


class ModelSpecies(Base):
    """Species Model"""

    __tablename__ = 'species'

    species_id = Column('species_id', Integer, primary_key=True)
    url_id = Column('url_id', Integer, unique=True)
    name = Column('name', String)
    classification = Column('classification', String)
    designation = Column('designation', String)
    average_height = Column('average_height', String)
    skin_colors = Column('skin_colors', String)
    hair_colors = Column('hair_colors', String)
    eye_colors = Column('eye_colors', String)
    average_lifespan = Column('average_lifespan', String)
    homeworld = Column('homeworld', Integer, ForeignKey('planet.url_id'))
    language = Column('language', String)
    created = Column('created', String)
    edited = Column('edited', String)


class ModelPlanet(Base):
    """Planet Model"""

    __tablename__ = 'planet'

    planet_id = Column('planet_id', Integer, primary_key=True)
    url_id = Column('url_id', Integer, unique=True)
    name = Column('name', String)
    rotation_period = Column('rotation_period', String)
    orbital_period = Column('orbital_period', String)
    diameter = Column('diameter', String)
    climate = Column('climate', String)
    gravity = Column('gravity', String)
    terrain = Column('terrain', String)
    surface_water = Column('surface_water', String)
    population = Column('population', String)
    created = Column('created', String)
    edited = Column('edited', String)

    resident_list = relationship(ModelPeople, backref='planet')
    species_list = relationship(ModelSpecies, backref='planet')


class ModelTransport:
    """Transport Model"""

    name = Column('name', String)
    model = Column('model', String)
    manufacturer = Column('manufacturer', String)
    cost_in_credits = Column('cost_in_credits', String)
    length = Column('length', String)
    max_atmosphering_speed = Column('max_atmosphering_speed', String)
    crew = Column('crew', String)
    passengers = Column('passengers', String)
    cargo_capacity = Column('cargo_capacity', String)
    consumables = Column('consumables', String)
    created = Column('created', String)
    edited = Column('edited', String)


class ModelVehicle(ModelTransport, Base):
    """Vehicle Model"""

    __tablename__ = 'vehicle'

    vehicle_id = Column('vehicle_id', Integer, primary_key=True)
    url_id = Column('url_id', Integer, unique=True)
    vehicle_class = Column('vehicle_class', String)


class ModelStarship(ModelTransport, Base):
    """Starship Model"""

    __tablename__ = 'starship'

    starship_id = Column('starship_id', Integer, primary_key=True)
    url_id = Column('url_id', Integer, unique=True)
    hyperdrive_rating = Column('hyperdrive_rating', String)
    mglt = Column('mglt', String)
    starship_class = Column('starship_class', String)
