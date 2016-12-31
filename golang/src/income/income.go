package income

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

// Returns a map from county FipsID to median income.
func ParseMedianIncomeCounties(filepath string) map[int]float64 {
	file, err := os.Open(filepath)
	if err != nil {
		log.Fatalf("ono %v", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	response := make(map[int]float64)
	// Key 1.
	scanner.Scan()
	// Key 2.
	scanner.Scan()
	// Column for whole US.
	scanner.Scan()
	for scanner.Scan() {
		parts := strings.Split(scanner.Text(), ",")
		fips, err := strconv.Atoi(parts[4])
		if err != nil {
			log.Fatalf("aw %v", err)
		}
		if fips < 100 {
			// State, not county.
			continue
		}
		income, err := strconv.ParseFloat(parts[7], 64)
		if err != nil {
			log.Fatalf("derp %v ", err)
		}
		response[fips] = income
	}
	return response
}
