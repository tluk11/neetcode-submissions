class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashmap = defaultdict(list)

        for course,prereq in prerequisites:
            hashmap[course].append(prereq)

        visited = set()
        checked = set()
        res = []
        def dfs(currCourse):
            if currCourse in visited:
                return False
            if currCourse in checked:
                return True
            toTake = hashmap[currCourse]
            visited.add(currCourse)
            for pre in toTake:
                if not dfs(pre):
                    return False
            visited.remove(currCourse)
            checked.add(currCourse)
            res.append(currCourse)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
            
        return res