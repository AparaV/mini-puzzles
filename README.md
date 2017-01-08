# Mini puzzle games

## 1. Morse Code Generator

Generates a morse code audio for a given text input.

##### Known Issue:
No pause between two different letters (could lead to ambiguity).

## 2. Enigma

A super simplified version of the original Enigma.

##### Algorithm:

Each letter in the input text is replaced by a letter at a position down the alphabets based on a key provided.

For example, the input is 'HELLO WORLD' and key is 'COUT'.

First, the distance of the first letter in the key (C) from the first letter of the alphabet (A) is computed. This would be 2.
Now the first letter of the input (H) is replaced with the letter that is 2 letters away from it. This would be J.

We roll back to A if we go beyond the letters of the alphabet.

The same process is repeated with the second letter of the input and second letter of the key. If we run out of letters in the key, we would start over from the beginning of the key.
This encryption would continue until we have successfully encrypted the entire input.

Therefore, 'HELLO WORLD' with the key 'COUT' would give 'JSFEQ KIKNR'.
