package main

import (
	"fmt"
	"veterans"
)

func main() {
	for i, s := range veterans.GetKeys("data/census/veterans/ACS_15_5YR_S2101_with_ann.csv") {
		fmt.Printf("%d: %s\n", i, s)
	}
}
