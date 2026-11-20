class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        courses_path = defaultdict(list)

        for course, prereq in prerequisites:
            courses_path[course].append(prereq)

        visited = set()
        taken = set()
        def validate_path(course):
            if course in visited: return False
            if course in taken: return True

            visited.add(course)
            for prereq in courses_path[course]:
                if not validate_path(prereq):
                    return False
            visited.remove(course)
            taken.add(course)
            return True
            
        for course in range(numCourses):
            if not validate_path(course):
                return False
        return True