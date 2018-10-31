import os
import re
import sys
import json
import requests
import fileinput

from swapiGraphQL.database import db_session
from swapiGraphQL.models import (
    ModelFilm, ModelPeople, ModelPlanet,
    ModelSpecies, ModelVehicle, ModelStarship
)

resources = ['planets', 'films', 'people',
             'species', 'starships', 'vehicles']
resource_map = {'planets': 'ModelPlanet', 'films': 'ModelFilm',
                'people': 'ModelPeople', 'species': 'ModelSpecies',
                'starships': 'ModelStarship', 'vehicles': 'ModelVehicle'}


def fetch_swapi_data():

    swapi_url = 'https://swapi.co/api'

    for resource in resources:
        r = requests.get(f'{swapi_url}/{resource}')
        resource_list = r.json().get('results')
        while r.status_code == 200 and r.json().get('next'):
            r = requests.get(r.json().get('next'))
            resource_list += r.json().get('results')
        with open(os.path.join(os.path.dirname(__file__),
                               'data', f'{resource}.json'), 'a') as fp:
            json.dump(resource_list, fp, indent=4)

        #print(f'{resource}.json')

        for line in fileinput.input(os.path.join(os.path.dirname(__file__),
                                                 'data', f'{resource}.json'),
                                    inplace=True):
            matchObj = re.match(f'(.*)"{swapi_url}/.*/(.*)/"(.*)', line, re.M)
            if matchObj:
                line = matchObj.group(1) + matchObj.group(2) \
                    + matchObj.group(3) + '\n'
            sys.stdout.write(line)

        for line in fileinput.input(os.path.join(os.path.dirname(__file__),
                                                 'data', f'{resource}.json'),
                                    inplace=True):
            matchObj = re.match(f'(.*)"url"(.*)', line, re.M)
            if matchObj:
                line = matchObj.group(1) + '"url_id"' \
                    + matchObj.group(2) + '\n'
            sys.stdout.write(line)


def load_swapi_data():
    for resource in resources:
        #print(resource)
        with open(os.path.join(os.path.dirname(__file__),
                               'data', f'{resource}.json')) as f:
            data = json.load(f)
            for rec in data:
                res_obj = eval(resource_map[resource] + '()')
                obj_fields = vars(eval(resource_map[resource]))
                for field in rec:
                    if field in obj_fields:
                        setattr(res_obj, field, rec[field])
                db_session.add(res_obj)
            db_session.commit()


def set_rel_swapi_data():
    # Handling relationships for ModelFilms
    for resource in ['planets', 'people', 'species', 'starships', 'vehicles']:
        with open(os.path.join(os.path.dirname(__file__),
                               'data', f'{resource}.json')) as f:
            data = json.load(f)
            for rec in data:
                if 'films' in rec:
                    parent = eval(f'db_session.query({resource_map[resource]})\
                                  .filter_by(url_id={rec["url_id"]}).first()')
                    for film_id in rec['films']:
                        child = db_session.query(ModelFilm)\
                                          .filter_by(url_id=film_id).first()
                        parent.film_list.append(child)
            db_session.commit()

    # Handling relationships for ModelPeople
    for resource in ['species', 'starships', 'vehicles']:
        if resource == 'species':
            field = 'people'
        else:
            field = 'pilots'

        with open(os.path.join(os.path.dirname(__file__),
                               'data', f'{resource}.json')) as f:
            data = json.load(f)
            for rec in data:
                if field in rec:
                    parent = eval(f'db_session.query({resource_map[resource]})\
                                  .filter_by(url_id={rec["url_id"]}).first()')
                    for people_id in rec[field]:
                        child = db_session.query(ModelPeople)\
                                          .filter_by(url_id=people_id).first()
                        if field == 'people':
                            parent.people_list.append(child)
                        else:
                            parent.pilot_list.append(child)
            db_session.commit()
