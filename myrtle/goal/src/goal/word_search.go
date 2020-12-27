package goal

//
//import (
//	"fmt"
//)
//
//// https://leetcode.com/problems/word-search/
//// 应该用 BFS
//
//type axis struct {
//	x int
//	y int
//}
//
//func (this *axis) key() string {
//	return fmt.Sprintf("%s_%s", this.x, this.y)
//}
//
//type path struct {
//	width   int
//	height  int
//	nodes   []*axis
//	visited map[string]bool
//}
//
//func (this *path) validNeighbors() []*axis {
//	tail := this.nodes[len(this.nodes)-1]
//	condidates := []*axis{
//		&axis{x: tail.x - 1, y: tail.y},
//		&axis{x: tail.x + 1, y: tail.y},
//		&axis{x: tail.x, y: tail.y - 1},
//		&axis{x: tail.x, y: tail.y + 1},
//	}
//	res := make([]*axis, 0)
//	for _, cond := range condidates {
//		if _, ok := this.visited[cond.key()]; ok {
//			continue
//		}
//		if cond.x < 0 || cond.x >= this.width {
//			continue
//		}
//		if cond.y < 0 || cond.y >= this.height {
//			continue
//		}
//		res = append(res, cond)
//	}
//	return res
//}
//
//func findPath(p *path, init int, board [][]byte, word string) bool {
//	if len(p.nodes) == len(word) {
//		return true
//	}
//	validNeighbors := p.validNeighbors()
//	if len(validNeighbors) == 0 {
//		return false
//	}
//	return true
//}
//
//func exist(board [][]byte, word string) bool {
//	if len(word) == 0 {
//		return true
//	}
//
//}
