package veterans

import (
	"bufio"
	"log"
	"os"
	"strings"
)

func GetKeys(filepath string) []string {
	file, err := os.Open(filepath)
	if err != nil {
		log.Fatalf("ono %v", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	scanner.Scan()
	scanner.Scan()
	return strings.Split(scanner.Text(), ",")
}
