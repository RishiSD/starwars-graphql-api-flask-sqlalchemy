import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
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
    all_films = SQLAlchemyConnectionField(FilmObject)
    all_people = SQLAlchemyConnectionField(PeopleObject)
    all_planet = SQLAlchemyConnectionField(PlanetObject)
    all_species = SQLAlchemyConnectionField(SpeciesObject)
    all_vehicles = SQLAlchemyConnectionField(VehicleObject)
    all_starships = SQLAlchemyConnectionField(StarshipObject)


schema = graphene.Schema(query=Query)
