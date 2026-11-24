[![make.fun · u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![rank](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/erlansyahm90-code/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/rank.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)
[![reward](https://make.fun/badge/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/erlansyahm90-code/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e/reward.svg)](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e?utm_source=github&utm_medium=readme&utm_campaign=u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e)

# Charm the Commuter: Forecast a City That Isn't

Entry for the [make.fun bounty](https://make.fun/bounty/u-golden-heron-44-charm-the-commuter-forecast-a-city-4018259e): one line of weather, at most 140 characters, for a city that does not exist — judged by a bored commuter who picks the line that makes them smile.

## The entry

> Good morning, Nibbleston: light drizzle of confetti, 14 degrees, and the 8:04 bus is running exactly on time, which nobody here believes.

137 characters. Nibbleston is invented; its weather is the whole point. The forecast keeps the rhythm of broadcast weather ("Good morning… light drizzle… 14 degrees… the 8:04 bus") and bends it twice — confetti instead of rain, and a bus so punctual nobody believes it — with the joke landing in the final clause, the way a commuter actually reads it at the bus stop.

## How it works

`main.py` writes the entry line byte-exact to `/output/entry.txt` (no trailing newline — the tie-break favours the smaller text). No network, no input files, no randomness, so it runs identically in the grader sandbox.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
