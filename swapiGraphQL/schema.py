import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from swapiGraphQL.database import db_session
from swapiGraphQL.models import (
    ModelFilm, ModelPeople, ModelPlanet,
    ModelSpecies, ModelVehicle, ModelStarship
)


class FilmObject(SQLAlchemyObjectType):
    class Meta:
        model = ModelFilm
        interfaces = (graphene.relay.Node, )


class PeopleObject(SQLAlchemyObjectType):
    class Meta:
        model = ModelPeople
        interfaces = (graphene.relay.Node, )


class PlanetObject(SQLAlchemyObjectType):
    class Meta:
        model = ModelPlanet
        interfaces = (graphene.relay.Node, )


class SpeciesObject(SQLAlchemyObjectType):
    class Meta:
        model = ModelSpecies
        interfaces = (graphene.relay.Node, )


class VehicleObject(SQLAlchemyObjectType):
    class Meta:
        model = ModelVehicle
        interfaces = (graphene.relay.Node, )


class StarshipObject(SQLAlchemyObjectType):
    class Meta:
        model = ModelStarship
        interfaces = (graphene.relay.Node, )


class Query(graphene.ObjectType):
    node = graphene.relay.Node.Field()
    film = graphene.Field(FilmObject, url_id=graphene.Int())
    film_title = graphene.List(FilmObject, title=graphene.String())
    people = graphene.Field(PeopleObject, url_id=graphene.Int())
    people_name = graphene.List(PeopleObject, name=graphene.String())
    planet = graphene.Field(PlanetObject, url_id=graphene.Int())
    planet_name = graphene.List(PlanetObject, name=graphene.String())
    species = graphene.Field(SpeciesObject, url_id=graphene.Int())
    species_name = graphene.List(SpeciesObject, name=graphene.String())
    vehicle = graphene.Field(VehicleObject, url_id=graphene.Int())
    vehicle_name = graphene.List(VehicleObject, name=graphene.String())
    starship = graphene.Field(StarshipObject, url_id=graphene.Int())
    starship_name = graphene.List(StarshipObject, name=graphene.String())
    all_films = SQLAlchemyConnectionField(FilmObject)
    all_people = SQLAlchemyConnectionField(PeopleObject)
    all_planet = SQLAlchemyConnectionField(PlanetObject)
    all_species = SQLAlchemyConnectionField(SpeciesObject)
    all_vehicles = SQLAlchemyConnectionField(VehicleObject)
    all_starships = SQLAlchemyConnectionField(StarshipObject)

    def resolve_film(self, info, url_id):
        return db_session.query(ModelFilm).filter(ModelFilm.url_id == url_id).one()

    def resolve_film_title(self, info, title):
        return db_session.query(ModelFilm).filter(ModelFilm.title.like(f"%{title}%")).all()

    def resolve_people(self, info, url_id):
        return db_session.query(ModelPeople).filter(ModelPeople.url_id == url_id).one()

    def resolve_people_name(self, info, name):
        return db_session.query(ModelPeople).filter(ModelPeople.name.like(f"%{name}%")).all()

    def resolve_planet(self, info, url_id):
        return db_session.query(ModelPlanet).filter(ModelPlanet.url_id == url_id).one()

    def resolve_planet_name(self, info, name):
        return db_session.query(ModelPlanet).filter(ModelPlanet.name.like(f"%{name}%")).all()

    def resolve_species(self, info, url_id):
        return db_session.query(ModelSpecies).filter(ModelSpecies.url_id == url_id).one()

    def resolve_species_name(self, info, name):
        return db_session.query(ModelSpecies).filter(ModelSpecies.name.like(f"%{name}%")).all()

    def resolve_vehicle(self, info, url_id):
        return db_session.query(ModelVehicle).filter(ModelVehicle.url_id == url_id).one()

    def resolve_vehicle_name(self, info, name):
        return db_session.query(ModelVehicle).filter(ModelVehicle.name.like(f"%{name}%")).all()

    def resolve_starship(self, info, url_id):
        return db_session.query(ModelStarship).filter(ModelStarship.url_id == url_id).one()

    def resolve_starship_name(self, info, name):
        return db_session.query(ModelStarship).filter(ModelStarship.name.like(f"%{name}%")).all()


schema = graphene.Schema(query=Query)
