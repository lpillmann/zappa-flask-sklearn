# flask-scikit-demo
A simple [Flask](http://flask.pocoo.org/) app - deployed with [Zappa](https://github.com/Miserlou/Zappa) - that returns a prediction using [scikit-learn](https://scikit-learn.org/) simple model. 


```bash
virtualenv -p ($which python3) env
source env/bin/activate
pip install -r requirements.txt
```

## Test locally

```bash
FLASK_APP=app.py flask run
```
Test endpoint: `http://localhost:5000/predict?x=1&y=2`


## Deploy
Modify the `zappa_settings.json` so it points to your bucket
```bash
zappa deploy
```
Test endpoint: `http://<zappa-deployment-url>/predict?x=1&y=2`

In case you have trouble to deploy, try renaming `zappa_settings.json` to, e.g., `zappa_settings_o.json` and run `zappa init` to generate a fresh settings file. Then, copy missing parameters from `_o` file to the new one (e.g. slim_handler=true).
