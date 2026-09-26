<h1 align="center">RPUK Seekers Website</h1>

<p align="center">
  <img width="300" alt="The Seekers logo" src="https://i.gyazo.com/d2aeabfdb81aae76884b54797527d5b0.png" />
</p>

<p align="center">
  <img alt="Inactive" src="https://img.shields.io/badge/status-inactive-lightgrey" />
  <img alt="Flask" src="https://img.shields.io/badge/Flask-000?logo=flask&logoColor=fff" />
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff" />
  <img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff" />
  <img alt="AWS" src="https://img.shields.io/badge/AWS-232F3E?logo=amazonwebservices&logoColor=fff" />
</p>

An inactive Flask website made for The Seekers, a former group on the [Roleplay UK](https://www.roleplay.co.uk) FiveM server.

The hosted site is no longer available. The repository remains as a small example of the original landing page and its historical AWS deployment setup. The deployment workflow is disabled.

## What the page does

The home page displays the group logo and the message “TRUST THE GOVERNMENT.” Hovering over the message changes it to “OR SEEK THE TRUTH.”

The wider plan was to host puzzles and alternate-reality-game content for players, but those additional pages were not built.

## Run locally

A modern Python environment may require dependency updates because the project pins Flask 2.2.5.

~~~bash
python -m pip install -r requirements.txt
python app.py
~~~

Open [http://localhost:5000](http://localhost:5000).

## Run with Docker

~~~bash
docker build -t rpuk-seekers .
docker run --rm -p 5000:5000 rpuk-seekers
~~~

The container uses Python 3.7.9 and Gunicorn. Python 3.7 is no longer a current runtime, so rebuilds may require updating the Docker base image and testing the pinned packages.

## Project layout

- `app.py`, Flask application and home route.
- `site/templates/home.html`, landing-page markup.
- `site/static/css/home.css`, page styling.
- `site/static/js/home.js`, hover behaviour.
- `site/static/img/`, logo and favicon.
- `Dockerfile`, production container using Gunicorn.
- `.github/workflows/deploy.yml`, historical AWS Elastic Beanstalk deployment.

## Historical deployment

The workflow builds a Docker image, pushes it to Amazon ECR, and deploys through Elastic Beanstalk. It expects these GitHub Actions secrets:

- `AWS_REGION`
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_ACCOUNT_ID`
- `ECR_REPO`
- `EB_APPLICATION`

Do not add real values to the repository. The workflow should remain disabled unless an authorised AWS environment has been prepared and its costs are understood.

## Known limitations

- Only one route exists.
- The live deployment is inactive.
- The Docker image uses an obsolete Python release.
- There are no tests, health endpoint, or local configuration options.
- The original puzzle and secret-page plans were never implemented.

## Licence

No project-level licence is currently included. The logo and custom font may have separate ownership or usage restrictions.
