## Sentiment API for [TrackMaven's NLP Meetup!](http://www.meetup.com/TrackMaven-Monthly-Challenge/)

Uses [textblob](https://textblob.readthedocs.org) with calculate the sentiment around a topic (with data provided with twitter).

Requires [Docker](https://docs.docker.com/installation/) + [Fig](http://fig.sh)

Create a `twitter_creds.json` in `web` with...
```
{
    "app_key": "bla",
    "app_secret": "biz",
    "oauth_token": "ha",
    "oauth_token_secret": "he"
}
````

Then start running it all with...
```
fig up.
```

Run a topic (with data pulled from twitter) against the API endpoint.

```
curl -H "Content-type: application/json" -X POST http://localdocker:5001/api/analyze/ -d '{"topic":"Pokemon"}'
```
