package project1;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class StringGuesser {
    private static final String TARGET = "(Generative AI) ";
    private static final int MAX_ATTEMPTS = 1000;
    private static final Random random = new Random();

    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();
        guessString();
        long endTime = System.currentTimeMillis();

        System.out.println("Time taken: " + (endTime - startTime) + " milliseconds.");
    }

    private static void guessString() {
        List<Character> currentGuess = initializeGuess();
        int attempts = 0;

        while (!isCorrectGuess(currentGuess) && attempts < MAX_ATTEMPTS) {
        	System.out.println("Current guess: " + listToString(currentGuess));
            updateGuess(currentGuess);
            attempts++;
        }

        if (isCorrectGuess(currentGuess)) {
            System.out.println("Target string found: " + listToString(currentGuess));
            System.out.println("Number of attempts: " + attempts);
        } else {
            System.out.println("Target string not found within max attempts.");
        }
    }

    private static List<Character> initializeGuess() {
        List<Character> guess = new ArrayList<>();
        for (int i = 0; i < TARGET.length(); i++) {
            guess.add(generateRandomCharacter());
        }
        return guess;
    }

    private static boolean isCorrectGuess(List<Character> guess) {
        StringBuilder guessString = new StringBuilder();
        for (Character c : guess) {
            guessString.append(c);
        }
        return guessString.toString().equals(TARGET);
    }

    private static void updateGuess(List<Character> guess) {
        for (int i = 0; i < TARGET.length(); i++) {
            if (guess.get(i) != TARGET.charAt(i)) {
                guess.set(i, generateRandomCharacter());
            }
        }
    }

    private static char generateRandomCharacter() {
        String validChars = "abcdefghıijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789!@#$%^&*()_+-=[]{};':,.<>/?";
        return validChars.charAt(random.nextInt(validChars.length()));
    }

    private static String listToString(List<Character> list) {
        StringBuilder sb = new StringBuilder();
        for (Character c : list) {
            sb.append(c);
        }
        return sb.toString();
    }
}
