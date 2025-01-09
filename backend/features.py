QUOTENUM = 128 # Number of quotes in json file

class Features:
    philosophies = [
    "Stoicism", "Mysticism", "Existentialism", "Classical Greek",
    "Transcendentalism", "Rationalism", "Empiricism"
    ]

    central_philosophies = ["Existentialism", "Rationalism", "Classical Greek"]

    other_philosophies = {
        "Mysticism": [1, 0, 1],               # Existentialism and Classical Greek
        "Transcendentalism": [0, 1, 1],       # Rationalism and Classical Greek
        "Stoicism": [1, 1, 0],                # Existentialism and Rationalism
        "Empiricism": [1, 1, 1]               # All three
    }
    
    characteristics = [
    "Analytical", "Inquisitive", "Modern", "Pragmatic", "Empathetic", 
    "Skeptical", "Introspective", "Philosophical", "Visionary", "Creative", 
    "Spiritual", "Challenging", "Hopeful", "Uplifting"
    ]

    central_characteristics = ["Analytical", "Empathetic", "Visionary"]

    other_characteristics = {
        "Inquisitive": [1, 0, 1],
        "Modern": [1, 0, 1],
        "Pragmatic": [1, 1, 0],
        "Skeptical": [1, 0, 0],
        "Introspective": [1, 1, 0],
        "Philosophical": [1, 1, 0],
        "Creative": [0, 0, 1],
        "Spiritual": [0, 1, 1],
        "Challenging": [1, 0, 1],
        "Hopeful": [0, 1, 1],
        "Uplifting": [0, 1, 0],
    }   