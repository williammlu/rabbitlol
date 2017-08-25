Smart bookmarking tool similar to bunnylol from Facebook. Rabbitlol instance forked from esert/rabbitlol running on Google's App Engine with updated dependencies.

Use with ctrl-L on Chrome for an extra efficient browsing experience!

## Requirements

1. [Google App Engine SDK for Python](https://cloud.google.com/appengine/docs/python/download)
2. virtualenv

## Running on Google App Engine

Go to <https://console.cloud.google.com/appengine> and create yourself a project, save your project ID. Go to repo's root directory and run `sh start.sh` to install dependencies and start a test session. Once all the packages are installed and the app appears to run properly in development, deploy the app to the Google App engine by running `sh deploy.sh`.

## Next Steps

Building and deploying app with hacky sh scripts instead of the Makefile, which had some problems. Fix build and tests for easier dependency installation and deployment.
