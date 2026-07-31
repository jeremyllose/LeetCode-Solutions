class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #Step 1: Build the graph.
        graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        #Stores courses currently being explored.
        visiting = set()
        #Stores courses already completely explored
        visited = set()

        def dfs(course):
            #Cycle Found.
            if course in visiting:
                return False
            #Already checked before.
            if course in visited:
                return True
            #Start exploring this course.
            visiting.add(course)
            #Visit every prerequisite.
            for prereq in graph[course]:
                if not dfs(prereq):
                    return False
            #Finished exploring this course.
            visiting.remove(course)
            visited.add(course)

            return True
            #Try Starting DFS from every course:
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

#    Step 1:
# Create a graph with numCourses nodes.
# Step 2:
# Use prerequisites to connect the nodes.

# Step 3:
# Run DFS starting from every course.

# Step 4:
# If DFS encounters a course that is already in the current DFS path,
# a cycle exists.

# Return False.

# Step 5:
# If every DFS finishes without finding a cycle,

# Return True.

