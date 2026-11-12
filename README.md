
# Jenkins CI Demo

A small Python project used to learn Continuous Integration with Jenkins.

## What it does

- Simple calculator module with unit tests (pytest)
- Linting with flake8
- Jenkins declarative pipeline defined in a `Jenkinsfile`

## Pipeline stages

1. **Checkout**: Pull the code from GitHub.
2. **Setup**: Create a virtual environment and install dependencies.
3. **Lint**: Run flake8.
4. **Test**: Run pytest and publish the JUnit report.

## Run locally

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pytest
```

## Jenkins setup

- Jenkins running in Docker (`jenkins/jenkins:lts`)
- Python 3, pip, and venv installed in the container
- Pipeline job using "Pipeline script from SCM" pointing to this repository
- Poll SCM trigger: `H/2 * * * *`

## What I learned

- Difference between CI and CD
- Writing a declarative Jenkinsfile
- Connecting Jenkins to GitHub
- Reading console output and test reports
- Debugging a failing build

## Next steps

- Add a Docker build and push stage (CD)
- Replace polling with GitHub webhooks
- Add Slack or email notifications
