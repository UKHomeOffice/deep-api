import os
MONGO_HOST = os.environ.get('MONGO_SERVICE_HOST')
MONGO_PORT = int(os.environ.get('MONGO_SERVICE_PORT'))

MONGO_DBNAME = 'deep'

XML = False
# Enable CORS for all domains
X_DOMAINS = "*"
X_HEADERS = "Content-Type, Accept, Authorization, X-Requested-With, " \
    " Access-Control-Request-Headers, Access-Control-Allow-Origin, " \
    " Access-Control-Allow-Credentials, X-HTTP-Method-Override, mozSystem, " \
    " Access-Control-Allow-Methods, If-Match "

RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

PUBLIC_METHODS = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE']
PUBLIC_ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'POST', 'DELETE']


deploys = {
    'schema': {
        'Timestamp': {
            'type': 'number'
        },
        'Images': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        },
        'tag': {
            'type': 'string'
        },
        'Namespace': {
            'type': 'string'
        },
        'Target': {
            'type': 'string'
        },
        'Source': {
            'type': 'string'
        },
        'Url': {
            'type': 'string'
        },
        'Token': {
            'type': 'string'
        }
    }
}

webhooks = {
    'schema': {
        'build': {
            'type': 'dict',
            'schema': {
                "author": {'type': 'string'},
                "author_avatar": {'type': 'string'},
                "author_email": {'type': 'string'},
                "branch": {'type': 'string'},
                "commit": {'type': 'string'},
                "created_at": {'type': 'number'},
                "enqueued_at": {'type': 'number'},
                "event": {'type': 'string'},
                "finished_at": {'type': 'number'},
                "link_url": {'type': 'string'},
                "message": {'type': 'string'},
                "number": {'type': 'number'},
                "ref": {'type': 'string'},
                "refspec": {'type': 'string'},
                "remote": {'type': 'string'},
                "started_at": {'type': 'number'},
                "status": {'type': 'string'},
                "timestamp": {'type': 'number'},
                "title": {'type': 'string'},
                "id": {'type': 'number'},
            },
        },
        'repo': {
            'type': 'dict',
            'schema': {
                "allow_deploys": {'type': 'boolean'},
                "allow_pr": {'type': 'boolean'},
                "allow_push": {'type': 'boolean'},
                "allow_tags": {'type': 'boolean'},
                "avatar_url": {'type': 'string'},
                "clone_url": {'type': 'string'},
                "default_branch": {'type': 'string'},
                "full_name": {'type': 'string'},
                "link_url": {'type': 'string'},
                "name": {'type': 'string'},
                "owner": {'type': 'string'},
                "private": {'type': 'boolean'},
                "timeout": {'type': 'number'},
                "id": {'type': 'number'},
                "trusted": {'type': 'boolean'},

            },
        }
    }
}

reports = {
    'schema': {
        'build': {'type': 'string'},
        'branch': {'type': 'string'},
        'repo': {'type': 'string'},
        'report': {'type': 'string'},
        'timestamp': {'type': 'string'}
    }
}

DOMAIN = {'deploys': deploys, 'webhooks': webhooks, 'reports': reports}
