class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        courses_path = defaultdict(list)
        for course, prereq in prerequisites:
            courses_path[course].append(prereq)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2
        states = [UNVISITED] * numCourses

        def validate_path(course):
            state = states[course]
            if state == VISITED: return True
            elif state == VISITING: return False

            states[course] = VISITING
            for prereq in courses_path[course]:
                if not validate_path(prereq):
                    return False
            states[course] = VISITED
            return True
            
        for course in range(numCourses):
            if not validate_path(course):
                return False
        return True