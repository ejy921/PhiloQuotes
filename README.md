## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/ejy921/PhiloQuotes.git

cd PhiloQuotes

If you don't have venv, type: pip install virtualenv

python -m venv PhiloQuotes-Env

PhiloQuotes-Env\Scripts\activate

pip install -r requirements.txt


## API is available here
https://philosophy-quotes-api.glitch.me

## Endpoints
https://philosophy-quotes-api.glitch.me/quotes   *retrieves all quotes*

https://philosophy-quotes-api.glitch.me/quotes/author/{parameter}   *retrieves quotes by author*

https://philosophy-quotes-api.glitch.me/quotes/philosophy/{parameter}   *retrieves quotes by philosophy*

## Characters (endpoint parameters)
A characteristic field was added to the quotes that contains 3 comma-seperated 
words that assign the quote values from a list of 14 total characters:

These are:
- Analytical
- Inquisitive
- Modern
- Pragmatic
- Empathetic
- Skeptical
- Introspective
- Philosophical
- Visionary
- Creative
- Spiritual
- Challenging
- Hopeful
- Uplifting

## Authors (endpoint parameters)
- Marcus Aurelius
- Seneca
- Epictetus
- Alan Watts
- Rumi
- Carl G. Jung
- Friedrich Nietzsche
- Jean-Paul Sartre
- Fyodor Dostoyevsky
- Plato
- Aristotle
- Henry David Thoreau
- Ralph Waldo Emerson
- Christopher McCandless
- René Descartes
- Baruch Spinoz
- Leibniz
- John Locke
- George Berkeley
- David Hume

## Philosophies (endpoint parameters)
- Stoicism
- Mysticism
- Existentialism
- Classical Greek
- Transcendentalism
- Rationalism
- Empiricism