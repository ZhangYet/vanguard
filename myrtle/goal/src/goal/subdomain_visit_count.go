package goal

import (
	"fmt"
	"strconv"

	"strings"
)

// https://leetcode.com/problems/subdomain-visit-count/

type domainCount struct {
	domain string
	count  int
}

func subdomainVisits(cpdomains []string) []string {
	countMap := make(map[string]int)
	for _, domain := range cpdomains {
		data := strings.Split(domain, " ")
		count, _ := strconv.ParseInt(data[0], 10, 64)
		countSubDomains(&domainCount{domain: data[1], count: int(count)}, &countMap)
	}
	ret := make([]string, 0, len(countMap))
	for domain, c := range countMap {
		ret = append(ret, fmt.Sprintf("%d %s", c, domain))
	}
	return ret
}

func countSubDomains(cpdomain *domainCount, countMap *map[string]int) {
	(*countMap)[cpdomain.domain] += cpdomain.count
	idx := strings.Index(cpdomain.domain, ".")
	if idx == -1 {
		return
	}

	countSubDomains(&domainCount{
		domain: cpdomain.domain[idx+1:],
		count:  cpdomain.count,
	}, countMap)
}
