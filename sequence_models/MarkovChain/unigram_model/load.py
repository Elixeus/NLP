def load_model(model_file):
    probabilities = {}
    with open(model_file, 'r') as model:
        for line in model:
            word, probability = line.split(':')
            probabilities[word] = float(probability)

    return probabilities
