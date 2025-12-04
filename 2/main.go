package main

import (
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

var filePath = "2.input"

func main() {
	f, err := os.Open(filePath)
	if err != nil {
		panic("Couldn't open file")
	}

	scanner := bufio.NewScanner(f)
	scanner.Scan()
	line := scanner.Text()
	ranges := strings.Split(line, ",")

	// part 1
	c := 0
	for _, r := range ranges {
		split := strings.Split(r, "-")
		if len(split[0])%2 == 1 && len(split[1])%2 == 1 {
			continue
		}
		start, _ := strconv.Atoi(split[0])
		end, _ := strconv.Atoi(split[1])

		for i := start; i <= end; i++ {
			hh := int(math.Log10(float64(i))) + 1
			if hh%2 == 1 {
				continue
			}
			h := int(math.Log10(float64(i))/2) + 1
			left := i / int(math.Pow10(h))
			right := i % int(math.Pow10(h))
			// fmt.Printf("i: %d, h:%d left: %d, right: %d\n", i, h, left, right)
			// fmt.Printf("len(%s)%%2 = %d && len(%s)%%2 = %d\n", split[0], len(split[0])%2, split[1], len(split[1])%2)
			if left == right {
				c += i
			}
		}
	}
	fmt.Printf("Answer 1: %d\n", c)

	// part 2
	c = 0

	for _, r := range ranges {
		split := strings.Split(r, "-")
		start, _ := strconv.Atoi(split[0])
		end, _ := strconv.Atoi(split[1])

		for i := start; i <= end; i++ {
			i_str := strconv.Itoa(i)
			for j := range len(i_str) {
				if j == 0 || len(i_str)%j != 0 {
					continue
				}
				if strings.Repeat(i_str[:j], len(i_str)/j) == i_str {
					c += i
					break
				}
			}
		}
	}

	fmt.Printf("answer 2: %d\n", c)
}
