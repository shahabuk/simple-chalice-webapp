# Simple Web App using Chalice for running in AWS Lambda

Uses `chalice` for deployment to `AWS Lambda`.

## One-off development environment setup

Based on the [Chalice instructions](https://github.com/aws/chalice)

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### One-off AWS admin

If you are going to deploy this to AWS (can skip until you do)

(login user testuser)[https://teamoptimization.signin.aws.amazon.com/console]

Edit `~/.aws/config` to become something like:

```
[default]
aws_access_key_id=YOUR_ACCESS_KEY_HERE
aws_secret_access_key=YOUR_SECRET_ACCESS_KEY
region=eu-west-2
output=json
```

## Development

### Before development

If not already in virtual environment (indicated by change in prompt to show "(venv39)" before your usual prompt):

```
source venv/bin/activate
```

### To run locally

```
chalice local --port=8001
```

then:

```
open http://127.0.0.1:8001
```

### To deploy to the internet

... and open the url just deployed to:

```
chalice deploy | tee tempout.txt && open `grep "Rest API URL" tempout.txt | cut -d " " -f 7` && rm tempout.txt
```
