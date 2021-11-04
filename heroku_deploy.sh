#!/bin/bash
# Script : heroku_deploy.sh
# Author : Yannis Saliniere
# Script bash to deploy a dockerized web application on Heroku

# Login to Heroku
echo $HEROKU_API_KEY | docker login --username=_ --password-stdin registry.heroku.com

# Destroy app
heroku apps:destroy --app=$HEROKU_APP_NAME --confirm=$HEROKU_APP_NAME

# Create app
heroku apps:create $HEROKU_APP_NAME

# Set environment variables
deploy_variables=`compgen -v | grep ^AWS_ && compgen -v | grep ^DJANGO_ && compgen -v | grep ^SENTRY_`
for deploy_variable in $deploy_variables
do
    heroku config:set $deploy_variable=${!deploy_variable} --app=$HEROKU_APP_NAME;
done

# Set maintenance mode on
heroku maintenance:on --app=$HEROKU_APP_NAME

# Push docker image on Heroku registry
docker pull $DOCKER_USER/$DOCKER_REPOSITORY:$CIRCLE_SHA1
docker tag $DOCKER_USER/$DOCKER_REPOSITORY:$CIRCLE_SHA1 registry.heroku.com/$HEROKU_APP_NAME/web
docker push registry.heroku.com/$HEROKU_APP_NAME/web

# Release app
heroku container:release --app=$HEROKU_APP_NAME web

# Set maintenance mode off
heroku maintenance:off --app=$HEROKU_APP_NAME