print("__________Typing Speed Tester__________")

import time
import random

sentences = [
    "The quick brown fox jumps over the lazy dog near the quiet river.",
    "Learning to code every day can improve your problem-solving skills significantly.",
    "A bright morning with fresh air always boosts energy and clears the mind."
]

def measure_accuracy(user_input, test_sentence):
    correct_chars = sum(1 for a, b in zip(user_input, test_sentence) if a == b)
    accuracy = (correct_chars / len(test_sentence)) * 100 if test_sentence else 0
    return accuracy

def typing_test():
    test_sentence = random.choice(sentences)
    print("Type this following sentence as fast you can:")
    print(test_sentence)
    input("Press Enter when you are ready...")
    start_time = time.time()  # Measure the start time
    user_input = input("\nStart typing:\n")
    end_time = time.time()   # Measure the end time
    time_taken = end_time - start_time
    # time_taken_in_minutes = time_taken / 60
    word_count = len(test_sentence.split(" "))

    print("Results: ")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Words typed: {word_count}")
    print(f"Typing Speed: {word_count / (time_taken / 60):.2f} words per minute")
    accuracy = measure_accuracy(user_input, test_sentence)
    print(f"Accuracy: {accuracy:.2f}%")

typing_test()
