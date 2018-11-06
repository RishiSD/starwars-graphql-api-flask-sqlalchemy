from swapiGraphQL.database import Base, engine
from swapiGraphQL.models import (
    ModelFilm, ModelPeople, ModelPlanet,
    ModelSpecies, ModelVehicle, ModelStarship
)
from swapiGraphQL.utils import (
    fetch_swapi_data,
    load_swapi_data,
    set_rel_swapi_data
)


if __name__ == '__main__':
    print('           *** Start Setup ***            ')
    print('         ** Creating Database **          ')
    Base.metadata.create_all(engine)
    print('       ****** Fetching Data ******        ')
    fetch_swapi_data()
    print('     ******** Loading Data *********      ')
    load_swapi_data()
    print('   ******* Set data relation *********    ')
    set_rel_swapi_data()
    print('************ Setup Finished **************')
    print('******* May the Force be with you ********')
