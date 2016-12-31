package main

import (
	"income"
	"log"
)

func main() {
	income07 := income.ParseMedianIncomeCounties("data/census/income/ACS_07_3YR_GCT1901.US05PR_with_ann.csv")
	income15 := income.ParseMedianIncomeCounties("data/census/income/ACS_15_5YR_GCT1901.US05PR_with_ann.csv")
	avgIncome07 := 0.0
	avgIncome15 := 0.0
	avgDiff := 0.0
	for fips, income := range income07 {
		avgIncome07 += income
		avgIncome15 += income15[fips]
		avgDiff += income15[fips] - income
	}
	log.Printf("07 avg by county: %f", avgIncome07/float64(len(income07)))
	log.Printf("15 avg by county: %f", avgIncome15/float64(len(income07)))
	log.Printf("Diff: %f", avgDiff/float64(len(income07)))
}
