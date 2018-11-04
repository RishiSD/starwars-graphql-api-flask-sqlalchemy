from flask import Flask, render_template
from flask_graphql import GraphQLView

from swapiGraphQL.config import Config
from swapiGraphQL.schema import schema


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route('/')
    def index():
        return render_template('index.html')

    app.add_url_rule(
        '/graphql',
        view_func=GraphQLView.as_view(
            'graphql',
            schema=schema,
            graphiql=True
            # for having the GraphiQL interface
        )
    )

    return app
