package project1;

import java.util.Arrays;
import java.util.Random;

public class GeneticAlgorithm {

    private static final String TARGET = "(Generative AI) ";
    private static final int POPULATION_SIZE = 100;
    private static final double MUTATION_RATE = 0.01;

    private static final Random random = new Random();

    public static void main(String[] args) {
    	double avarageSolutionTime = 0;
    	double avarageSolutionGeneration = 0;
        for (int i = 0; i < 2; i++) {
            long startTime = System.currentTimeMillis();
            int generation = evolve();
            long endTime = System.currentTimeMillis();

            System.out.println("Solution found in " + generation + " generations.");
            System.out.println("Time taken: " + (endTime - startTime) + " milliseconds.");
            System.out.println();
            avarageSolutionTime += (endTime - startTime);
            avarageSolutionGeneration += generation;
        }
        System.out.println("Avarage generation: " + (avarageSolutionGeneration / 2) + " generations.");
        System.out.println("Avarage time taken: " + (avarageSolutionTime / 2) + " milliseconds.");
    }

    private static int evolve() {
        char[][] population = new char[POPULATION_SIZE][TARGET.length()];
        double[] fitness = new double[POPULATION_SIZE];

        // Initialize population
        for (int i = 0; i < POPULATION_SIZE; i++) {
            population[i] = generateRandomString();
        }

        int generation = 0;
        int flagOfClosestSolution = 0;
        while (true) {
            // Calculate fitness for each individual in population
            for (int i = 0; i < POPULATION_SIZE; i++) {
                fitness[i] = calculateFitness(population[i]);
                if (fitness[i] == 1) {
                    System.out.print("Solution found: ");
                    System.out.println(population[i]);
                    return generation;
                }
            }
            
            // Since printing all generations would take up unnecessary space, 
            // a generation is written once every 100 generations.
            if (flagOfClosestSolution % 100 == 0) {
            	findClosestSolution(fitness, population, generation);
            }

            // Create new generation
            char[][] newPopulation = new char[POPULATION_SIZE][TARGET.length()];
            for (int i = 0; i < POPULATION_SIZE; i++) {
                char[] parent1 = selectParent(population, fitness);
                char[] parent2 = selectParent(population, fitness);
                char[] child = crossover(parent1, parent2);
                mutate(child);
                newPopulation[i] = child;
            }
            population = newPopulation;

            generation++;
            flagOfClosestSolution++;
        }
    }
    
	private static void findClosestSolution(double[] fitness, char[][] population, int generation) {
        int bestIndividualIndex = 0;
        for (int i = 1; i < POPULATION_SIZE; i++) {
            if (fitness[i] > fitness[bestIndividualIndex]) {
                bestIndividualIndex = i;
            }
        }

        System.out.print("Generation " + generation + ": ");
        System.out.println(population[bestIndividualIndex]);
	}

    private static char[] generateRandomString() {
        char[] randomString = new char[TARGET.length()];
        String validChars = "abcdefghıijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789!@#$%^&*()_+-=[]{};':,.<>/?";
        Random random = new Random();

        for (int i = 0; i < TARGET.length(); i++) {
            randomString[i] = validChars.charAt(random.nextInt(validChars.length()));
        }

        return randomString;
    }


    private static double calculateFitness(char[] candidate) {
        double fitness = 0;
        for (int i = 0; i < TARGET.length(); i++) {
            if (candidate[i] == TARGET.charAt(i)) {
                fitness++;
            }
        }
        return fitness / TARGET.length();
    }

    private static char[] selectParent(char[][] population, double[] fitness) {
        double totalFitness = Arrays.stream(fitness).sum();
        double randomFitness = random.nextDouble() * totalFitness;
        double sum = 0;
        for (int i = 0; i < POPULATION_SIZE; i++) {
            sum += fitness[i];
            if (sum >= randomFitness) {
                return population[i];
            }
        }
        return population[POPULATION_SIZE - 1];
    }
    
    private static char[] crossover(char[] parent1, char[] parent2) {
        char[] child = new char[TARGET.length()];
        int midpoint = random.nextInt(TARGET.length());
        for (int i = 0; i < TARGET.length(); i++) {
            if (i < midpoint) {
                child[i] = parent1[i];
            } else {
                child[i] = parent2[i];
            }
        }
        return child;
    }

    private static void mutate(char[] child) {
        String validChars = "abcdefghıijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 0123456789!@#$%^&*()_+-=[]{};':,.<>/?";
        for (int i = 0; i < TARGET.length(); i++) {
            if (random.nextDouble() < MUTATION_RATE) {
                int randomIndex = random.nextInt(validChars.length());
                child[i] = validChars.charAt(randomIndex);
            }
        }
    }

}