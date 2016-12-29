package main

import (
	"bufio"
	"elections"
	"log"
	"os"
)

func main() {
	file, err := os.Open("data/elections/US_County_Level_Presidential_Results_08-16.csv")
	if err != nil {
		log.Fatalf("ono! %v", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	var counties []elections.County
	for scanner.Scan() {
		counties = append(counties, elections.ParseRow(scanner.Text()))
	}

	if err := scanner.Err(); err != nil {
		log.Fatal("poo %v", err)
	}

	rToD, dToR := elections.GetFlippedCounties0816(counties)
	log.Printf("08-16: R->D: %d, D->R: %d", len(rToD), len(dToR))

	rToD, dToR = elections.GetFlippedCounties1216(counties)
	log.Printf("12-16: R->D: %d, D->R: %d", len(rToD), len(dToR))

	for _, flip := range dToR {
		log.Printf("%d", flip.ID)
	}
}
