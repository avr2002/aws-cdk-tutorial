# AWS CDK Crash Course by `Be a Better Dev`

- <a href="https://youtu.be/D4Asp5g4fp8?si=Iq9LO8qQR2pJzoVq" target="_blank"><b>🔗 Video Link</b></a>
- <a href="https://docs.aws.amazon.com/cdk/v2/guide/home.html" target="_blank"><b>🔗 AWS CDK Docs</b></a>


## Commands:

```bash
# Install aws-cdk cli: https://docs.aws.amazon.com/cdk/v2/guide/cli.html
npm install -g aws-cdk

# Check the version if installed correctly
cdk --version

# Configure AWS CLI
aws configure sso --profile <profile-name>
# OR
aws sso login --profile <profile-name>

# To initialize a new CDK project
cdk init app --language python

# To install the required dependencies: Install `aws-cdk-lib`
pip install -r requirements.txt

# Prepare an AWS environment for CDK deployments: https://docs.aws.amazon.com/cdk/v2/guide/ref-cli-cmd-bootstrap.html
cdk bootstrap --profile <profile-name>

# Synthesize the CloudFormation template
cdk synth

# Deploy the stack
cdk deploy --profile <profile-name>

# Continuously watch a project for changes to perform deployments and hotswaps.
cdk watch

# Destroy the stack
cdk destroy --profile <profile-name>
```


# Welcome to your CDK Python project!

This is a blank project for CDK development with Python.

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.

To manually create a virtualenv on MacOS and Linux:

```
$ python3 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation

Enjoy!
